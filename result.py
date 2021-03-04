

f = open('temp.txt', 'r')
a = f.readline()
b = f.readline()
print(a)
if a > '11110':
    import verystrong
elif a > '1110':
    import strong
elif a > '110':
    import good
elif a > '10':
    import bad
else:
    import verybad