/**
 * KernelGuard Theme Toggle
 * - Detects OS preference (prefers-color-scheme)
 * - Allows manual override stored in localStorage
 * - Animated sun/moon icon transition
 * - Applies to all pages via shared script
 */

(function () {
    const STORAGE_KEY = 'kg-theme';

    // Determine initial theme: localStorage > OS preference > light
    function getPreferredTheme() {
        const stored = localStorage.getItem(STORAGE_KEY);
        if (stored) return stored;

        // Check OS-level preference
        if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
            return 'dark';
        }
        return 'light';
    }

    // Apply theme to the document
    function applyTheme(theme) {
        document.documentElement.setAttribute('data-theme', theme);
        localStorage.setItem(STORAGE_KEY, theme);
    }

    // Apply immediately (before DOMContentLoaded) to prevent flash
    applyTheme(getPreferredTheme());

    // Listen for OS preference changes in real-time
    if (window.matchMedia) {
        window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
            // Only auto-switch if user hasn't manually set a preference
            if (!localStorage.getItem(STORAGE_KEY)) {
                applyTheme(e.matches ? 'dark' : 'light');
            }
        });
    }

    // Wire up the toggle button
    document.addEventListener('DOMContentLoaded', () => {
        const btn = document.getElementById('btn-theme');
        if (!btn) return;

        btn.addEventListener('click', () => {
            const current = document.documentElement.getAttribute('data-theme') || 'light';
            const next = current === 'dark' ? 'light' : 'dark';
            applyTheme(next);
        });
    });
})();
