"""
    Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
    A subsequence of a string is a new string that is formed from the original string by deleting
     some (can be none) of the characters without disturbing the relative positions of the 
     remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
"""

def is_subsequence(s, t):
    s_idx = 0
    t_idx = 0
    s_len = len(s)
    t_len = len(t)

    while s_idx < s_len and t_idx < t_len:
        if s[s_idx] == t[t_idx]:
            s_idx += 1
        
        t_idx += 1
        
    return True if s_idx == s_len-1 else False