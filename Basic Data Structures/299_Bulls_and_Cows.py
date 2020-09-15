def getHint(secret, guess):
    res = []
    bull, cow = 0, 0
    toremove = []
    secret_d, guess_d = {}, {}
    for ix in range(len(secret)):
        if secret[ix] == guess[ix]:
            toremove.append(ix)
    sl  = {k:v for k, v in enumerate(secret) if k not in toremove}
    return res


    if __name__ == "__main__":
        print(getHint('1807', '7810'))