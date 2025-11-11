## 1) has_adjacent_duplicate(L)
## Return True if the list L has any two equal elements next to each other.
## otherwise return False.
## Empty or 1-element lists → False.


L = [1,2,3,4,4,5]



def has_adjacent_duplicate(L):
    
    
    if len(L) == 0:
        return False
    
    if L[0] == L[-1]:
        return False
    
    Counter = 1
    m = L[Counter]
    for n in L:
            if n == m:
                print(n,m)
                return True
            else:
                Counter = Counter + 1
                m = L[Counter]
                if m == L[-1]:
                    return False
               

    pass
    ### Replace with your own code (end)   ###

print(has_adjacent_duplicate(L))