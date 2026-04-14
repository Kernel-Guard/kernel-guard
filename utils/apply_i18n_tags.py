import os
import re
import glob

# =============================================================================
# This script adds data-i18n attributes to all translatable text elements
# across all HTML files, and wires up the i18n.js script.
# =============================================================================

def add_i18n_script_tag(content):
    """Add <script src="...js/i18n.js" defer></script> if not already present."""
    if 'i18n.js' in content:
        return content
    # Insert right after ui.js script tag
    content = content.replace(
        '<script src="js/ui.js" defer></script>',
        '<script src="js/i18n.js" defer></script>\n    <script src="js/ui.js" defer></script>'
    )
    content = content.replace(
        '<script src="../js/ui.js" defer></script>',
        '<script src="../js/i18n.js" defer></script>\n    <script src="../js/ui.js" defer></script>'
    )
    return content

def tag_index_html(content):
    """Add data-i18n attributes to index.html translatable elements."""

    # Nav links
    content = content.replace(
        '<a href="#services">What We Build</a>',
        '<a href="#services" data-i18n="nav.whatWeBuild">What We Build</a>'
    )
    content = content.replace(
        '<a href="#work">Projects</a>',
        '<a href="#work" data-i18n="nav.projects">Projects</a>'
    )
    content = content.replace(
        '<a href="#about">About</a>',
        '<a href="#about" data-i18n="nav.about">About</a>'
    )
    content = content.replace(
        '<a href="#contact">Contact</a>',
        '<a href="#contact" data-i18n="nav.contact">Contact</a>'
    )

    # Search placeholder
    content = content.replace(
        'placeholder="Search all of KernelGuard"',
        'placeholder="Search all of KernelGuard" data-i18n-placeholder="nav.search.placeholder"'
    )

    # Language dropdown header
    content = content.replace(
        '<div class="dropdown-header">Select Language</div>',
        '<div class="dropdown-header" data-i18n="nav.lang.header">Select Language</div>'
    )

    # Help panel
    content = content.replace(
        '<h2>Help &amp; Information</h2>',
        '<h2 data-i18n="nav.help.title">Help &amp; Information</h2>'
    )

    # Help quick links (be careful with SVG inside)
    for old, key in [
        ('Getting Started', 'nav.help.gettingStarted'),
        ('Documentation', 'nav.help.documentation'),
        ('API Reference', 'nav.help.apiReference'),
        ('Security Policy', 'nav.help.securityPolicy'),
    ]:
        # We need to wrap the text node, not the SVG
        # Pattern: >TEXT <svg  -> ><span data-i18n="key">TEXT</span> <svg
        content = content.replace(
            f'>{old} <svg',
            f'><span data-i18n="{key}">{old}</span> <svg'
        )

    # About company block
    content = content.replace(
        'KernelGuard Inc.<br>\n                Secure Systems Infrastructure<br>\n                v2.1.0-beta',
        '<span data-i18n="nav.help.companyBlock">KernelGuard Inc.<br>Secure Systems Infrastructure<br>v2.1.0-beta</span>'
    )
    # Try alternate whitespace patterns
    content = re.sub(
        r'KernelGuard Inc\.\s*<br>\s*Secure Systems Infrastructure\s*<br>\s*v2\.1\.0-beta',
        '<span data-i18n="nav.help.companyBlock">KernelGuard Inc.<br>Secure Systems Infrastructure<br>v2.1.0-beta</span>',
        content
    )

    # Contact Support button
    content = content.replace(
        '>Contact Support →</button>',
        ' data-i18n="nav.help.contactSupport">Contact Support →</button>'
    )

    # User dropdown
    content = content.replace(
        '<div class="user-name">KernelGuard Team</div>',
        '<div class="user-name" data-i18n="nav.user.teamName">KernelGuard Team</div>'
    )
    # Team desc in user-email div
    content = re.sub(
        r'<div class="user-email"[^>]*>A specialized 3-person.*?</div>',
        '<div class="user-email" style="white-space: normal; line-height: 1.5; margin-top: 8px;" data-i18n="nav.user.teamDesc">A specialized 3-person development collective focused on systems engineering, rigorous cybersecurity, and scalable full-stack infrastructure.</div>',
        content, flags=re.DOTALL
    )
    content = content.replace(
        '>My Profile</a>',
        ' data-i18n="nav.user.myProfile">My Profile</a>'
    )
    content = content.replace(
        '>My Projects</a>',
        ' data-i18n="nav.user.myProjects">My Projects</a>'
    )

    # Hero section
    content = re.sub(
        r'<p class="hero-tagline[^"]*"[^>]*>.*?</p>',
        '<p class="hero-tagline fade-up" data-i18n="hero.tagline">Kernel Guard builds secure systems, intelligent infrastructure, and scalable web platforms.<br><br>We focus on cybersecurity, systems engineering, and production-grade software designed for reliability, performance, and long-term maintainability.</p>',
        content, flags=re.DOTALL
    )
    content = content.replace(
        '>See Our Work</a>',
        ' data-i18n="hero.cta">See Our Work</a>'
    )

    # Services section title
    content = re.sub(
        r'(<h2 class="text-section-title fade-up"[^>]*>)What We Build(</h2>)',
        r'\1<span data-i18n="services.title">What We Build</span>\2',
        content
    )

    # Service cards
    service_map = [
        ('Secure systems and security-focused infrastructure.', 'services.secure'),
        ('Intelligent platforms powered by AI and data-driven engineering.', 'services.intelligent'),
        ('Scalable backend and web applications.', 'services.scalable'),
        ('High-performance software with strong operational discipline.', 'services.highPerf'),
    ]
    for text, key in service_map:
        content = content.replace(
            f'<p class="service-desc">{text}</p>',
            f'<p class="service-desc" data-i18n="{key}">{text}</p>'
        )

    # Core Areas title
    content = content.replace(
        '>Core Areas</h2>',
        ' data-i18n="core.title">Core Areas</h2>'
    )

    # Core area items - these have SVG icons followed by text
    core_map = [
        ('Cybersecurity Engineering', 'core.cybersecurity'),
        ('eBPF and Runtime Security', 'core.ebpf'),
        ('Systems Programming', 'core.systems'),
        ('Cloud and Infrastructure Engineering', 'core.cloud'),
        ('AI-Driven Systems', 'core.ai'),
        ('Scalable Web Platforms', 'core.web'),
    ]
    for text, key in core_map:
        # Pattern: </svg> Text</div>  ->  </svg> <span data-i18n="key">Text</span></div>
        content = content.replace(
            f'</svg> {text}</div>',
            f'</svg> <span data-i18n="{key}">{text}</span></div>'
        )

    # Flagship Projects title
    content = content.replace(
        '>Flagship Projects</h2>',
        ' data-i18n="projects.title">Flagship Projects</h2>'
    )
    content = content.replace(
        '>Open Source Projects</div>',
        ' data-i18n="projects.openSource">Open Source Projects</div>'
    )
    content = content.replace(
        '>Closed Source Projects (Demos)</div>',
        ' data-i18n="projects.closedSource">Closed Source Projects (Demos)</div>'
    )

    # Project cards
    proj_map = [
        ('Aegis-BPF', 'projects.aegis.title',
         'A runtime security engine built with eBPF CO-RE and LSM-based enforcement, designed for synchronous kernel-level protection.', 'projects.aegis.desc'),
        ('CathodeX', 'projects.cathodex.title',
         'High-performance userspace networking stack engineered in C, optimized for massive concurrency and determinism.', 'projects.cathodex.desc'),
        ('EduHub Campus', 'projects.eduhub.title',
         'A B2B enterprise room and resource reservation system with secure tenant-based isolation and audit trails.', 'projects.eduhub.desc'),
        ('Ref Atelier', 'projects.refatelier.title',
         'A high-performance luxury e-commerce frontend architecture ensuring fast load times and seamless localization.', 'projects.refatelier.desc'),
    ]
    for title, title_key, desc, desc_key in proj_map:
        content = content.replace(
            f'<h3>{title}</h3>',
            f'<h3 data-i18n="{title_key}">{title}</h3>'
        )
        content = content.replace(
            f'<p>{desc}</p>',
            f'<p data-i18n="{desc_key}">{desc}</p>'
        )

    # About / Engineering Principles
    content = content.replace(
        '>Engineering Principles</h2>',
        ' data-i18n="about.principles.title">Engineering Principles</h2>'
    )
    content = content.replace(
        '>We value:</p>',
        ' data-i18n="about.principles.weValue">We value:</p>'
    )
    principles_map = [
        ('Security by design', 'about.principles.security'),
        ('Measured performance', 'about.principles.performance'),
        ('Clear operational contracts', 'about.principles.contracts'),
        ('Production readiness', 'about.principles.production'),
        ('Evidence over claims', 'about.principles.evidence'),
    ]
    for text, key in principles_map:
        content = content.replace(
            f'<li>{text}</li>',
            f'<li data-i18n="{key}">{text}</li>'
        )

    content = content.replace(
        '>Mission</h2>',
        ' data-i18n="about.mission.title">Mission</h2>'
    )
    content = re.sub(
        r'(<p class="mission"[^>]*>)\s*Kernel Guard exists to build software.*?</p>',
        r'\1<span data-i18n="about.mission.text">Kernel Guard exists to build software that is not only functional, but secure, resilient, and engineered to hold up under real-world conditions.</span></p>',
        content, flags=re.DOTALL
    )

    # Footer
    content = content.replace(
        '>Ready to build something serious?</h2>',
        ' data-i18n="footer.cta.title">Ready to build something serious?</h2>'
    )
    content = re.sub(
        r'<p>For collaborations, partnerships.*?</p>',
        '<p data-i18n="footer.cta.desc">For collaborations, partnerships, or technical discussions, feel free to reach out.</p>',
        content
    )
    content = content.replace(
        '>Contact Us</a>',
        ' data-i18n="footer.cta.btn">Contact Us</a>'
    )

    # Footer nav links
    content = re.sub(
        r'(<div class="footer-nav">)\s*<a href="#services">What We Build</a>',
        r'\1\n                    <a href="#services" data-i18n="nav.whatWeBuild">What We Build</a>',
        content
    )

    return content

def tag_subpage_nav(content):
    """Add data-i18n to nav elements in project/page sub-files."""

    # Nav links (../index.html#...)
    content = re.sub(
        r'href="(\.\./index\.html#services)">(What We Build)</a>',
        r'href="\1" data-i18n="nav.whatWeBuild">\2</a>',
        content
    )
    content = re.sub(
        r'href="(\.\./index\.html#work)">(Projects)</a>',
        r'href="\1" data-i18n="nav.projects">\2</a>',
        content
    )
    content = re.sub(
        r'href="(\.\./index\.html#about)">(About)</a>',
        r'href="\1" data-i18n="nav.about">\2</a>',
        content
    )
    content = re.sub(
        r'href="(\.\./index\.html#contact)">(Contact)</a>',
        r'href="\1" data-i18n="nav.contact">\2</a>',
        content
    )

    # Search placeholder
    content = content.replace(
        'placeholder="Search all of KernelGuard"',
        'placeholder="Search all of KernelGuard" data-i18n-placeholder="nav.search.placeholder"'
    )

    # Language dropdown header
    content = content.replace(
        '<div class="dropdown-header">Select Language</div>',
        '<div class="dropdown-header" data-i18n="nav.lang.header">Select Language</div>'
    )

    # User dropdown
    content = content.replace(
        '<div class="user-name">KernelGuard Team</div>',
        '<div class="user-name" data-i18n="nav.user.teamName">KernelGuard Team</div>'
    )
    content = re.sub(
        r'<div class="user-email"[^>]*>A specialized 3-person.*?</div>',
        '<div class="user-email" style="white-space: normal; line-height: 1.5; margin-top: 8px;" data-i18n="nav.user.teamDesc">A specialized 3-person development collective focused on systems engineering, rigorous cybersecurity, and scalable full-stack infrastructure.</div>',
        content, flags=re.DOTALL
    )
    content = content.replace(
        '>My Profile</a>',
        ' data-i18n="nav.user.myProfile">My Profile</a>'
    )
    content = content.replace(
        '>My Projects</a>',
        ' data-i18n="nav.user.myProjects">My Projects</a>'
    )

    # Project detail page elements
    content = content.replace(
        '>Back to Directory',
        ' data-i18n="project.back">Back to Directory'
    )
    content = re.sub(
        r'>\s*Technical Overview\s*</div>',
        ' data-i18n="project.techOverview">Technical Overview</div>',
        content
    )
    content = re.sub(
        r'>\s*Value Proposition\s*</div>',
        ' data-i18n="project.valueProp">Value Proposition</div>',
        content
    )

    # Help panel elements (same as index)
    content = content.replace(
        '<h2>Help &amp; Information</h2>',
        '<h2 data-i18n="nav.help.title">Help &amp; Information</h2>'
    )
    for old, key in [
        ('Getting Started', 'nav.help.gettingStarted'),
        ('Documentation', 'nav.help.documentation'),
        ('API Reference', 'nav.help.apiReference'),
        ('Security Policy', 'nav.help.securityPolicy'),
    ]:
        content = content.replace(
            f'>{old} <svg',
            f'><span data-i18n="{key}">{old}</span> <svg'
        )
    content = content.replace(
        '>Contact Support →</button>',
        ' data-i18n="nav.help.contactSupport">Contact Support →</button>'
    )
    content = re.sub(
        r'KernelGuard Inc\.\s*<br>\s*Secure Systems Infrastructure\s*<br>\s*v2\.1\.0-beta',
        '<span data-i18n="nav.help.companyBlock">KernelGuard Inc.<br>Secure Systems Infrastructure<br>v2.1.0-beta</span>',
        content
    )

    return content

# ---- PROCESS ALL FILES ----

# index.html
with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()
c = add_i18n_script_tag(c)
c = tag_index_html(c)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)
print("Tagged index.html")

# pages/*.html
for path in glob.glob('pages/*.html'):
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()
    c = add_i18n_script_tag(c)
    c = tag_subpage_nav(c)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f"Tagged {path}")

# projects/*.html
for path in glob.glob('projects/*.html'):
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()
    c = add_i18n_script_tag(c)
    c = tag_subpage_nav(c)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f"Tagged {path}")

print("All files tagged with data-i18n attributes.")
