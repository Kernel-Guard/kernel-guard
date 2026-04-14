import glob

# Add error-boundary.js as the VERY FIRST script in all HTML files
all_files = ['index.html'] + glob.glob('pages/*.html') + glob.glob('projects/*.html')

for f_path in all_files:
    with open(f_path, 'r', encoding='utf-8') as f:
        c = f.read()
    
    if 'error-boundary.js' not in c:
        # Insert before theme.js (which is the current first script)
        c = c.replace(
            '<script src="js/theme.js">',
            '<script src="js/error-boundary.js"></script>\n    <script src="js/theme.js">'
        )
        c = c.replace(
            '<script src="../js/theme.js">',
            '<script src="../js/error-boundary.js"></script>\n    <script src="../js/theme.js">'
        )
    
    with open(f_path, 'w', encoding='utf-8') as f:
        f.write(c)

print("Added error-boundary.js to all HTML files")
