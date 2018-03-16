def max(arr):
    if arr == []:
        return None
    elif len(arr) == 1:
        return arr[0]
    else:
        submax = max(arr[1:])
        return arr[0] if arr[0]>submax else submax

lst = [23423,4,25,341,5,324,6,536,345,1,342,35,243,5,235324,6]
print(max(lst))

        
