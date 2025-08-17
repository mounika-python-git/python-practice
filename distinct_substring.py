    def countSubstr (self, s, k):
        # Code here
        l=len(s)
        c=0
        for i in range(0,l):
            m=set()
            for j in range(i,l):
                m.add(s[j])
                
                if len(m)==k:
                    c+=1
                elif len(m)>k:
                    break
        return c