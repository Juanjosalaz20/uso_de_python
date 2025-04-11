# List_1 = [1,2,3,4,5,6,6]
# List_2 = [5,6,7,8,9,10]

# def inter_listas(a,b): 
#     return list(set(a) & set(b))

# print(inter_listas(List_1, List_2))

clave=1234
intentosF=0

for intentos in range(1,4):
    pin = int(input("ingrese clave: "))
    if pin == clave:
        print("ingreso exitoso")
        break
    else:
        print("clave erronea")
        intentosF+=1
        print("intento fallido",intentosF)