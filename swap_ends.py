## 2) swap_ends(L, k)
 #  Return a NEW list formed by swapping the first k elements 
 ## with the last k
 #  elements. Keep the order of elements inside each part the same.
  # Also return the number of swaps performed as a tuple (new_list, num_swaps).
   # Do NOT change the original list.
   # If k <= 0, the list is empty, or k is larger than half of the list length,
   # return (a copy of L, 0).

L = [1,2,3,4,5]
k = 6

def swap_ends(L, k):

    if k <= 0 or len(L) ==0 or k >= len(L)/2:
        L1 = L.copy()
        return L1, 0
    
    
    else:
        newel1 = L[:k]
        newel2 = L[-k:]
        
        NL = L[k:-k]
        NL.extend(newel1)
        newel2.extend(NL)
        num_swaps= k
    
    
    return (newel2, num_swaps)

    pass

print(swap_ends(L, k))


