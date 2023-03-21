""" f = open('alumnos.txt','r')
nombres = f.read()
print(nombres)
f.seek(0) # podemos controlar apartir de donde lea el archivo
nombres2 = f.read()
print(nombres2)
f.close()
 """
 
""" f = open('alumnos.txt','r')
#nombres = f.readline() #Just read one
nombres = f.readlines()
for item in nombres:
    print(item, end='')
    
f.close() """

#f = open('alumnos.txt', 'w') #if not exist create one
f = open('alumnos.txt', 'a') #if not create but if exist append
f.write('\n' + '!!!Hola mundo¡¡¡')
f.close()
 