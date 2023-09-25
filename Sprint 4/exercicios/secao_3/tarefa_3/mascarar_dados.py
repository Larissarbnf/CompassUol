import hashlib

while True:
    texto= input("Digite uma string (ou pressione Enter para sair): ")
    
    if not texto:
        break
    
    hash_obj = hashlib.sha1(texto.encode())
    hex_dig = hash_obj.hexdigest()
    print(f'O hash SHA-1 da string é: {hex_dig}\n')
