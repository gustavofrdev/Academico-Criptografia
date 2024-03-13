# Crie uma cifra de substituição simples, onde você mapeia cada letra para
# outra letra do alfabeto. for i in range(1000):
import random
import os, sys

alphabet = 'abcdefghijklmnopqrstuvwyz'
key = ""
result = ""


def generateRandomAlphabet():
    resultRand = ""
    lettersUsed = []
    i = 0
    print(len(alphabet))
    while i < len(alphabet) - 1:
        index = random.randint(1, len(alphabet) - 1)
        if not alphabet[index] in lettersUsed:
            resultRand += alphabet[index]
            lettersUsed.append(alphabet[index])
            i += 1
    return resultRand + 'a'


def checkDoubleLetters(string):
    duplicates = []
    for letter in string:
        if string.count(letter) > 1 and letter not in duplicates:
            duplicates.append(letter)
    return duplicates

usage = str(input("[NUKKLE]\n Escolha a ação: \n 1 - Criptografar \n 2 - Descriptografar"))
if usage.isnumeric() and int(usage) == 1:
    text = str(input("Digite o texto a ser encriptado:"))
    choice = str(input("[NUKKLE]\n 1 - Sistema gerará a chave de encriptação\n 2 - Você digita sua própria chave de encriptação"))
    text = text.lower()
    if choice.isnumeric() and int(choice) == 1:
        newAlphabet = generateRandomAlphabet()
        print("[NUKKLE]\n Sistema gerará sua chave de encriptação")
        print("[NUKKLE]\n Chave gerada: ", newAlphabet)
        key = newAlphabet
    if choice.isnumeric() and int(choice) == 2:
        print('[NUKKLE]\n Você escreverá sua chave\n A chave deverá ter o mesmo tamanho do alfabeto\n[''ALERTA CRIACAO DE CHAVES]\n**Lembrando que: Uma chave de substituição deverá ser sua representação do alfabeto e portando, não pode ter palavras repetidas. \nCausará confusão ao remover a criptografia da imagem**\nCaso não se sinta seguro em criar sua própria chave, mande o sistema gerar. ',len(alphabet))
        while True:
            newKey = str(input("Digite a chave de encriptação personalizada: "))
            if checkDoubleLetters(newKey):
                print("[NUKKLE]\n Há letras repetidas no seu alfabeto personalizado.\n")
            elif len(newKey) < len(alphabet):
                print("[NUKKLE]\n Sua chave de encriptação personalizada deverá conter a mesma quantidade de caractéres do alfabeto comum. \n Seu Alfabeto: ",len(newKey), "alfabeto comum: ", len(alphabet))
            else:
                break
        key = newKey
    ## Encriptar usando a chave concedida:
    for i in text:
        indexLetter = alphabet.find(i)
        if indexLetter != -1:
            refInKey = key[indexLetter]
            result += refInKey
        elif indexLetter == -1:
            result += i

    print("[NUKKLE]\n Resultado da cifra:", result, "\n Usando a chave: ", key,'\n ####[COMPARAÇÃO]####\n Mensagem original'':', text, "\n Alfabeto Original:", alphabet)
    os.system('pause')
elif usage.isnumeric() and int(usage) == 2:
    m = 0
    cryptoText = str(input("Digite o texto cifrado"))
    cryptoKey = str(input("Digite a chave do texto cifrado"))
    for i in cryptoText:
        indexLetter = cryptoKey.find(i)
        if indexLetter != -1:
            refInKey = alphabet[indexLetter]
            result += refInKey
        else:
            result += i
    print("[NUKKLE]\n Resultado da cifra reversa*substituição*:", result, "\n Usando a chave: ", cryptoKey,'\n Do texto cifrado:', cryptoText)
    os.system('pause')
# Gustavo Ferreira dos Reis
# Github/gustavofrdev
# Fatec Americana - Criptografia - Segurança da Informação
