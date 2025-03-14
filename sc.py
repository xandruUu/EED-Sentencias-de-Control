#Bifurcación

a=50
if a%2 == 0:
    print(f"El valor {a} es un número par")
else:
    print(f"El valor {a} es n número impar")

if a>50 :
    print(f"El valor {a} es mayor de 50")
elif a<50:
    print(f"El valor {a} es menor de 50")
else:
    print(f"El valor {a} es 50")    

num= input("Introduce un valor...")    
print("Valor introducido", num)  #input siempre devuelve una cadena de caracteres

num=int(num)

a=0
while a<num:
    print("a:", a)
    a+=1

#bucle que solicite numeros al usuario hasta que se introdusca un número par
num= int (input("Introduzca un valor..."))
while num % 2 !=0:
    num= int (input("Introduzca un valor..."))
print("Número de fin:", num)    
exit(0)

#while not numEsPar:

#bucle que solicite numeros al usuario hasta que se introduzcan dos numeros pares consecutivos

"""int= num1(int)
int= num2(int)

numPar = False

while not numPar:
    num1= input("Introduce un valor para num1.")
    num2= input("Introduce un valor para num1.")

    if(num1%2== 0 and num2%2==0):
        print("los dos son pares")
        numPar=True
    else:
        print("Ambos no son pares")
            
"""

