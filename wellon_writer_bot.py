import keyboard
FILE_NAME = "hexa.txt"


def read_file():
    hexaCodeString = ""
    try:
        with open(FILE_NAME, "r") as file:
            hexaCodeList = file.read().split('\n')
            for item in hexaCodeList:
                hexaCodeString += item
            return hexaCodeString
    except FileNotFoundError:
        print("Error: File not found")


def writing(file):
    print("Listening...")
    # El programa se espera hasta presionar la tecla
    keyboard.wait('left ctrl')
    # Comenzamos a escribir con el teclado
    keyboard.write(file)


def main():
    file = read_file()
    writing(file)


if __name__ == "__main__":
    main()
