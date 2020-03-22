def is_palindrome_perm(s):
    s = s.lower().replace(" ", "")
    d = {}
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    max_non_pair = 0 if len(s) % 2 == 0 else 1
    for k in d.keys():
        if d[k] % 2 != 0:
            max_non_pair -= 1
        if max_non_pair < 0:
            return False
    return True

if __name__ == '__main__':
    print(is_palindrome_perm("Able was I ere I saw Elba".lower().replace(" ", "")))
