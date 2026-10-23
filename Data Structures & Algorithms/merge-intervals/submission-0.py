class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        def recurse(l1, l2):
            if l2[0] <= l1[1]:
                return [min(l1[0], l2[0]), max(l1[1], l2[1])]
            return None

        res = [intervals[0]]
        for i in range(1, len(intervals)):
            temp = recurse(res[-1], intervals[i]) 
            
            if temp:
                res[-1] = temp
            else:
                res.append(intervals[i])
            

        return res



            

