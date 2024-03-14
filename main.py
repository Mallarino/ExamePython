bandas=[]


opcion=100
while(opcion != 5):
    print('***********FESTIVAL ALTAVOZ**************')
    print('1. Registrar banda')
    print('2. Ver el cartel del festival')
    print('3. Buscar banda')
    print('4. Modificar banda')
    print('5. Finalizar')
    opcion=int(input('digita una opcion'))

    if opcion == 1:
        banda={}
        banda["id"]=int(input("ID: "))
        banda["nombre"]=input("Nombre: ")
        banda["genero"]=input("Genero: ")
        banda["costo"]=int(input("Costo: "))

        bandas.append(banda)
        

    elif opcion == 2:
        for banda in bandas:
            print(f'{banda["id"]}--{banda["nombre"]}')
        
    elif opcion == 3:
        userInput = input('Filtra por nombre: ')
        for banda in bandas:
            if userInput == banda["nombre"]:
                print('encontrada')
            
        
        
    elif opcion == 4:
        pass
    elif opcion == 5:
        pass
    else:
        print('opcion invalida !')