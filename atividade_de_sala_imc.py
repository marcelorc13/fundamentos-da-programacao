def calcular_imc (altura, peso):
    resultado = peso/(altura * 2)
    
    if resultado < 18.5:
        return('Abaixo do Peso')
    elif resultado < 25:
        return('Peso Ideal')
    elif resultado < 30:
        return('Levemente acima do peso')
    elif resultado < 35:
        return('Obesidade Grau I')
    elif resultado < 40:
        return('Obesidade Grau II')
    else :
        return('Obesidade III (Mórbida)')
            

res = calcular_imc(1.8, 50)

print(res)