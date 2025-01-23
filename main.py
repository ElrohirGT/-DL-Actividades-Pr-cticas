from enum import Enum, auto

import re
import csv

TAMAÑO_BUFFER = 10


class State(Enum):
    SEARCH_TAG = auto()
    START_TAG = auto()
    I_FOUND = auto()
    M_FOUND = auto()
    IMG_FOUND = auto()
    S_FOUND = auto()
    R_FOUND = auto()
    SRC_FOUND = auto()
    READ_SRC_VALUE = auto()
    A_FOUND = auto()
    L_FOUND = auto()
    ALT_FOUND = auto()
    READ_ALT_VALUE = auto()
    IMG_SRC_READ = auto()


content = ""
with open("page.html", "r", encoding="utf-8") as htmlFile:
    content = htmlFile.read()

output = ["URL de la Imagen,Nombre del producto\n"]

state = State.SEARCH_TAG

urls = []
titles = []
localBuffer = ""
i = 0
while i < len(content):
    byteRead = content[i : i + 1]
    i += 1

    # print("readByte:", byteRead)
    # if state == State.IMG_FOUND or state == State.SRC_FOUND or state == State.ALT_FOUND:
    #     print("STATE: ", state)
    #     print("localBuffer:", localBuffer)

    match state:
        case State.SEARCH_TAG:
            match byteRead:
                case "<":
                    state = State.START_TAG

                case _:
                    pass
        case State.START_TAG:
            if byteRead == "i":
                state = State.I_FOUND
            else:
                state = State.SEARCH_TAG

        case State.I_FOUND:
            if byteRead == "m":
                state = State.M_FOUND
            else:
                state = State.SEARCH_TAG

        case State.M_FOUND:
            if byteRead == "g":
                if content[i] == " ":
                    i + 1
                state = State.IMG_FOUND
            else:
                state = State.SEARCH_TAG

        case State.IMG_FOUND:
            if byteRead == "s":
                state = State.S_FOUND
            elif byteRead == ">":
                state = State.SEARCH_TAG
            else:
                state = State.IMG_FOUND

        case State.A_FOUND:
            if byteRead == "l":
                state = State.L_FOUND
            else:
                state = State.IMG_SRC_READ

        case State.L_FOUND:
            if byteRead == "t":
                state = State.ALT_FOUND
            else:
                state = State.IMG_SRC_READ

        case State.ALT_FOUND:
            if byteRead == "=":
                if content[i] == '"':
                    i += 1
                state = State.READ_ALT_VALUE
            else:
                state = State.IMG_SRC_READ

        case State.READ_ALT_VALUE:
            if byteRead == '"':  # Reached end of SRC value
                state = State.IMG_FOUND
                titles.append(localBuffer)
                localBuffer = ""
            else:
                localBuffer += byteRead

        case State.S_FOUND:
            if byteRead == "r":
                state = State.R_FOUND
            else:
                state = State.IMG_FOUND

        case State.R_FOUND:
            if byteRead == "c":
                state = State.SRC_FOUND
            else:
                state = State.IMG_FOUND

        case State.SRC_FOUND:
            if byteRead == "=":
                if content[i] == '"':
                    i += 1
                state = State.READ_SRC_VALUE
            else:
                state = State.IMG_FOUND

        case State.READ_SRC_VALUE:
            if byteRead == '"':  # Reached end of SRC value
                state = State.IMG_SRC_READ
                urls.append(localBuffer)
                localBuffer = ""
            else:
                localBuffer += byteRead

        case State.IMG_SRC_READ:
            if byteRead == "a":
                state = State.A_FOUND
            elif byteRead == ">":
                state = State.SEARCH_TAG


# print("URLS\n", urls)
# print("TITLES\n", titles)


# imgRegepx = r"<img src=\"(.*?aspect=true)\" [A-z =\"]* alt=\"(.*?)\""
# imgs = re.findall(imgRegepx, content)
# transformedImgs = [",".join(['"' + y + '"' for y in x]) + "\n" for x in imgs]
# print(transformedImgs)

urls = list(filter(lambda url: url.endswith("true"), urls))
# print(len(titles), len(urls))

imgs = list(zip(titles, urls))
# print(imgs)

transformedImgs = [",".join(['"' + y + '"' for y in x]) + "\n" for x in imgs]
# print(transformedImgs)
with open("output.csv", "w", encoding="utf-8") as csvFile:
    csvFile.write('"Nombre del producto","URL de la imagen"\n')
    csvFile.writelines(transformedImgs)
