# funciones
''''
def sumar():
    print('llamando a la funcion sumar')
    print('este codigo pertenece a la funcion')

sumar()

def multiplicar(num1,num2):
    return num1*num2


resultado = multiplicar(5,2)
print(resultado)
'''
'''
opcion = 0
contactos= []
while opcion!=5:
    print('=====BIENVENIDO AL SISTEMA=====')
    print('*****Menu principal*****')
    print('1.crear contacto')
    print('2.mostrar todos los contactos')
    print('3.actualizar un cotacto')
    print('4.eliminar un contacto')
    print('5.salir')
    print('-------------------')
    opcion = int(input())

    if opcion == 1:
        nombre = input('ingresa el nombre ')
        apellido = input('ingresa el apellido ')
        celular = input('ingresa el celular ')
        correo = input('ingresa el correo ')
        print('contacto creado con los datos: '+nombre+' '+apellido+' '+celular+' '+correo)

        contactos.append({
            'nombre': nombre,
            'apellido': apellido,
            'celular': celular,
            'correo': correo

            })
        input('pesione una telca para contiuar')
    elif opcion==2:
        for x in range(0,len(contactos)):
            print(contactos[x])
'''       
# contar ocurrencias de las letras de un texto #
# primera forma 
''''
texto = "esta lloviendo"

letrasUnicas=[]

for letra in texto:
    cont = 0
    for letraUnica in letrasUnicas:
        if letraUnica== letra:
            cont +=1

    if cont == 0:
        letrasUnicas.append(letra)

for letraUnica in letrasUnicas:
    print(letraUnica,texto.count(letraUnica))


# ocurrencias segunda forma

resultado = {}


for letra in texto:
    if resultado.get(letra):
      resultado[letra] += 1  
    else: resultado[letra] = 1
    
print(resultado)

'''
#----------------------------------

print('multiplicacion')
numero = input('ingresse la multiplicacion ')


