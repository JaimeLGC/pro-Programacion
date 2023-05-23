class MobilePhone:
    def __init__(self, manufacturer: str, screen_size: float, num_cores: int):
        self.manufacturer = manufacturer
        self.screen_size = screen_size
        self.num_cores = num_cores
        self.status = False
        self.apps = []

    def power_on(self):
        if not self.status:
            self.status  = True

    def power_off(self):
        if self.status:
            not self.status 

    def install_app(self, app: str):
        if app not in self.apps:
            self.apps.append(app)

    def uninstall_app(self, app: str):
        if app in self.apps:
            self.apps.remove(app)
