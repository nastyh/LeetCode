def spiralMatrixIII(R, C, r0, c0):  # O(max(R, C)^2) b/c of the spiral. O(1) w/o the result, O(RC) otherwise
    directions = [(0,1), (1,0), (0,-1), (-1,0)]
    pointer, j = 0, 1
    result = [[r0,c0]]
    while len(result) < R * C:
        for _ in range(2):
            rd, cd = directions[pointer]
            for i in range(j):
                r0 += rd
                c0 += cd
                if 0 <= r0 < R and 0 <= c0 < C:
                    result.append([r0,c0])
            if pointer == 3:
                pointer = 0
            else:
                pointer += 1
        j += 1
    return result


def spiralMatrixIII_another(R, C, r0, c0):
    res = [[r0, c0]]
    step = 0
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    # Variable cnt keeps track of the direction, when we switch to go left count will equal to 2 and at that point the step size needs to increase. 
    # The step size also increases after we complete a full spiral.
    while len(res) < R * C:
        cnt = 0
        step += 1
        for x, y  in directions:
            cur = 0
            if cnt == 2:
                step += 1
            # Take all steps and append those within bounds
            while cur < step:
                r0 += x
                c0 += y
                cur += 1
                if 0 <= r0 < R and 0 <= c0 < C:
                    res.append([r0, c0])
            # Keeping track of which direction we are going
            cnt += 1
    return res