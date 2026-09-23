## domain name nv97.de memo

```
this is how i think:
a-new-voyage
a-new-voyage-1697
anv1697

no creativity found

ask gemini to shorten it (meaningfully of course)
nv97 is suggested
i find it great
nv, 97 - both are essence and easy to type and remember
and extremely short

since anv is never good
1697 is too long and hard to type

here is the thing:
there is no great domain suffix options, 
even at high price
i do not like the look and sound of nv, 97, or de
but they are extremely short and neat

```

## code

```
# quality drop obvious even at 100, not sure why
# python is same

# 1st cd into cwd

w=1200
q=100
for f in *.jpg; do
  sips --resampleWidth "$w" \
  -s format jpeg \
  -s formatOptions "$q" \
  "$f" \
  --out "${f%.jpg}-${w}-${q}.jpg"
done
```

##

```
pngquant --quality=75-80 x.png

for img in *.png; do pngquant --quality=75-80 --ext .png --force "$img"; done

for img in *.jpg; do jpegoptim --max=75 --strip-all "$img"; done
```