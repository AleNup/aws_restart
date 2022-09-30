#Retorna un string concatenado dos alfabetos
def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet
#Entrar mensaje a encriptar
def getMessage():
    stringToEncrypt = input("Please enter a message to encrypt: ")
    return stringToEncrypt
#Ingresa la cantidad de letras que estará saltando
def getCipherKey():
    shiftAmount = input( "Please enter a key (whole number from 1-25): ")
    return shiftAmount
#Se encripta el mensaje
def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    uppercaseMessage = ""
    uppercaseMessage = message.upper() #convertirenmayuscula
    for currentCharacter in uppercaseMessage: 
        position = alphabet.find(currentCharacter) #Guarda la posicion inicial del caracter
        newPosition = position + int(cipherKey) #Nueva posición 
        if currentCharacter in alphabet:
            encryptedMessage = encryptedMessage + alphabet[newPosition]
        else:
            encryptedMessage = encryptedMessage + currentCharacter #Se acumulan los caracteres hasta que el valor sea correcto
    return encryptedMessage
#se verifica que el mensaje se haya encriptado correctamente
def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -1 * int(cipherKey)
    return encryptMessage(message, decryptKey, alphabet)
#Se invoca la función    
def runCaesarCipherProgram():
    myAlphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alphabet: {myAlphabet}')
    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    print(f'Alphabet2: {myAlphabet2}')
    myMessage = getMessage() #se trae el mensaje
    print(myMessage)
    myCipherKey = getCipherKey() # se trae la llave
    print(myCipherKey)
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2) #se encripta la llave
    print(f'Encrypted Message: {myEncryptedMessage}')
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2) #se desencripta la llave
    print(f'Decypted Message: {myDecryptedMessage}')

runCaesarCipherProgram() #se corre el programa