def repeatLength_back(s, l):
    bigl = [[s[0], 1]]
    res = ''
    for ch in s[1:]:
        if bigl[-1][0] != ch:
            # curr_count = 1
            bigl.append([ch, 1])
        else:
            bigl[-1][1] += 1
    for pair in bigl[::-1]:
        if pair[1] < l:
            res += pair[1] * pair[0]
    return res[::-1]


if __name__ == '__main__':
    # print(repeatLength('abbccccdd', 3))
    # print(repeatLength('abbcccdeaffff', 3))
    # print(repeatLength_alt('abbcccdeaffff', 3))
    print(repeatLength_back('abbccccdd', 3))
    print(repeatLength_back('abbcccdeaffff', 3))