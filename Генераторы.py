def all_variants(s):
    def subsequence(s, i, result):
        if i == len(s):
            yield ''.join(result)
        else:
            subsequence(s, i + 1, result)
            result.append(s[i])
            yield from subsequence(s, i + 1, result)
            result.pop()

    yield from subsequence(s, 0, [])

# Пример использования функции
a = all_variants("abc")
for i in a:
    print(i)