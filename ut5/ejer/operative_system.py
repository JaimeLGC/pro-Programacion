import random


class os:
    def __init__(
        self,
        name: str,
        graphic_interface: bool,
        packages: list,
        shell: str,
        version: str,
    ):

        self.name = name
        self.graphic_interface = graphic_interface
        self.ip = ""
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

    def stablish_ip(self):
        self.ip = f"{random.randint(100, 999)}.{random.randint(100, 999)}.{random.randint(10, 99)}.{random.randint(10, 99)}"
        print(f"Your new IP is {self.ip}")


os1 = os("os1", True, [], "bash", "1.0")
os1.stablish_ip()
