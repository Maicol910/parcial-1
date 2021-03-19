parrafo = """este es un texto el cual deben contar el numero
de palabras que tiene, deben tener en cuenta,
que algunas palabras se separa por un punto, y una
coma, tambien hay que tener en cuenta, que las palabras
escritas EN MAYUSCULAS mayusculas y minusculas cuenta como una este. Texto """
#caracteres que no son palabras
eliminar = ";:.\n,!\"'"
for caracter in eliminar:
    #remplazar bacio 
    parrafo = parrafo.replace(caracter,
                          "")
parrafo = parrafo.lower()
palabras = parrafo.split(" ")
conteo = {}
for palabra in palabras:
    if palabra in conteo:
        conteo[palabra] += 1
    else:
        conteo[palabra] = 1
for palabra in conteo:
    repeticion = conteo[palabra]
    print(f"palabra --> (( {palabra} )) se repite ---> {repeticion}")
