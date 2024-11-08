def get_password_for_key(random_key):
    result = ""
    par_list = []
    para = [1, 2]
    while sum(para) <= random_key:
        if (random_key % sum(para) == 0) and (not_in_list(para, par_list)) and (para[0] != para[1]):
            par_list.append([para[0], para[1]])
            par_list.append([para[1], para[0]])
            result = result + str(para[0]) + str(para[1])
        para[1] = para[1] + 1
        if sum(para) > random_key:
            para[1] = 1
            para[0] = para[0] + 1
    return result

def not_in_list(para_elem, list_of_elements):
    result = True
    for m in list_of_elements:
        if (m[0] == para_elem[0] and m[1] == para_elem[1]) or (m[1] == para_elem[0] and m[0] == para_elem[1]):
            result = False
            break
    return result

def test():
    test_list = ['', '', '', '12', '13', '1423', '121524', '162534', '13172635', '1218273645', '141923283746', '11029384756', '12131511124210394857',
            '112211310495867', '1611325212343114105968', '1214114232133124115106978', '1317115262143531341251161079', '11621531441351261171089',
            '12151811724272163631545414513612711810', '118217316415514613712811910','13141911923282183731746416515614713812911']
    for i in range(3, 20):
        res = get_password_for_key(i)
        if res == test_list[i]:
            print(f'OK. {i} - {test_list[i]}')
        else:
            print(f'!!. {i} - {test_list[i]}')

random_key = int(input("Введите число-ключ (от 3 до 20): "))
password = get_password_for_key(random_key)
print(f'Пароль для ключа {random_key} = {password}')



