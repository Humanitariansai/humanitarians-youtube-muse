# SOURCES.md — review-tanaka

## Source artifacts

- `branding-and-ai/PPTX/TANAKA_MANYARA_A11_Final_Presentation.pptx`

## Extraction method
- PPTX: python-pptx text + embedded images
- PDF: PyMuPDF text + page renders at 150 DPI
- HTML: curl fetch + regex text extraction
- DOCX: zipfile XML extraction (fallback)

## Path
Path B
