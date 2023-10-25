class Solution(object):
    def minimumRounds(self, tasks):
        """
        :type tasks: List[int]
        :rtype: int
        """
        d = {}

        def get_batches(num):
            quotient = num//3
            remainder = num %3
            if remainder == 0:  # if remainder is 0 then all the batches can be split into 3
                return quotient
            # if remainder == 1 eg 4 then we can reduce 1 from quotient and add 2 which is basically same as quotient+1
            # for 4 quotient = 1, if we remove 1 quotient = 0, remainder = 4 (2*2 batches) same with 7, quotient = 2, rem 1
            # if we reduce quotient by 1 we will have quotient 1, rem 4 (2*2 batches) i.e quotient + 1 batchees
            return quotient + 1 

        for t in tasks:
            if t not in d:
                d[t] = 1
            else:
                d[t]+=1
        
        total = 0
        for k, v in d.items():
            if v == 1:
                return -1
            total = total + get_batches(v)
        return total
