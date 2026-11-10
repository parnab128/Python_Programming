# Example 1: Mobile_ringtone Hierarchy

class Mobile:
    def __init__(self, name):
        self.name=name
    def ringtone(self):
        pass
class Apple(Mobile):
    def ringtone(self):
        return f"Apple mobile's ringtone is: {self.name}!"
class Samsung(Mobile):
    def ringtone(self):
        return f"Samsung mobile's ringtone is: {self.name}!"
class Realme(Mobile):
    def ringtone(self):
        return f"Realme mobile's ringtone is: {self.name}!"
class Vivo(Mobile):
    def ringtone(self):
        return f"Vivo mobile's ringtone is: {self.name}!"
class Oppo(Mobile):
    def ringtone(self):
        return f"Oppo mobile's ringtone is: {self.name}!"
class Xiaomi(Mobile):
    def ringtone(self):
        return f"Xiaomi mobile's ringtone is: {self.name}!"
# Usage
apple=Apple("Jay Shree Ram...")
samsung=Samsung("Hare-krishna...")
realme=Realme("Hori-bol...")
vivo=Vivo("Jay Jagannath")
oppo=Oppo("Jay Ma..., Jay Ma...")
xiaomi=Xiaomi("Suno na sang maar maar...")
print(apple.ringtone())
print(samsung.ringtone())
print(realme.ringtone())
print(vivo.ringtone())
print(oppo.ringtone())
print(xiaomi.ringtone())