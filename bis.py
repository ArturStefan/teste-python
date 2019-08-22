def anobissexto(ano):
    
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        resultado = 'É Bissexto'
    else:
        resultado = 'Não é Bissexto'
    return resultado
