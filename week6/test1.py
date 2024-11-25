class Gun:
    def __init__(self,name,ammo):
        self.name = name
        self.ammo = ammo
    def add_ammo(self,ammo):
        self.ammo += ammo
gun1 = Gun("M4",25)
gun1.add_ammo(5)
print(gun1.ammo)