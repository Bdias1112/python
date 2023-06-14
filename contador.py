frase = 'Senai Armando de Arruda Pereira'
caractere = 'a'
contador = 0
for letra in frase:
    if letra == caractere:
        contador +=1
print(f'Há {contador} letras {caractere} na frase')