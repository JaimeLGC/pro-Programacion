class os:
    def __init__(
        self,
        name: str,
        graphic_interface: bool,
        packages: list,
        shell: str,
        version: str,
        ip: str,
    ):

        self.name = name
        self.graphic_interface = graphic_interface
        self.ip = ip
        self.packages = packages
        self.kernel = True
        self.booted = False
        self.shell = shell
        self.version = version

    def boot(self):
        if self.booted:
            not self.booted
        else:
            self.booted = True

    def show_information(self):
        if self.booted:
            print(
                f"Nombre: {self.name}\nVersión: {self.version}\nIP: {self.ip}\nShell: {self.shell}\nPaquetes instalados: {self.packages}\n"
            )

    def change_ip(self, ip: str):
        if self.booted:
            self.ip = ip
            print(f"Su nueva ip es: {self.ip}")

    def install_package(self, *packages_to_be_installed: str):
        if self.booted:
            for package in packages_to_be_installed:
                if package not in self.packages:
                    self.packages.append(package)
                    print(f"{package} se ha instalado satisfactoriamente")
                else:
                    print(f"{package} ya está en el sistema")

    def uninstall_package(self, *packages_to_be_uninstalled: str):
        if self.booted:
            for package in packages_to_be_uninstalled:
                if package in self.packages:
                    self.packages.remove(package)
                    print(f"{package} se ha eliminado satisfactoriamente")
                else:
                    print(f"{package} no existe en el sistema")

    def browse_package(self, desired_package: str):
        if self.booted:
            if desired_package in self.packages:
                print(f"{desired_package} se encuentra en el sistema")
            else:
                print("No se encuentran resultados")


os1 = os("os1", True, [], "bash", "1.0", "134.234.65.66")
os1.boot()
os1.show_information()
