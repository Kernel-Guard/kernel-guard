import re
import glob

# 1. Update dropdowns in all files
# We replace the static JS avatar with the 3 person team + the skeleton comment
new_dropdown_header = '''
                    <div class="dropdown-user-header">
                        <div class="avatar-circle">KG</div>
                        <div class="user-name">KernelGuard Team</div>
                        <div class="user-email" style="white-space: normal; line-height: 1.5; margin-top: 8px;">A specialized 3-person development collective focused on systems engineering, rigorous cybersecurity, and scalable full-stack infrastructure.</div>
                    </div>
                    <!-- 
                       Suggested React/Tailwind Loading Skeleton for data fetch:
                       <div className="animate-pulse flex space-x-4 p-4">
                         <div className="rounded-full bg-gray-200 h-10 w-10"></div>
                         <div className="flex-1 space-y-3 py-1">
                           <div className="h-2 bg-gray-200 rounded w-3/4"></div>
                           <div className="h-2 bg-gray-200 rounded w-5/6"></div>
                         </div>
                       </div>
                    -->
'''

files = ['index.html'] + glob.glob('pages/*.html') + glob.glob('projects/*.html')
for f_path in files:
    with open(f_path, 'r', encoding='utf-8') as f:
        c = f.read()
    
    # regex to find dropdown-user-header and replace it
    c = re.sub(r'<div class="dropdown-user-header">.*?</div>\s*<a href', new_dropdown_header + '<a href', c, flags=re.DOTALL)
    
    with open(f_path, 'w', encoding='utf-8') as f:
        f.write(c)

# 2. Add About Section to index.html
with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

about_section_html = '''
    <!-- About Section -->
    <section class="section border-top" id="about">
        <div class="container fade-up">
            <h2 class="text-section-title">About KernelGuard</h2>
            <div style="font-size: 20px; line-height: 1.6; color: var(--color-gray-100); max-width: 800px; margin-top: 32px;">
                <p style="margin-bottom: 24px;">
                    We are a specialized 3-member engineering collective bridging the gap between rigorous academic research and production-grade software. Rooted in our foundational work at Dokuz Eylül University, we architect high-performance systems with an authoritative focus on eBPF, deep Linux security, and scalable infrastructure.
                </p>
                <p>
                    By synthesizing theoretical computer science with pragmatic development methodologies, we don't just build typical applications—we engineer resilient, state-of-the-art technological foundations built to withstand both heavy scale and modern cybersecurity threats.
                </p>
            </div>
        </div>
    </section>
'''

# insert before <footer
if 'id="about"' not in c:
    c = re.sub(r'(<footer class="footer">)', about_section_html + r'\n    \1', c)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)

print('Updated Dropdowns and About section')
