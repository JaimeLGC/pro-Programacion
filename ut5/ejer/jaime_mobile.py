power_drainage = {"Samsung": 0.85, "Xiaomi": 1.00, "Nokia": 1.10, "Alcatel": 1.25}


class MobilePhone:
    def __init__(
        self, manufacturer: str, screen_size: float, num_cores: int, power: int
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
            self.power_drain(10)

    def power_warning(self):
        if self.status:
            if self.power <= self.power * 0.20 and self.power > self.power * 0.10:
                print("Aviso, batería baja")
            elif self.power <= self.power * 0.10 and self.power > 0:
                print("Aviso, batería MUY baja")
            elif self.power == 0:
                print("Apagando...")
                self.switch()

    def power_drain(self, power_spent):
        self.power = -power_spent * power_drainage[self.manufacturer]
        self.power_warning()

    def install_app(self, *apps_to_be_installed: str):
        for app in apps_to_be_installed:
            if app in self.apps:
                print(f"{app} ya está en el dispositivo")
            else:
                self.power_drain(30)
                if self.status:
                    self.apps.append(app)

    def uninstall_app(self, app: str):
        self.power_drain(15)
        if self.status:
            self.apps.remove(app)


mobile1 = MobilePhone("Xiaomi", 6.78, 4, 1000)
