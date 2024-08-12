calls = 0

def count_calls():
    global calls
    calls = calls + 1

def string_info(string):
    str_i = (len(string), string.upper(), string.lower())
    count_calls()
    return str_i
def is_contains(root_word, list_to_search):
    count_calls()
    for i in range(len(list_to_search)):
        if list_to_search[i].lower() in root_word.lower():
            return True
        if root_word.lower() in list_to_search[i].lower():
            return True
    return False

print(string_info('Capibara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
