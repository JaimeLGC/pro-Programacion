power_drainage = {"Samsung": 0.85, "Xiaomi": 1.00, "Nokia": 1.10, "Alcatel": 1.25}


class MobilePhone:
    def __init__(
        self, manufacturer: str, screen_size: float, num_cores: int, power: float
    ):
        self.manufacturer = manufacturer
        self.screen_size = screen_size
        self.num_cores = num_cores
        self.apps = []
        self.status = False
        self.power = power

    def switch(self):
        if self.status:
            not self.status
        elif not self.status:
            self.status = True
            self.drain_power(20)

    def warn_power(self):
        if self.status:
            if self.power <= self.power * 0.20 and self.power > self.power * 0.10:
                print("Aviso, batería baja")
            elif self.power <= self.power * 0.10 and self.power > 0:
                print("Aviso, batería MUY baja")
            elif self.power == 0:
                print("Apagando...")
                self.switch()

    def drain_power(self, power_spent):
        self.power = -power_spent * power_drainage[self.manufacturer]
        self.warn_power()

    def install_app(self, *apps_to_be_installed: str):
        if self.status:
            for app in apps_to_be_installed:
                if app in self.apps:
                    print(f"{app} ya está en el dispositivo")
                else:
                    self.drain_power(30)
                    self.apps.append(app)

    def uninstall_app(self, app: str):
        self.drain_power(10)
        if self.status:
            self.apps.remove(app)


mobile1 = MobilePhone("Xiaomi", 6.78, 4, 1000)
