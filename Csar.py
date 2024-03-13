# Implemente a Cifra de César, uma técnica de criptografia simples que desloca cada letra do alfabeto por um número fixo de posições.
import os
alphabet = ('abcdefghijklmnopqrstuvwyz')
mode = str(input("\n[NUKKLE]\nEscolha o modo que o programa correrá:\n 1 - Criptografar\n 2 - Descriptografar"))
cezarOk = ""
if mode.isnumeric():
    if int(mode) == 1:
        # Criptografar Usando a Cifra de Cézar
        key = int(input("Digite a chave da criptografia"))
        text = str(input("Digite o texto á ser criptografado"))
        text = text.lower()
        for w in text:
            pos = alphabet.find(w)
            pos += key
            if pos > len(alphabet):
                pos -= len(alphabet)
            cezarOk += alphabet[pos]
        print("Cira de César concluída: ", cezarOk)
        os.system('pause')
    elif int(mode) == 2:
        key = int(input("Digite a chave"))
        text = str(input("Digite o texto"))
        for w in text:
            pos = alphabet.find(w)
            pos -= key
            if pos > len(alphabet):
                pos -= len(alphabet)
            cezarOk += alphabet[pos]
        print("Cira de César Reversa concluída: ", cezarOk)
        os.system("pause")