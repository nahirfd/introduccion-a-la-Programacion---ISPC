""" EJERCICIO 3: Un hincha de fútbol desea conocer la cantidad de puntos que su
equipo lleva acumulados en el campeonato, para ello recibe cada semana la
información de la cantidad total de partidos, desde el inicio del campeonato, que
el equipo ha perdido, ha empatado y ha ganado. Por cada partido empatado
recibe un punto, por cada partido ganado tres puntos y por los perdidos cero
puntos.
 """
def calcular_puntos(ganados, empatados, perdidos):
    puntos = (ganados * 3) + (empatados * 1) + (perdidos * 0)
    return puntos


ganados = int(input("Ingrese la cantidad de partidos ganados: "))
empatados = int(input("Ingrese la cantidad de partidos empatados: "))
perdidos = int(input("Ingrese la cantidad de partidos perdidos: "))


puntos_acumulados = calcular_puntos(ganados, empatados, perdidos)
print(f"El equipo ha acumulado {puntos_acumulados} puntos en el campeonato.")
