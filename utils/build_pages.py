import os
import re

# 1. Update index.html

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

new_grid_html = '''
            <div style="margin-bottom: 24px; font-weight: 600; color: var(--color-gray-100);">Open Source Projects</div>
            <div class="projects-grid" style="margin-bottom: 64px;">
                <a href="project-aegis.html" class="project-card fade-up" style="text-decoration: none; color: inherit; display: block;">
                    <h3>Aegis-BPF</h3>
                    <p>A runtime security engine built with eBPF CO-RE and LSM-based enforcement, designed for synchronous kernel-level protection.</p>
                </a>
                
                <a href="project-cathodex.html" class="project-card fade-up" style="text-decoration: none; color: inherit; display: block;">
                    <h3>CathodeX</h3>
                    <p>High-performance userspace networking stack engineered in C, optimized for massive concurrency and determinism.</p>
                </a>
            </div>

            <div style="margin-bottom: 24px; font-weight: 600; color: var(--color-gray-100); border-top: 1px solid var(--color-gray-20); padding-top: 32px;">Closed Source Projects (Demos)</div>
            <div class="projects-grid">
                <a href="project-eduhub.html" class="project-card fade-up" style="text-decoration: none; color: inherit; display: block;">
                    <h3>EduHub Campus</h3>
                    <p>A B2B enterprise room and resource reservation system with secure tenant-based isolation and audit trails.</p>
                </a>

                <a href="project-refatelier.html" class="project-card fade-up" style="text-decoration: none; color: inherit; display: block;">
                    <h3>Ref Atelier</h3>
                    <p>A high-performance luxury e-commerce frontend architecture ensuring fast load times and seamless localization.</p>
                </a>

                <a href="project-hrportal.html" class="project-card fade-up" style="text-decoration: none; color: inherit; display: block;">
                    <h3>Nexus HR Portal</h3>
                    <p>A fully integrated internal hiring and applicant tracking portal designed for high data integrity and workflow automation.</p>
                </a>
            </div>
'''

block = re.search(r'<div class="projects-grid">.*?</div>(?=\s*</div>\s*</section>)', c, flags=re.DOTALL)
if block:
    c = re.sub(r'<div class="projects-grid">.*?</div>(?=\s*</div>\s*</section>)', new_grid_html, c, flags=re.DOTALL)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(c)
    print("Updated index.html")
else:
    print("Could not find projects grid in index.html")

# 2. Extract Header and Footer from index.html to wrap our new pages
header_match = re.search(r'(<!DOCTYPE html>.*?</header>)', c, flags=re.DOTALL)
footer_match = re.search(r'(<footer class="footer">.*</html>)', c, flags=re.DOTALL)

header = header_match.group(1) if header_match else ""
footer = footer_match.group(1) if footer_match else ""

# Helper to generate page
def generate_page(filename, title, desc, tags, box1_title, box1_desc, box2_title, box2_desc, btn_text):
    tags_html = "".join([f'<span class="project-tag">{t}</span>' for t in tags])
    content = f'''{header}
    <main>
        <div class="container project-page">
            <a href="index.html#work" class="project-back">
                <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><line x1="19" y1="12" x2="5" y2="12"></line><polyline points="12 19 5 12 12 5"></polyline></svg>
                Back to Directory
            </a>

            <h1 class="project-title">{title}</h1>
            <p class="project-desc">{desc}</p>

            <div class="project-tags">
                {tags_html}
            </div>

            <div class="project-grid">
                <div class="project-card">
                    <div class="project-card-header">
                        <svg class="project-card-icon" viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>
                        {box1_title}
                    </div>
                    <p>{box1_desc}</p>
                </div>
                <div class="project-card">
                    <div class="project-card-header">
                        <svg class="project-card-icon" viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><circle cx="12" cy="12" r="6"></circle><circle cx="12" cy="12" r="2"></circle></svg>
                        {box2_title}
                    </div>
                    <p>{box2_desc}</p>
                </div>
            </div>

            <button class="btn btn-primary" style="display:inline-flex; align-items:center; gap:8px;">
                {btn_text}
                <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" style="transform: rotate(45deg);"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
            </button>
        </div>
    </main>
{footer}'''
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Created {filename}")

# Generate all 5 pages
generate_page(
    'project-aegis.html',
    'Aegis-BPF',
    'A runtime security engine built with eBPF CO-RE and LSM-based enforcement, designed for synchronous kernel-level protection.',
    ['C', 'eBPF', 'Linux Kernel', 'Rust'],
    'Technical Overview',
    'Implemented in C and Rust for memory safety and raw kernel performance. Utilizes eBPF CO-RE to ensure portability across different Linux kernel builds without requiring local recompilation on the target host.',
    'Value Proposition',
    'Enables deep, invisible synchronous container and host protection. As containerization abstracts the operating system, Aegis-BPF provides the highest tier of host-level enforcement with sub-millisecond overhead.'
    ,'View Source Code'
)

generate_page(
    'project-cathodex.html',
    'CathodeX',
    'High-performance userspace networking stack engineered in C, optimized for massive concurrency and determinism.',
    ['C', 'Networking', 'DPDK', 'TCP/IP'],
    'Technical Overview',
    'Bypasses the standard Linux kernel network stack using DPDK to deliver millions of packets per second. Features a custom state machine for TCP tracking and zero-copy packet forwarding.',
    'Value Proposition',
    'Dramatically reduces packet latency and CPU consumption in high-throughput environments like micro-trading, telecom gateways, and custom ingress firewalls.',
    'View Source Code'
)

generate_page(
    'project-eduhub.html',
    'EduHub Campus',
    'A B2B enterprise room and resource reservation system with secure tenant-based isolation and audit trails.',
    ['React', 'Node.js', 'PostgreSQL', 'Identity'],
    'Technical Overview',
    'Single-page application featuring strict Role-Based Access Control (RBAC) and tenant isolation at the database layer using Row-Level Security (RLS). Includes a fully custom IAM auth flow equivalent to IBM Verify.',
    'Value Proposition',
    'Empowers large academic organizations to manage thousands of conflicting physical resources securely. Reduces double-bookings to zero and ensures all manual overrides are cryptographically logged.',
    'View Demo Portal'
)

generate_page(
    'project-refatelier.html',
    'Ref Atelier',
    'A high-performance luxury e-commerce frontend architecture ensuring fast load times and seamless localization.',
    ['Next.js', 'Vercel', 'Tailwind', 'GraphQL'],
    'Technical Overview',
    'Headless e-commerce architecture relying on static site generation and edge caching for sub-100ms LCP (Largest Contentful Paint). Integated directly with headless CMS solutions for completely decoupled inventory management.',
    'Value Proposition',
    'Solves the classic "slow storefront" conversion dropoff by rendering everything instantly at the CDN edge. Minimalist UI pushes focus entirely onto the luxury apparel.',
    'View Storefront'
)

generate_page(
    'project-hrportal.html',
    'Nexus HR Portal',
    'A fully integrated internal hiring and applicant tracking portal designed for high data integrity and workflow automation.',
    ['TypeScript', 'Vue', 'Express', 'Redis'],
    'Technical Overview',
    'Complex state-managed web application with live applicant lifecycle tracking, automated pre-screening via integrated logic workers, and real-time candidate communications over WebSockets.',
    'Value Proposition',
    'Provides Human Resources departments an "air-traffic control" view of their hiring pipeline, dramatically decreasing candidate time-in-stage while enforcing strict data compliance.',
    'View Internal Demo'
)
