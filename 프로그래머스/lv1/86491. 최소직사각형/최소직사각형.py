def solution(sizes):
    large, small = [], []
    for item in sizes:
        if item[0] < item[1]:
            large.append(item[1])
            small.append(item[0])
        else:
            large.append(item[0])
            small.append(item[1])

    return max(large) * max(small) 