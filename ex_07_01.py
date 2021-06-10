#Escriba un programa que solicite un nombre de archivo, luego abra ese archivo y lea el archivo e imprima el contenido
#del archivo en mayúsculas. Utilice el archivo words.txt para producir el resultado a continuación.
name = input("Please write the name of the file: ")
ofile = open(name)
rname = ofile.read()
rname = rname.upper()
print(rname)
