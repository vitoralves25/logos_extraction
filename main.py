import fitz
import re
file =  'Marcas2845.pdf'
open_file = fitz.open(file)
for pag in open_file:
    print(pag)
