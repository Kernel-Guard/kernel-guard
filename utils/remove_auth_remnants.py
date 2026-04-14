import os, glob, re

def update_htmls():
    files = ['index.html'] + glob.glob('pages/*.html') + glob.glob('projects/*.html')
    for f_path in files:
        with open(f_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remove Billing and Log Out lines
        content = re.sub(r'\s*<button class="dropdown-item">Billing</button>', '', content)
        content = re.sub(r'\s*<button class="dropdown-item danger" id="btn-logout">Log Out</button>', '', content)
        
        with open(f_path, 'w', encoding='utf-8') as f:
            f.write(content)

def update_uijs():
    ui_path = os.path.join('js', 'ui.js')
    if os.path.exists(ui_path):
        with open(ui_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        content = re.sub(r'const btnLogout = document\.getElementById\(\'btn-logout\'\);\s*', '', content)
        content = re.sub(r'// --- Logout Mock logic ---.*?}\s*}\);?\s*}\s*', '', content, flags=re.DOTALL)
        
        with open(ui_path, 'w', encoding='utf-8') as f:
            f.write(content)

update_htmls()
update_uijs()
print('Removed billing and log out.')
