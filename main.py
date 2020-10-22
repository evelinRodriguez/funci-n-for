'''
def funcionfor01(a):
  for x in range(a):
    print (x)
def funcionfor02(a,b):
  for x in range(a,b):
    print (x)    
#funcion para imprimir hasta 10
#funcionfor01(10)
#funcion imprimir hasta 15
#funcionfor02(5, 15)

#conteo de personas
personas = ["luisa" , "ana" , "maria" ]
for x in personas:
  print(x)
'''
#es un for(i=0 ; i<=a ; i++)(sum=i)
def funcionWhile(a):
  suma=0
  i=0
  while i <= a:
    suma= suma + i #equivalente a suma+=i
    i+= 1
    print(suma)

funcionWhile(10)