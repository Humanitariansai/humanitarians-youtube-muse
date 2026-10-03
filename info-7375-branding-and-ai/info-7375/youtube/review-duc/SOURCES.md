# SOURCES.md — review-duc

## Source artifacts

- `branding-and-ai/PPTX/Nguyen_Duc_Final_BrandPortfolio.pptx`

## Extraction method
- PPTX: python-pptx text + embedded images
- PDF: PyMuPDF text + page renders at 150 DPI
- HTML: curl fetch + regex text extraction
- DOCX: zipfile XML extraction (fallback)

## Path
Path B
