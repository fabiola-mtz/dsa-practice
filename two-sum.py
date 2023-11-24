def two_sum(arr, target):
    h_map = dict()

    for i in range(arr):
        num2 = target - arr[i]

        if num2 in h_map.keys():
            return [i, h_map[num2]]
        
        h_map[num2] = i
    
    return -1