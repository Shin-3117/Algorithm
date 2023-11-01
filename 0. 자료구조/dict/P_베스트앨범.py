#1. 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
#2. 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
#3. 장르 내에서 재생 횟수가 같은 노래 중에서는 
#고유 번호가 낮은 노래를 먼저 수록합니다.
#
#조건을 잘보자...

def solution(genres, plays):
    answer = []
    obj = {}
    for idx in range(len(genres)):
        if genres[idx] in obj:
            obj[genres[idx]]['total'] += plays[idx]
            obj[genres[idx]]['sings'].append([plays[idx],idx])
        else: 
            obj[genres[idx]] = {
                'total' : 0,
                'sings' : []
            }
            obj[genres[idx]]['total'] += plays[idx]
            obj[genres[idx]]['sings'].append([plays[idx],idx])
    print(obj)
    
    total_sort = []
    for key in obj:
        total_sort.append((obj[key]['total'],key))
    total_sort.sort(reverse=True)
    print(total_sort)
    
    for arr in total_sort:
        obj[arr[1]]['sings'].sort(key= lambda x:(-x[0],x[1]))
        answer.append(obj[arr[1]]['sings'][0][1])
        try:
            answer.append(obj[arr[1]]['sings'][1][1])
        except: continue
    return answer