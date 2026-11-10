# Example 1: Storage Hierarchy

class Storage:
    def __init__(self, name):
        self.name=name
    def data_speed(self):
        pass
class SataHDD_III(Storage):
    def ringtone(self):
        return f"SataHDD_III's Data Speed is: {self.name}!"
class SataSSD_III(Storage):
    def ringtone(self):
        return f"SataSSD_III's Data Speed is: {self.name}!"
class NVMePCIegen3(Storage):
    def ringtone(self):
        return f"NVMePCIegen3's Data Speed is: {self.name}!"
class NVMePCIegen4(Storage):
    def ringtone(self):
        return f"NVMePCIegen4's Data Speed is: {self.name}!"
class NVMePCIegen5(Storage):
    def ringtone(self):
        return f"NVMePCIegen5's Data Speed is: {self.name}!"
class NVMePCIegen6(Storage):
    def ringtone(self):
        return f"NVMePCIegen6's Data Speed is: {self.name}!"
# Usage
satahdd_III=SataHDD_III("80 mbps to 120 mbps")
satassd_III=SataSSD_III("480 mbps to 580 mbps")
nvmepciegen3=NVMePCIegen3("2000 mbps to 3500 mbps")
nvmepciegen4=NVMePCIegen4("3500 mbps to 7500 mbps")
nvmepciegen5=NVMePCIegen5("9000 mbps to 14000 mbps")
nvmepciegen6=NVMePCIegen6("15000 mbps to 25000 mbps")
print(satahdd_III.ringtone())
print(satassd_III.ringtone())
print(nvmepciegen3.ringtone())
print(nvmepciegen4.ringtone())
print(nvmepciegen5.ringtone())
print(nvmepciegen6.ringtone())