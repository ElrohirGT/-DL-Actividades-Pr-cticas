# Flavio Galán 22386
# José Prince 22087
# Andre Jo 22199

TAMAÑO_BUFFER = 10

# Código base para iniciar
def cargar_buffer(entrada, inicio, tamano_buffer):
    buffer = entrada[inicio : inicio + tamano_buffer]
    if len(buffer) < tamano_buffer:
        buffer.append("eof")

    for i in range(10- len(buffer)):
        buffer.append("")
    return buffer


def procesar_buffer(entrada, TAMAÑO_BUFFER):
    # Procesar y extraer lexemas del buffer
    
    inicio = 0
    avance = 0

    #Pegar buffer
    buffer = cargar_buffer(entrada, 0, TAMAÑO_BUFFER)

    lexemas = []

    localBuffer = ""
    while buffer[inicio % TAMAÑO_BUFFER] != "eof":

       
        if avance != 0 and avance % TAMAÑO_BUFFER == 0:
            buffer = cargar_buffer(entrada, avance, TAMAÑO_BUFFER)

        idx = avance % TAMAÑO_BUFFER

        if (buffer[idx] == " " or buffer[idx] == "eof"):
            if (buffer[idx] == "eof"):
                inicio = avance
            else:
                inicio = avance+1
            lexemas.append(localBuffer)
            print("Lexema encontrado!", localBuffer)
            localBuffer = ""
            
        else:
            localBuffer += buffer[idx]
        
        avance+=1

    return lexemas

    
entrada = list("Esto es un ejemplo eof")
inicio = 0

lexemas = procesar_buffer(entrada, TAMAÑO_BUFFER)


print(lexemas)