class Ip:
    def __init__(self, ip: str):
        try:
            assert ip.count(".") == 3
        except (AttributeError, TypeError):
            print("La ip ha de ser un string")
        except AssertionError:
            print("Ip inválida")
        else:
            self.ip, self.cidr = ip.split("/")

    def get_bin(self):
        binary = []
        octet = self.ip.split(".")
        for o in octet:
            real_bin = f"{int(o, 10):b}"
            oct_bin = f"{int(real_bin):08d}"
            binary.append(oct_bin)
        return ".".join(binary)

    def get_int(self, num: str):
        octet = num.split(".")
        res = list(int(o, 2) for o in octet)
        return ".".join(str(i) for i in res)

    def get_mask(self):
        cidr = int(self.cidr)
        bits = 0
        mask_list = []
        for i in range(32):
            if cidr > 0:
                mask_list.append("1")
                cidr -= 1
            else:
                mask_list.append("0")
            bits += 1
            if bits == 8 and i < 31:
                mask_list.append(".")
                bits = 0
        res_bin = "".join(mask_list)
        return self.get_int(res_bin)


ip1 = Ip("92.128.23.44/8")
print(ip1.get_bin())
print(ip1.get_int(ip1.get_bin()))
print(ip1.get_mask())
