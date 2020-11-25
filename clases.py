import csv
class Participante:
    def __init__(self, idParticipante, nombre, apellido, edad, sexo):
        self.idParticipante = id
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.sexo = sexo
    def __str__(self):
        return 'ID:{}: la persona es de nombre {}, apellido {}, tiene {} años y es de sexo {}.'.format(self.id, self.nombre, self.apellido, self.edad, self.sexo)
    

class Disparo(Participante):
    def __init__(self, idParticipante, nombre, apellido, edad, sexo, x1, y1, x2, y2, x3, y3):
        Participante.__init__(self, idParticipante, apellido, nombre, edad, sexo)
        self.disparo1=float((x1**2+y1**2)**.5)
        self.disparo2=float((x2**2+y2**2)**.5)
        self.disparo3=float((x3**2+y3**2)**.5)
        self.mejorDisparo=sorted([self.disparo1, self.disparo2, self.disparo3])[0]
        self.promedioDisparo=((self.disparo1+self.disparo2+self.disparo3)/3)
    def __str__(self):
        return ('{}, {}, {}, {}, {}, {:3f}, {:3f}, {:3f}, {:3f}, {:3f}'.format(self.idParticipante, self.nombre, self.apellido, self.edad, self.sexo, self.disparo3, self.disparo2, self.disparo3, self.mejorDisparo, self.promedioDisparo))

class Concurso:
    participantes=[]

    def agregarParticipante(self, disparo):
        self.participantes.append(disparo)

    def mostrarParticipantes(self):
        print('\n\nId Part., Nombre, Apellido, Edad, Sexo, Disparo.1, Disparo.2, Disparo.3, MejorDisparo, PromedioDisparo\n')
        for p in self.participantes:
            print(p)
    
    def ordenar(self):
        for i in range(len(self.participantes)-1):
            for j in range(len(self.participantes)-1-i):
                if self.participantes[i].promedioDisparo>self.participantes[i+j+1].promedioDisparo:
                    self.participantes[i],self.participantes[i+j+1]=self.participantes[i+j+1],self.participantes[i]
    
    def mostrarPodio(self):
        print('\n\nLos mejores participantes son: ')
        print('\nId Part., Nombre, Apellido, Edad, Sexo, Dist.1, Dist.2, Dist.3, MejorDisparo, PromedioDisparo\n')
        self.ordenar()
        for p in range(3):
            print(self.participantes[p])

    def mostrarCantidadParticipantes(self):
        print('\n\nFueron: {}\n el total de los participantes'.format(len(self.participantes)))
        pass

    def mostrarUltimo(self):
        self.ordenar()
        print('\n\nEl último participante fue: \n')
        print('Id Part., Nombre, Apellido, Edad, Sexo, Disparo.1, Disparo.2, Disparo.3, MejorDisparo, PromedioDisparo\n')
        print(self.participantes[-1])
        pass

    def listarporedad(self):
        print('\n\nParticipantes ordenados por edad:')
        for i in range(len(self.participantes)-1):
            for j in range(len(self.participantes)-1-i):
                if self.participantes[i].edad>self.participantes[i+j+1].edad:
                    self.participantes[i],self.participantes[i+j+1]=self.participantes[i+j+1],self.participantes[i]
        self.mostrarUltimo()

    def promedio(self):
        suma=0
        for i in self.participantes:
            suma=suma+i.promdisp
            prom=suma/(len(self.participantes))
        print('\n\nEl promedio de los participantes fue: {:3f}\n'.format(prom))
        pass

    def guardar(self):
        with open('Concurso.csv', 'a+', newline='') as archivo:
            archconcurso=csv.writer(archivo)
            archconcurso.writerow(['Id Part.', 'Nombre', 'Apellido', 'Edad', 'Sexo', 'Disparo.1', 'Disparo.2', 'Disparo.3', 'MejorDisparo', 'PromedioDisparo'])
            for elem in self.participantes:                
                registro=[elem.id, elem.nom, elem.ape, elem.edad, elem.sexo, elem.dist1, elem.dist2, elem.dist3, sorted([elem.dist1, elem.dist2, elem.dist3])[0], ((elem.dist1+elem.dist2+elem.dist3)/3)]
                archconcurso.writerow(registro)