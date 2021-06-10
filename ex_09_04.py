#Escriba un programa para leer mbox-short.txt y averiguar quién ha enviado la mayor cantidad de mensajes de correo.
#El programa busca las líneas "De" y toma la segunda palabra de esas líneas como la persona que envió el correo.
#El programa crea un diccionario Python que asigna la dirección de correo del remitente a un recuento de la cantidad de veces
#que aparecen en el archivo. Una vez producido el diccionario, el programa lee el diccionario utilizando un bucle máximo para
#encontrar el autor más prolífico.
ofile = open("mbox-short.txt")
mails = list()
bag = dict()
for line in ofile:
    if line.startswith("From "):
        line = line.split()
        mails.append(line[1])
for line in mails:
    bag[line] = bag.get(line, 0) + 1
max = None
name = None
for k,v in bag.items():
    if max is None or v>max:
        max = v
        name = k
print(bag)
print(name, max)
