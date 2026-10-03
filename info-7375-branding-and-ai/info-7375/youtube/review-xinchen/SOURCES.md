# SOURCES.md — review-xinchen

## Source artifacts

- `branding-and-ai/PPTX/Xinchen_Zu_Final_Brand_Portfolio_Presentation.pptx`

## Extraction method
- PPTX: python-pptx text + embedded images
- PDF: PyMuPDF text + page renders at 150 DPI
- HTML: curl fetch + regex text extraction
- DOCX: zipfile XML extraction (fallback)

## Path
Path A
