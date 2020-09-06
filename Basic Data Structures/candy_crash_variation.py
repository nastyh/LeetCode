def candy_var(s):
    d, res = [], []
    d.append([s[0], 1])
    for ch in s[1:]:
        if ch == d[-1][0]:
            d[-1][1] += 1
        else:
            d.append([ch, 1])
    for combo in d:
        if combo[1] < 3:
            res.append(combo[0] * combo[1])
        else:
            res.append(combo[0] * (combo[1] % 3))
    return ''.join(i for i in res if i != '')


if __name__ == '__main__':
    print(candy_var('abbbc'))
    print(candy_var('abbbbc'))
    print(candy_var('abbc'))