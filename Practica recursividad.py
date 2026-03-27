# E: Numero entero
# S: Suma de impares


def suma_impar(num):
    if num == 0:
        return 0
    
    digito = num % 10
    if digito % 2 != 0:
        return digito + suma_impar(num // 10)
    else:
        return suma_impar(num // 10)
   
    
