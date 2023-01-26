
#jose Alberto
#20-0441
#PRT04 - Factura de productos

import random

class Factura:
    def __init__(self):
        self.nombre_cliente = ""
        self.productos = []
        self.numero_factura = ""

    def capturar_datos(self):
        self.nombre_cliente = input("Ingrese el nombre del cliente: ")
        cantidad_productos = int(input("Ingrese la cantidad de productos a capturar: "))
        for i in range(cantidad_productos):
            nombre_producto = input("Ingrese el nombre del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            cantidad = int(input("Ingrese la cantidad de productos: "))
            self.productos.append({"nombre": nombre_producto, "precio": precio, "cantidad": cantidad})

    def generar_factura(self):
        importe = 0
        total_articulos = 0
        for producto in self.productos:
            importe += producto["precio"] * producto["cantidad"]
            total_articulos += producto["cantidad"]
        total_pagar = importe * 1.16
        self.numero_factura = str(random.randint(1000000, 9999999))
        print("Factura #" + self.numero_factura)
        print("Cliente: " + self.nombre_cliente)
        print("Productos:")
        for producto in self.productos:
            print("- " + producto["nombre"] + " x " + str(producto["cantidad"]) + " @ " + str(producto["precio"]))
        print("Importe: $" + str(importe))
        print("Total de artículos: " + str(total_articulos))
        print("Total a pagar: $" + str(total_pagar))

factura = Factura()
factura.capturar_datos()
factura.generar_factura()
