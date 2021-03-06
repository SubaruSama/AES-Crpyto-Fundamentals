#!/usr/bin/python
﻿# coding = UTF-8

'''
Chave AES foi criptografada com RSA
Foi salva em um arquivo
Entrar o caminho em que a chave do AES esta protegida com RSA
para descriptografar, entrar com a chave privada do RSA
e voila, chave do AES esta ai
'''


import os
import os.path as path
import pyaes
import time
# import argparse
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

'''
Gerar um par de chaves RSA protegida por um passphrase
Criptografar a chave do AES gerado com a chave privada do RSA
Descritpografar a chave do AES com a chave publica da pessoa que enviou
'''


def hello():
   print u''' 
 █████╗ ███████╗███████╗     ██████╗██████╗  ██████╗       ███████╗ ██████╗██████╗ 
██╔══██╗██╔════╝██╔════╝    ██╔════╝██╔══██╗██╔════╝       ██╔════╝██╔════╝██╔══██╗
███████║█████╗  ███████╗    ██║     ██████╔╝██║            █████╗  ██║     ██████╔╝
██╔══██║██╔══╝  ╚════██║    ██║     ██╔══██╗██║            ██╔══╝  ██║     ██╔══██╗
██║  ██║███████╗███████║    ╚██████╗██████╔╝╚██████╗▄█╗    ███████╗╚██████╗██████╔╝
╚═╝  ╚═╝╚══════╝╚══════╝     ╚═════╝╚═════╝  ╚═════╝╚═╝    ╚══════╝ ╚═════╝╚═════╝ 
                                                                                   
 █████╗ ███╗   ██╗██████╗     ██████╗ ███████╗ █████╗                              
██╔══██╗████╗  ██║██╔══██╗    ██╔══██╗██╔════╝██╔══██╗                             
███████║██╔██╗ ██║██║  ██║    ██████╔╝███████╗███████║                             
██╔══██║██║╚██╗██║██║  ██║    ██╔══██╗╚════██║██╔══██║                             
██║  ██║██║ ╚████║██████╔╝    ██║  ██║███████║██║  ██║                             
╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝'''

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def createKey(size):
    key = os.urandom(size)

    return key

def createIV(size):
    iv = os.urandom(size)

    return iv

### AES ECB ###
def aes_ecb():
    print("O AES-ECB possui dois tamanhos de chave no programa: 128 e 256 bits. Escholha um.\n1 - 128 bits\n2 - 256 bits")
    tamanho = int(raw_input(">> "))

    if tamanho == 1:

        aes_ecb_128()
        # vai para a funcao de aes ecb com 128 bits

    elif tamanho == 2:

        aes_ecb_256()
        # vai para a funcao de aes ecb com 256 bits

    else:

        print("Wat... Alguma coisa deu errado :<")
        aes_ecb()


def aes_ecb_128():

    # Function to encrypt with AES in mode ECB with key size 128 bits
    print("Bem vindo ao modulo de criptografia com o algoritmo AES no modo ECB 128 bits")
    # Encrypt or Decrypt?
    print("O modulo possui duas opcoes:\n1 - Criptografar\n2 - Decritpografar")
    crypt_or_decrypt = int(raw_input(">> "))

    if crypt_or_decrypt == 1: # Encrypt data

        clear()
        print("Funcao que ira tratar o AES no modo ECB com o tamanho da chave 128 bits")
        print("O texto que ira entrar TEM QUE TER 16 BYTES\n")
        plaintext = str(raw_input("Plaintext: "))
        conferindo_text = len(plaintext)

        if conferindo_text < 16:

            print("Plaintext precisa de mais caracteres. O texto possui: {} letras".format(len(conferindo_text)))
            time.sleep(2)
            aes_ecb_128()

        elif conferindo_text > 16:

            print("Plaintext precisa de menos caracteres. O texto possui: {} letras".format(len(conferindo_text)))
            time.sleep(2)
            aes_ecb_128()

        # Abrir o arquivo e escrever nele
        nome_arquivo = raw_input("Digite o nome do arquivo para ser criado: ")
        print("Criando arquivo...")
        # x da funcao de encriptogragar
        file_in = open(nome_arquivo + '.txt', 'w+')
        file_in_hex = open(nome_arquivo + '_in_hex' + '.txt', 'w+')

        escolha = raw_input("Deseja gerar uma chave randomicamente? (AES + key pair RSA) (Y/N): ")

        if escolha == 'Y' or escolha == 'y':

            key_gerada = createKey(16)
            # Para o RSA
            supah_secret_code = str(raw_input("Para gerar um par de chaves para o RSA, precisamos que entre com uma passphrase: "))
            # Para motivos de nomes de arquivo
            nome_user = str(raw_input("Por favor, digite o seu nome: "))
            # Tamanho da chave = 2048 bits recomendado
            key_pair = RSA.generate(2048)
            enc_key = key_pair.exportKey(passphrase=supah_secret_code)
            key_pub = key_pair.publickey().exportKey()
            key_prv8 = key_pair.exportKey()
            # Criptografando a chave AES com RSA aqui
            cipher_RSA = PKCS1_OAEP.new(key_pair.publickey())
            aes_encrypted_with_RSA = cipher_RSA.encrypt(key_gerada)
            file_out_aes_encrypted_RSA = open('aes_key_rsa', 'wb')
            file_out_aes_encrypted_RSA.write(aes_encrypted_with_RSA)
            file_out_aes_encrypted_RSA.close()
            # Terminando aqui
            file_out_pub = open('%s' % nome_user + '.pu', 'wb') # para chave publica
            file_out_prv8 = open('%s' % nome_user + '.pr', 'wb') # para a chave privada
            print("Chave criada em ascii: {}".format(key_gerada))
            print("Chave criada em hex: {}".format(key_gerada.encode('hex')))
            print("Chave publica:\n%s" % (key_pub))
            aes_exec = pyaes.AESModeOfOperationECB(key_gerada)
            ciphertext = aes_exec.encrypt(plaintext)
            # Escrever no arquivo o ciphertext
            file_in.write("{}".format(ciphertext))
            file_in_hex.write("{}".format(ciphertext.encode('hex')))
            file_out_pub.write(key_pub)
            file_out_prv8.write(key_prv8)
            file_out_pub.close()
            file_out_prv8.close()
            file_in.close()
            file_in_hex.close()

        elif escolha == 'N' or escolha == 'n':

            print("A chave TEM QUE TER 16 BYTES\n")
            print("!!! tenha certeza que ninguem esta olhando !!!").upper()
            key_user = str(raw_input("K: "))
            conferindo_chave = len(key_user)

            if conferindo_chave < 16:

                print("Coloque mais caracteres para fechar 16 bytes. A chave possui {} caracteres".format(len(conferindo_chave)))
                aes_ecb_128()

            elif conferindo_chave > 16:

                print("Retire mais caracteres para fechar 16 bytes. A chave possui {} caracteres".format(len(conferindo_chave)))
                aes_ecb_128()

            else:

                aes_exec = pyaes.AESModeOfOperationECB(key_user)
                ciphertext = aes_exec.encrypt(plaintext)
                # file_in.write("{}\n".format(ciphertext.encode('hex')))
                file_in.write("{}".format(ciphertext)) # Writing in ascii mode
                file_in_hex.write("{}".format(ciphertext.encode('hex'))) # Writing in hex mode in a file
                file_in.close()
                file_in_hex.close()

        print("Ciphertext em ascii: {}".format(ciphertext))
        print("Ciphertext em hex: {}".format(ciphertext.encode('hex')))

    elif crypt_or_decrypt == 2:
        nome_arquivo = raw_input("Digite o nome do arquivo para abrir: ")

        if os.path.isfile(nome_arquivo + '.txt'):
            print("Existe")
            # Agora que ja sei que o arquivo existe, vamos ler o que tem dentro
            file_out = open(nome_arquivo + '.txt', 'r')
            conteudo = file_out.read()
            print(conteudo)

            try:

                key = raw_input("Digite a chave: ")
                key = key.decode('hex')

            except ValueError:

                print("Tamanho da chave nao e 16 bytes")
                aes_ecb_128()

            except TypeError:

                print("Chave tem que ser em hexadecimal\n")
                aes_ecb_128()

            aes_decrypt = pyaes.AESModeOfOperationECB(key)
            x = aes_decrypt.decrypt(conteudo)

            plaintext = raw_input("Digite o nome do arquivo para salvar o X: ")
            plaintext_arquivo = open(plaintext + '.txt', 'w+')
            plaintext_arquivo.write("{}".format(x))
            plaintext_arquivo.close()

        else:

            print("Arquivo inexistente")
            aes_ecb_128()

        # file_out = open(nome_arquivo + '.txt', 'w+')

def aes_ecb_256():
    print("Bem vindo ao modulo de criptografia com o algoritmo AES no modo ECB 256 bits")
    # Encrypt or Decrypt?
    print("O modulo possui duas opcoes:\n1 - Criptografar\n2 - Decritpografar")
    crypt_or_decrypt = int(raw_input(">> ")) 

    if crypt_or_decrypt == 1: # Encrypting data

        clear()
        print("Funcao que ira tratar o AES no modo ECB com o tamanho da chave 256 bits")
        print("O texto que ira entrar TEM QUE TER 16 BYTES\n")
        plaintext = str(raw_input("Plaintext: "))
        conferindo_text = len(plaintext)

        if conferindo_text < 16:

            print("Plaintext precisa de mais caracteres. O texto possui {} caracteres".format(len(conferindo_text)))
            time.sleep(2)
            aes_ecb_256()

        elif conferindo_text > 16:

            print("Plaintext precisa de menos caracteres. O texto possui {} caracteres".format(len(conferindo_text)))
            time.sleep(2)
            aes_ecb_256()

        # Abrir o arquivo e escrever nele
        nome_arquivo = raw_input("Digite o nome do arquivo para ser criado: ")
        print("Criando arquivo...")
        # x da funcao de encriptogragar
        file_in = open(nome_arquivo + '.txt', 'w+')
        file_in_hex = open(nome_arquivo + '_in_hex' + '.txt', 'w+')

        escolha = raw_input("Deseja gerar uma chave randomicamente? (Y/N): ")

        if escolha == 'Y' or escolha == 'y':

            # key_gerada = createKey(32)
            # print("Chave criada em ascii: {}".format(key_gerada))
            # print("Chave criada em hex: {}".format(key_gerada.encode('hex')))
            # aes_exec = pyaes.AESModeOfOperationECB(key_gerada)
            # ciphertext = aes_exec.encrypt(plaintext)
            # # Escrever no arquivo o ciphertext
            # # file_in.write("{}\n".format(ciphertext.encode('hex')))
            # file_in.write("{}".format(ciphertext))
            # file_in_hex.write("{}".format(ciphertext.encode('hex')))
            # file_in.close()
            # file_in_hex.close()

            key_gerada = createKey(32)
            # Para o RSA
            supah_secret_code = str(raw_input("Para gerar um par de chaves para o RSA, precisamos que entre com uma passphrase: "))
            # Para motivos de nomes de arquivo
            nome_user = str(raw_input("Por favor, digite o seu nome: "))
            # Tamanho da chave = 2048 bits recomendado
            key_pair = RSA.generate(2048)
            enc_key = key_pair.exportKey(passphrase=supah_secret_code)
            key_pub = key_pair.publickey().exportKey()
            key_prv8 = key_pair.exportKey()
            # Criptografando a chave AES com RSA aqui
            cipher_RSA = PKCS1_OAEP.new(key_pair.publickey())
            aes_encrypted_with_RSA = cipher_RSA.encrypt(key_gerada)
            file_out_aes_encrypted_RSA = open('aes_key_rsa', 'wb')
            file_out_aes_encrypted_RSA.write(aes_encrypted_with_RSA)
            file_out_aes_encrypted_RSA.close()
            # Terminando aqui
            file_out_pub = open('%s' % nome_user + '.pu', 'wb') # para chave publica
            file_out_prv8 = open('%s' % nome_user + '.pr', 'wb') # para a chave privada
            print("Chave criada em ascii: {}".format(key_gerada))
            print("Chave criada em hex: {}".format(key_gerada.encode('hex')))
            print("Chave publica:\n%s" % (key_pub))
            aes_exec = pyaes.AESModeOfOperationECB(key_gerada)
            ciphertext = aes_exec.encrypt(plaintext)
            # Escrever no arquivo o ciphertext
            file_in.write("{}".format(ciphertext))
            file_in_hex.write("{}".format(ciphertext.encode('hex')))
            file_out_pub.write(key_pub)
            file_out_prv8.write(key_prv8)
            file_out_pub.close()
            file_out_prv8.close()
            file_in.close()
            file_in_hex.close()

        elif escolha == 'N' or escolha == 'n':

            print("A chave TEM QUE TER 32 BYTES\n")
            print("!!! tenha certeza que ninguem esta olhando !!!").upper()
            key_user = str(raw_input("K: "))
            conferindo_chave = len(key_user)

            if conferindo_chave < 32:

                print("Coloque mais caracteres para fechar 32 bytes. A chave possui {} caracteres".format(len(conferindo_chave)))
                aes_ecb_256()

            elif conferindo_chave > 32:

                print("Retire mais caracteres para fechar 32 bytes. A chave possui {} caracteres".format(len(conferindo_chave)))
                aes_ecb_256()

            else:

                aes_exec = pyaes.AESModeOfOperationECB(key_user)
                ciphertext = aes_exec.encrypt(plaintext)
                # file_in.write("{}\n".format(ciphertext.encode('hex')))
                file_in.write("{}".format(ciphertext))
                file_in_hex.write("{}".format(ciphertext.encode('hex')))
                file_in.close()
                file_in_hex.close()

        print("Ciphertext em ascii: {}".format(ciphertext))
        print("Ciphertext em hex: {}".format(ciphertext.encode('hex')))

    elif crypt_or_decrypt == 2:
        nome_arquivo = raw_input("Digite o nome do arquivo para abrir: ")

        if os.path.isfile(nome_arquivo + '.txt'):
            print("Existe")
            # Agora que ja sei que o arquivo existe, vamos ler o que tem dentro
            file_out = open(nome_arquivo + '.txt', 'r')
            conteudo = file_out.read()
            print(conteudo)

            try:

                key = raw_input("Digite a chave: ")
                key = key.decode('hex')

            except ValueError:

                print("Tamanho da chave nao e 32 bytes")
                aes_ecb_256()

            except TypeError:

                print("Chave tem que ser em hexadecimal\n")
                aes_ecb_256()

            aes_decrypt = pyaes.AESModeOfOperationECB(key)
            x = aes_decrypt.decrypt(conteudo)

            plaintext = raw_input("Digite o nome do arquivo para salvar o X: ")
            plaintext_arquivo = open(plaintext + '.txt', 'w+')
            plaintext_arquivo.write("{}".format(x))
            plaintext_arquivo.close()

        else:

            print("Arquivo inexistente")
            aes_ecb_256()
### AES ECB ###

### AES CBC ###
def aes_cbc():
    clear()
    print("O AES-CBC possui dois tamanhos de chave no programa: 128 e 256 bits. Escholha um.\n1 - 128 bits\n2 - 256 bits")
    tamanho = int(raw_input(">> "))

    if tamanho == 1:

        aes_cbc_128()

    elif tamanho == 2:

        aes_cbc_256()

    else:
        print("Wat... Alguma coisa deu errado :<")

def aes_cbc_128():
    print("Bem vindo ao modulo de criptografia com o algoritmo AES no modo CBC 128 bits")
    # Encrpyt or Decrypt?
    print("O modulo possui duas opcoes:\n1 - Criptografar\n2 - Decritpografar")
    crypt_or_decrypt = int(raw_input(">> ")) 

    if crypt_or_decrypt == 1: # Criptografando os dados

        clear()
        print("Funcao que ira tratar o AES no modo CBC com o tamanho da chave 128 bits")
        print("O texto que ira entrar TEM QUE TER 16 BYTES\n")
        plaintext = str(raw_input("Plaintext: "))
        conferindo_text = len(plaintext)

        if conferindo_text < 16:

            print("Plaintext precisa de mais caracteres")
            time.sleep(2)
            aes_cbc_128()

        elif conferindo_text > 16:

            print("Plaintext precisa de menos caracteres")
            time.sleep(2)
            aes_cbc_128()

        # Abrir o arquivo e escrever nele
        nome_arquivo = raw_input("Digite o nome do arquivo para ser criado: ")
        print("Criando arquivo...")
        # x da funcao de encriptografar
        file_in = open(nome_arquivo + '.txt', 'w+')
        file_in_hex = open(nome_arquivo + '_in_hex' + '.txt', 'w+')

        escolha_iv = raw_input("Deseja gerar um IV randomicamente? (Y/N): ")

        if escolha_iv == 'Y' or escolha_iv == 'y':

            iv_gerado = createIV(16)
            print("IV criado em ascii: {}".format(iv_gerado))
            print("IV criado em hex: {}".format(iv_gerado.encode('hex')))
            iv_final = iv_gerado

        elif escolha_iv == 'N' or escolha_iv == 'n':
            print("IV TEM QUE SER 16 BYTES")
            iv = raw_input("Digite o IV: ")
            iv_final = iv

        escolha = raw_input("Deseja gerar uma chave randomicamente? (Y/N): ")

        if escolha == 'Y' or escolha == 'y':

            # key_gerada = createKey(16)
            # print("Chave criada em ascii: {}".format(key_gerada))
            # print("Chave criada em hex: {}".format(key_gerada.encode('hex')))
            # aes_exec = pyaes.AESModeOfOperationCBC(key_gerada, iv = iv_final)
            # ciphertext = aes_exec.encrypt(plaintext)
            # # Escrever no arquivo o ciphertext
            # # file_in.write("{}\n".format(ciphertext.encode('hex')))
            # file_in.write("{}".format(ciphertext))
            # file_in_hex.write("{}".format(ciphertext.encode('hex')))
            # file_in.close()
            # file_in_hex.close()

            key_gerada = createKey(16)
            # Para o RSA
            supah_secret_code = str(raw_input("Para gerar um par de chaves para o RSA, precisamos que entre com uma passphrase: "))
            # Para motivos de nomes de arquivo
            nome_user = str(raw_input("Por favor, digite o seu nome: "))
            # Tamanho da chave = 2048 bits recomendado
            key_pair = RSA.generate(2048)
            enc_key = key_pair.exportKey(passphrase=supah_secret_code)
            key_pub = key_pair.publickey().exportKey()
            key_prv8 = key_pair.exportKey()
            # Criptografando a chave AES com RSA aqui
            cipher_RSA = PKCS1_OAEP.new(key_pair.publickey())
            aes_encrypted_with_RSA = cipher_RSA.encrypt(key_gerada)
            file_out_aes_encrypted_RSA = open('aes_key_rsa', 'wb')
            file_out_aes_encrypted_RSA.write(aes_encrypted_with_RSA)
            file_out_aes_encrypted_RSA.close()
            # Terminando aqui
            file_out_pub = open('%s' % nome_user + '.pu', 'wb') # para chave publica
            file_out_prv8 = open('%s' % nome_user + '.pr', 'wb') # para a chave privada
            print("Chave criada em ascii: {}".format(key_gerada))
            print("Chave criada em hex: {}".format(key_gerada.encode('hex')))
            print("Chave publica:\n%s" % (key_pub))
            aes_exec = pyaes.AESModeOfOperationCBC(key_gerada, iv = iv_final)
            ciphertext = aes_exec.encrypt(plaintext)
            # Escrever no arquivo o ciphertext
            file_in.write("{}".format(ciphertext))
            file_in_hex.write("{}".format(ciphertext.encode('hex')))
            file_out_pub.write(key_pub)
            file_out_prv8.write(key_prv8)
            file_out_pub.close()
            file_out_prv8.close()
            file_in.close()
            file_in_hex.close()

        elif escolha == 'N' or escolha == 'n':

            print("A chave TEM QUE TER 16 BYTES\n")
            print("!!! tenha certeza que ninguem esta olhando !!!").upper()
            key_user = str(raw_input("K: "))
            conferindo_chave = len(key_user)

            if conferindo_chave < 16:

                print("Coloque mais caracteres para fechar 16 bytes")
                aes_cbc_128()

            elif conferindo_chave > 16:

                print("Retire mais caracteres para fechar 16 bytes")
                aes_cbc_128()

            else:

                aes_exec = pyaes.AESModeOfOperationCBC(key_user, iv = iv_final)
                ciphertext = aes_exec.encrypt(plaintext)
                # file_in.write("{}\n".format(ciphertext.encode('hex')))
                file_in.write("{}".format(ciphertext))
                file_in_hex.write("{}".format(ciphertext.encode('hex')))
                file_in.close()
                file_in_hex.close()

        print("Ciphertext em ascii: {}".format(ciphertext))
        print("Ciphertext em hex: {}".format(ciphertext.encode('hex')))

    elif crypt_or_decrypt == 2:
        nome_arquivo = raw_input("Digite o nome do arquivo para abrir: ")

        if os.path.isfile(nome_arquivo + '.txt'):
            print("Existe")
            # Agora que ja sei que o arquivo existe, vamos ler o que tem dentro
            file_out = open(nome_arquivo + '.txt', 'r')
            conteudo = file_out.read()
            print(conteudo)

            try:
                key = raw_input("Digite a chave: ")
                key = key.decode('hex')
            except ValueError:
                print("Tamanho da chave nao e 16 bytes")
                aes_cbc_128()
            except TypeError:
                print("Chave tem que ser em hexadecimal\n")
                aes_cbc_128()

            try:
                iv = raw_input("Digite o IV: ")
                iv = iv.decode('hex')
            except ValueError:
                print("Tamanho do IV nao e 16 bytes")
                aes_cbc_128()
            except TypeError:
                print("IV tem que ser em hexadecimal\n")
                aes_cbc_128()

            aes_decrypt = pyaes.AESModeOfOperationCBC(key, iv = iv)
            x = aes_decrypt.decrypt(conteudo)

            plaintext = raw_input("Digite o nome do arquivo para salvar o X: ")
            plaintext_arquivo = open(plaintext + '.txt', 'w+')
            plaintext_arquivo.write("{}".format(x))
            plaintext_arquivo.close()

def aes_cbc_256():
    print("Bem vindo ao modulo de criptografia com o algoritmo AES no modo CBC 256 bits")
    print("O modulo possui duas opcoes:\n1 - Criptografar\n2 - Decritpografar")
    crypt_or_decrypt = int(raw_input(">> ")) 

    if crypt_or_decrypt == 1: # Criptografando os dados

        clear()
        print("Funcao que ira tratar o AES no modo CBC com o tamanho da chave 256 bits")
        print("O texto que ira entrar TEM QUE TER 16 BYTES\n")
        plaintext = str(raw_input("Plaintext: "))
        conferindo_text = len(plaintext)

        if conferindo_text < 16:

            print("Plaintext precisa de mais caracteres")
            time.sleep(2)
            aes_cbc_256()

        elif conferindo_text > 16:

            print("Plaintext precisa de menos caracteres")
            time.sleep(2)
            aes_cbc_256()

        # Abrir o arquivo e escrever nele
        nome_arquivo = raw_input("Digite o nome do arquivo para ser criado: ")
        print("Criando arquivo...")
        # x da funcao de encriptografar
        file_in = open(nome_arquivo + '.txt', 'w+')
        file_in_hex = open(nome_arquivo + '_in_hex' + '.txt', 'w+')

        escolha_iv = raw_input("Deseja gerar um IV randomicamente? (Y/N): ")

        if escolha_iv == 'Y' or escolha_iv == 'y':

            iv_gerado = createIV(16)
            print("IV criado em ascii: {}".format(iv_gerado))
            print("IV criado em hex: {}".format(iv_gerado.encode('hex')))

        elif escolha_iv == 'N' or escolha_iv == 'n':
            print("IV TEM QUE SER 16 BYTES")
            iv = raw_input("Digite o IV: ")

        escolha = raw_input("Deseja gerar uma chave randomicamente? (Y/N): ")

        if escolha == 'Y' or escolha == 'y':

            # key_gerada = createKey(32)
            # print("Chave criada em ascii: {}".format(key_gerada))
            # print("Chave criada em hex: {}".format(key_gerada.encode('hex')))
            # aes_exec = pyaes.AESModeOfOperationCBC(key_gerada, iv = iv_gerado)
            # ciphertext = aes_exec.encrypt(plaintext)
            # # Escrever no arquivo o ciphertext
            # # file_in.write("{}\n".format(ciphertext.encode('hex')))
            # file_in.write("{}".format(ciphertext))
            # file_in_hex.write("{}".format(ciphertext.encode('hex')))
            # file_in.close()
            # file_in_hex.close()

            key_gerada = createKey(32)
            # Para o RSA
            supah_secret_code = str(raw_input("Para gerar um par de chaves para o RSA, precisamos que entre com uma passphrase: "))
            # Para motivos de nomes de arquivo
            nome_user = str(raw_input("Por favor, digite o seu nome: "))
            # Tamanho da chave = 2048 bits recomendado
            key_pair = RSA.generate(2048)
            enc_key = key_pair.exportKey(passphrase=supah_secret_code)
            key_pub = key_pair.publickey().exportKey()
            key_prv8 = key_pair.exportKey()
            # Criptografando a chave AES com RSA aqui
            cipher_RSA = PKCS1_OAEP.new(key_pair.publickey())
            aes_encrypted_with_RSA = cipher_RSA.encrypt(key_gerada)
            file_out_aes_encrypted_RSA = open('aes_key_rsa', 'wb')
            file_out_aes_encrypted_RSA.write(aes_encrypted_with_RSA)
            file_out_aes_encrypted_RSA.close()
            # Terminando aqui
            file_out_pub = open('%s' % nome_user + '.pu', 'wb') # para chave publica
            file_out_prv8 = open('%s' % nome_user + '.pr', 'wb') # para a chave privada
            print("Chave criada em ascii: {}".format(key_gerada))
            print("Chave criada em hex: {}".format(key_gerada.encode('hex')))
            print("Chave publica:\n%s" % (key_pub))
            aes_exec = pyaes.AESModeOfOperationCBC(key_gerada, iv = iv_gerado)
            ciphertext = aes_exec.encrypt(plaintext)
            # Escrever no arquivo o ciphertext
            file_in.write("{}".format(ciphertext))
            file_in_hex.write("{}".format(ciphertext.encode('hex')))
            file_out_pub.write(key_pub)
            file_out_prv8.write(key_prv8)
            file_out_pub.close()
            file_out_prv8.close()
            file_in.close()
            file_in_hex.close()

        elif escolha == 'N' or escolha == 'n':

            print("A chave TEM QUE TER 32 BYTES\n")
            print("!!! tenha certeza que ninguem esta olhando !!!").upper()
            key_user = str(raw_input("K: "))
            conferindo_chave = len(key_user)

            if conferindo_chave < 32:

                print("Coloque mais caracteres para fechar 32 bytes")
                aes_cbc_256()

            elif conferindo_chave > 32:

                print("Retire mais caracteres para fechar 32 bytes")
                aes_cbc_256()

            else:

                aes_exec = pyaes.AESModeOfOperationCBC(key_user, iv = iv)
                ciphertext = aes_exec.encrypt(plaintext)
                # file_in.write("{}\n".format(ciphertext.encode('hex')))
                file_in.write("{}".format(ciphertext))
                file_in_hex.write("{}".format(ciphertext.encode('hex')))
                file_in.close()
                file_in_hex.close()

        print("Ciphertext em ascii: {}".format(ciphertext))
        print("Ciphertext em hex: {}".format(ciphertext.encode('hex')))

    elif crypt_or_decrypt == 2:
        nome_arquivo = raw_input("Digite o nome do arquivo para abrir: ")

        if os.path.isfile(nome_arquivo + '.txt'):
            print("Existe")
            # Agora que ja sei que o arquivo existe, vamos ler o que tem dentro
            file_out = open(nome_arquivo + '.txt', 'r')
            conteudo = file_out.read()
            print(conteudo)

            try:
                key = raw_input("Digite a chave: ")
                key = key.decode('hex')
            except ValueError:
                print("Tamanho da chave nao e 32 bytes")
                aes_cbc_256()
            except TypeError:
                print("Chave tem que ser em hexadecimal\n")
                aes_cbc_256()

            try:
                iv = raw_input("Digite o IV: ")
                iv = iv.decode('hex')
            except ValueError:
                print("Tamanho do IV nao e 16 bytes")
                aes_cbc_256()
            except TypeError:
                print("IV tem que ser em hexadecimal\n")
                aes_cbc_256()

            aes_decrypt = pyaes.AESModeOfOperationCBC(key, iv = iv)
            x = aes_decrypt.decrypt(conteudo)

            plaintext = raw_input("Digite o nome do arquivo para salvar o X: ")
            plaintext_arquivo = open(plaintext + '.txt', 'w+')
            plaintext_arquivo.write("{}".format(x))
            plaintext_arquivo.close()
### AES CBC ###

# escolha do modo de operacao
clear()
hello()
print("Usando o algoritmo AES com dois modos: ECB e CBC. Por favor, escolha um:\n1 - Modo ECB\n2 - Modo CBC")
modo_operacao = int(raw_input("Entre com a sua escolha: "))

if modo_operacao == 1:
    aes_ecb()
elif modo_operacao == 2:
    aes_cbc()
else:
    print("Wat... Alguma coisa deu errado :<")
