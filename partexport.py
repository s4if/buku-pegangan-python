import os
import pypandoc

input_dir = "chapters"
output_dir = "my_book"
output_filename = "part_book_output.pdf"

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Build the pandoc options as a string
pandoc_cmd = [
    "--table-of-contents",
    "--toc-depth=2",
    "--number-sections",
    "--resource-path=.",
    "--pdf-engine=xelatex",
    "--metadata-file",
    "metadata.yml",
    "--include-in-header",
    "main.tex",
    "--highlight-style",
    "pygments.theme",
    "--include-before-body",
    "cover.tex",
    "-V",
    "toc-title=Daftar Isi",
]

output_path = os.path.join(output_dir, output_filename)
# Convert all markdown files in the chapters/ subdirectory.
input_files = [
    os.path.join(input_dir, "chapter_01.md"),
    os.path.join(input_dir, "chapter_02.md"),
    os.path.join(input_dir, "chapter_03.md"),
    os.path.join(input_dir, "chapter_04.md")
]

pypandoc.convert_file(
    input_files,
    "pdf",
    outputfile=output_path,
    extra_args=pandoc_cmd,
)

print(f"Conversion completed. Output saved to: {output_path}")
