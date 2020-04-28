def square(x):
    return x * x
def even_or_odd(n):
    if n % 2 == 0:
        print("even")
        return
    print("odd")
def nth_root(radicand, n):
    return radicand ** (1 / n)

print(square(5))
w = even_or_odd(6)
if w is None:
    print("w is None")

print(nth_root(16, 2))
print(nth_root(27, 3))

# import a module frm our project
# from words import fetch_words
import words
words.main('http://sixty-north.com/c/t.txt')
help(words)
