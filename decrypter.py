import os
import pyaes

def decrypt_file(file_name, key, output_file_name):
    try:
        with open(file_name, "rb") as file:
            file_data = file.read()

        aes = pyaes.AESModeOfOperationCTR(key)
        decrypt_data = aes.decrypt(file_data)

        os.remove(file_name)

        with open(output_file_name, "wb") as new_file:
            new_file.write(decrypt_data)

        print(f"Arquivo {file_name} descriptografado com sucesso para {output_file_name}.")

    except Exception as e:
        print(f"Erro durante a descriptografia: {e}")

key = b"testeransomwares"
file_name = "teste.txt.ransom"
output_file_name = "teste.txt"

decrypt_file(file_name, key, output_file_name)
