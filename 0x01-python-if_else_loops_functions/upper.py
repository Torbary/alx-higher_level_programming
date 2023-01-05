def uppercase(s):
    output = ''
    for c in s:
        if 'a' <= c <= 'z':
            c = chr(ord(c) - ord('a') + ord('A'))
        output += c
    print(output)
    print()
