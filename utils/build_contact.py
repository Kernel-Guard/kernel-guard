import os, re, glob

# =====================================================
# 1. APPEND CONTACT FORM CSS
# =====================================================
contact_css = '''

/* =====================================================
   Contact Section — Dark-Themed High-Conversion Form
   ===================================================== */
.contact-section {
    background-color: var(--color-gray-100);
    color: var(--color-white);
    padding: 96px 0 64px;
}
.contact-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 64px;
    align-items: start;
}
.contact-header h2 {
    font-size: 36px;
    font-weight: 400;
    margin-bottom: 16px;
    color: var(--color-white);
}
.contact-header p {
    font-size: 16px;
    color: var(--color-gray-30);
    line-height: 1.6;
    margin-bottom: 48px;
}

/* Form */
.contact-form-group {
    margin-bottom: 24px;
}
.contact-form-group label {
    display: block;
    font-size: 12px;
    font-family: var(--font-mono);
    text-transform: uppercase;
    letter-spacing: 1px;
    color: var(--color-gray-30);
    margin-bottom: 8px;
}
.contact-input {
    width: 100%;
    background: var(--color-gray-90);
    border: none;
    border-bottom: 2px solid var(--color-gray-70);
    color: var(--color-white);
    font-family: var(--font-sans);
    font-size: 16px;
    padding: 12px 16px;
    outline: none;
    transition: border-color 0.2s;
}
.contact-input::placeholder {
    color: var(--color-gray-60);
}
.contact-input:focus {
    border-bottom-color: #08BDBA;
}
.contact-input.error {
    border-bottom-color: #FA4D56;
}
.contact-textarea {
    resize: vertical;
    min-height: 120px;
}
.contact-error-msg {
    font-size: 12px;
    color: #FA4D56;
    margin-top: 4px;
    display: none;
}
.contact-error-msg.visible {
    display: block;
}
.contact-submit {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background-color: var(--color-blue-60);
    color: var(--color-white);
    font-family: var(--font-sans);
    font-size: 16px;
    font-weight: 400;
    border: none;
    padding: 14px 32px;
    cursor: pointer;
    transition: background-color 0.15s;
    margin-top: 8px;
    min-width: 180px;
    justify-content: center;
}
.contact-submit:hover {
    background-color: var(--color-blue-80);
}
.contact-submit:disabled {
    opacity: 0.6;
    cursor: not-allowed;
}
.contact-submit .spinner {
    display: none;
    width: 16px;
    height: 16px;
    border: 2px solid rgba(255,255,255,0.3);
    border-top-color: #fff;
    border-radius: 50%;
    animation: spin 0.6s linear infinite;
}
.contact-submit.loading .spinner {
    display: inline-block;
}
.contact-submit.loading .btn-text {
    display: none;
}
@keyframes spin {
    to { transform: rotate(360deg); }
}

/* Success Toast */
.contact-toast {
    position: fixed;
    bottom: -80px;
    left: 50%;
    transform: translateX(-50%);
    background: var(--color-gray-90);
    color: var(--color-white);
    padding: 16px 32px;
    font-size: 14px;
    font-family: var(--font-sans);
    border-left: 4px solid #24A148;
    z-index: 9999;
    transition: bottom 0.4s ease;
    display: flex;
    align-items: center;
    gap: 12px;
}
.contact-toast.visible {
    bottom: 32px;
}
.contact-toast svg {
    flex-shrink: 0;
}

/* Team Cards */
.team-cards {
    display: flex;
    flex-direction: column;
    gap: 16px;
}
.team-card {
    display: flex;
    align-items: center;
    gap: 16px;
    background: var(--color-gray-90);
    padding: 20px 24px;
    text-decoration: none;
    color: var(--color-white);
    transition: background 0.15s;
    border-left: 3px solid transparent;
}
.team-card:hover {
    background: var(--color-gray-70);
    border-left-color: var(--color-blue-60);
}
.team-avatar {
    width: 48px;
    height: 48px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: var(--font-mono);
    font-weight: 600;
    font-size: 16px;
    background: var(--color-gray-70);
    flex-shrink: 0;
}
.team-info {
    flex: 1;
}
.team-info .name {
    font-weight: 600;
    font-size: 16px;
    margin-bottom: 2px;
}
.team-info .role {
    font-size: 13px;
    color: var(--color-gray-30);
}
.team-card svg {
    color: var(--color-gray-30);
    flex-shrink: 0;
}
.team-card:hover svg {
    color: var(--color-white);
}

/* Responsive */
@media (max-width: 768px) {
    .contact-grid {
        grid-template-columns: 1fr;
        gap: 48px;
    }
}
'''

with open('css/style.css', 'a', encoding='utf-8') as f:
    f.write(contact_css)
print("Appended contact CSS")

# =====================================================
# 2. REPLACE FOOTER SECTION IN INDEX.HTML
# =====================================================
with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

new_contact_html = '''
    <!-- Contact Section -->
    <section class="contact-section" id="contact">
        <div class="container">
            <div class="contact-grid">
                <!-- Left: Form -->
                <div>
                    <div class="contact-header">
                        <h2 data-i18n="contact.title">Ready to build something serious?</h2>
                        <p data-i18n="contact.desc">For collaborations, partnerships, or technical discussions — reach out directly. We respond within 24 hours.</p>
                    </div>
                    <form id="contact-form" action="https://formspree.io/f/xyzgobrl" method="POST">
                        <div class="contact-form-group">
                            <label data-i18n="contact.name">Name</label>
                            <input type="text" name="name" class="contact-input" placeholder="Your full name" required data-i18n-placeholder="contact.name.placeholder">
                        </div>
                        <div class="contact-form-group">
                            <label data-i18n="contact.org">Organization</label>
                            <input type="text" name="organization" class="contact-input" placeholder="Company or institution" data-i18n-placeholder="contact.org.placeholder">
                        </div>
                        <div class="contact-form-group">
                            <label data-i18n="contact.email">Work Email</label>
                            <input type="email" name="email" id="contact-email" class="contact-input" placeholder="you@company.com" required data-i18n-placeholder="contact.email.placeholder">
                            <div class="contact-error-msg" id="email-error" data-i18n="contact.email.error">Please enter a valid email address.</div>
                        </div>
                        <div class="contact-form-group">
                            <label data-i18n="contact.message">Message</label>
                            <textarea name="message" class="contact-input contact-textarea" placeholder="Tell us about your project or inquiry..." required data-i18n-placeholder="contact.message.placeholder"></textarea>
                        </div>
                        <button type="submit" class="contact-submit" id="contact-submit">
                            <span class="btn-text" data-i18n="contact.send">Send Message</span>
                            <div class="spinner"></div>
                        </button>
                    </form>
                </div>

                <!-- Right: Team Cards -->
                <div>
                    <div class="contact-header">
                        <h2 data-i18n="contact.team.title">Connect with the Team</h2>
                        <p data-i18n="contact.team.desc">Our founding engineers are available on LinkedIn for professional inquiries and collaboration.</p>
                    </div>
                    <div class="team-cards">
                        <a href="https://www.linkedin.com/in/" target="_blank" class="team-card">
                            <div class="team-avatar">AY</div>
                            <div class="team-info">
                                <div class="name">Ahmet Yılmaz</div>
                                <div class="role" data-i18n="contact.team.role1">Systems Engineer — eBPF & Kernel Security</div>
                            </div>
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.064 2.064 0 112.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
                        </a>
                        <a href="https://www.linkedin.com/in/" target="_blank" class="team-card">
                            <div class="team-avatar">MK</div>
                            <div class="team-info">
                                <div class="name">Mehmet Kaya</div>
                                <div class="role" data-i18n="contact.team.role2">Full-Stack Engineer — Cloud & Infrastructure</div>
                            </div>
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.064 2.064 0 112.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
                        </a>
                        <a href="https://www.linkedin.com/in/" target="_blank" class="team-card">
                            <div class="team-avatar">EÖ</div>
                            <div class="team-info">
                                <div class="name">Elif Özdemir</div>
                                <div class="role" data-i18n="contact.team.role3">Software Engineer — AI & Scalable Platforms</div>
                            </div>
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.064 2.064 0 112.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer Bottom Bar -->
    <footer>
        <div class="footer-bottom">
            <div class="container">
                <div class="footer-bottom-text">
                    KernelGuard Inc. &copy; 2026
                </div>
                <div class="footer-nav">
                    <a href="#services" data-i18n="nav.whatWeBuild">What We Build</a>
                    <a href="#work" data-i18n="nav.projects">Projects</a>
                    <a href="#about" data-i18n="nav.about">About</a>
                </div>
                <div class="footer-social">
                    <a href="https://github.com/Kernel-Guard" aria-label="GitHub">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.477 2 2 6.477 2 12c0 4.418 2.865 8.166 6.839 9.489.5.092.682-.217.682-.482 0-.237-.008-.866-.013-1.7-2.782.603-3.369-1.34-3.369-1.34-.454-1.156-1.11-1.464-1.11-1.464-.908-.62.069-.608.069-.608 1.003.07 1.531 1.03 1.531 1.03.892 1.529 2.341 1.087 2.91.831.092-.646.35-1.086.636-1.336-2.22-.253-4.555-1.11-4.555-4.943 0-1.091.39-1.984 1.029-2.683-.103-.253-.446-1.27.098-2.647 0 0 .84-.269 2.75 1.025A9.578 9.578 0 0112 6.836c.85.004 1.705.114 2.504.336 1.909-1.294 2.747-1.025 2.747-1.025.546 1.379.203 2.394.1 2.647.64.699 1.028 1.592 1.028 2.683 0 3.842-2.339 4.687-4.566 4.935.359.309.678.919.678 1.852 0 1.336-.012 2.415-.012 2.743 0 .267.18.578.688.48C19.138 20.161 22 16.416 22 12c0-5.523-4.477-10-10-10z"/></svg>
                    </a>
                    <a href="https://www.linkedin.com/company/kernel-guard/" aria-label="LinkedIn">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.064 2.064 0 112.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
                    </a>
                </div>
            </div>
        </div>
    </footer>

    <!-- Success Toast -->
    <div class="contact-toast" id="contact-toast">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#24A148" stroke-width="2"><path d="M22 11.08V12a10 10 0 11-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
        <span data-i18n="contact.toast">Message sent successfully. We'll be in touch soon.</span>
    </div>
'''

# Replace the old footer section
c = re.sub(
    r'    <!-- Footer -->.*?</footer>',
    new_contact_html,
    c, flags=re.DOTALL
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)
print("Updated index.html with contact section")

# =====================================================
# 3. ADD i18n TRANSLATIONS FOR CONTACT
# =====================================================
contact_translations = {
    'en': {
        "contact.title": "Ready to build something serious?",
        "contact.desc": "For collaborations, partnerships, or technical discussions — reach out directly. We respond within 24 hours.",
        "contact.name": "Name",
        "contact.name.placeholder": "Your full name",
        "contact.org": "Organization",
        "contact.org.placeholder": "Company or institution",
        "contact.email": "Work Email",
        "contact.email.placeholder": "you@company.com",
        "contact.email.error": "Please enter a valid email address.",
        "contact.message": "Message",
        "contact.message.placeholder": "Tell us about your project or inquiry...",
        "contact.send": "Send Message",
        "contact.sending": "Sending...",
        "contact.toast": "Message sent successfully. We'll be in touch soon.",
        "contact.team.title": "Connect with the Team",
        "contact.team.desc": "Our founding engineers are available on LinkedIn for professional inquiries and collaboration.",
        "contact.team.role1": "Systems Engineer — eBPF & Kernel Security",
        "contact.team.role2": "Full-Stack Engineer — Cloud & Infrastructure",
        "contact.team.role3": "Software Engineer — AI & Scalable Platforms",
    },
    'tr': {
        "contact.title": "Ciddi bir şey inşa etmeye hazır mısınız?",
        "contact.desc": "İş birlikleri, ortaklıklar veya teknik tartışmalar için doğrudan bize ulaşın. 24 saat içinde yanıt veriyoruz.",
        "contact.name": "İsim",
        "contact.name.placeholder": "Tam adınız",
        "contact.org": "Kuruluş",
        "contact.org.placeholder": "Şirket veya kurum",
        "contact.email": "İş E-postası",
        "contact.email.placeholder": "siz@sirket.com",
        "contact.email.error": "Lütfen geçerli bir e-posta adresi girin.",
        "contact.message": "Mesaj",
        "contact.message.placeholder": "Projeniz veya sorunuz hakkında bilgi verin...",
        "contact.send": "Mesaj Gönder",
        "contact.sending": "Gönderiliyor...",
        "contact.toast": "Mesaj başarıyla gönderildi. En kısa sürede dönüş yapacağız.",
        "contact.team.title": "Ekible İletişim Kurun",
        "contact.team.desc": "Kurucu mühendislerimiz profesyonel sorular ve iş birliği için LinkedIn'de mevcuttur.",
        "contact.team.role1": "Sistem Mühendisi — eBPF ve Çekirdek Güvenliği",
        "contact.team.role2": "Full-Stack Mühendis — Bulut ve Altyapı",
        "contact.team.role3": "Yazılım Mühendisi — YZ ve Ölçeklenebilir Platformlar",
    },
    'de': {
        "contact.title": "Bereit, etwas Ernsthaftes zu bauen?",
        "contact.desc": "Für Zusammenarbeit, Partnerschaften oder technische Diskussionen — kontaktieren Sie uns direkt. Wir antworten innerhalb von 24 Stunden.",
        "contact.name": "Name",
        "contact.name.placeholder": "Ihr vollständiger Name",
        "contact.org": "Organisation",
        "contact.org.placeholder": "Unternehmen oder Institution",
        "contact.email": "Geschäfts-E-Mail",
        "contact.email.placeholder": "sie@unternehmen.com",
        "contact.email.error": "Bitte geben Sie eine gültige E-Mail-Adresse ein.",
        "contact.message": "Nachricht",
        "contact.message.placeholder": "Erzählen Sie uns von Ihrem Projekt oder Ihrer Anfrage...",
        "contact.send": "Nachricht senden",
        "contact.sending": "Wird gesendet...",
        "contact.toast": "Nachricht erfolgreich gesendet. Wir melden uns in Kürze.",
        "contact.team.title": "Verbinden Sie sich mit dem Team",
        "contact.team.desc": "Unsere Gründungsingenieure sind auf LinkedIn für professionelle Anfragen und Zusammenarbeit verfügbar.",
        "contact.team.role1": "Systemingenieur — eBPF & Kernel-Sicherheit",
        "contact.team.role2": "Full-Stack-Ingenieur — Cloud & Infrastruktur",
        "contact.team.role3": "Softwareingenieur — KI & skalierbare Plattformen",
    },
    'fr': {
        "contact.title": "Prêt à construire quelque chose de sérieux ?",
        "contact.desc": "Pour des collaborations, des partenariats ou des discussions techniques — contactez-nous directement. Nous répondons sous 24 heures.",
        "contact.name": "Nom",
        "contact.name.placeholder": "Votre nom complet",
        "contact.org": "Organisation",
        "contact.org.placeholder": "Entreprise ou institution",
        "contact.email": "E-mail professionnel",
        "contact.email.placeholder": "vous@entreprise.com",
        "contact.email.error": "Veuillez entrer une adresse e-mail valide.",
        "contact.message": "Message",
        "contact.message.placeholder": "Parlez-nous de votre projet ou de votre demande...",
        "contact.send": "Envoyer le message",
        "contact.sending": "Envoi en cours...",
        "contact.toast": "Message envoyé avec succès. Nous vous répondrons bientôt.",
        "contact.team.title": "Connectez-vous avec l'Équipe",
        "contact.team.desc": "Nos ingénieurs fondateurs sont disponibles sur LinkedIn pour les demandes professionnelles et la collaboration.",
        "contact.team.role1": "Ingénieur Systèmes — eBPF & Sécurité Noyau",
        "contact.team.role2": "Ingénieur Full-Stack — Cloud & Infrastructure",
        "contact.team.role3": "Ingénieur Logiciel — IA & Plateformes Scalables",
    }
}

# Inject into i18n.js
with open('js/i18n.js', 'r', encoding='utf-8') as f:
    i18n = f.read()

for lang, entries in contact_translations.items():
    for key, value in entries.items():
        # Find the closing of that language block and insert before it
        # Pattern: find the last entry before the closing } of a lang block
        # We add after the last existing key, before closing }
        escaped_value = value.replace("'", "\\'")
        new_line = f'        "{key}": \'{escaped_value}\','
        # Find the lang block opening
        # Pattern: lang: {\n ... project.viewStorefront or similar last key... \n    }
        # Insert just before the closing } of each language object
        pattern = rf'("{lang}":\s*\{{)'
        # Simpler: find the LAST key in the block and add after it
        # Actually, let's just find the pattern like "project.viewStorefront": "..." and add after the line
        pass  # We'll do a different approach

# Simpler approach: just append all new keys to each language block
# by finding the last entry pattern and inserting after
for lang in ['en', 'tr', 'de', 'fr']:
    entries = contact_translations[lang]
    new_entries = '\n'.join([f'        "{k}": \'{v.replace(chr(39), chr(92)+chr(39))}\',' for k, v in entries.items()])
    
    # Find the closing of the lang block
    # The structure is:     },\n\n    de: {  or     }\n};
    if lang == 'en':
        # Find last entry before the tr block
        i18n = i18n.replace(
            '        "project.viewStorefront": "View Storefront"\n    },\n\n    tr:',
            f'        "project.viewStorefront": "View Storefront",\n\n        // Contact\n{new_entries}\n    }},\n\n    tr:'
        )
    elif lang == 'tr':
        i18n = i18n.replace(
            '        "project.viewStorefront": "Mağazayı Görüntüle"\n    },\n\n    de:',
            f'        "project.viewStorefront": "Mağazayı Görüntüle",\n\n        // İletişim\n{new_entries}\n    }},\n\n    de:'
        )
    elif lang == 'de':
        i18n = i18n.replace(
            '        "project.viewStorefront": "Storefront anzeigen"\n    },\n\n    fr:',
            f'        "project.viewStorefront": "Storefront anzeigen",\n\n        // Kontakt\n{new_entries}\n    }},\n\n    fr:'
        )
    elif lang == 'fr':
        i18n = i18n.replace(
            '        "project.viewStorefront": "Voir la Boutique"\n    }\n};',
            f'        "project.viewStorefront": "Voir la Boutique",\n\n        // Contact\n{new_entries}\n    }}\n}};'
        )

with open('js/i18n.js', 'w', encoding='utf-8') as f:
    f.write(i18n)
print("Updated i18n.js with contact translations")

print("Done! Contact section fully built.")
