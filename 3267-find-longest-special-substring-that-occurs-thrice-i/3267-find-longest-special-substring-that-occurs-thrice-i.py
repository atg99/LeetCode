class Solution:
    def maximumLength(self, s: str) -> int:
        for i in range(len(s)-2,0,-1):
            dct = {}
            for j in range(len(s)):
                if i!=1 and len(set(s[j:j+i]))==1:
                    print(s[j:j+1])
                    dct[s[j:j+i]] = dct.get(s[j:j+i],0)+1
                elif i==1 and j!=len(s)-1 and s[j]!=s[j+1]:
                    dct[s[j]] = dct.get(s[j],0)+1
                elif i==1 and s[j]:
                    dct[s[j]] = dct.get(s[j],0)+1
            if max(dct.values())>=3:
                print(dct.values(),dct.keys())
                return i
        return -1
                
