#7.2 Escriba un programa que solicite un nombre de archivo, luego abra ese archivo y lea el archivo,
#buscando líneas del formulario:Confianza en X-DSPAM: 0,8475 Cuente estas líneas y extraiga los valores
#de punto flotante de cada una de las líneas y calcule el promedio de esos valores y genere un resultado como
#se muestra a continuación. No use la función sum () o una variable llamada sum en su solución.
name = input("Please write the name of the file: ")
ofile = open(name)
count = 0
tot = 0
for line in ofile:
    if line.startswith("X-DSPAM-Confidence:"):
        line = line[19:]
        line = float(line)
        tot = tot+line
        count = count+1
media = tot/count
print("Average spam confidence:",media)
