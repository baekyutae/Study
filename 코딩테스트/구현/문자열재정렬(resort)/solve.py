# 시간복잡도 : O(NlogN)
'''
for i in give => n

sort => nlogn

for c in give => n

"".join(str_list) =>n

'''


input_str = input()

def resort(give):
    str_list = []
    num_sum = 0
    
    for i in give:
        
        if i.isalpha():
            str_list.append(i)
        else:
            num_sum += int(i)
            
    
    str_list.sort()
    
    if num_sum != 0 or any(c.isdigit() for c in give):
        str_list.append(str(num_sum))
        
    return "".join(str_list)


resort(input_str)