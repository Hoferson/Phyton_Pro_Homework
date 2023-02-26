import re

text = 'vsRbbr678j'                 # 1

pattern = r'[R]b+[r]'

result = re.search(pattern, text)

print(result.group())



text = '9999-9999-9999-9989'            # 2

pattern = r'[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{4}' # for any card
pettern2 = r'9{4}-9{4}-9{4}-9{4}' # for card (9999-9999-9999-9999)

result = re.search(pattern, text)

print(result.group())



text = 'ry66uYf-Y1z_p@gmail.com'                        # 3

def is_it_gmail(text):

    regular = r'^[a-zA-Z0-9][a-zA-Z0-9_-]*@gmail.com$'
    if re.search(regular, text):
        if len(re.findall(r'-', text))>1:
            return False
        else:
            return True
    return False


print(is_it_gmail(text))



login = '25i6Yu59t9'                                # 4

def login_check(login):
    pattern = r'^[0-9a-zA-Z]{2,10}$'
    if re.search(pattern, login):
        return True
    else:
        return False

print(login_check(login))