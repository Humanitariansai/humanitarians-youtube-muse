# SOURCES.md — review-denis

## Source artifacts

- `branding-and-ai/PPTX/Madison_Complete_Brand_System_Bykov.pptx`
- `branding-and-ai/PDF/Madison_Tool_Documentation.pdf`

## Extraction method
- PPTX: python-pptx text + embedded images
- PDF: PyMuPDF text + page renders at 150 DPI
- HTML: curl fetch + regex text extraction
- DOCX: zipfile XML extraction (fallback)

## Path
Path B
