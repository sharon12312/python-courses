import time


# # the menu list is being created only once
# def add_spam(menu=[]):
#     menu.append('spam')
#     return menu


# the menu list is being created each time when we call the function
def add_spam(menu=None):
    if menu is None:
        menu = []
    menu.append('spam')
    return menu


def show_default(arg=time.ctime()):
    print(arg)


def banner(message, border='-'):
    line = border * len(message)
    print(line)
    print(message)
    print(line)


banner('Hello Client, How are you today?')

# the default value hasn't changed
show_default()
show_default()
show_default()

# in each time 'span' is added to the list
# the default list is been created only once
breakfast = ['bacon', 'eggs']
print(add_spam(breakfast))
lunch = ['backed beans']
print(add_spam(lunch))
print(add_spam())
print(add_spam())
print(add_spam())
