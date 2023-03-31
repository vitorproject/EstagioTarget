def inverter_string(s):
    invertida = ''
    for i in range(len(s) - 1, -1, -1):
        invertida += s[i]
    return invertida

entrada = input("Digite uma string: ")
string_invertida = inverter_string(entrada)

print("String invertida:", string_invertida)
