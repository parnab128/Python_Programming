class College:
   
    def __department(self, dept_name,t_name):#private method
        self._dept_name= dept_name
        self.__t_name = t_name
    def set_dept(self,dept_name,t_name):
        self.__department(dept_name,t_name)
    
    def show(self):
        print("Course name is: ",self._dept_name)
        print("Text name is: ", self.__t_name)
ob = College()
ob.set_dept("BCA","hgfghgf")
ob.show()