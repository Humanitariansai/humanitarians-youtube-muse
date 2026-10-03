# SOURCES.md — review-raksha

## Source artifacts

- `branding-and-ai/PPTX/threadline_final_presentation.pptx`

## Extraction method
- PPTX: python-pptx text + embedded images
- PDF: PyMuPDF text + page renders at 150 DPI
- HTML: curl fetch + regex text extraction
- DOCX: zipfile XML extraction (fallback)

## Path
Path B
