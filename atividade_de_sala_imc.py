def calcular_imc (altura, peso):
    resultado = peso/(altura * 2)
    
    if resultado < 18.5:
        return(f'Seu IMC é {resultado} Abaixo do Peso')
    elif resultado < 25:
        return(f'Seu IMC é {resultado} Peso Ideal')
    elif resultado < 30:
        return(f'Seu IMC é {resultado} Levemente acima do peso')
    elif resultado < 35:
        return(f'Seu IMC é {resultado} Obesidade Grau I')
    elif resultado < 40:
        return(f'Seu IMC é {resultado} Obesidade Grau II')
    else :
        return(f'Seu IMC é {resultado} Obesidade III (Mórbida)')
            

print(calcular_imc(1.8, 50))