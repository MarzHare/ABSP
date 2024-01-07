import traceback

# AssertionError if spam is an int less than 10
try:
    spam = int(input("Spam: "))
except ValueError:
    # Saves ValueError traceback as .txt file
    error_file = open('error_info.txt', 'w')
    error_file.write(traceback.format_exc())
    error_file.close()
    print('The traceback info was written to error_info.txt')
else:
    assert spam >= 10, 'Spam is less than 10!'

# AssertionError if the strings are the same despite case
eggs = "hellO"
bacon = "Hello"
assert eggs.lower() != bacon.lower()

# Always AssertionError
assert True == False

