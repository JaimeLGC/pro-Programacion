import re
import sqlite3

DB_PATH = "mail.db"

"""
Diagrama de clases:

        ┌──────────┐                  ┌──────────┐
        │          │                  │          │
     ┌──┤  DBUtils ├─────┐            │ MailError│
     │  │          │     │            │          │
     │  └──────────┘     │            └──────────┘
     │                   │
     │                   │
     │                   │
     ▼                   ▼
┌─────────┐      ┌─────────────┐
│         │      │             │
│ Mail    │      │ MailServer  │
│         │      │             │
└─────────┘      └─────────────┘
"""


class DbUtils:
    def __init__(self, db_path: str = DB_PATH):
        """Crea la conexión a la base de datos y el cursor correspondiente.
        También establece la factoría de registros como filas (diccionarios).
        Atributos a crear:
        - con
        - cur
        """
        self.con = sqlite3.connect(DB_PATH)
        self.con.row_factory = sqlite3.Row
        self.cur = self.con.cursor()


class Mail(DbUtils):
    def __init__(self, sender: str, recipient: str, subject: str, body: str):
        """Construye un objeto Mail con los mismos atributos que parámetros.
        Esta clase hereda de DbUtils..."""
        super().__init__()
        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        self.body = body

    def send(self) -> None:
        """Simula el envío de este correo guardando todos sus campos en la tabla activity"""
        send = """INSERT INTO activity(sender, recipient, subject, body) VALUES(?, ?, ?, ?)"""
        select = self.cur.execute(
            f"SELECT * FROM login WHERE username = '{self.sender}'"
        )
        domain = select.fetchone()["domain"]
        self.cur.execute(
            send, (f"{self.sender}@{domain}", self.recipient, self.subject, self.body)
        )
        self.con.commit()

    def __str__(self):
        """Representa un objeto de tipo Mail de la siguiente forma:
        From: <remitente>
        To: <destinatario>
        ---
        <asunto pasado a mayúsculas>
        <cuerpo del correo>
        """
        return f"From: {self.sender}\nTo: {self.recipient}\n---\n{self.subject.upper()}:\n{self.body}"


class MailServer(DbUtils):
    def __init__(self, username: str, password: str):
        """Construye un MailServer guardando los atributos de nombre de usuario y contraseña.
        También es necesario crear un atributo logged (booleano) que indique si se ha logeado.
        Esta clase hereda de DbUtils..."""
        self.username = username
        self.password = password
        self.logged = False

        self.con = sqlite3.connect(DB_PATH)
        self.con.row_factory = sqlite3.Row
        self.cur = self.con.cursor()

    def login(self) -> None:
        """Realiza/comprueba el login del usuario actualizado los atributos:
        - domain
        - logged
        La comprobación hay que hacerla consultando la base de datos.
        """
        # check = self.cur.execute(
        #     f"SELECT * FROM login WHERE username = {self.username}"
        # )
        # self.domain = check.fetchone()["domain"]

    @staticmethod
    def login_required(method):
        """Decorador que lanza una excepción MailError si el usuario no está logeado.
        El mensaje de la excepción debe ser:
        User "<username>" not logged in!

        Ojo! La excepción recibe en su constructor tanto el mensaje de error
        como el objeto actual de tipo MailServer."""

        def wrapper(*args, **kwargs):
            return method(*args, **kwargs)

        return wrapper

    @property
    def sender(self) -> str:
        """Formato: <nombre-de-usuario>@<dominio>

        No hay que aplicar decorador pero debes saber que esta propiedad
        sólo va a funcionar si se ha hecho login previamente, ya que en otro caso
        no disponemos del dominio."""
        domain = self.cur.execute(
            f"SELECT * FROM login WHERE username = '{self.username}'"
        )
        res = domain.fetchone()["domain"]
        return f"{self.username}@{res}"

    @login_required
    def send_mail(self, *, recipient: str, subject: str, body: str) -> None:
        """Realiza el "envío" de un correo a través del método definido en Mail.
        Si recipient no tiene un formato válido de email se debe lanzar una excepción
        de tipo MailError con el mensaje:
        Recipient "<recipient>" has invalid mail format!

        Ojo! La excepción recibe en el constructor tanto el mensaje
        como el objeto actual de tipo MailServer."""
        regex = r"^[a-z]+@[a-z]+.[a-z]+$"
        if not re.match(regex, recipient):
            raise MailError(f"Recipient '{recipient}' has invalid mail format!")
        mail = Mail(self.username, recipient, subject, body)
        mail.send()

    @login_required
    def get_emails(self, sent: bool = True):
        """Consulta los mails almacenados hasta el momento.
        - Si el parámetro sent está a True se devuelven los enviados por el usuario.
        - Si el parámetro sent está a False se devuelven los recibidos por el usuario.
        Debe ser una función generadora que devuelva objetos de tipo Mail."""
        if sent:
            res = "SELECT * FROM activity WHERE sender = ?"
        else:
            res = "SELECT * FROM activity WHERE recipient = ?"
        query = self.cur.execute(res, (self.username)).fetchall()
        for row in query:
            yield Mail(row["sender"], row["recipient"], row["subject"], row["body"])


class MailError(Exception):
    def __init__(self, message: str, mail_handler: Mail | MailServer):
        mail_handler.con.close()
        return message
