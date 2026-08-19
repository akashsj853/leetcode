class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        def fun(s,t):
            if len(t)==k:
                res.append(t[::])
                return
            for i in range(s,n+1):
                t.append(i)
                fun(i+1,t)
                t.pop()
        fun(1,[])
        return res            