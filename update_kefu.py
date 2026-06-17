#!/usr/bin/env python3
"""Update kefu button to show text alongside icon"""
import os

old_btn_start = '<a href="https://work.weixin.qq.com/kfid/kfc51319098bfc114c1" target="_blank" style="position:fixed; right:24px; bottom:80px; z-index:999; width:56px; height:56px; background:var(--gd); border-radius:50%; box-shadow:0 4px 20px rgba(0,0,0,.2); display:flex; align-items:center; justify-content:center; transition:.3s;" title="在线咨询">'

count = 0
for root, dirs, files in os.walk('.'):
    dirs[:] = [d for d in dirs if d not in ('.git', '__pycache__', 'images', 'css', 'js')]
    for f in files:
        if f.endswith('.html'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as fp:
                c = fp.read()
            if old_btn_start not in c:
                continue

            # Determine language
            norm_path = path.replace('\\', '/')
            is_en = '/en/' in norm_path

            # Find the old button block
            start = c.find(old_btn_start)
            end_a = c.find('</a>', start) + 4

            if is_en:
                new_btn = '<a href="https://work.weixin.qq.com/kfid/kfc51319098bfc114c1" target="_blank" style="position:fixed; right:20px; bottom:80px; z-index:999; display:flex; align-items:center; gap:8px; background:var(--gd); color:#fff; border-radius:28px; box-shadow:0 4px 20px rgba(0,0,0,.2); padding:12px 20px 12px 14px; text-decoration:none; font-size:15px; font-weight:600; transition:.3s;" title="Contact Us">\n  <svg width="24" height="24" viewBox="0 0 24 24" fill="white"><path d="M20 2H4c-1.1 0-2 .9-2 2v18l4-4h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zm0 14H5.2L4 17.2V4h16v12z"/></svg>\n  Contact Us\n</a>'
            else:
                new_btn = '<a href="https://work.weixin.qq.com/kfid/kfc51319098bfc114c1" target="_blank" style="position:fixed; right:20px; bottom:80px; z-index:999; display:flex; align-items:center; gap:8px; background:var(--gd); color:#fff; border-radius:28px; box-shadow:0 4px 20px rgba(0,0,0,.2); padding:12px 20px 12px 14px; text-decoration:none; font-size:15px; font-weight:600; transition:.3s;" title="在线咨询">\n  <svg width="24" height="24" viewBox="0 0 24 24" fill="white"><path d="M20 2H4c-1.1 0-2 .9-2 2v18l4-4h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zm0 14H5.2L4 17.2V4h16v12z"/></svg>\n  点击咨询客服\n</a>'

            c = c[:start] + new_btn + c[end_a:]
            with open(path, 'w', encoding='utf-8') as fp:
                fp.write(c)
            count += 1

print(f'Updated {count} files with text buttons')
