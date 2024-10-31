name = "Muhammad Taha Tariq".replace(' ','').lower()
unique = []
results = []

for i in range(len(name)):
    if name[i] not in unique:
        unique.append(name[i])

for i in range(len(unique)):
    count = 0
    for j in range(len(name)):
        if unique[i] == name[j]:
            count += 1;

    results.append(f"{count}{unique[i]}")


print(''.join(results))
