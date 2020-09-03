n = ['a', 'b', 'c', 'd', 'e']
if len(n) % 2 == 0:
    i = 0
    while i < len(n):
        el = n[i]
        n[i] = n[i+1]
        n[i+1] = el
        i += 2
else:
    i = 0
    while i < len(n) - 1:
        el = n[i]
        n[i] = n[i + 1]
        n[i + 1] = el
        i += 2
print(n)