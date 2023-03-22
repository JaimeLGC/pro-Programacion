class MobilePhone:
    def __init__(self, manufacturer: str, screen_size: float, num_cores: int):
        self.manufacturer = manufacturer
        self.screen_size = screen_size
        self.num_cores = num_cores
        self.apps = []
        self.status = False

    def power_on(self):
        self.status = True

    def power_off(self):
        self.status = False

    def install_app(self, app: str):
        self.apps.append(app)

    def uninstall_app(self, app: str):
        self.apps.remove(app)


mobile1 = MobilePhone("Xiaomi", 6.78, 4)

mobile1.install_app("Telegram")
print(mobile1.num_cores)
