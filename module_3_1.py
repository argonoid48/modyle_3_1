# Галкин Андрей
# Задача "Счётчик вызовов"

calls = 0

def string_info(string):
    global calls
    calls += 1
    return len(string),string.upper(), string.lower()

def is_contains(string, list_to_search):
    global calls
    calls += 1
    string_upp = string.upper()
    uppercase_list = [s.upper() for s in list_to_search]
    if string_upp in uppercase_list:
        return True
    else:
        return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)