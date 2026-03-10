Algoritmo geometric_areas
	//declarar variables o constantes
	Definir pi_valvue Como Real
	Definir lado Como Real
	Definir baseRect, alturaRect Como Real
	Definir baseTri, alturaTri Como Real
	Definir radio Como Real
	Definir areaCuadrado, areaRectangulo, areaTriangulo, areaCirculo Como Real
	Definir totalAreas Como Real
	//Asignar o inicializar variables o constantes
	pi_valvue<-3.1416
	lado<-0
	baseRect<- 0
	alturaRect<-0
	baseTri<-0
	alturaTri<-0
	radio<-0
	//Inputs
	// Cuadrado
	Escribir "Ingrese el valor del lado del cuadrado:"
	Leer lado
	// Rectángulo
	Escribir "Ingrese la base del rectángulo:"
	Leer baseRect
	Escribir "Ingrese la altura del rectángulo:"
	Leer alturaRect
	// Triángulo
	Escribir "Ingrese la base del triángulo:"
	Leer baseTri
	Escribir "Ingrese la altura del triángulo:"
	Leer alturaTri
	// Círculo
	Escribir "Ingrese el radio del círculo:"
	Leer radio
	//Procesos
	
	// Cuadrado
	areaCuadrado<-lado * lado
	// Rectángulo
	areaRectangulo<-baseRect * alturaRect
	// Triángulo
	areaTriangulo<-(baseTri * alturaTri) / 2
	// Círculo
	areaCirculo<-PI * (radio * radio)
	
	// Total de áreas
	totalAreas<-areaCuadrado + areaRectangulo + areaTriangulo + areaCirculo
	
	// Outpust
	Escribir "Área del cuadrado: ", areaCuadrado
	Escribir "Área del rectángulo: ", areaRectangulo
	Escribir "Área del triángulo: ", areaTriangulo
	Escribir "Área del círculo: ", areaCirculo
	Escribir "Total de todas las áreas: ", totalAreas


FinAlgoritmo