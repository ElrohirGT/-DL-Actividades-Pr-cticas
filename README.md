# -DL-Actividades-Pr-cticas

Este documento explica el funcionamiento de un script que extrae imágenes y sus nombres asociados desde el contenido HTML de una página web. 

## **Caracteristicas Generales del Código**

- **Entrada de Datos**:
   - Se lee el contenido de la página HTML desde un archivo (`page.html`).
   - El archivo debe contener etiquetas `<img>` con atributos `src` (URL de la imagen) y `alt` (nombre del producto).

- **Exportación a CSV**:
   - Los datos extraídos se escriben en un archivo llamado `output.csv`, en formato `"Nombre del producto","URL de la imagen"`.

## **Componentes Principales**

El código utiliza una **enumeración (`Enum`)** llamada `State` para definir los diferentes estados de la máquina de estados. Cada estado representa un paso en el análisis de la etiqueta `<img>`:

- **SEARCH_TAG**: Busca el inicio de una etiqueta HTML (`<`).
- **START_TAG**: Identifica si la etiqueta es un `<img>`.
- **IMG_FOUND**: Comienza a buscar atributos dentro de la etiqueta `<img>`.
- **SRC_FOUND y READ_SRC_VALUE**: Extraen el valor del atributo `src` (URL de la imagen).
- **ALT_FOUND y READ_ALT_VALUE**: Extraen el valor del atributo `alt` (nombre del producto).
- **IMG_SRC_READ**: Verifica si la etiqueta contiene más atributos o si ha terminado (`>`).

El estado cambia dependiendo del carácter leído y del contexto, garantizando que solo se procesen etiquetas `<img>`.

El contenido del archivo HTML se recorre byte por byte utilizando un bucle `while`. Cada carácter leído se analiza en función del estado actual de la máquina de estados:

- **Identificación de Etiquetas**: Cuando se encuentra un `<`, el estado cambia a `START_TAG`.
- **Extracción de Atributos**:
  - Si se encuentra `src="`, el estado cambia a `READ_SRC_VALUE`, donde se lee y almacena la URL de la imagen.
  - Si se encuentra `alt="`, el estado cambia a `READ_ALT_VALUE`, donde se lee y almacena el nombre del producto.

El script utiliza un **buffer local (`localBuffer`)** para almacenar temporalmente los valores de los atributos hasta que se complete la lectura.

## Ejemplo de Funcionamiento

### Entrada
Archivo `page.html` con el siguiente contenido:
```
<img src="producto1.jpg?aspect=true" alt="Producto 1">
<img src="producto2.jpg?aspect=true" alt="Producto 2">
```

### Salida
Archivo `output.csv` generado:
```
"Nombre del producto","URL de la imagen"
"Producto 1","producto1.jpg?aspect=true"
"Producto 2","producto2.jpg?aspect=true"
```
