#!/usr/bin/env python3

# # Basic float operations
# f1 = 3.14
# f2 = 1.5
# print(f"f1: {f1}, id: {id(f1)}")
# result_f_add = f1 + f2
# result_f_mul = f1 * f2
# print(f"Float Addition: {result_f_add}")
# print(f"Float Multiplication: {result_f_mul}")

# my_tuple = (1, 2, 3)
# new_tuple = my_tuple + (4, 5)
# print(
#     f"Original tuple after concat: {my_tuple}, id: {id(my_tuple)}"
# )  # Original unchanged
# print(f"New tuple after concat: {new_tuple}, id: {id(new_tuple)}")  # New object created

# # tuple unpack
# a, b, c = my_tuple
# print(f"{a} {b} {c}")


# my_dict = {"a": 1, "b": 2}
# print(f"Initial dict: {my_dict}, id: {id(my_dict)}")
# my_dict["c"] = 3  # Add a new key-value pair
# print(f"Dict after adding 'c': {my_dict}, id: {id(my_dict)}")  # id remains same
# my_dict["a"] = 10  # Modify an existing value
# print(f"Dict after modifying 'a': {my_dict}")


# # Aliasing with mutable objects
# list1 = [1, 2, 3]
# list2 = list1  # list2 now references the *same* list object as list1
# print(f"\nList1: {list1}, id: {id(list1)}")
# print(f"List2: {list2}, id: {id(list2)}")
# list2.append(4)  # Modify list2
# print(f"After list2.append(4):")
# print(f"List1: {list1}, id: {id(list1)}")  # List1 is also changed!
# print(f"List2: {list2}, id: {id(list2)}")

# a = 100
# print(f"a has id:{id(a)}")
# b = float(50.5)
# c = a + b
# print(f" {a} has id:{id(a)}, {b} has id:{id(b)}, {c} has id: {id(c)}")

x = 0
y = "hello"
z = []
w = None

if x:
    print("x is truthy")
else:
    print("x is falsy")

if y:
    print("y is truthy")
else:
    print("y is falsy")

if z:
    print("z is truthy")
else:
    print("z is falsy")
if w:
    print("w is truthy")
else:
    print("w is falsy")

print("more tests here")
if y or z:
    print("true")
else:
    print("false")
