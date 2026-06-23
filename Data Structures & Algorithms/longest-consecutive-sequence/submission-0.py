class Solution(object):
    def longestConsecutive(self, nums):
        d = {}
        occured = {}
        m = 1 if nums else 0
        for n in nums:
          if n not in occured:
            occured[n]=1
            if n-1 not in d and n+1 not in d:
                d[n]=[n, n]
            else:
                if n-1 in d:
                    d[n]=[d[n-1][0], n]
                    d[d[n-1][0]]= d[n]
                    m = max(m, d[n][1]-d[n][0]+1 )
                    if n+1 in d:
                       d[d[n+1][1]]= [d[n][0], d[n+1][1]]
                       d[d[n][0]] = d[d[n+1][1]]
                       m = max(m, d[d[n][0]][1]-d[d[n][0]][0]+1 )
                else:
                    d[d[n+1][1]]= [n, d[n+1][1]]
                    d[n] = d[d[n+1][1]]
                    m = max(m, d[n][1]-d[n][0]+1 )
        return m