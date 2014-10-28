


class ManejoArchivos:
	filasX = 0
	matrizX = []
	cantidadX = 0
	listaY = []
	operacion = 0
	operacionA = 0
	#def __init__():
		#archivoXG = ""
		#filasX = 0
	
	def leerAchivoX(archivo):
		contador = 0
		ManejoArchivos.matrizX = [] # esta sera mi matriz, pero python no se digna a trabajar asi solo con una libreria numpy o con listas asi que hare listas.
		# en este archivo tengo que ver cuantas X me quiere mandar entonces....
		try:
			archivoX=open(archivo,'r')
			linea=archivoX.readline()
			linea = linea.replace("\n", "")
			listaTX = linea.split(",") 
			ManejoArchivos.cantidadX = len(listaTX) # aqui obtengo mi cantidad de Xs de columnas para mi matriz
			# aqui defino mi matriz ya se que no es efectivo pero repetire la lectura nuevamente para q me almacene los valores en ella!
			for i in range(ManejoArchivos.filasX):
				ManejoArchivos.matrizX.append([])
				for j in range(ManejoArchivos.cantidadX):
					ManejoArchivos.matrizX[i].append(None)
					
		# entonces tendria q agarrar mi matriz y empezar a insertar.
		# de primero la fila que tengo afuera
			i = 0;
			for x in listaTX:								
				ManejoArchivos.matrizX[0][i] = float(x)
				i = i + 1
				
		
			while linea!="":
				contador = contador + 1
				#print(linea)
				linea=archivoX.readline()
				linea = linea.replace("\n", "")
				listaTX = linea.split(",")
				# y aqui ya el que llena toda la matriz
				i = 0;
				if contador < ManejoArchivos.filasX:
					for x in listaTX:								
						ManejoArchivos.matrizX[contador][i] = float(x)
						i = i + 1
			archivoX.close()
		except:
			print('ese archivo no existe! meta uno que si sirva! gracias '+ archivo)			
		#print(ManejoArchivos.cantidadX)
		#print(contador)
		#print('la matriz')
		#print(ManejoArchivos.matrizX)
		
		
	def leerArchivoY(archivo1):
		# en este archivo solo viene una variable que es x, por lo que es suficiente utilizar una lista
		# y que se utilice 
		print('leerY')
		#archivoXG = archivoX
		archivoY=open(archivo1,'r')
		lineaY=archivoY.readline() 		
		while lineaY!="":			
			#print(lineaY)
			lineaY = lineaY.replace("\n", "")
			ManejoArchivos.listaY.append(float(lineaY))
			lineaY=archivoY.readline()			
		archivoY.close()
		ManejoArchivos.filasX = len(ManejoArchivos.listaY) # y aqui sacamos la cantidad de X's que esperamos para llenar nuestra matriz.	
		#print(listaY)
