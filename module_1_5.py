immutable_var = (1, 25.2, [3, 3], 'a', 'Test_par')
print(immutable_var)
#immutable_var[1]=2 #TypeError: объект кортеж не поддерживает назначение элемента

mutable_list=[1, 'qwerty', 25.1, 16/4]
mutable_list[2] = 2
mutable_list[0] = 'qw'
print(mutable_list)