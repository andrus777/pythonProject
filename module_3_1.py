def count_calls(f_name):
    global calls
    calls += 1 # подсчет количества выполнения всех функций

    # подсчет количества выполнения каждой функции в отдельности
    global calls_personal
    if calls_personal.get(f_name, 0) == 0:
        calls_personal[f_name] = 1
    else:
        calls_personal[f_name] = int(calls_personal[f_name]) + 1

def string_info(string):
    count_calls("string_info")
    list_tmp = [len(string), str(string).upper(), str(string).lower()]
    return tuple(list_tmp)

def is_contains(string, list_to_search):
    count_calls("is_contains")
    result = False
    for element in list_to_search:
        if str(string).upper() == str(element).upper():
            result = True
    return result

calls = 0 # подсчет количества выполнения всех функций
calls_personal = {} # подсчет количества выполнения каждой функции в отдельности
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(string_info('ТЕстовая строка'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
print(calls_personal)