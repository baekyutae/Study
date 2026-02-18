def removeDuplicates(nums):
    # 예외 처리: 배열 길이가 2 이하면 그냥 길이 반환 
    if len(nums) <= 2: return len(nums)


    # nums[0], nums[1]은 무조건 통과
    k = 2 

    # 2. 배열 순회 
    for i in range(2, len(nums)):
        
        if nums[i] != nums[k-2]:
            nums[k] = nums[i]
            
            
            k += 1

    return k
