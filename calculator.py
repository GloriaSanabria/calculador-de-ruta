mapa=[['o' for i in range (5)]for i in range (5)]
print(mapa)


# Solicitar al usuario que ingrese las coordenadas x e y separadas por un espacio
coordenadas_inicio = input("Ingresa las coordenadas de inicio: ")

# Dividir las coordenadas ingresadas en dos partes usando split()
inicio_x, inicio_y = map(int, coordenadas_inicio.split())

mapa[inicio_x][inicio_y]="i"


coordenadas_final = input("Ingrese las cordenadas finales: ")

final_x,final_y= map(int,coordenadas_final.split())





mapa[final_x][final_y]= "s"


for i in mapa:
    print(" ".join(i))

obstaculos=[]

