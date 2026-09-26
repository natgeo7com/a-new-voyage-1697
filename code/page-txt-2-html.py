# how to:
# root dir is set, run this code from anywhere 
# change root dir if proj dir moved

import os
import re
import urllib.parse

root = "/Users/alex/Downloads/a-new-voyage-1697"
gtag = open(f'{root}/code/gtag.html', 'r').read()

def g_fig(string_block):
    # Matches: // img:\n[file]\n[width]\n[caption]
    pattern = r"^\/\/\s*img:\s*\n([^\n]+)\n([^\n]+)\n([\s\S]*)$"
    match = re.match(pattern, string_block)
    if not match:
        return ""
    file, w, cap = match.groups()
    return f"""
    <figure>
        <img src="{file}" alt="{cap}" style="width: {w}%;">
        <figcaption>{cap}</figcaption>
    </figure>
    """

def g_map(string_block):
    # Matches: // map:\n[old_name]\n[new_name]
    pattern = r"^\/\/\s*map:\s*\n(.+)\n(.+)$"
    match = re.match(pattern, string_block)
    if not match:
        return ""
    old, new_ = match.groups()
    encoded_new = urllib.parse.quote(new_.strip())
    return f'<p><a href="https://www.google.com/maps/search/{encoded_new}" target="_blank">📍 {old.strip()}, modern day {new_}</a></p>'

def g_fig_ss(n_str):
    # Converts e.g., "005" to 5 to remove 0 padding for the text
    num = int(n_str)
    cap = f"Page {num} screenshot."
    return f"""
    <figure>
        <img src="/img/p/chapters/{n_str}.jpg" alt="{cap}">
    </figure>
    """

def process(text):
    # Split by double newlines, clean up, and remove empty blocks
    # .replace("\r\n", "\n") normalizes Windows line endings
    blocks = [b.strip() for b in text.replace("\r\n", "\n").split("\n\n") if b.strip()]
    
    html_out = []
    for s in blocks:
        if s.startswith('// p:'):
            html_out.append(f'<p class="gray">[{s[6:]}]</p>')
        elif s.startswith('// y:'):
            html_out.append(f'<p class="gray">[{s[6:]}]</p>')
        elif s.startswith('// pt:'):
            html_out.append(f'<p class="gray">[{s[7:]}]</p>')
        elif s.startswith('// w:'):
            html_out.append(f'<p class="gray">[{s[6:]}]</p>')
        elif s.startswith('// h1:'):
            html_out.append(f'<h1>{s[7:]}</h1>')
        elif s.startswith('// sub:'):
            html_out.append(f'<p class="subtitle">{s[8:]}</p>')
        elif s.startswith('// dropcap:'):
            html_out.append(f'<p class="dropcap">{s[12:]}</p>')
        elif s.startswith('// img:'):
            html_out.append(g_fig(s))
        elif s.startswith('// map:'):
            html_out.append(g_map(s))
        else:
            html_out.append(f'<p>{s}</p>')
            
    return "".join(html_out)

def main(file_number_str):
    # Ensure file_number_str is 3 digits padded (e.g., "005")
    n_padded = file_number_str.zfill(4)
    input_filename = f"{root}/pt/{n_padded}.txt"
    output_filename = f"{root}/p/{n_padded}.html"
    
    if not os.path.exists(input_filename):
        print(f"Error: {input_filename} not found.")
        return

    # Read text file
    with open(input_filename, "r", encoding="utf-8") as f:
        text_content = f.read()

    # Process content
    left_side_html = g_fig_ss(n_padded)
    right_side_html = process(text_content)

    # Combine into a structured layout mirroring your JS DOM assignment
    full_html = f"""<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page {file_number_str} Screenshot & Transcript (Extracted Text) | A New Voyage Round the World by William Dampier, 1697 Edition</title>
    {gtag}
    <link rel="icon" type="image/png" href="/favicon.png">
    <link rel="stylesheet" href="/css/comm.css">
</head>

<body>

    <article>
        <section id="left">{left_side_html}</section>
        <section id="right">{right_side_html}</section>
    </article>

</body>
</html>"""

    # Save html file
    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"Successfully created {output_filename}")

# Run code for file "005.txt"
if __name__ == "__main__":
    for i in range(550):
        main(str(i+1)) 
