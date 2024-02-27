def impar_ou_par(numero): 
    resultado = numero % 2
    
    if resultado == 0 :
        return(f'O número {numero} é Par')
    else :
        return(f'O número {numero} é Ímpar')
    
print (impar_ou_par(2))
print (impar_ou_par(3))