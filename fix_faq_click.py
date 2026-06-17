#!/usr/bin/env python3
"""Fix faq-q onclick from toggleAfaq to toggleFaq"""
for lang in ['zh', 'en']:
    path = f'{lang}/faq.html'
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()

    before = c.count('toggleFaq(this)')
    c = c.replace('onclick="toggleAfaq(this)">', 'XXXXX')  # temp

    # Now only fix the ones inside faq-q (which should all be toggleAfaq)
    # After the replacement above, we need to put back the afaq-header ones
    # Actually let me just replace all <div class="faq-q" occurrences

    # Restore first
    c = c.replace('XXXXX', 'onclick="toggleAfaq(this)">')

    # Now do the targeted replacement
    old_pattern = 'class="faq-q" style="'
    # Find all lines with faq-q and toggleAfaq
    lines = c.split('\n')
    fixed = 0
    for i, line in enumerate(lines):
        if 'class="faq-q"' in line and 'toggleAfaq' in line:
            lines[i] = line.replace('toggleAfaq(this)', 'toggleFaq(this)')
            fixed += 1

    c = '\n'.join(lines)
    after = c.count('toggleFaq(this)')
    print(f'{lang}: fixed {fixed} lines, toggleFaq count: {before} -> {after}')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(c)

    print(f'{lang}: Done!')
