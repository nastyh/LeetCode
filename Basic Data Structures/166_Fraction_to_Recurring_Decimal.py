class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        # store the sign so we can simplify the long division
        # by using only positive values
        sign = '-' if numerator * denominator < 0 else ''

        number, rem = divmod(abs(numerator), abs(denominator))

        # will store the visited remainder information plus the index
        # where it occurred
        seen = {}

        # the decimals
        tail = ''

        while rem > 0:
            # this means we have a
            # repitition, so let's stop
            if rem in seen:
                break

            # store the index where we
            # first seen this remainder
            seen[rem] = len(tail)

            n, rem = divmod(rem * 10, abs(denominator))

            # our decimals
            tail += str(n)
        result = sign + str(number) + '.'

        # rem == 0 means our long
        # division is clean (no repitition)
        if rem <= 0:
            result += tail
        else:
            result += tail[:seen[rem]] + '(' + tail[seen[rem]:] + ')'

        # clean trailing dot
        return result.rstrip('.')
