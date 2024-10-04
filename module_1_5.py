immutable_var = 360, 'memories', True, 'Love'
print(immutable_var)
#immutable_var[0] = 180
#print(immutable_var) Вылезает ошибка, т.к кортеж не поддерживает изменения, он
                    # нужен для списков которые должны оставаться неизменными, нетронутыми. 

mutable_list = [0, 'never', False, 'control']
mutable_list[0] = 666
print(mutable_list)
