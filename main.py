import fitz
import re

#Selecionei o caminho do arquivo
file =  'Marcas2845.pdf'

#Abri o arquivo
open_file = fitz.open(file)



#Pegar cada página do arquivo e cada imagem dele
for page in range(len(dir(open_file))): 
    if page > 10 and page < 12:
        pagina = open_file.load_page(page)
        page = pagina.get_images(full=True)

        text = pagina.get_text()
        print(text)
        print(page)
        for pos, i in enumerate(page):
            print(f'Imagem_{pos}.png')


    