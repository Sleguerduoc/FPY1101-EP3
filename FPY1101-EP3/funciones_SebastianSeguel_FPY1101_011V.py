

def RegistrarLibro(libros):
    try:
        titulo = input("Ingrese el título del libro: ").lower()
        autor = input("Ingrese el autor del libro: ").lower()
        publicacion =int ( input("Ingrese año de publicación del libro:"))
        sku1=""
        sku2= ""
        for i in range (6):
            sku1 += (titulo[i])
        for i in range (3):
            sku2 += (autor[i])
        sku = f"{sku1}-{sku2}-{publicacion}"
        print ("\nLibro registrado correctamente.\n")
        
        libros.append({"Título": titulo, 
                       "Autor": autor, 
                       "Año de Publicación": publicacion,
                       "Sku": sku
                       })
    except ValueError:
        print ("error en los datos ingresados. Intente nuevamente.")
    
    
    
def PrestarLibro(libros, librosPrestados):
    nombreUsuario = input("Ingrese su nombre de usuario ").lower()
    skui = input("Ingrese el SKU del libro que desea prestar: ").lower()
    for Libro in libros:
        if Libro["Sku"] == skui:
            fechaPrestamo = input("Ingrese la fecha de préstamo (dd/mm/yyyy): ")
            print ("\nLibro prestado correctamente.\n")
            
            librosPrestados.append({"nombre":nombreUsuario, 
                                    "titulo": Libro["Título"], 
                                    "fechaPrestamo": fechaPrestamo,
                                })
            libros.remove(Libro)
            
        else: 
            print ("El libro no se encuentra en la biblioteca o los datos ingresados no son validos")    

def listarLibros(libros):
    print ("\nListado de libros:\n")
    for Libro in libros:
        print ("TITULO \t\t AUTOR \t\t AÑO DE PUBLICACIÓN \t\t SKU \n")
        print (f"{Libro['Título']}\t\t {Libro['Autor']}\t\t {Libro['Año de Publicación']}\t\t\t\t {Libro['Sku']}")

def imprimirReporte(librosPrestados):
    reporteImprimir = librosPrestados
    nombreArchivo = "reportePrestamos.txt"
    with open(nombreArchivo, "w") as archivo:
        archivo.write("Reporte de préstamos:\n")
        archivo.write("USUARIO \t\t TITULO \t\t FECHA DE PRESTAMO\n")
        for libro in reporteImprimir:
            archivo.write (f"{libro['nombre']}\t\t {libro['titulo']}\t\t {libro['fechaPrestamo']}\n")
          