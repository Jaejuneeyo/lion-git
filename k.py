def solution(array, commands):
    result = []
    for i in range(len(commands)):
        tmp = array[commands[i][0]-1:commands[i][1]] # i부터 j까지 자르기
        tmp.sort()
        result.append(tmp[commands[i][2]-1]) # 인덱스는 0부터 시작하므로 -1
    return result

array = [1,5,2,6,3,7,4]
commands = [[2,5,3],[4,4,1],[1,7,3]]

print(solution(array,commands))

