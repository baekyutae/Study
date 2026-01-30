def finder(shop_list, order_list):
    shop_list = sorted(shop_list)
    result = []
    for i in order_list:
        target = i
        start = 0
        end = len(shop_list) -1
        check = False
        while start <= end:
            mid = (start+end) // 2
            if shop_list[mid] == target:
                check = True
                result.append("yes")
                break
            elif shop_list[mid] > target:
                end = mid - 1
            elif shop_list[mid] < target:
                start = mid + 1
                
        if check == False:
            result.append("no")
        

    return result