def poorPigs(buckets, minutesToDie, minutesToTest):
    """
    If minutesToTest / minutesToDie = 1 then the pig has a time to die from the poison, that means that now there are two states available for the pig : alive or dead.
    If minutesToTest / minutesToDie = 2 then there are three available states for the pig : alive / dead after the first test / dead after the second test.
    The number of available states for the pig is states = minutesToTest / minutesToDie + 1.
    one pig has two available states, x pigs could test 2^x buckets
    the problem is to find x such that states^x >= buckets
    x >= log_states(buckets)

    """
    states = minutesToTest // minutesToDie + 1
    return math.ceil(math.log(buckets) / math.log(states))