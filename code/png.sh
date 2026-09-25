#!/bin/bash

a="/Users/alex/Downloads/a.png"
b="/Users/alex/Downloads/b.png"

pngquant \
  --quality=75-80 \
  --strip \
  --output "$b" \
  "$a"