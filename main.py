import fitz
import re


file =  'Marcas2845.pdf'
open_file = fitz.open(file)
for page in range(len(dir(open_file))):
    if page > 10 and page < 12:
        pagina = open_file.load_page(page)
        page = pagina.get_images(full=True)
        print(page)

        for i in page:
            print(i)
    