import numpy as np

# Definimos meses y departamentos
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
         "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

departamentos = ["Ropa", "Deportes", "Juguetería"]


ventas = np.zeros((12, len(departamentos)), dtype=int)



def crear_departamento():
    global ventas  
    departamento = input("Ingrese el nombre del departamento: ")

    if departamento in departamentos:
        print("Este departamento ya existe.")
        return

    departamentos.append(departamento)
    
    nueva_columna = np.zeros((12, 1), dtype=int)
    
    ventas = np.hstack((ventas, nueva_columna))

    print(f"Departamento '{departamento}' creado exitosamente.")


def insertar_venta(mes, departamento, cantidad):
    if mes in meses and departamento in departamentos:
        i = meses.index(mes)         
        j = departamentos.index(departamento) 
        ventas[i, j] = cantidad
        print(f"Venta agregada: {cantidad} en {departamento}, mes {mes}")
    else:
        print("Mes o departamento no válido")


def buscar_venta(mes, departamento):
    if mes in meses and departamento in departamentos:
        i = meses.index(mes)
        j = departamentos.index(departamento)
        return ventas[i, j]
    else:
        print("Mes o departamento no válido")
        return None


def eliminar_venta(mes, departamento):
    if mes in meses and departamento in departamentos:
        i = meses.index(mes)
        j = departamentos.index(departamento)
        ventas[i, j] = 0
        print(f"Venta eliminada en {departamento}, mes {mes}")
    else:
        print("Mes o departamento no válido")


insertar_venta("Enero", "Ropa", 5000)
insertar_venta("Febrero", "Deportes", 3000)
insertar_venta("Febrero", "Juguetería", 4500)

print("\nBuscar venta:")
print("Febrero, Juguetería →", buscar_venta("Febrero", "Juguetería"))

print("\nEliminando venta:")
eliminar_venta("Enero", "Ropa")

print("\nCreando un nuevo departamento:")
crear_departamento()  

print("\nEstado final de las ventas:")
print(ventas)
print("\nDepartamentos:", departamentos)
