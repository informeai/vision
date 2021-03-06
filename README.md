![OpenSource](https://img.shields.io/static/v1?label=GitHub&message=Opensource&color=blue&logo=github&logoColor=violet)
![BuildPassing](https://img.shields.io/static/v1?label=build&message=passing&color=brightgreen)
![PythonVersion](https://img.shields.io/static/v1?label=python&message=>=3.6&color=brightgreen&logo=python&logoColor=white)
[![Pypi](https://img.shields.io/static/v1?label=Pypi&logo=pypi&logoColor=white&message=v1.0.1&color=9f55ff)](https://pypi.org/project/visionPDF/)

# visionPDF
Módulo Python para Leitura, Tradução e Escrita em Arquivos PDF.

Com uso dos módulos PyPDF2, reportlab e karkipytranslator , sintetizados em um único módulo, mas com todo o poder dos mesmos.

## Instalação:
`$ pip install visionPDF`

## Uso:
```
>> import visionPDF

------- LER -------

>> reader = visionPDF.PDFReader(file_in)    # Arquivo PDF a ser lido.
>> reader.get_text(page)                    # Retorna o texto da Pagina.

------- TRADUZIR ------

>> transl = visionPDF.PDFTranslate(to_lang)  # to_lang -> Linguagem para 
                                                    qual deseja traduzir.
                                                         Ex: pt,kr,en,...
>> transl.translate(text)                    # text -> Texto a ser traduzido.

-------- ESCREVER ---------

>> writer = visionPDF.PDFWriter(file_out,orientation)   # file_out -> Arquivo de Saida.
                                                        # orientation -> Orientação do documento. Ex: portrait/landscape.
>> writer.addText(text,x,y,font,size,color)            # Escreve um texto no documento.
>> writer.save_page()                                   # Salva o conteudo gravado na pagina e fecha ela.
>> writer.close()                                       # Fecha o Documento PDF.
```


## Contato:
@informeai

[![Facebook](https://img.shields.io/static/v1?label=facebook&style=social&logo=Facebook&message=page)](https://www.facebook.com/informeai/)
[![Instagram](https://img.shields.io/static/v1?label=instagram&style=social&logo=Instagram&message=perfil)](https://www.instagram.com/informeaioficial/)
[![Twitter](https://img.shields.io/static/v1?label=twitter&style=social&logo=Twitter&message=desenvolvedor)](https://twitter.com/WellingtonGade4)