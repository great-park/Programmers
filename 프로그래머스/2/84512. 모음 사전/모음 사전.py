from itertools import product

def solution(word):
    dictionary = []
    
    for i in range(6):
        tmp = list(product(['A', 'E', 'I', 'O', 'U'], repeat = i)) # 중복 조합
        for item in tmp:
            string_item = ("").join(item)
            dictionary.append(string_item)
    dictionary.sort()
    
    return dictionary.index(word)
















# from itertools import product
# def solution(word):
#     words = []
#     for i in range(1, 6):
#         for c in product(['A', 'E', 'I', 'O', 'U'], repeat=i):
#             print(c)
#             words.append(''.join(list(c)))

#     words.sort()
#     return words.index(word) + 1