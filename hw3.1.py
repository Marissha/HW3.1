calls = 0

def count_calls():
    global calls
    calls = calls + 1

def string_info(string):
    str_i = (len(string), string.lower(), string.upper())
    count_calls()
    return str_i, count_calls()
def is_contains(list, list_to_search):
    for i in range(len(list_to_search)):
        if list_to_search[i].lower() == list.lower():
            return True
        else:
            return False
    count_calls()

print(string_info('Capibara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)