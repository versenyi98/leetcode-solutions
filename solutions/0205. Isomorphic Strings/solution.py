class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        st_mapping = {key: set() for key in s}
        ts_mapping = {key: set() for key in t}

        for s_, t_ in zip(list(s), list(t)):
            st_mapping[s_].add(t_)
            ts_mapping[t_].add(s_)
        return all(len(m) == 1 for m in st_mapping.values()) and all(len(m) == 1 for m in ts_mapping.values())