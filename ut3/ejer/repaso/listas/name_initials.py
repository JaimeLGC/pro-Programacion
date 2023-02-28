# **********************
# INICIALES DE UN NOMBRE
# **********************


def run(fullname: str) -> str:
    loco = []
    for names in fullname.upper().split(","):
        for name in names.split(" "):
            loco.append(name.split()[0])
    print(loco)


#    initials =

#    return initials


if __name__ == "__main__":
    run("Delgado Quintero, sergio")
