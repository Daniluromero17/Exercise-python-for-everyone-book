#Abra el archivo romeo.txt y léalo línea por línea. Para cada línea, divida la línea en una lista de palabras usando el método
#split (). El programa debe crear una lista de palabras. Para cada palabra en cada línea, verifique si la palabra ya está en
#la lista y si no, añádala a la lista. Cuando el programa se complete, clasifique e imprima las palabras resultantes en orden
#alfabético.
name = input("Please write the name of the file: ")
ofile = open(name)
strilist = list()
for line in ofile:
    words = line.split()
    #print(strilist)
    for word in words:
        if word in strilist:continue
        strilist.append(word)
    strilist.sort()
print(strilist)
