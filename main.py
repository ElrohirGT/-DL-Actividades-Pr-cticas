import re
import csv

with open("page.html", "r", encoding="utf-8") as htmlFile:
    content = htmlFile.read()

    imgRegepx = r"<img src=\"(.*?aspect=true)\" [A-z =\"]* alt=\"(.*?)\""
    imgs = re.findall(imgRegepx, content)
    transformedImgs = [",".join(['"' + y + '"' for y in x]) + "\n" for x in imgs]
    print(transformedImgs)

    with open("output.csv", "w", encoding="utf-8") as csvFile:
        csvFile.write("URL de la imagen,Nombre del producto\n")

        csvFile.writelines(transformedImgs)
