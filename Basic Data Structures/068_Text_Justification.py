def fullJustify(words, maxWidth):
    currWidth, currLine, result = 0, "", []
    i=0
    while i < len(words):
        word = words[i]
        currWidth += len(word) + 1
        if currWidth-1 > maxWidth:
            currLine = currLine[:-1]
            currLength = len(currLine)
            extraSpaces = maxWidth - currLength
            currLine = self.addExtraSpaces(currLine, extraSpaces, maxWidth)
            result.append(currLine)
            currLine = ""
            currWidth = 0
            continue
        currLine += word + " "
        i+=1
    if len(currLine) <= maxWidth:
        currLine = currLine[:-1]
        spaces = maxWidth-len(currLine)
        print(spaces)
        currLine = currLine + " "*spaces
    elif len(currLine) == maxWidth+1:
        currLine = currLine[:-1]
    result.append(currLine)
    return result

def addExtraSpaces(line, spaceCount, maxWidth):
    spc = line.count(" ")
    try:
        spdiv = spaceCount // spc
    except:
        if len(line)<maxWidth:
            spaces = maxWidth-len(line)
            line = line + " "*spaces
        return line
    line = line.replace(" ", " "+" "*spdiv)
    added = spdiv * spc
    pending = spaceCount-added
    line = line.replace(" "+" "*spdiv, " "+" "*spdiv+ " ", pending)
    return line


 def fullJustify_popping(words, maxWidth):
    ans = []
    
    # iterate over all the words
    while words:
        w = words.pop(0)
        counter = len(w) # count the number of characters
        aux = []         # store the words that can be in one line
        
        # while there are words and the length of all words together 
        # plus the spaces between each words is less or iqual add the word
        while words and counter + len(words[0]) + len(aux)+1 <= maxWidth:
            aux.append(words.pop(0))
            counter += len(aux[-1])
        aux.insert(0, w)
        
        if words: # it is not the last line
            remainder = maxWidth - counter
            if remainder: 
                n_spaces = len(aux)-1
                if n_spaces > 0: #there are more than one word in the line
                    add, r = divmod(remainder, n_spaces)
                    
                    for i, a in enumerate(aux[:-1]):
                        aux[i] = aux[i] + ' '*add
                        # for the extra spaces on the left slots
                        if i < r: aux[i] = aux[i] + ' ' 

                else: # the line is just one word
                    aux[0] = aux[0] + ' '* remainder
            ans.append(''.join(aux))
        else: # this is the last word
            line = ' '.join(aux)
            line = line + ' '*(maxWidth-len(line))
            ans.append(line)
            
    return ans