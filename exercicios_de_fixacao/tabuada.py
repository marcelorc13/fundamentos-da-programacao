def tabuada(numero) :
    multiplicador = 1
    while multiplicador <= 10 :
        resultado = numero * multiplicador
        print(f'{numero} x {multiplicador} = {resultado}')
        
        multiplicador += 1
        
tabuada(2)