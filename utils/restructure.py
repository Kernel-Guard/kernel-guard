import os
import glob
import re

if not os.path.exists('projects'): os.makedirs('projects')
if not os.path.exists('pages'):    os.makedirs('pages')
if not os.path.exists('utils'):    os.makedirs('utils')

for py in glob.glob('*.py'):
    if py != 'restructure.py':
        os.rename(py, os.path.join('utils', py))

if os.path.exists('dummy.txt'):
    os.rename('dummy.txt', os.path.join('utils', 'dummy.txt'))

for pf in glob.glob('project-*.html'):
    os.rename(pf, os.path.join('projects', pf))

for pf in ['profile.html', 'settings.html']:
    if os.path.exists(pf):
        os.rename(pf, os.path.join('pages', pf))

# Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

c = re.sub(r'href="(project-[^"]+\.html)"', r'href="projects/\1"', c)
c = re.sub(r'href="(profile\.html)"', r'href="pages/\1"', c)
c = re.sub(r'href="(settings\.html)"', r'href="pages/\1"', c)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)

# Helper to process subpages in pages/ and projects/
def process_subpage(path, prefix='../'):
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()
    
    # CSS/JS
    c = c.replace('href="css/', f'href="{prefix}css/')
    c = c.replace('src="js/', f'src="{prefix}js/')
    
    # Root links
    c = c.replace('href="index.html"', f'href="{prefix}index.html"')
    
    # Nav links (# -> ../index.html#)
    nav_links_block = re.search(r'<nav class="nav-links">.*?</nav>', c, flags=re.DOTALL)
    if nav_links_block:
        nav_html = nav_links_block.group(0)
        nav_html_fixed = re.sub(r'href="#([a-zA-Z0-9_-]+)"', f'href="{prefix}index.html#\\1"', nav_html)
        c = c.replace(nav_links_block.group(0), nav_html_fixed)

    # Back to directory link in projects
    c = c.replace('href="index.html#work"', f'href="{prefix}index.html#work"')
    
    # Cross references
    c = re.sub(r'href="(project-[^"]+\.html)"', f'href="{prefix}projects/\\1"', c)
    c = re.sub(r'href="(profile\.html)"', f'href="{prefix}pages/\\1"', c)
    c = re.sub(r'href="(settings\.html)"', f'href="{prefix}pages/\\1"', c)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(c)

for pf in glob.glob('projects/*.html'):
    process_subpage(pf)

for pf in glob.glob('pages/*.html'):
    process_subpage(pf)

# 3. Update ui.js routing logic so that dropdown links work regardless of directory depth
ui_path = os.path.join('js', 'ui.js')
if os.path.exists(ui_path):
    with open(ui_path, 'r', encoding='utf-8') as f:
        ui = f.read()
    
    # The current ui.js has raw settings.html and profile.html hrefs in strings.
    # Replace the dropdown items
    ui = ui.replace('href="profile.html"', 'href="pages/profile.html"')
    ui = ui.replace('href="settings.html"', 'href="pages/settings.html"')
    
    # Add absolute-path-aware base prefix calculation to top of ui.js
    prefix_code = """
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
"""
    ui = prefix_code + ui
    with open(ui_path, 'w', encoding='utf-8') as f:
        f.write(ui)

print('Folder restructuring and path fixing complete.')
