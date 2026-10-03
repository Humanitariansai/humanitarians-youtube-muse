# SOURCES.md — review-hammad

## Source artifacts

- `branding-and-ai/PPTX/Rana_Hammad_Final_Brand_Presentation.pptx`
- `branding-and-ai/DOCX/Hammad_Rana_Visual_Resume.docx (text only)`

## Extraction method
- PPTX: python-pptx text + embedded images
- PDF: PyMuPDF text + page renders at 150 DPI
- HTML: curl fetch + regex text extraction
- DOCX: zipfile XML extraction (fallback)

## Path
Path A
