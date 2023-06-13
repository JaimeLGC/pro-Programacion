from __future__ import annotations

import re
import sqlite3

DB_PATH = "ecommerce.db"

# ************************************************************
# Usuario
# ************************************************************


class User:
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    def __init__(self, username: str, name: str, surname: str, id: int = None):
        """Comprueba que el username siga el siguiente patrón (usando regex):
        - Empezar con una letra minúscula.
        - Terminar con un dígito.
        - Estar formado por letras, números y guiones bajos.
        - Tener un mínimo de 8 caracteres.
        Si no sigue este patrón, hay que elevar una excepción ValueError con el
        mensaje: User "<username>" does not follow security rules!

        A continuación guarda los atributos pasados por parámetro."""
        regex = r"^[a-z]\w+\d$"
        if not re.match(regex, username):
            raise ValueError(f'User "{username}" does not follow security rules!')

        self.username = username
        self.name = name
        self.surname = surname
        self.id = id

    def save(self):
        """Almacena el objeto actual en la base de datos y actualiza el
        identificador del objeto desde la base de datos."""
        sql = "INSERT INTO user(username, name, surname) VALUES(?, ?, ?)"
        self.cur.execute(sql, (self.username, self.name, self.surname))
        self.con.commit()
        self.id = self.cur.lastrowid

    def update(self):
        """Actualiza todos los campos del objeto en la base de datos usando
        el identificador como referencia.
        Si el objeto aún no se ha guardado en la base de datos, lanza una excepción de tipo
        ValueError con el mensaje: User "<username>" has not been yet saved into DB!"""
        if not isinstance(self.id, int):
            raise ValueError(f'User "{self.username}" has not been yet saved into DB!')
        sql = "UPDATE user SET username = ?, name = ?, surname = ? where id = ?"
        self.cur.execute(sql, (self.username, self.name, self.surname, self.id))
        self.con.commit()

    def __str__(self):
        """Representación en formato:
        <name> <surname>"""
        return f"{self.name} {self.surname}"

    @classmethod
    def from_id(cls, user_id: int) -> User:
        """Construye un objeto User a partir del identificador de usuario consultando
        la base de datos.
        Si el identificador de usuario no existe hay que lanzar una excepción de tipo
        ValueError con el mensaje: User with id <user_id> does not exist in DB!"""
        res = cls.cur.execute(f"SELECT * FROM user WHERE id = {user_id}")
        if not res.fetchone():
            raise ValueError(f"User with id {user_id} does not exist in DB!")
        sql = f"SELECT * FROM user WHERE id = {user_id}"
        row = cls.cur.execute(sql).fetchone()
        return User(row["username"], row["name"], row["surname"], row["id"])


# ************************************************************
# Producto
# ************************************************************


class Product:
    # Conexión (modo fila para la factoría) y cursor como atributos de clase
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    def __init__(self, name: str, stock: int, price: float, id: int = None):
        """Construye el objeto creando atributos a base de los parámetros."""
        self.name = name
        self.stock = stock
        self.price = price
        self.id = id

    def save(self):
        """Almacena el objeto actual en la base de datos y actualiza el
        identificador del objeto desde la base de datos."""
        sql = "INSERT INTO product(name, stock, price) VALUES(?, ?, ?)"
        self.cur.execute(sql, (self.name, self.stock, self.price))
        self.con.commit()
        self.id = self.cur.lastrowid

    def update(self):
        """Actualiza todos los campos del objeto en la base de datos usando
        el identificador como referencia.
        Si el objeto aún no se ha guardado en la base de datos, lanza una excepción de tipo
        ValueError con el mensaje: Product "<nombre-producto>" has not been yet saved into DB!
        """
        if not isinstance(self.id, int):
            raise ValueError(f'Product "{self.name}" has not been yet saved into DB!')
        sql = "UPDATE product SET name = ?, stock = ?, price = ? where id = ?"
        self.cur.execute(sql, (self.name, self.stock, self.price, self.id))
        self.con.commit()

    def sell(self, qty: int) -> None:
        """Si la cantidad a vender es mayor que el stock hay que lanzar una excepción de tipo
        ValueError con el mensaje: Not enough stock for product "<nombre-producto>"
        Si todo ha ido bien hay que actualizar el atributo de stock del objeto y actualizar
        la información del objeto en la base de datos."""
        if qty > self.stock:
            raise ValueError(f'Not enough stock for product "{self.name}"!')
        self.stock -= qty
        self.update()

    def restock(self, qty: int) -> None:
        """Actualiza el atributo stock del objeto según corresponda y actualiza la información
        del objeto en la base de datos.
        Haz uso de métodos ya implementados."""
        self.stock += qty
        self.update()

    def __str__(self):
        """El product se representa por su nombre."""
        return self.name

    def __eq__(self, other: Product | object):
        """Comprueba que dos productos son iguales únicamente a través de su nombre."""
        return self.name == other

    @classmethod
    def from_id(cls, product_id: int) -> Product:
        """Construye un objeto Product a partir del identificador de producto consultando
        la base de datos.
        Si el identificador de producto no existe hay que lanzar una excepción de tipo
        ValueError con el mensaje: Product with id <product_id> does not exist in DB!"""
        res = cls.cur.execute(f"SELECT * FROM product WHERE id = {product_id}")
        if not res.fetchone():
            raise ValueError(f"Product with id {product_id} does not exist in DB!")
        sql = f"SELECT * FROM product WHERE id = {product_id}"
        row = cls.cur.execute(sql).fetchone()
        return Product(row["name"], row["stock"], row["price"], row["id"])


# ************************************************************
# Carrito
# ************************************************************


class Cart:
    # Conexión (modo fila para la factoría) y cursor como atributos de clase
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    @classmethod
    def purchase(cls, user_id: int, product_id: int, qty: int) -> None:
        """El usuario compra qty unidades de producto.
        Esto implica que hay que actualizar el stock del producto así como añadir
        una nueva fila en la tabla "cart" con la operación.
        Aprovecha métodos ya definidos en las clases anteriores para algunas de las
        partes que debes implementar."""
        sql = "INSERT INTO cart(user_id, product_id, qty) VALUES(?, ?, ?)"
        cls.cur.execute(sql, (user_id, product_id, qty))
        cls.cur.execute(
            f"UPDATE product SET stock = stock - {qty} where id = {product_id}"
        )
        cls.con.commit()

    @classmethod
    def clean(cls, user_id: int) -> None:
        """Vaciar el carrito de la compra.
        Hay que actualizar el stock de los productos que había en el carrito
        así como eliminar los productos en sí mismos del carrito.
        Aprovecha métodos ya definidos en las clases anteriores para algunas de las
        partes que debes implementar."""
        product_id, qty = cls.cur.execute(
            f"SELECT product_id, qty FROM cart where user_id = {user_id}"
        ).fetchone()

        cls.cur.execute(f"UPDATE cart SET qty = 0 where user_id = {user_id}")
        cls.cur.execute(
            f"UPDATE product SET stock = stock + {qty} where id = {product_id}"
        )
        cls.con.commit()
