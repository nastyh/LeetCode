from collections import Counter

def maxNumberOfBalloons(text):

    # problems with edge cases

    text_d = Counter(text)
    balloon_d = Counter('balloon')
    c = {key: text_d[key] - balloon_d.get(key, 0) for key in text_d}

    if max([v for k,v in c.items() if k in balloon_d.keys()]) > 0:
        return max([v for k,v in c.items() if k in balloon_d.keys()])
    else:
        return 0


def maxNumberOfBalloons_alt(text):
    string = "balloon"
    sctr = Counter(string)

    # Keeping only characters of interest from text
    ltext = [c for c in text if c in string]

    # If we don't have any characters from 'balloon' - return 0 instantly
    if not ltext:
        return 0

    # Creating a map for text under consideration
    tctr = Counter(ltext)

    # If both the hashmaps are equal - then return 1
    if tctr == sctr:
        return 1
    # Then we have to calculate the actual count
    else:
        rmap = {}
        for k,v in sctr.items():
            if k == 'l' or k == 'o':
                rmap[k] = tctr[k] // 2
            else:
                rmap[k] = tctr[k]
        return min(rmap.values())


if __name__ == '__main__':
    print(maxNumberOfBalloons('nlaebolko'))



