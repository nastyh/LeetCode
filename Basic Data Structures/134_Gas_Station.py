def canCompleteCircuit(gas, cost):  # O(n) both. Max run is O(3n)
    diff = [gas[i] - cost[i] for i in range(len(gas))]
    diff_total = sum(diff)
    if diff_total < 0:
        return -1
    else:
        starting, tank = 0, 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                starting = i + 1
                tank = 0
    return starting