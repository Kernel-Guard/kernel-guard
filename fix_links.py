import os
import glob
import re

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Remove the hrportal card block
c = re.sub(r'<a href="projects/project-hrportal\.html"\s+class="project-card fade-up"[^>]*>.*?</a>', '', c, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)

# 2. Update projects/*.html to make the buttons clickable links
for pf in glob.glob('projects/*.html'):
    with open(pf, 'r', encoding='utf-8') as f:
        c = f.read()
    
    # We replace <button class="btn btn-primary" ...> with <a href="#" class="btn btn-primary" ... text-decoration:none; width:max-content;>
    # And replace </button> with </a> at the end of the file container.
    
    # Find the button block
    button_match = re.search(r'<button class="btn btn-primary"[^>]*>(.*?)</button>', c, flags=re.DOTALL)
    if button_match:
        inner_content = button_match.group(1)
        new_button = f'<a href="#" class="btn btn-primary" style="display:inline-flex; align-items:center; gap:8px; text-decoration:none; width:max-content;">{inner_content}</a>'
        c = c.replace(button_match.group(0), new_button)
        
        with open(pf, 'w', encoding='utf-8') as f:
            f.write(c)

print('Updated index.html to remove HR portal and wrapped buttons in links.')
