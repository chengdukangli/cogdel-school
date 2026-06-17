#!/usr/bin/env python3
"""Add Home breadcrumb to deep EN article pages"""
import os

# Fix EN articles - add Home before News
articles_dir = os.path.join('en', 'articles')
for f in os.listdir(articles_dir):
    if not f.endswith('.html'):
        continue
    path = os.path.join(articles_dir, f)
    with open(path, 'r', encoding='utf-8') as fp:
        c = fp.read()
    orig = c

    # Add Home before News
    old = '<div class="breadcrumb"><a href="../news.html">News</a>'
    new = '<div class="breadcrumb"><a href="../index.html" style="font-weight:700;color:var(--dp);">Home</a> &#187; <a href="../news.html">News</a>'
    if old in c:
        c = c.replace(old, new)

    # Fix results-admissions articles
    old2 = '<div class="breadcrumb"><a href="../results-admissions.html">Results</a>'
    new2 = '<div class="breadcrumb"><a href="../index.html" style="font-weight:700;color:var(--dp);">Home</a> &#187; <a href="../results.html">Results</a> &#187; <a href="../results-admissions.html">Admissions</a>'
    if old2 in c:
        c = c.replace(old2, new2)

    if c != orig:
        with open(path, 'w', encoding='utf-8') as fp:
            fp.write(c)
        print(f'Fixed: {path}')

# Fix EN student-life etc - add Home before pages with no Home link
for f in ['student-life.html', 'results.html', 'faq.html']:
    path = os.path.join('en', f)
    if not os.path.exists(path):
        continue
    with open(path, 'r', encoding='utf-8') as fp:
        c = fp.read()
    orig = c
    # Check if already has Home
    if 'Home' not in c.split('breadcrumb')[1][:80] if 'breadcrumb' in c else True:
        continue
    with open(path, 'w', encoding='utf-8') as fp:
        fp.write(c)

print('Done!')
