from time import perf_counter

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

start = perf_counter()
unique_src = []
for elem in src:
    if src.count(elem) == 1:
        unique_src.append(elem)
print (unique_src, perf_counter() - start)

start = perf_counter()
unique_src = [elem for elem in src if src.count(elem) == 1]
print(unique_src, perf_counter() - start)

