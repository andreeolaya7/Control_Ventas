class Cliente:
    def __init__(self, id_cliente, nombre, apellido, telefono=""):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}, ID: {self.id_cliente}, Teléfono: {self.telefono}"