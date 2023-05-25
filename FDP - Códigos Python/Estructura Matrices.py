# Matriz (Array)
# Conjunto formado por columnas y filas

#Matriz unidimensional (6) - Vertical
for i in range(1,7):
    print (i)
    
print ('\n')
#Matriz unidimensional (6) - Horizontal 
for i in range(1,7):
    print(i, end = '  ')
    
print('\n')

#Matriz bidimensional (6 x 6)
#For Anidado
for i in range(1,7):
    for j in range(1,7):
        print (0, end ='   ')
    print('')
print('\n')
for i in range(1,7):
    for j in range(1,7):
        print (f'({i},{j})', end ='  ')
    print ('')
print('\n')
# Colocar 1 en la diagonal principal
for i in range(1,7):
    for j in range(1,7):
        if (i==j):
            print (1, end ='   ')
        else:
            print (0, end ='   ')
    print('')
