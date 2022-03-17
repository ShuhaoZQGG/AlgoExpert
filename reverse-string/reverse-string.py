class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def swap(head, tail, ls):
            if head >= tail:
                return
            ls[head], ls[tail] = ls[tail], ls[head]
            swap(head+1, tail-1, ls)
        
        swap(0, len(s)-1,s)