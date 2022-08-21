from  collections import Counter
import collections
filename = 'A a C c c B b b B'
lista = filename.lower().split()



mais_comum = collections.Counter(lista).most_common(20)

for key, value in mais_comum:
    print(key, value)