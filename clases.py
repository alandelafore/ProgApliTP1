class Participante:
    def __init__(self, nombre, apellido, edad, sexo):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.sexo = sexo
    def __str__(self):
        return 'la persona es de nombre {self.nombre}, apellido {self.apellido}, tiene {self.edad} años y es de sexo {}.'.format(self = self)
    

class Disparo(Participante):
    def__init(Self, nombre, apellido, edad, sexo, disparo)
        super().__init__(nombre, apellido, edad, sexo)
        self.disparo = disparo

class Concurso:
    def __init__():
