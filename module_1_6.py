my_dict = {"Kurt" : 1994, "Viktor" : 1990}
print(my_dict)
print(my_dict.get("Viktor"))
print(my_dict.get("Cris"))
my_dict["Chester"] = 2017
my_dict["James"] = 1970
a = my_dict.pop("Kurt")
print(a)
print(my_dict)

my_set = {1, 2, 2, "Phone", "Phone", "Throne"}
print(my_set)
my_set.add(5)
my_set.add(8)
my_set.discard("Throne")
print(my_set)
