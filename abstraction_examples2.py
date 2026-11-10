class ATM:
    def set_info(self, AC, ID, Name):
        self.__ac=AC      # private
        self._id=ID       # protected
        self.name=Name    # public
    def get_info(self):
        print(self.__ac)
obj=ATM()
obj.set_info("123456", "ABCDEF", "Parnab Mondal")
print("Customar name is: ",obj.name)       # Public attribute
print(obj._id)        # Protected attribute
obj.get_info()   # Private attribute (name mangling)