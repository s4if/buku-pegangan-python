#!/bin/bash

# Define input files
files=(
    "main.md"
    "chapter_1.md"
    "chapter_2.md"
    "chapter_3.md"
    "chapter_4.md"
    "chapter_5.md"
    "chapter_6.md"
    "chapter_7.md"
    "chapter_8.md"
)

# Check if pandoc is installed
if ! command -v pandoc &> /dev/null; then
    echo "Error: pandoc is not installed. Please install it first."
    exit 1
fi

# Check if all markdown files exist
for file in "${files[@]}"; do
    if [ ! -f "$file" ]; then
        echo "Error: File $file not found!"
        exit 1
    fi
done

# Convert to PDF using pandoc
pandoc "${files[@]}" -o book.pdf \
    --pdf-engine=lualatex \
    --toc --toc-depth=2 \
    --highlight-style=tango \
    -V geometry=a4paper \
    -V fontsize=11pt \
    -V linkcolor=blue \
    -V mainfont="Ubuntu Nerd Font" \
    -V sansfont="FiraCode Nerd Font Mono" 

# Check if conversion was successful
if [ $? -eq 0 ]; then
    echo "Successfully created book.pdf"
else
    echo "Error: PDF conversion failed"
    exit 1
fi