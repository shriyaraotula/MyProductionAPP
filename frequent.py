def top_k_frequent(nums, k):
    from collections import Counter
    Num=Counter(nums)
    """result=[]
    for item, _ in Num.most_common(k):
        result.append(item)
    return result"""
    return [item for item,_ in Counter(nums).most_common(k)]


nums = [1, 1, 1, 2, 2, 3,3,4,4,4]
k = 3
result=top_k_frequent(nums,k)
print(result)
