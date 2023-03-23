class MobilePhone:
    def __init__(self, manufacturer: str, screen_size: float, num_cores: int):
        self.manufacturer = manufacturer
        self.screen_size = screen_size
        self.num_cores = num_cores
        self.apps = []
        self.status = False
        self.power = 100

    def power_drain(self):
        if self.manufacturer == 'Xiaomi':
            self.power -= 2

    def switch(self):
        if self.status == True:  
            self.status = False
        elif self.status == False:      
            self.status = True

    def install_app(self, app: str):
        self.apps.append(app)

    def uninstall_app(self, app: str):
        self.apps.remove(app)

    def power_warning(self):
        if self.power == 20:
            print('Aviso, batería baja')
        elif self.power == 10:
            print('Aviso, batería MUY baja')
        elif self.power == 0:

mobile1 = MobilePhone("Xiaomi", 6.78, 4)

mobile1.install_app("Telegram")
print(mobile1.num_cores)
