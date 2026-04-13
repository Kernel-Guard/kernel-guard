document.addEventListener("DOMContentLoaded", () => {
    const observerOptions = {
      root: null,
      rootMargin: "0px",
      threshold: 0.1
    };
  
    const intersectionObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
            // Add visible class
            entry.target.classList.add('visible');
            // Stop observing once animated
            observer.unobserve(entry.target);
        }
      });
    }, observerOptions);
  
    // Find all fade-up elements and add them to the observer
    const fadeElements = document.querySelectorAll('.fade-up');
    
    // To handle staggering, we can group elements in the same row/container
    // Or simpler: handle staggered transition delays in CSS based on child-index or add style dynamically
    fadeElements.forEach((el, index) => {
        // Find if it's part of a grid, e.g. services, tech logos, or timeline
        // If it's a descendant of a grid, grab its index among siblings for a delay
        const parent = el.parentElement;
        const siblings = Array.from(parent.children).filter(child => child.classList.contains('fade-up'));
        
        let delayIndex = 0;
        if (siblings.length > 1) {
            delayIndex = siblings.indexOf(el);
        }

        // Apply dynamic delay (staggered 100ms per element)
        if (delayIndex > 0) {
            el.style.transitionDelay = `${delayIndex * 100}ms`;
        }

        intersectionObserver.observe(el);
    });
});
