class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        ns, np = len(s), len(p)
        if ns < np:
            return []
        p_counter = collections.Counter(p)
        s_counter = collections.Counter()
        for i in range(ns):
            s_counter[s[i]] += 1
            if i >= np:
                if s_counter[s[i - np]] == 1:
                    del s_counter[s[i - np]]
                else:
                    s_counter[s[i - np]] -= 1
            if p_counter == s_counter:
                res.append(i - np + 1)
        return res