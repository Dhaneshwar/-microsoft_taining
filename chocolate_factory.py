def insertion_sort(a):
    for i in range(1, len(a)):
        val = a[i]       
        j = i - 1        
        while j >= 0 and a[j] > val:
            a[j + 1] = a[j]  
            j -= 1           
        a[j + 1] = val
a = [4, 5, 0, 1, 9, 0, 5, 0]
insertion_sort(a)
a.reverse()
print("Sorted list:", a)




















            
            
