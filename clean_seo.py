import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove wrapper version
    content = re.sub(r'<div class="seo-text-wrapper">[\s\S]*?<div class="sub-header-seo-text">.*?</div>\s*</div>\s*</div>\s*', '', content)
    # Remove simple version
    content = re.sub(r'<div class="sub-header-seo-text">.*?</div>\s*', '', content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("SEO text completely removed from all files.")
