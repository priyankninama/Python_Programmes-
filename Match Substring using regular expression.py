import re
def text_match(text):
        patterns = '^[a-zA-Z0-9_]*$'
        if re.search(patterns,  text):
                return ('Found a match \n')
        else:
                return('Not matched any number and underscore in string \n')

print(text_match("Gec gandhinagar."))
print(text_match("Python_practical_24"))