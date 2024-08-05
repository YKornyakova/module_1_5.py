# ДЗ урок 4 Кортежи module_1_5.py
#immutable_var = 1, 2, 3, "dog", "cat"
#print(tuple(immutable_var))
#immutable_var_1 = [1, 2, 3, "dog", "cat"]
#print(tuple(immutable_var_1))
#immutable_var_2 = ([1, 2, 3, "dog", "cat"])
#print(tuple(immutable_var_2))
#print(tuple(immutable_var_2)[0])
#tuple(immutable_var_2)[0] = 3
mutable_list = [3, 5, "orange", "melon"]
print(mutable_list)
print(mutable_list[2])
mutable_list[2] = "apple"
print(mutable_list)
mutable_list.append(15)
print(mutable_list)
