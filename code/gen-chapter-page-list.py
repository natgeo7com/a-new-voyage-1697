# how to
# run this code anywhere

root = "/Users/alex/Downloads/a-new-voyage-1697"
gtag = open(f'{root}/code/gtag.html', 'r').read()

chapters = [
    (1, 1, 11),
    (2, 11, 24),
    (3, 25, 66),
    (4, 67, 92),
    (5, 93, 129),
    (6, 130, 160),
    (7, 161, 209),
    (8, 210, 236),
    (9, 237, 278),
    (10, 279, 304),
    (11, 305, 323),
    (12, 324, 344),
    (13, 345, 374),
    (14, 375, 402),
    (15, 403, 440),
    (16, 441, 470),
    (17, 471, 490),
    (18, 491, 520),
    (19, 521, 535),
    (20, 536, 550),
]

for ch, start, end in chapters:
  links = "\n".join(
      f'<li><a href="/p/{f"{p:04}"}.html">{p}</a></li>'
      for p in range(start, end + 1)
  )
  html = f"""<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chapter {ch} Page List | A New Voyage Round the World by William Dampier, 1697 Edition</title>
    {gtag}
    <link rel="icon" href="/favicon.jpg">
    <link rel="apple-touch-icon" href="/favicon.jpg">
    <style>
    html {{
      font-size: 20px;
    }}
    </style>
<h1>Chapter {ch}</h1>
<ol>
{links}
</ol>
"""

  with open(f"{root}/c/{ch:03}.html", "w") as f:
    f.write(html)