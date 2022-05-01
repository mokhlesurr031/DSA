class Person:
    name = 'mahin'
    age = 12

    def get_name(self):
        address = 'Dhaka'
        # print(self.name, address)
        print('hasatt', hasattr(Person, 'name'))


p = Person()
#
p.get_name()
#
# x = hasattr(Person, 'name')
# y = hasattr(Person, 'address')
# z = hasattr(p, 'get_name')
# add = hasattr(p, 'adress')
#
# print(x)
# print(y)
# print(z)
# print(add)