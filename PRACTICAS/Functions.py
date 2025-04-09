#def Num_pares (limit):
    #for num in range(0, limit+1, 2):
       # yield num

#for par in Num_pares (50):
   #print(par)

#def Num_impares (limit):
    #for numi in range(1, limit+1, 2):
        #yield numi

#for impar in Num_impares (20):
    #print(impar)

List_1 = [1,2,3,4,5,6,6]
List_2 = [5,6,7,8,9,10]

def inter_listas(a,b): 
    return list(set(a) & set(b))

print(inter_listas(List_1, List_2))