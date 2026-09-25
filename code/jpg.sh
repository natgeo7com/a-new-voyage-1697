#!/bin/bash

a="/Users/alex/Downloads/a.jpg"
b="/Users/alex/Downloads/b.jpg"

cp "$a" "$b"

jpegoptim \
  --max=75 \
  --strip-all \
  "$b"