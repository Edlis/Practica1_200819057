import ManejoArchivos
import random


clase = ManejoArchivos.ManejoArchivos 
			
print('Escriba la cadena') # pido la cadena :)

cadena = input() # jalo la cadena espero que no tenga error :O
listaTetas = []
sumatoria = 0
n = 0
m = 0


def suma():
	operacion = 0
	i = 0
	while i < m:
		for j in range(n):
			# aqui tiene que ir las x's por las tetas la suma una por una
			operacion = operacion + listaTetas[j]*clase.matrizX[i][j]
			#print(operacion)
		operacion = operacion - clase.listaY[i]# aqui restamos a y 
		operacion = operacion*operacion # aqui elevamos al cuadrado 
		#print(operacion) # y en teoria ya esta entonces estos tengo que sumarlos todos para dividirlo por 1/2m
		operacion = (1/(2*m)) * operacion
		i = i+1
	#print(operacion)
	clase.operacionA = clase.operacion
	clase.operacion = operacion
	
def gradiente(a):
	#hacemos lo del gradiente y le voy poniendo nuevos valores a las tetas
	for j in range(n):
		listaTetas[j] = listaTetas[j]-a*clase.operacion
		
			
			
		
	
	
	
		
	
if cadena == "hola":
	print('si es hola')
	#leerArchivo()
else:
	#print(cadena)
	lista = cadena.split(" ")
	if len(lista) == 5:
		variablesX = lista[0]
		#clase.leerAchivoX(variablesX) lo quito temporalmente xq me conviene mas encontrar la longitud de Y
		variablesY = lista[1]
		clase.leerArchivoY(variablesY)
		clase.leerAchivoX(variablesX)
		#print(clase.filasX)
		alfa = float(lista[2])
		iteraciones = float(lista[3])
		tolerancia = float(lista[4])
		#empezar a operar pss :S
		#print(random.uniform(0,10)) # asi se sacan los random float!
		#Entonces hare una mi lista de randoms para utilizar los tetas, esta lista se ira reemplazando por cada nuevo teta
		n = clase.cantidadX # le cambio a las variables solo para tener mejor manejo yo.
		m = clase.filasX
		i = 0
		while i<= n: # o delimito por una teta por cada X		
			listaTetas.append(random.uniform(0,1))
			i = i + 1
		
		#jalamos la sumatoria
		
		#jalamos lo del gradiente y lo miramos por las iteraciones 		
		
		archivo=open('Archivo.csv','a')
		archivo.write('iteracion, costo \n')
		w = 0
		while w < iteraciones:
			suma()
			gradiente(alfa)
			if tolerancia >= (clase.operacion - clase.operacionA): # la tolerancia se compara con la de costo del valor anterior
				break
			else:
				#sino lo escribimos en el archivo				
				archivo.write(str(w)+','+str(clase.operacion)+'\n')							
			w=w+1
		archivo.close()
		#imprimmos las tetas finales
		print('Y los tetas mejor son: ')
		for z in range(n):
			print('Teta'+str(z)+' = '+str(listaTetas[z]))
			
		
		#i = 0
		#while i <= iteraciones:
			
			 
		#print(variablesX + ' ' + variablesY+' '+alfa+' '+ iteraciones+' '+tolerancia+' ')
	else:
		print('No es correcta la cadena de entrada, ingrese la cadena correcta')
		#print(lista)
		


