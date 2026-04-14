import glob

# Add theme.js script to all HTML files — BEFORE main.js (non-deferred for instant theme)
all_files = ['index.html'] + glob.glob('pages/*.html') + glob.glob('projects/*.html')

for f_path in all_files:
    with open(f_path, 'r', encoding='utf-8') as f:
        c = f.read()
    
    if 'theme.js' not in c:
        # For root files
        c = c.replace(
            '<script src="js/main.js" defer>',
            '<script src="js/theme.js"></script>\n    <script src="js/main.js" defer>'
        )
        # For subdir files
        c = c.replace(
            '<script src="../js/main.js" defer>',
            '<script src="../js/theme.js"></script>\n    <script src="../js/main.js" defer>'
        )
    
    with open(f_path, 'w', encoding='utf-8') as f:
        f.write(c)

print("Added theme.js to all HTML files")
