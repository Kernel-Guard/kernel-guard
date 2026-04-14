import os, re, glob

# =====================================================
# 1. PREPEND THEME CSS VARIABLES TO style.css
# =====================================================
theme_css = '''
/* =====================================================
   Dark / Light Theme System
   ===================================================== */

/* Light Theme (default) — IBM Carbon Light */
:root,
[data-theme="light"] {
    --theme-bg: #FFFFFF;
    --theme-bg-secondary: #F4F4F4;
    --theme-bg-tertiary: #E0E0E0;
    --theme-border: #E0E0E0;
    --theme-text-primary: #161616;
    --theme-text-secondary: #6F6F6F;
    --theme-text-tertiary: #525252;
    --theme-nav-bg: #FFFFFF;
    --theme-card-bg: #F4F4F4;
    --theme-card-hover: #E0E0E0;
    --theme-hero-svg: #161616;
    --theme-tag-border: #C6C6C6;
    --theme-tag-text: #161616;
    --theme-action-hover-bg: #F4F4F4;
}

/* Dark Theme — Deep Charcoal Cybersecurity Palette */
[data-theme="dark"] {
    --theme-bg: #0D1117;
    --theme-bg-secondary: #161B22;
    --theme-bg-tertiary: #21262D;
    --theme-border: #30363D;
    --theme-text-primary: #E6EDF3;
    --theme-text-secondary: #8B949E;
    --theme-text-tertiary: #6E7681;
    --theme-nav-bg: #010409;
    --theme-card-bg: #161B22;
    --theme-card-hover: #21262D;
    --theme-hero-svg: #E6EDF3;
    --theme-tag-border: #30363D;
    --theme-tag-text: #E6EDF3;
    --theme-action-hover-bg: #21262D;
}

/* Core Overrides */
[data-theme="dark"] body,
[data-theme="dark"] {
    background-color: var(--theme-bg);
    color: var(--theme-text-primary);
}

[data-theme="dark"] .navbar {
    background-color: var(--theme-nav-bg);
    border-bottom-color: var(--theme-border);
}

[data-theme="dark"] a {
    color: var(--theme-text-primary);
}

[data-theme="dark"] .nav-action-btn {
    color: var(--theme-text-primary);
}
[data-theme="dark"] .nav-action-btn:hover {
    background-color: var(--theme-action-hover-bg);
}

/* Hero */
[data-theme="dark"] .hero {
    background-color: var(--theme-bg);
}
[data-theme="dark"] .hero-tagline {
    color: var(--theme-text-secondary);
}
[data-theme="dark"] .hero-visual svg {
    color: var(--theme-hero-svg);
}

/* Services */
[data-theme="dark"] .services {
    background-color: var(--theme-bg);
}
[data-theme="dark"] .service-card {
    background-color: var(--theme-card-bg);
    border-color: var(--theme-border);
}
[data-theme="dark"] .service-desc {
    color: var(--theme-text-secondary);
}
[data-theme="dark"] .service-icon svg {
    color: var(--theme-text-secondary);
}

/* Tech Stack */
[data-theme="dark"] .tech-stack {
    background-color: var(--theme-bg-secondary);
}
[data-theme="dark"] .tech-stack-label {
    color: var(--theme-text-tertiary);
}
[data-theme="dark"] .tech-logo {
    color: var(--theme-text-secondary);
}
[data-theme="dark"] .tech-logo svg {
    fill: var(--theme-text-tertiary);
}

/* Flagship Projects */
[data-theme="dark"] .featured {
    background-color: var(--theme-bg);
}
[data-theme="dark"] .projects-grid .project-card,
[data-theme="dark"] .projects-grid a {
    background-color: var(--theme-card-bg);
    color: var(--theme-text-primary);
}
[data-theme="dark"] .projects-grid .project-card:hover,
[data-theme="dark"] .projects-grid a:hover {
    background-color: var(--theme-card-hover);
}
[data-theme="dark"] .projects-grid p {
    color: var(--theme-text-secondary);
}

/* About Section */
[data-theme="dark"] .about {
    background-color: var(--theme-bg);
    border-top-color: var(--theme-border);
}
[data-theme="dark"] .about .carbon-list li {
    color: var(--theme-text-secondary);
}
[data-theme="dark"] .about .mission {
    color: var(--theme-text-secondary) !important;
}

/* Dropdowns */
[data-theme="dark"] .nav-dropdown {
    background-color: var(--theme-bg-secondary);
    border-color: var(--theme-border);
}
[data-theme="dark"] .dropdown-header {
    color: var(--theme-text-tertiary);
}
[data-theme="dark"] .lang-row {
    color: var(--theme-text-primary);
}
[data-theme="dark"] .lang-row:hover {
    background-color: var(--theme-bg-tertiary);
}
[data-theme="dark"] .dropdown-user-header {
    border-bottom-color: var(--theme-border);
}
[data-theme="dark"] .dropdown-item {
    color: var(--theme-text-primary);
}
[data-theme="dark"] .dropdown-item:hover {
    background-color: var(--theme-bg-tertiary);
}
[data-theme="dark"] .user-name {
    color: var(--theme-text-primary);
}
[data-theme="dark"] .user-email {
    color: var(--theme-text-secondary);
}

/* Help Panel */
[data-theme="dark"] .side-panel {
    background-color: var(--theme-bg-secondary);
    border-left-color: var(--theme-border);
}
[data-theme="dark"] .panel-header {
    border-bottom-color: var(--theme-border);
}
[data-theme="dark"] .panel-header h2 {
    color: var(--theme-text-primary);
}
[data-theme="dark"] .quick-link {
    color: var(--theme-text-primary);
    border-bottom-color: var(--theme-border);
}
[data-theme="dark"] .about-company-block {
    color: var(--theme-text-tertiary);
}
[data-theme="dark"] .panel-footer {
    border-top-color: var(--theme-border);
}

/* Search Overlay */
[data-theme="dark"] .nav-search-overlay {
    background-color: var(--theme-nav-bg);
    border-bottom-color: var(--theme-border);
}
[data-theme="dark"] .nav-search-input {
    color: var(--theme-text-primary);
}

/* Footer Bottom */
[data-theme="dark"] .footer-bottom {
    background-color: var(--theme-nav-bg);
    border-top-color: var(--theme-border);
}
[data-theme="dark"] .footer-bottom-text {
    color: var(--theme-text-tertiary);
}
[data-theme="dark"] .footer-nav a {
    color: var(--theme-text-secondary);
}
[data-theme="dark"] .footer-social a {
    color: var(--theme-text-secondary);
}

/* Project Detail Pages */
[data-theme="dark"] .project-page {
    background-color: var(--theme-bg);
}
[data-theme="dark"] .project-title {
    color: var(--theme-text-primary);
}
[data-theme="dark"] .project-desc {
    color: var(--theme-text-secondary);
}
[data-theme="dark"] .project-tag {
    border-color: var(--theme-tag-border);
    color: var(--theme-tag-text);
}
[data-theme="dark"] .project-grid .project-card {
    background-color: var(--theme-card-bg);
}
[data-theme="dark"] .project-card-header {
    color: var(--theme-text-primary);
}
[data-theme="dark"] .project-card p {
    color: var(--theme-text-secondary);
}
[data-theme="dark"] .project-back {
    color: var(--theme-text-secondary);
}

/* Overlay */
[data-theme="dark"] .overlay-backdrop {
    background-color: rgba(0, 0, 0, 0.6);
}

/* Theme Toggle Button Animation */
.theme-toggle {
    position: relative;
    overflow: hidden;
}
.theme-toggle .icon-sun,
.theme-toggle .icon-moon {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    transition: opacity 0.3s ease, transform 0.3s ease;
}
.theme-toggle .icon-sun {
    opacity: 1;
    transform: translate(-50%, -50%) rotate(0deg);
}
.theme-toggle .icon-moon {
    opacity: 0;
    transform: translate(-50%, -50%) rotate(-90deg);
}
[data-theme="dark"] .theme-toggle .icon-sun {
    opacity: 0;
    transform: translate(-50%, -50%) rotate(90deg);
}
[data-theme="dark"] .theme-toggle .icon-moon {
    opacity: 1;
    transform: translate(-50%, -50%) rotate(0deg);
}

/* Smooth global transition */
body,
.navbar,
.service-card,
.project-card,
.side-panel,
.nav-dropdown,
.footer-bottom,
.nav-search-overlay {
    transition: background-color 0.3s ease, color 0.3s ease, border-color 0.3s ease;
}
'''

with open('css/style.css', 'a', encoding='utf-8') as f:
    f.write(theme_css)
print("Appended theme CSS")

# =====================================================
# 2. ADD THEME TOGGLE BUTTON TO ALL HTML FILES
# =====================================================

# The toggle button HTML — placed right before the search button
toggle_btn_html = '''<button class="nav-action-btn theme-toggle" id="btn-theme" aria-label="Toggle Theme" title="Toggle Theme">
                    <svg class="icon-sun" viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/></svg>
                    <svg class="icon-moon" viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.79A9 9 0 1111.21 3 7 7 0 0021 12.79z"/></svg>
                </button>
                '''

all_files = ['index.html'] + glob.glob('pages/*.html') + glob.glob('projects/*.html')
for f_path in all_files:
    with open(f_path, 'r', encoding='utf-8') as f:
        c = f.read()
    
    # Only add if not already present
    if 'btn-theme' not in c:
        # Insert right before the search button
        c = c.replace(
            '<button class="nav-action-btn" id="btn-search"',
            toggle_btn_html + '<button class="nav-action-btn" id="btn-search"'
        )
    
    with open(f_path, 'w', encoding='utf-8') as f:
        f.write(c)

print("Added theme toggle button to all HTML files")

print("Done! Theme system installed.")
