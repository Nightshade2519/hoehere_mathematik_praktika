import timeit

import numpy as np


def fact_rec(n):
    if n < 0 or np.trunc(n) != n:
        raise Exception('The factorial is defined only for positive integers')
    if n <= 1:
        return 1
    else:
        return n * fact_rec(n - 1)


def fact_for(n):
    if n < 0 or np.trunc(n) != n:
        raise Exception('The factorial is defined only for positive integers')
    if n <= 1:
        return 1
    else:
        value = 1
        for i in range(2, n + 1):
            value *= i

        return value


t1=timeit.repeat("fact_rec(500)", "from __main__ import fact_rec", number=100)
t2=timeit.repeat("fact_for(500)", "from __main__ import fact_for", number=100)

# r = min(t1)
# f = min(t2)
# print(r)
# print(f)
# print(f"Difference in factor rec/for: {r / f}")

#Welche der beiden Funktionen ist schneller und um was für einen Faktor? Weshalb?
#Die For-Loop ist schneller mit etwa dem Faktor 3.5 (Rechner abhängig).
#Rekursiv ist langsamer, da es sich selber aufrufen muss und beim rekursive die Werte immer gespeichert werden muss

#Gibt es in Python eine obere Grenze für die Fakultät von n
#als ganze Zahl (vom Typ 'integer')? Versuchen Sie hierzu, das Resultat für n ∈ [190, 200] als integer auszugeben.
# for n in range(190, 201):
#     print(n, int(fact_for(n)))
# scheint nicht der Fall zu sein

#als reelle Zahl (vom Typ float')? Versuchen Sie hierzu, das Resultat für n ∈ [170, 171] als float auszugeben.
# for n in range(170, 172):
#     print(n, float(fact_for(n)))
#170 geht noch aber ab 171 kommt der Error: OverflowError: int too large to convert to float