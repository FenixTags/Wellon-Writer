CHAR_VALUES = "abcdefghijklmnopqrstuvwxyz0123456789 "


HEX_VALUES = ['77', '7C', '39', '5E', '79', '71', '6F', '76', '30', '1E',
            '76', '38', '15', '54', '3F', '73', '67', '50', '6D', '78',
            '3E', '1C', '2A', '76', '6E', '5B', '3F', '06', '5B', '4F',
            '66', '6D', '7D', '07', '7F', '6F', '00']


def start_input():
    textInput = str(input("Inserte su cadena de texto: "))
    textInput = textInput.lower()
    return textInput


def convert_input(textInput):
    textOutput = ""
    for item in textInput:
        char = CHAR_VALUES.find(item)
        textOutput += HEX_VALUES[char] + ' '
    return textOutput


def main():
    print("Decodificador para Practica 4")
    while True:
        textInput = start_input()
        textOutput = convert_input(textInput)
        print("\nTu salida es:")
        print(textOutput, end="\n\n")


if __name__ == '__main__':
    main()
