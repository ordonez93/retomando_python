operacion = input('ingrese la multitiplicacion -->>  ')
datos = operacion.split('*')

valores =[]

for valor in datos:
    valores.append(int(valor))
        
def multiplicar (valor_sumado,cantidad_veces):
    if cantidad_veces < 0:
        return -multiplicar(valor_sumado,-cantidad_veces)
    elif cantidad_veces==0:
        return 0
    elif cantidad_veces==1:
        return valor_sumado
    else:
        return valor_sumado + multiplicar(valor_sumado,cantidad_veces-1)

print(valores)

producto=[]
posicion=0
for resultado_suma  in valores:
    resultado_suma = multiplicar(valores[posicion],valores[posicion])
    producto.append(int(resultado_suma))
    posicion += 1


print(producto)