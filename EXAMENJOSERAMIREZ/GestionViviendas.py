from CasasUni import casasUni
from Comunidad import comunidad
from Habitaciones import habitaciones
from Inquilino import inquilino
from Pisos import pisos

if __name__ == "__main__":
    
    comu = comunidad(
    nombre="Comunidad 1", direccion_ref="garcia quijano",presupuesto_anual=30000)



    piso1 = pisos(calle="rafael alberti",numero=12,ciudad="cadiz",superficie=80,precio_mensual=900,estado=True,planta=2,num_puerta="A",garaje=True,trastero=False)

    casa1 = casasUni(calle="jose ramirez",numero=5,ciudad="Sevilla",superficie=120,precio_mensual=1200,estado=True,patio=True,jardin=True,adosadas=False,aparcamiento=True)


    habitacion1 = habitaciones("Dormitorio", 12, True)
    habitacion2 = habitaciones("Salón", 20, True)


    inquilino1 = inquilino("jose", "12345678", "62738194")
    inquilino2 = inquilino("ramirez", "2340542", "722334235")



    print("estado inicial")
    print(comu, "\n")
    print(piso1, "\n")
    print(casa1, "\n")
    print(inquilino1, "\n")
    print(inquilino2, "\n")


    comu.agregar_vivienda(piso1)
    comu.agregar_vivienda(casa1)


    piso1.habitaciones.append(habitacion1)
    piso1.habitaciones.append(habitacion2)

    piso1.inquilino = inquilino1
    inquilino1.cambiar_vivienda(piso1)

    casa1.inquilino = inquilino2
    inquilino2.cambiar_vivienda(casa1)



    print("estado final")
    print(comu, "\n")
    print(piso1, "\n")
    print(casa1, "\n")
    print(inquilino1, "\n")
    print(inquilino2, "\n")
