class Producto:
    def __init__(self, codigo, nombre, precio, stock=0):
        if precio < 0 or stock < 0:
            raise ValueError("El precio y el stock no pueden ser negativos.")
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def hay_stock(self, cantidad):
        return self.stock >= cantidad

    def descontar_stock(self, cantidad):
        if not self.hay_stock(cantidad):
            raise ValueError(f"Estock insuficiente para el producto {self.nombre}.")
        self.stock -= cantidad

    def reponer_stock(self, cantidad):
        if cantidad <=0:
            raise ValueError("La cantidad debe de ser mayor a 0.")
        self.stock += cantidad

    def __str__(self):
        return f"{self.codigo} | {self.nombre} | Precio: S/. {self.precio:.2f} | Stock: {self.stock}"

