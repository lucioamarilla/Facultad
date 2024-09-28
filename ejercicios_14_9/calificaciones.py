fileName = "calificaciones.csv"
fileAverage = "promedio.csv"
calificaciones = open(fileName , "r")
promedios = open(fileAverage, "w")
for numero, linea in enumerate(calificaciones):
    if numero != 0: # El cero es la primera linea
        lineaNotas = linea.split(";")
        if "\n" in lineaNotas[4]:
            lineaNotas[4] = lineaNotas[4].replace("\n", "")
        for notas in lineaNotas[2:5]:
            if "," in notas:
                lineaNotas[lineaNotas.index(notas)] = notas.replace(",",".")
        promedio = (float(lineaNotas[2]) + float(lineaNotas[3]) + float(lineaNotas[4])) / 3
        promedios.write(lineaNotas[0]+";"+lineaNotas[1]+";"+str(promedio)+"\n")
promedios.close()
calificaciones.close()