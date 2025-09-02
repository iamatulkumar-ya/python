from PyPDF2 import PdfMerger
import os

sourceDir = os.path.join(os.path.dirname(__file__), "datafiles")
print(sourceDir)
source_pdfs = ['first.pdf', 'second.pdf', 'third.pdf']

merger = PdfMerger()

for pdf in source_pdfs:
    merger.append(os.path.join(sourceDir, pdf))

merger.write(os.path.join(sourceDir, "Consolidated.pdf"))
merger.close()