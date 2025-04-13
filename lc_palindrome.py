from copy import deepcopy
from functools import cache
from itertools import accumulate
import operator


def palinLength(s: str) -> int:
    """ s is palindromic if S has length L and for every 0 <= j < L//2,
        s[j] = s[L-j]
    """
    sL = len(s) - 1
    isPal = True
    if sL > 1:
        for j in range(sL // 2 + 1):
            # fold, don't go letter by letter
            isPal = isPal and (s[j] == s[sL - j])
    else:
        isPal = isPal and (s[0] == s[sL])
    out = sL + 1 if isPal else 0
    return out


@cache
def palinLength_fold(s: str) -> int:  # fold strings
    foldlen = divmod(len(s), 2)
    lh = s[:foldlen[0]]
    rh = s[foldlen[0] + foldlen[1]:]
    lh_mirror = ''.join([t for t in reversed(lh)])
    out = [y[0] == y[1] for x, y in enumerate(zip(lh_mirror, rh))]
    out_int = 2 * sum([x for x in accumulate(out, operator.and_)])
    out_int = out_int + 1 if foldlen[1] == 1 else out_int
    return out_int


pl = cache(palinLength)


def get_change_idx(s: str) -> list[int]:
    """it's not efficient to loop over all possible pairs of left,right pointers
       when there are many repeated characters. this is only the changepoints
    """
    current_idx = 0
    current_char = s[0]
    change_idx = [0]
    while len(s) > 1:
        current_idx += 1
        s = s[1:]
        if current_char != s[0]:
            change_idx.append(current_idx)
            current_char = s[0]
    # hack to avoid changepoints at ends of palindromes
    # breakpoint()
    changepoint_diffs = [x - change_idx[_ - 1] for _, x in enumerate(change_idx)]
    double_idx_change = [(_ + 1, x == 2) for _, x in enumerate(changepoint_diffs[1:-1])]
    for cz in double_idx_change:
        if cz[1] == True:
            interp_index = change_idx[cz[0]] + change_idx[cz[0] - 1]
            change_idx.append(interp_index // 2)
    return sorted(change_idx)


def clipS(s):
    "doesn't handle the complexity!"
    out = palinLength(s)
    counter = 0
    while s and (out == 0):  # don't do this, do all pairs of cutpoints
        # print(s)
        ls = int(counter % 2 == 0)  # when counter is even, start at index 1 (remove left)
        rs = -1 if (counter % 2 != 0) else len(s)  # when counter is odd, remove right
        out += palinLength(s[ls:rs])
        counter += 1
        s = s[ls:rs]
    else:
        return s


@cache  # let's burn that memory limit
def old_ptr_clipS_UC(s):
    "dual bointers, withOUT checks for long-repeated characters"
    max_out = palinLength(s)
    if max_out == len(s):
        return s
    else:
        storing = {max_out: (0, len(s))}
        for lhs_p in range(len(s) - 1):
            for rhs_p in range(len(s), lhs_p, -1):
                out = palinLength(s[lhs_p:rhs_p])
                if out > max_out:
                    storing |= {out: (lhs_p, rhs_p)}

        max_idx = max(storing.keys())
        return s[storing[max_idx][0]:storing[max_idx][1]]


@cache  # let's burn that memory limit
def old_ptr_clipS_c(s):
    "dual bointers, withOUT checks for long-repeated characters"
    max_out = palinLength(s)
    if max_out == len(s):
        return s
    else:
        storing = {max_out: (0, len(s))}
        for lhs_p in range(len(s) - 1):
            for rhs_p in range(len(s), lhs_p, -1):
                out = pl(s[lhs_p:rhs_p])
                if out > max_out:
                    storing |= {out: (lhs_p, rhs_p)}

        max_idx = max(storing.keys())
        return s[storing[max_idx][0]:storing[max_idx][1]]


@cache  # let's burn that memory limit
def ptr_clipS_c(s):
    "dual bointers, with checks for long-repeated characters"
    max_out = palinLength(s)
    if max_out == len(s):
        return s
    else:
        storing = {max_out: (0, len(s))}

        lhs_stops = get_change_idx(s)
        for lhs_p in lhs_stops:
            rhs_stops = [x for x in lhs_stops if x > lhs_p] + [len(s)]
            for rhs_p in rhs_stops:
                out = pl(s[lhs_p:rhs_p])
                if out > max_out:
                    storing |= {out: (lhs_p, rhs_p)}

        max_idx = max(storing.keys())
        return s[storing[max_idx][0]:storing[max_idx][1]]


@cache  # let's burn that memory limit
def ptr_clipS_UC(s):
    "dual bointers, but palinlength function is not cached to stay in memory limit for whole-alphabet problems"
    max_out = palinLength(s)
    if max_out == len(s):
        return s
    else:
        storing = {max_out: (0, len(s))}
        lhs_stops = get_change_idx(s)
        for lhs_p in lhs_stops:
            rhs_stops = [x for x in lhs_stops if x > lhs_p] + [len(s)]
            for rhs_p in rhs_stops:
                out = palinLength(s[lhs_p:rhs_p])
                if out > max_out:
                    storing |= {out: (lhs_p, rhs_p)}

        max_idx = max(storing.keys())
        return s[storing[max_idx][0]:storing[max_idx][1]]


def splitS(s):
    "too slow! but recursion is fun"
    out = palinLength(s)
    longest_substr = '' if out == 0 else s

    if out == 0:
        for j in range(1, len(s)):
            lhs = s[:j]
            lhs_str = splitS(lhs)
            longest_substr = lhs_str if (
                    (palinLength(lhs_str) > 0) and (len(lhs_str) > len(longest_substr))) else longest_substr
            rhs = s[j:]
            rhs_str = splitS(rhs)
            longest_substr = rhs_str if (
                    (palinLength(rhs_str) > 0) and (len(rhs_str) > len(longest_substr))) else longest_substr

    return longest_substr


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # is the whole string palindromic? no? recurse until you find one and report lengthw
        # work in from the outside

        s = s[0] if (len(s) == 2) and (s[0] != s[1]) else s
        # rs = ''.join([t for t in reversed(s)])
        if palinLength(s) != len(s):
            s = ptr_clipS_c(s)

        return s
