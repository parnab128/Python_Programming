class Device:
    def __init__(self,brand,voltage):
        self.brand=brand
        self.voltage=voltage
    def power_on(self):
        print(self.brand,"Device is now on")
        
class smart_phone(Device):
    def __init__(self,brand,voltage,n):
        
        super().__init__(brand,voltage)
        self.n = n
            
    def call(self):
        print("Dialing Number is:",self.n)
        
a=smart_phone("Lenovo","15","9339634720")
a.power_on()
a.call()
