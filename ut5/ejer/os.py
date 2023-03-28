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
            self.booted

    def change_ip(self, ip: str):
        self.ip = ip
        print(f"Your new IP is {self.ip}")

    def install_package(self, *packages_to_be_installed: str):
        for package in packages_to_be_installed:
            if package not in self.packages:
                self.packages.append(package)
                print(f"{package} se ha instalado satisfactoriamente")
            else:
                print(f"{package} ya está en el sistema")


os1 = os("os1", True, [], "bash", "1.0")
os1.stablish_ip()
