input = "abcabcabcabcdededededede"


def string_compression(string):
    answer=[]
    temp_array = [] 
    for i in range(1, len(string)):#처음에 길이 1개 그다음에 2개~문자열길이까지
        temp_array = [] 
        for k in range(0, len(string), i):
            temp_array.append(string[k:k+i])
        #print(temp_array)
        temp_array.append(0)
        result_array = ""
        before_state = ""
        repeat_time = 1
        for k in temp_array:
            if(k == 0):
                if(repeat_time != 1):
                    result_array += str(repeat_time)
                if(repeat_time > 1):
                    repeat_time = 1
                    result_array += before_state
                    before_state = k
            if(before_state != k):
                if(repeat_time != 1):
                    result_array += str(repeat_time)
                if(repeat_time > 1):
                    repeat_time = 1
                    result_array += before_state
                    before_state = k
                elif(repeat_time == 1):
                    result_array += before_state
                    before_state = k
            else:
                repeat_time += 1
        #print(result_array)
        answer.append(len(result_array))
    return min(answer)


print(string_compression(input))  # 14 가 출력되어야 합니다!
print("정답 = 3 / 현재 풀이 값 = ", string_compression("JAAA"))
print("정답 = 9 / 현재 풀이 값 = ", string_compression("AZAAAZDWAAA"))
print("정답 = 12 / 현재 풀이 값 = ", string_compression('BBAABAAADABBBD'))