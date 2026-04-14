
// Calculate relative path prefix for links if we're in a sub-directory
const basePath = window.location.pathname.includes('/pages/') || window.location.pathname.includes('/projects/') ? '../' : './';

// Fix static dropdown links dynamically depending on where the user is
document.addEventListener('DOMContentLoaded', () => {
    const dropdownLinks = document.querySelectorAll('.dropdown-item');
    dropdownLinks.forEach(link => {
        let href = link.getAttribute('href');
        if(href === 'pages/profile.html' || href === 'pages/settings.html' || href === 'index.html' || href === '#') {
           // Do not prepend if it's # format or absolute, etc.
           if(href !== '#') {
               link.setAttribute('href', basePath + href);
           }
        }
    });
});
document.addEventListener("DOMContentLoaded", () => {
    // 1. Language Dropdown
    const btnLang = document.getElementById('btn-lang');
    const dropdownLang = document.getElementById('dropdown-lang');
    
    // 2. User Dropdown (Mocking State)
    const btnUser = document.getElementById('btn-user');
    const dropdownUser = document.getElementById('dropdown-user');
    // 3. Help Panel
    const btnHelp = document.getElementById('btn-help');
    const panelHelp = document.getElementById('panel-help');
    const btnCloseHelp = document.getElementById('btn-close-help');
    const overlay = document.getElementById('overlay');

    // --- Overlay & Panel Handlers ---
    const openHelp = () => {
        if(panelHelp) panelHelp.classList.add('active');
        if(overlay) overlay.classList.add('active');
        closeAllDropdowns();
    };

    const closeHelp = () => {
        if(panelHelp) panelHelp.classList.remove('active');
        if(overlay) overlay.classList.remove('active');
    };

    if(btnHelp) btnHelp.addEventListener('click', openHelp);
    if(btnCloseHelp) btnCloseHelp.addEventListener('click', closeHelp);
    if(overlay) overlay.addEventListener('click', closeHelp);

    // --- Dropdown Handlers ---
    const closeAllDropdowns = () => {
        if(dropdownLang) dropdownLang.classList.remove('active');
        if(dropdownUser) dropdownUser.classList.remove('active');
    };

    if(btnLang) {
        btnLang.addEventListener('click', (e) => {
            e.stopPropagation();
            const isActive = dropdownLang.classList.contains('active');
            closeAllDropdowns();
            if(!isActive) dropdownLang.classList.add('active');
        });
    }

    if(btnUser) {
        btnUser.addEventListener('click', (e) => {
            e.stopPropagation();
            const isActive = dropdownUser.classList.contains('active');
            closeAllDropdowns();
            if(!isActive) dropdownUser.classList.add('active');
        });
    }

    // Auto close clicking outside
    document.addEventListener('click', () => {
        closeAllDropdowns();
    });

    // Search Overlay Logic
    const btnSearch = document.getElementById('btn-search');
    const searchOverlay = document.getElementById('search-overlay');
    const searchCloseBtn = document.getElementById('btn-search-close');
    const searchInput = document.getElementById('search-input');

    const closeSearch = () => {
        if(searchOverlay) searchOverlay.classList.remove('active');
    };

    if(btnSearch && searchOverlay) {
        btnSearch.addEventListener('click', (e) => {
            e.stopPropagation();
            closeAllDropdowns();
            closeHelp();
            searchOverlay.classList.add('active');
            if(searchInput) setTimeout(() => searchInput.focus(), 50);
        });
    }

    if(searchCloseBtn) {
        searchCloseBtn.addEventListener('click', closeSearch);
    }

    if(searchOverlay) {
        searchOverlay.addEventListener('click', (e) => {
            if(!e.target.closest('#search-input')) {
                closeSearch();
            }
        });
    }

    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            closeAllDropdowns();
            closeHelp();
            closeSearch();
        }
    });

    // --- Language Translation Logic (Full i18n) ---
    const langRows = document.querySelectorAll('.lang-row');

    langRows.forEach(row => {
        row.addEventListener('click', () => {
            const lang = row.getAttribute('data-lang');
            // Use the global applyTranslation from i18n.js
            if (typeof applyTranslation === 'function') {
                applyTranslation(lang);
            }
            // dropdown closes naturally from document bubbling
        });
    });

    // stop propagation on dropdown contents so clicking inside doesn't close
    if(dropdownLang) {
        dropdownLang.addEventListener('click', e => {
            if(!e.target.closest('.lang-row')) e.stopPropagation();
        });
    }
    if(dropdownUser) {
        dropdownUser.addEventListener('click', e => {
            if(!e.target.closest('.dropdown-item')) e.stopPropagation();
        });
    }

    // --- Settings Logic ---
    const saveBar = document.getElementById('sticky-save');
    const toast = document.getElementById('toast');

    if(saveBar) {
        let isDirty = false;
        
        document.querySelectorAll('.toggle-switch').forEach(toggle => {
            toggle.addEventListener('click', () => {
                toggle.classList.toggle('active');
                markDirty();
            });
        });

        document.querySelectorAll('.form-input').forEach(input => {
            input.addEventListener('input', () => {
                markDirty();
            });
        });

        function markDirty() {
            if(!isDirty) {
                isDirty = true;
                saveBar.classList.add('visible');
            }
        }

        const saveBtn = document.getElementById('btn-save');
        if(saveBtn) {
            saveBtn.addEventListener('click', () => {
                isDirty = false;
                saveBar.classList.remove('visible');
                
                if(toast) {
                    toast.classList.add('active');
                    setTimeout(() => {
                        toast.classList.remove('active');
                    }, 3000);
                }
            });
        }
    }
});
