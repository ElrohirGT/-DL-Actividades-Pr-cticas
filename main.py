import re
import csv

TAMAÑO_BUFFER = 10


# Código base para iniciar
# def cargar_buffer(entrada, inicio, tamano_buffer):
#     buffer = entrada[inicio : inicio + tamano_buffer]
#     if len(buffer) < tamano_buffer:
#         buffer.append("eof")
#
#     for i in range(10 - len(buffer)):
#         buffer.append("")
#     return buffer


with open("page.html", "r", encoding="utf-8") as htmlFile:
    content = htmlFile.read()

    imgRegepx = r"<img src=\"(.*?aspect=true)\" [A-z =\"]* alt=\"(.*?)\""
    imgs = re.findall(imgRegepx, content)
    transformedImgs = [",".join(['"' + y + '"' for y in x]) + "\n" for x in imgs]
    print(transformedImgs)

    with open("output.csv", "w", encoding="utf-8") as csvFile:
        csvFile.write("URL de la imagen,Nombre del producto\n")

        csvFile.writelines(transformedImgs)
