def solution(participant, completion):
    participant.sort()
    completion.sort()

    return 
    '''timeout
    for com in completion:
        participant.remove(com)
    sol = participant[0]
    return participant
    '''
    


a1 = solution(["leo", "kiki", "eden"],["eden", "kiki"])
print(a1)
a2 = solution(["marina", "josipa", "nikola", "vinko", "filipa"],["josipa", "filipa", "marina", "nikola"])
print(a2)
a3 = solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"])
print(a3)