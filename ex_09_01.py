#Escriba un programa que lea las palabras en words.txt y las almacene como claves en un diccionario.
#No importa cuáles sean los valores. Luego, puede usar el operador in como una forma rápida de verificar
#si una cadena está en el diccionario.
ofile = open("words.txt")
bag = dict()
count = 0
for line in ofile:
    words = line.split()
    for word in words:
        count += 1
        if word in bag:continue
        bag[word]= count
print(bag)
comp = input("Please write a word")
if comp in bag:
    print("true")
else:
    print("false")
