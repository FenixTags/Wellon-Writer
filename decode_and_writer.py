CHAR_VALUES = "abcdefghijklmnopqrstuvwxyz0123456789 "

HEX_VALUES = ['77', '7C', '39', '5E', '79', '71', '6F', '76', '30', '1E',
              '76', '38', '15', '54', '3F', '73', '67', '50', '6D', '78',
              '3E', '1C', '2A', '76', '6E', '5B', '3F', '06', '5B', '4F',
              '66', '6D', '7D', '07', '7F', '6F', '00']

# Nombre del archivo
FILE_NAME = "hexa.txt"
# Tamaño de palabra del display
SIZE_WORD = 8


def start_input():
    textInput = "        "
    # Funcion para introducir el texto y convertirlo a minusculas
    textInput += str(input("Inserte su cadena de texto: "))
    textInput = textInput.lower()
    return textInput


def convert_input(textInput):
    # Reemplaza la entrada a su equivalente en hexadecimal
    textOutput = ""
    for item in textInput:
        # Localiza la letra de la palabra en la lista del hexadecimal
        char = CHAR_VALUES.find(item)
        textOutput += HEX_VALUES[char]
    return textOutput


"""
def input_saver():
    extendedList = []
    repeatFunction = False
    while not repeatFunction:
        textInput = start_input()
        textOutput = convert_input(textInput)
        extendedList.append(textOutput)
        answer = str(input("¿Desea finalizar el programa? [s] ")).lower()
        if answer == 's': repeatFunction = True
    return extendedList
"""


def writer_file(extendedList):
    # Creamos y escribimos un archivo de texto con una lista
    with open(FILE_NAME, "w") as file:
        file.write("\n".join(extendedList))


def splitter_file():
    # Numero de lineas de direccion de datos
    exponent = 15
    # Crea una lista y establece el primer valor en 00 * tamaño de la palabra
    extendedList = ["00" * SIZE_WORD]
    # Obtenemos el texto de entrada
    textInput = start_input()
    sizeWord = len(textInput)
    # En caso de que la frase sea multiplo de 8 se usa esta variable
    # wordMultiSizeWord = True
    while exponent > 1:
        # Capacidad de almacenamiento por cada linea
        twoMultiplier = 2**exponent
        if sizeWord > twoMultiplier and sizeWord % twoMultiplier != 0:
            # wordMultiSizeWord = False
            # En caso de que el tamaño de la palabra no sea
            # de un multiplo de 8, se rellenan los faltantes con espacios
            for index in range(twoMultiplier - (len(textInput) % twoMultiplier)):
                textInput += " "
            break
        elif sizeWord == twoMultiplier:
            break
        exponent -= 1

    # Obtiene el numero de words que se van a ocupar y le suma 1
    sizeWord = len(textInput)
    """
    if wordMultiSizeWord: sizeWord += 1
    # Le suma una word mas para rellenar huecos faltantes y filtrar
    for index in range(SIZE_WORD - (len(textInput) % SIZE_WORD)):
        textInput += " "
    """

    # Para realizar la animacion, elevamos 2 al numero de words para obtener las lineas
    for index in range(sizeWord - 1):
        row = ""
        indexWord = 0
        # Dividimos nuestra entrdaa en words
        while indexWord < SIZE_WORD:
            textInput += " "
            row += textInput[indexWord]
            indexWord += 1
        # Convertimos la word resultante en su equivalente en hexadecimal
        textOutput = convert_input(row)
        # La word en hexadecimal la agregamos a una lista
        extendedList.append(textOutput)
        # Eliminamos la primera palabra de cada word para hacer la animacion
        textInput = textInput[1:]

    return extendedList


def main():
    print("Decodificador para Practica 4")
    """extendedList = input_saver()"""
    extendedList = splitter_file()
    writer_file(extendedList)
    print(extendedList)


if __name__ == '__main__':
    main()
