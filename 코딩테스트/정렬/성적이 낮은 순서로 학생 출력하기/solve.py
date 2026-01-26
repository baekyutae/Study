def print_sorted_info(info_list):

    sorted_info = sorted(info_list, key=lambda x: x[1])

    for i in sorted_info:
        print(i[0], end=' ')