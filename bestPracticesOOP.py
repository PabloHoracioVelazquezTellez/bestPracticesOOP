class Alumno:
    def __init__(self): #funcion de tipo constructor
        # Atributos privados
        self.__nombre = None
        self.__apellido_paterno = None
        self.__apellido_materno = None
        self.__no_control = None
        self.__semestre = None

    # Métodos para establecer los valores (setters)
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_apellido_paterno(self, apellido_paterno):
        self.__apellido_paterno = apellido_paterno

    def set_apellido_materno(self, apellido_materno):
        self.__apellido_materno = apellido_materno

    def set_no_control(self, no_control):
        self.__no_control = no_control

    def set_semestre(self, semestre):
        self.__semestre = semestre

    # Métodos para obtener los valores (getters)
    def get_nombre(self):
        return self.__nombre

    def get_apellido_paterno(self):
        return self.__apellido_paterno

    def get_apellido_materno(self):
        return self.__apellido_materno

    def get_no_control(self):
        return self.__no_control

    def get_semestre(self):
        return self.__semestre

    def get_visualizarNombreCompleto(self): #Get para brindar el nombre completo la instancia alumno
        print("Nombre comleto:",self.__nombre,self.__apellido_paterno,self.__apellido_materno)

# Crear instancia de Alumno
alumno = Alumno()

#Diccionario para almacenar a los 50 alumnos
registro_Alumnos = {}

for i in range(3):#Capturar registros
    alumno = Alumno()
    alumno.set_nombre(input(f"Ingrese el nombre del alumno {i+1}: "))
    alumno.set_apellido_paterno (input(f"Ingrese el apellido paterno del alumno {i+1}: "))
    alumno.set_apellido_materno (input(f"Ingrese el apellido materno del alumno {i+1}: "))
    alumno.set_no_control (input(f"Ingrese el número de control del alumno {i+1}: "))
    alumno.set_semestre (int(input(f"Ingrese el semestre del alumno {i+1}: ")))
    registro_Alumnos[i] = alumno

for i in range(3): #Mostrar registros
    print(f"Alumno: {registro_Alumnos[i].get_nombre()}")

# Asignar valores usando los Setters
"""alumno.set_nombre('Pablo')
alumno.set_apellido_paterno('Velazquez')
alumno.set_apellido_materno('Tellez')
alumno.set_no_control("24200102")
alumno.set_semestre(3)"""

# # Obtener los valores
# print(alumno1.get_nombre())
# print(alumno1.get_apellido_paterno())
# print(alumno1.get_apellido_materno())
# print(alumno1.get_no_control())
# print(alumno1.get_semestre())
# alumno1.get_visualizarNombreCompleto()
#
# """" Cambiar el nombre del alumno
# alumno1.set_nombre("Carlos")
#
# # Verificar el cambio
# print(alumno1.get_nombre())
