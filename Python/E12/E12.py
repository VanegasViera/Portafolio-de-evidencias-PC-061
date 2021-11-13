import argparse
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
translated = ''

parser = argparse.ArgumentParser()
parser.add_argument('-msg',dest="msg",help='El mensaje que desea cifrar')
parser.add_argument('-msgc',dest="msgc",help='El mensaje cifrado')
parser.add_argument('-pc', dest="pc",help='Palabra clave para cifrar/decifrar')

args=parser.parse_args()
#---cifrar---#
message=(args.msg)
#---decifrar---#
messagec=(args.msgc)
#---clave--#
clave=(args.pc)
if clave!=None:
    key=len(clave)
#--------------------Cifrar un mensaje dada una clave--------------------#
if message!=None and clave!=None:
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex + key
            
            if translatedIndex >= len(SYMBOLS):
                translatedIndex = translatedIndex - len(SYMBOLS)
            elif translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

            translated = translated + SYMBOLS[translatedIndex]
        else:
            translated = translated + symbol
#--------------------Cifrar un mensaje dada una clave--------------------#
if messagec!=None and clave!=None:
    for symbol in messagec:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex - key
            
            if translatedIndex >= len(SYMBOLS):
                translatedIndex = translatedIndex - len(SYMBOLS)
            elif translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

            translated = translated + SYMBOLS[translatedIndex]
        else:
            translated = translated + symbol
print(translated)
#--------------------Crackear un mensaje cifrado--------------------#
if messagec!=None and clave==None:
    for key in range(len(SYMBOLS)):
        translated = ''
        for symbol in messagec:
            if symbol in SYMBOLS:
                symbolIndex = SYMBOLS.find(symbol)
                translatedIndex = symbolIndex - key
                if translatedIndex < 0:
                    translatedIndex = translatedIndex + len(SYMBOLS)
                translated = translated + SYMBOLS[translatedIndex]
            else:
                translated = translated + symbol
        print('Key #%s: %s' % (key, translated))
#--------------------validar que sea un mensaje en español--------------------#

    MAYUSCULAS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    LETRAS_Y_ESPACIOS = MAYUSCULAS + MAYUSCULAS.lower() + ' \t\n'

    def loadDictionary():
        dictionaryFile = open('dictEsp.txt', encoding='utf-8')
        englishWords = {}
        for word in dictionaryFile.read().split('\n'):
            word = word.upper()
            englishWords[word] = None
        dictionaryFile.close()
        return englishWords

    SPANISH_WORDS = loadDictionary()

    def getSpanishCount(message):
        message = message.upper()
        message = removeNonLetters(message)
        possibleWords = message.split()
        if possibleWords == []:
            return 0.0

        matches = 0
        for word in possibleWords:
            if word in SPANISH_WORDS:
                matches += 1
        return float(matches) / len(possibleWords)


    def removeNonLetters(message):
        lettersOnly = []
        for symbol in message:
            if symbol in LETRAS_Y_ESPACIOS:
                lettersOnly.append(symbol)
        return ''.join(lettersOnly)


    def isSpanish(message, wordPercentage=40, letterPercentage=85):

        wordsMatch = getSpanishCount(message) * 100 >= wordPercentage
        numLetters = len(removeNonLetters(message))
        messageLettersPercentage = float(numLetters) / len(message) * 100
        lettersMatch = messageLettersPercentage >= letterPercentage
        return wordsMatch and lettersMatch

    def crackeo(mensaje):
        SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
        for key in range(1, len(SYMBOLS)):
            trad = ''
            for abc in mensaje:
                if abc in SYMBOLS:
                    abcIndex = SYMBOLS.find(abc)
                    tradIndex = abcIndex - key

                    if tradIndex < 0:
                        tradIndex = tradIndex + len(SYMBOLS)

                    trad = trad + SYMBOLS[tradIndex]

                else:
                    trad = trad + abc


            if isSpanish(trad):
                print("Key:", str(key)+". Mensaje encontrado: "+trad[:100])
                print("Válido para idioma español")
    print()
    crackeo(messagec)

