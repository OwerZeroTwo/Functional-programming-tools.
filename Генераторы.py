def all_variants(s):
    for i in range(len(s) + 1):
        for j in range(i, len(s) + 1):
            yield s[i:j]

a = all_variants("abc")
for i in a:
    print(i)
