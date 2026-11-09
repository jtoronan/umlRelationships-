class Key:
    def unlock(self):
        print("Click! Lock opened.")

class Person:
    def enter_house(self, key_object):
        key_object.unlock()

my_key = Key()
me = Person()
me.enter_house(my_key) 
