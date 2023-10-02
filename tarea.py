class Estudiante:
    def __init__(self,nombre) :
        self.nombre=nombre
        self.calificaciones=[]
    def agregar_calificacion(self,calificacion):
        self.calificaciones.append(calificacion)
    def promedio_calificaciones(self):
        if len(self.calificaciones)==0:
            return 0
        suma_calificaciones=0
        for calificacion in self.calificaciones:
            suma_calificaciones=suma_calificaciones+calificacion
        return suma_calificaciones/len(self.calificaciones)
    def ha_aprobado(self):
        promedio=self.promedio_calificaciones()
        if promedio >= 5.0:
            print(self.nombre +" has aprobado con una nota igual a: "+str(promedio))
        else: 
            print(self.nombre +" has reprobado con "+str(promedio))


estudiante1= Estudiante("mario")
estudiante1.agregar_calificacion(5)
estudiante1.agregar_calificacion(3)
estudiante1.agregar_calificacion(2)
estudiante1.agregar_calificacion(10)
estudiante1.agregar_calificacion(9)
print(estudiante1.promedio_calificaciones())
estudiante1.ha_aprobado()
