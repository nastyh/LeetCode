def minAvailableDuration(slots1, slots2, duration):  # doesn't work right
    slots1.sort()
    slots2.sort()
    i, j = 0, 0
    while i < len(slots1) and j < len(slots2):
        if slots1[i][0] > slots2[j][1]:
            j += 1
        elif slots2[j][0] > slots1[i][1]:
            i += 1
        elif slots1[i][0] <= slots2[j][1] and abs(max(slots1[i][0], slots2[j][0]) - min(slots1[i][0], slots2[j][1])) >= duration:
            return [max(slots1[i][0], slots2[j][0]), max(slots1[i][0], slots2[j][0]) + duration]
        elif slots2[j][0] <= slots1[i][1] and abs(max(slots1[i][0], slots2[j][0] - min(slots2[j][1], slots1[i][1]))) >= duration:
            return [max(slots1[i][0], slots2[j][0]), max(slots1[i][0], slots2[j][0]) + duration]
        elif slots2[j][0] <= slots1[i][1]:
            j += 1
        else:
            pass
    return []

def minAvailableDuration_alt(slots1, slots2, duration):
    if not slots1 or not slots2: return []
    slots1 = sorted(slots1, key = lambda x:x[0])
    slots2 = sorted(slots2, key = lambda x:x[0])
    i,j = 0, 0
    while (i<len(slots1) and j<len(slots2)):            
        start1, end1 = slots1[i][0], slots1[i][1]
        start2, end2 = slots2[j][0], slots2[j][1]
        #print (' --> i, j, start1, start2 - ',i,j,start1, start2)
        if (start1 > end2): 
            j+=1
        elif start2 > end1:
            i+=1
        elif start1 <= end2 and abs(max(start1, start2) - min(end1, end2)) >= duration:
            return [max(start1, start2) , max(start1, start2) +duration]                
        elif start1 <= end2:
            i+=1
        elif start2 <= end1 and abs(max(start1, start2) - min(end1, end2)) >= duration:
            return [max(start1, start2) , max(start1, start2) +duration]
        elif start2 <= end1:
            j+=1            
        else:
            pass
    return []

if __name__ == '__main__':
    # print(minAvailableDuration([[10,50],[60,120],[140,210]], [[0,15],[60,70]], 8))
    # print(minAvailableDuration([[10,50],[60,120],[140,210]], [[0,15],[60,70]], 12))
    print(minAvailableDuration_alt([[10,50],[60,120],[140,210]], [[0,15],[60,70]], 8))
    print(minAvailableDuration_alt([[10,50],[60,120],[140,210]], [[0,15],[60,70]], 12))