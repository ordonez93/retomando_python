texto = input('ingrese un verbo en infinitivo-->> ')
texto = texto.lower()

verbo=(texto[len(texto)-2]+texto[len(texto)-1])

if verbo == 'ar':
    print('yo '+texto.replace(texto[len(texto)-2]+texto[len(texto)-1],'o'))
    print('tu '+texto.replace(texto[len(texto)-2]+texto[len(texto)-1],'as'))
    print('el '+texto.replace(texto[len(texto)-2]+texto[len(texto)-1],'a'))
    print('nosotros '+texto.replace(texto[len(texto)-2]+texto[len(texto)-1],'amos'))
    print('vosotros '+texto.replace(texto[len(texto)-2]+texto[len(texto)-1],'ais'))
    print('ellos '+texto.replace(texto[len(texto)-2]+texto[len(texto)-1],'an'))
    
elif verbo == 'er':
    print('yo '+texto.replace(texto[len(texto)-2]+texto[len(texto)-1],'o'))
    print('tu '+texto.replace(texto[len(texto)-2]+texto[len(texto)-1],'es'))
    print('el '+texto.replace(texto[len(texto)-2]+texto[len(texto)-1],'e'))
    print('nosotros '+texto.replace(texto[len(texto)-2]+texto[len(texto)-1],'emos'))
    print('vosotros '+texto.replace(texto[len(texto)-2]+texto[len(texto)-1],'eis'))
    print('ellos '+texto.replace(texto[len(texto)-2]+texto[len(texto)-1],'en'))

elif verbo == 'ir':
    print('yo '+texto.replace(texto[len(texto)-2]+texto[len(texto)-1],'o'))
    print('tu '+texto.replace(texto[len(texto)-2]+texto[len(texto)-1],'es'))
    print('el '+texto.replace(texto[len(texto)-2]+texto[len(texto)-1],'e'))
    print('nosotros '+texto.replace(texto[len(texto)-2]+texto[len(texto)-1],'imos'))
    print('vosotros '+texto.replace(texto[len(texto)-2]+texto[len(texto)-1],'eis'))
    print('ellos '+texto.replace(texto[len(texto)-2]+texto[len(texto)-1],'en'))

else : 
    print('el texto no es un verbo o no esta en infinitivo' )