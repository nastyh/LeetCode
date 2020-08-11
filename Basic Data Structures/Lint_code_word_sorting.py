def wordSorting(alphabet, words):
    new_words, new_nums = [], []
    for word in words:
        curr = []
        for ch in word:
            curr.append(alphabet.index(ch))
        new_nums.append(curr)
    new_nums.sort()
    for word in new_nums:
        curr = ''
        for ch in word:
            curr += alphabet[ch]
        new_words.append(curr)
    return new_words


if __name__ == '__main__':
    print(wordSorting(['c','b','a','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'], ['cab', 'cba', 'abc']))