calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    string_data = (len(string), string.upper(), string.lower())
    print(string_data)

def is_contains(string, list_to_search):
    count_calls()
    string = string.lower()
    for item in list_to_search:
        item = item.lower()
        if item in string:
            return True
    return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)



