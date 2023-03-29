# Diccionario que guarda los usuarios junto con sus contraseñas
users = {
    "Jaime": "J41m3",
}


class os:
    def __init__(
        self,
        name: str,
        graphic_interface: bool,
        packages: list,
        version: str,
        ip: str,
    ):

        self.name = name
        self.graphic_interface = graphic_interface
        self.ip = ip
        self.packages = packages
        self.kernel = True
        self.booted = False
        self.loged = False
        self.version = version

    @staticmethod
    def check_status(method):
        def wrapper(self, *args, **kwargs):
            if self.booted and self.loged:
                return method(self, *args, **kwargs)
            else:
                return None

        return wrapper

    def boot(self):
        if self.booted:
            not self.booted
        else:
            self.booted = True

    def login(self, username: str, password: str):
        if self.booted:
            if username in users:
                if password == users[username]:
                    self.loged = True
                    print(f"Bienvenido/a {username}")
                else:
                    print("Contraseña incorrecta, vuelva a intentarlo")
            else:
                print(f"{username} no existe, introduzca un usuario válido")

    @check_status
    def logout(self):
        self.loged = False

    @check_status
    def show_information(self):
        print(
            f"Nombre: {self.name}\nVersión: {self.version}\nIP: {self.ip}\nPaquetes instalados: {self.packages}\n"
        )

    @check_status
    def change_ip(self, ip: str):
        self.ip = ip
        print(f"Su nueva IP es: {self.ip}")

    @check_status
    def install_package(self, *packages_to_be_installed: str):
        for package in packages_to_be_installed:
            if package not in self.packages:
                self.packages.append(package)
                print(f"{package} se ha instalado satisfactoriamente")
            else:
                print(f"{package} ya está en el sistema")

    @check_status
    def uninstall_package(self, *packages_to_be_uninstalled: str):
        for package in packages_to_be_uninstalled:
            if package in self.packages:
                self.packages.remove(package)
                print(f"{package} se ha eliminado satisfactoriamente")
            else:
                print(f"{package} no existe en el sistema")

    @check_status
    def browse_package(self, desired_package: str):
        if self.booted:
            if desired_package in self.packages:
                print(f"{desired_package} se encuentra en el sistema")
            else:
                print("No se encuentran resultados")


os1 = os("os1", True, [], "bash", "1.0", "134.234.65.66")
os1.boot()
os1.login("Jaime", "J41m3")
os1.show_information()
