count = 0


def show_count():
    print(count)


# count is a local variable in the function scope
# count variable will be deleted once the function wil end
def set_count(c):
    count = c


def set_global_count(c):
    global count
    count = c


show_count()
set_count(5)
show_count()
set_global_count(5)
show_count()