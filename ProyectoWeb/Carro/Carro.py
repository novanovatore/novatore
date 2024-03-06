
class Carro():
    """
    Carro de compras.
    
    Este carro de compras contiene los productos que el usuario
    quiere comprar. Contiene lo siguiente:
    - id del producto
    - nombre
    - cantidad
    - precio
    - imagen
    
    """
    def __init__(self, request):
        # almacenamos la peticion actual para poder usarla más adelante
        self.request = request
        # vamos a almacenar la session
        self.session = request.session

        # tenemos que construir un carro de compra para la sesión de
        # usuario
        # Cuando el usuario entra por primera vez, creamos un nuevo
        # carro
        # Si para el usuario ya se había creado un carro y volvió a
        # entrar en la página (misma session), utilizamos el carro 
        # que ya está.
        carro = self.session.get("carro")

        # si no existe el carro, lo creamos
        if not carro:
            # el carro es un diccionario en el que guardamos los 
            # productos
            # carro = {id_producto: {nombre, precio, imagen...},}
            self.carro = self.session["carro"] = {}
        else:
            # el usuario tenía productos en su carro, pero salió
            # de la página y ahora volvió
            self.carro = carro
    
    def agregar(self, producto):
        # El objetivo es agregar un producto a un carro de compras
        # si ya está el producto en el carro, para agregar nuevas
        # unidades el usuario debe pulsar sobre el producto y
        # automáticamente se agregará 1 unidad de ese producto
        # dentro del carro

        # debemos comprobar que el producto a agregar no esté en
        # el carro

        producto_en_carro = self.carro.get(str(producto.id), None)

        if producto_en_carro is None: # el producto no existe en carro
            
            self.carro[producto.id] = {
                "id_producto": producto.id,
                "nombre": producto.nombre,
                "precio": producto.precio,
                "cantidad": 1
            }
            if producto.imagen == "":
                self.carro[producto.id]["imagen"] = None
            else:
                self.carro[producto.id]["imagen"] = producto.imagen.url

        else:
            producto_en_carro["cantidad"] += 1
            producto_en_carro["precio"] += producto.precio
        
        # Todo lo que hayamos hecho debe guardarse en la session
        self.guardar_carro()
    

    def guardar_carro(self):
        self.session["carro"] = self.carro
        self.session.modified = True

    
    def eliminar(self, producto):
        if str(producto.id) in self.carro:
            del self.carro[str(producto.id)]
            self.guardar_carro()
    
    def restar_producto(self, producto):
        producto_en_carro = self.carro.get(str(producto.id), None)
        if producto_en_carro is not None:
            if producto_en_carro["cantidad"] > 1:
                producto_en_carro["cantidad"] -= 1
                producto_en_carro["precio"] -= producto.precio
            else:
                del self.carro[str(producto.id)]

            self.guardar_carro()
        
    
    def limpia_carro(self):
        self.carro = {}
        self.guardar_carro()


    def get_compra_str(self):
        compra = ""
        for key, value in self.carro.items():
            producto = f"Producto: {value['nombre']}\nCantidad: {value['cantidad']}\nPrecio: CLP${value['precio']}\n\n"
            compra += producto

        return compra            