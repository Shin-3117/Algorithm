def solution(citations):
    answer = 0
    sort_citations = sorted(citations, reverse=True)
    lst_len = len(sort_citations)
    for i in range(lst_len,0,-1):# 7 6 5 ~ 1
        if sort_citations[i-1] >= i: return i
    return answer

a=solution([0, 1, 3, 300, 350, 400, 500])
print(a)#4 7-3