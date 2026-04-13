import os

svg_3x3 = '''
<svg viewBox="0 0 32 32" width="24" height="24" style="margin-right: 12px; flex-shrink: 0;">
    <circle cx="4" cy="4" r="3" fill="#0043CE" opacity="0.2"/>
    <circle cx="28" cy="4" r="3" fill="#0043CE" opacity="0.2"/>
    <circle cx="4" cy="28" r="3" fill="#0043CE" opacity="0.2"/>
    <circle cx="28" cy="28" r="3" fill="#0043CE" opacity="0.2"/>
    <circle cx="16" cy="4" r="3" fill="#0043CE" opacity="0.6"/>
    <circle cx="4" cy="16" r="3" fill="#0043CE" opacity="0.6"/>
    <circle cx="28" cy="16" r="3" fill="#0043CE" opacity="0.6"/>
    <circle cx="16" cy="28" r="3" fill="#0043CE" opacity="0.6"/>
    <circle cx="16" cy="16" r="4.5" fill="#0043CE"/>
</svg>
'''

nav_logo_html = f'''<div class="nav-brand">
                <a href="index.html" style="display:flex; align-items:center; text-decoration:none; color:inherit; font-family: var(--font-sans);">
                    {svg_3x3}
                    <div><span style="font-weight: 300; letter-spacing: 0.5px;">Kernel</span><span style="font-weight: 700;">Guard</span></div>
                </a>
            </div>'''

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()
c = c.replace('<div class="nav-brand">KernelGuard</div>', nav_logo_html)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)

for fn in ['settings.html', 'profile.html']:
    with open(fn, 'r', encoding='utf-8') as f:
        c = f.read()
    c = c.replace('<div class="nav-brand"><a href="index.html" style="text-decoration:none; color:inherit;">KernelGuard</a></div>', nav_logo_html)
    with open(fn, 'w', encoding='utf-8') as f:
        f.write(c)

print('Replaced nav-brand correctly')
