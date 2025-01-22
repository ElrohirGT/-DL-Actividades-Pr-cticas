# -DL-Actividades-Pr-cticas

Este código implementa un sistema de lectura de cadenas utilizando un buffer fijo. 

## Objetivo

El propósito principal del código es dividir una cadena de entrada en "lexemas" utilizando un buffer de tamaño fijo (tamaño fijo de 10).

## Funcionalidad Principal

### 1. **Función `cargar_buffer`**

Carga un segmento de la cadena de entrada dentro de un buffer de tamaño predefinido. Si la cantidad de caracteres restantes en la entrada es menor que el tamaño del buffer, el buffer se rellena con el marcador `"eof"` (end of file) y espacios en blanco para completar el tamaño.

#### Parámetros:
- `entrada`: Lista de caracteres que representan la cadena de entrada.
- `inicio`: Índice inicial desde donde se debe leer la cadena.
- `tamano_buffer`: Tamaño máximo del buffer.

#### Retorno:
- Una lista de tamaño fijo que contiene los caracteres leídos, completados con `"eof"` y espacios si es necesario.

---

### 2. **Función `procesar_buffer`**

Lee y procesa la cadena de entrada en segmentos utilizando el buffer cargado por `cargar_buffer`. Identifica "lexemas" separados por espacios y los almacena en una lista.

#### Parámetros:
- `entrada`: Lista de caracteres que representan la cadena de entrada.
- `TAMAÑO_BUFFER`: Tamaño del buffer fijo.

#### Proceso:
1. **Inicialización:**
   - Define índices `inicio` y `avance` para controlar la posición en la cadena.
   - Llama a `cargar_buffer` para inicializar el buffer.
   - Define una lista `lexemas` para almacenar los lexemas encontrados.

2. **Procesamiento del Buffer:**
   - Lee caracteres del buffer y construye un lexema en `localBuffer`.
   - Si encuentra un espacio o `"eof"`, considera el contenido acumulado como un lexema y lo almacena en `lexemas`.
   - Si el índice `avance` alcanza el final del buffer, se recarga con nuevos datos de la entrada.

3. **Condiciones de Término:**
   - Finaliza cuando se alcanza el marcador `"eof"`.
   - Tiene un límite de iteraciones para evitar bucles infinitos (parámetro de depuración).

#### Retorno:
- Una lista de lexemas extraídos de la cadena de entrada.

---

## Ejemplo de Ejecución

### Entrada:
```python
entrada = list("Esto es un ejemplo eof")
```

### Salida:
```python
['Esto', 'es', 'un', 'ejemplo','eof']
```
