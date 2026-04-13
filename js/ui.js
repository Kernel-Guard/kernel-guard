document.addEventListener("DOMContentLoaded", () => {
    // 1. Language Dropdown
    const btnLang = document.getElementById('btn-lang');
    const dropdownLang = document.getElementById('dropdown-lang');
    
    // 2. User Dropdown (Mocking State)
    const btnUser = document.getElementById('btn-user');
    const dropdownUser = document.getElementById('dropdown-user');
    const btnLogout = document.getElementById('btn-logout');
    
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

    // --- Language Translation Logic (Mock) ---
    const langRows = document.querySelectorAll('.lang-row');
    const dummyDict = {
        'en': { tagline: "Kernel Guard builds secure systems, intelligent infrastructure, and scalable web platforms.<br><br>We focus on cybersecurity..." },
        'tr': { tagline: "Kernel Guard güvenli sistemler, akıllı altyapılar ve ölçeklenebilir web platformları kurar.<br><br>Siber güvenliğe odaklanıyoruz..." },
        'de': { tagline: "Kernel Guard baut sichere Systeme, intelligente Infrastruktur und skalierbare Webplattformen auf.<br><br>Wir konzentrieren uns auf Cybersicherheit..." },
        'fr': { tagline: "Kernel Guard crée des systèmes sécurisés, des infrastructures intelligentes et des plateformes web évolutives..." }
    };
    const heroTagline = document.querySelector('.hero-tagline');

    langRows.forEach(row => {
        row.addEventListener('click', () => {
            const lang = row.getAttribute('data-lang');
            langRows.forEach(r => r.classList.remove('active'));
            row.classList.add('active');
            
            // Apply mock translation to tagline
            if(heroTagline && dummyDict[lang]) {
                heroTagline.innerHTML = dummyDict[lang].tagline;
            }

            // Decorator dot on globe
            if(lang !== 'en') {
                btnLang.classList.add('active');
            } else {
                btnLang.classList.remove('active');
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

    // --- Logout Mock logic ---
    if(btnLogout) {
        btnLogout.addEventListener('click', () => {
            alert('Successfully logged out.');
            if(dropdownUser) {
                dropdownUser.innerHTML = `
                    <a href="#" class="dropdown-item">Log In</a>
                    <a href="#" class="dropdown-item">Sign Up</a>
                `;
            }
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
