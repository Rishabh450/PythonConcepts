def hundred():
    i = 0
    while i < 100:
        yield i
        i += 1


print(hundred())
g = hundred()
print(list(g))
# while True:
#     print(i)
#     if next(g) is None:
#         break
#     i = next(g)


