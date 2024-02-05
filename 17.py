##############################################################
# 1. შექმენი კლასი რომელსაც ექნება public, protected და private პარამეტრები. გამოიყენე @property დეკორატორი და ასევე შექმენი setter და getter დეკორატორებიანი ფუნქციები პარამეტრებზე წვდომისა და რედაქტირებისთვის.
##############################################################

class MyClass:
    def __init__(self, public, protected, private):
        self.public = public
        self._protected = protected
        self.__private = private

    @property
    def protected(self):
        return self._protected

    @protected.setter
    def protected(self, value):
        self._protected = value

    @property
    def private(self):
        return self.__private

    @private.setter
    def private(self, value):
        self.__private = value

#  კლასის გამოყენება
obj = MyClass("Public data", "Protected data", "Private data")
print(obj.public)  #  public პარამეტრის ბეჭვდა
print(obj.protected)  # დაბეჭდეთ protected პარამეტრიშ ბეჭვდა
print(obj.private)  # დაბეჭდეთ private პარამეტრის ბეჭვდა

# შევცვალოთ protected და private პარამეტრები
obj.protected = "New protected data"
obj.private = "New private data"

#  შეცვლილი პარამეტრების ბეჭვდა
print(obj.protected)
print(obj.private)




##############################################################
#2. შექმენი მისი შვილობილი კლასი და შეუცვალე რაიმე არსებული მეთოდი.
##############################################################


class ChildClass(MyClass):  # MyClass-ის შვილობილი კლასი ChildClass
    def do_something(self):
        super().do_something()  

# ChildClass-ის გამოსაყენებლად
obj_child = ChildClass()
obj_child.do_something()  