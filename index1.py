def first_unique_char(s):
    from collections import Counter
    count = Counter(s)
    for idx, char in enumerate(s):
        if count[char] == 1:
            return idx
    return -1
s='aabcdcde'
result=first_unique_char(s)
print(result)
