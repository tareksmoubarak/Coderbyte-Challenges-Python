# def letterCapitalize(string):
#     return string.title()
def letterCapitalize(string):
    array = string.split()
    newArray = ''
    for word in array:
        newArray += ' ' + word.capitalize()
    return newArray

print letterCapitalize(raw_input())