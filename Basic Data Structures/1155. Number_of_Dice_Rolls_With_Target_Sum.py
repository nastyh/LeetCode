def numRollsToTarget_dp(d, f, target):  # O(target*d) both
	dp = [[0 for _ in range(target + 1)] for _ in range(d)]
	dp[0][0] = 0
	for i in range(1, min(f, target) + 1):
		dp[0][i] = 1
	for z in range(1, d):
		for i in range(1, target + 1):
			for x in range(1, f + 1):
				if i - x >= 0:
					dp[z][i] += dp[z - 1][i - x]

	return dp[-1][-1] % 1000000007


def count_combos_math(dice, faces:, target):   # O(d^2) and O(1)
    # Shortcut if target is unattainable.
    if target < dice or target > dice * faces:
        return 0
	# Slight optimization: because problem is symmetric, choose smaller target.
	mirror_target = dice * (faces + 1) - target
	if mirror_target < target:
		target = mirror_target
    # If we had unlimited faces, the following line would give the answer:
    combo_count = choose_mod(target - 1, dice - 1)
    # But the above may include combinations where one or more dice are
    # assigned a greater value than the number of faces, so we must reduce
    # the total count to compensate.
    max_bad_dice = (target - dice) // faces  # at most dice/2
    for bad_dice in range(1, max_bad_dice + 1):
        # We can get a "bad" solution by solving a sub-problem and then
        # adding `faces` to any die (like rolling 7-12 on a 6-sided die).
        # Do this for each of our "bad" dice.
        pips_to_withhold = bad_dice * faces
        sub_count = choose_mod(target - 1 - pips_to_withhold, dice - 1)
        ways_to_choose_bad = choose_mod(dice, bad_dice)
        sub_combo = sub_count * ways_to_choose_bad % MOD

        # We alternate subtracting and adding this sub-combo; just as the
        # initial calculation included bad combinations, the count of bad
        # solutions with one bad die double-counts all bad solutions with
        # two bad dice, and so on.
        if bad_dice % 2 == 1:
            combo_count -= sub_combo
        else:
            combo_count += sub_combo
    return combo_count % MOD
