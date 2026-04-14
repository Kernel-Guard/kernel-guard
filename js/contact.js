/**
 * KernelGuard Contact Form Handler
 * - Client-side email validation
 * - EmailJS auto-reply (sends confirmation to the submitter)
 * - Formspree submission (receives the inquiry)
 * - Success toast notification
 */

// ── EmailJS Configuration ──
const EMAILJS_PUBLIC_KEY  = '8sBuRqIaclGno0KjA';
const EMAILJS_SERVICE_ID  = 'service_9vcrgt7';
const EMAILJS_TEMPLATE_ID = 'template_li5fxw7';

// Initialize EmailJS as soon as SDK is ready
function initEmailJS() {
    if (typeof emailjs !== 'undefined') {
        emailjs.init(EMAILJS_PUBLIC_KEY);
        console.log('EmailJS initialized.');
    } else {
        // SDK might not have loaded yet — retry once
        setTimeout(() => {
            if (typeof emailjs !== 'undefined') {
                emailjs.init(EMAILJS_PUBLIC_KEY);
                console.log('EmailJS initialized (retry).');
            } else {
                console.warn('EmailJS SDK failed to load.');
            }
        }, 1500);
    }
}
initEmailJS();

document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('contact-form');
    const emailInput = document.getElementById('contact-email');
    const emailError = document.getElementById('email-error');
    const submitBtn = document.getElementById('contact-submit');
    const toast = document.getElementById('contact-toast');

    if (!form) return;

    // Email validation
    function validateEmail(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(email);
    }

    // Real-time validation on blur
    if (emailInput) {
        emailInput.addEventListener('blur', () => {
            const val = emailInput.value.trim();
            if (val && !validateEmail(val)) {
                emailInput.classList.add('error');
                if (emailError) emailError.classList.add('visible');
            } else {
                emailInput.classList.remove('error');
                if (emailError) emailError.classList.remove('visible');
            }
        });
        emailInput.addEventListener('input', () => {
            emailInput.classList.remove('error');
            if (emailError) emailError.classList.remove('visible');
        });
    }

    /**
     * Send auto-reply confirmation email to the submitter via EmailJS.
     */
    async function sendAutoReply(name, email) {
        if (typeof emailjs === 'undefined') {
            console.warn('EmailJS SDK not available.');
            return false;
        }

        const templateParams = {
            to_email: email,
            to_name: name || 'there',
            from_name: 'KernelGuard Team',
            subject: "Thanks for reaching out! We'll be in touch.",
            message: "Hi " + (name || 'there') + ",\n\nThanks for getting in touch with us!\n\nOne of our team members is already looking over your message. We aim to get back to everyone as quickly as possible\u2014usually within a business day.\n\nIf you have anything else to add, just reply to this email. We're excited to see how we can work together!\n\nCheers,\nEren Ar\u0131 & The KernelGuard Team"
        };

        try {
            const result = await emailjs.send(EMAILJS_SERVICE_ID, EMAILJS_TEMPLATE_ID, templateParams);
            console.log('Auto-reply sent successfully:', result.status, result.text);
            return true;
        } catch (err) {
            console.error('Auto-reply failed:', err);
            return false;
        }
    }

    // Form submission
    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        const email = emailInput ? emailInput.value.trim() : '';
        if (!validateEmail(email)) {
            emailInput.classList.add('error');
            if (emailError) emailError.classList.add('visible');
            emailInput.focus();
            return;
        }

        // Capture values before reset
        const nameInput = form.querySelector('input[name="name"]');
        const senderName = nameInput ? nameInput.value.trim() : '';

        // Loading state
        submitBtn.classList.add('loading');
        submitBtn.disabled = true;

        // Run both in parallel so Formspree failure doesn't block auto-reply
        const formData = new FormData(form);

        const formspreePromise = fetch(form.action, {
            method: 'POST',
            body: formData,
            headers: { 'Accept': 'application/json' }
        }).catch(err => {
            console.warn('Formspree submission failed:', err);
        });

        const emailPromise = sendAutoReply(senderName, email);

        // Wait for both to finish
        await Promise.allSettled([formspreePromise, emailPromise]);

        // Show success toast
        if (toast) {
            toast.classList.add('visible');
            setTimeout(() => toast.classList.remove('visible'), 5000);
        }
        form.reset();

        submitBtn.classList.remove('loading');
        submitBtn.disabled = false;
    });
});
