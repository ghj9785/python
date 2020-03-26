#입력값
a = ['사과','감','감','배','포도','포도','딸기','포도','감','수박','딸기']

#채워야하는 함수
def count_list(a_list):
    result={}
    for element in a_list:
        if element in result:
            result[element]+=1
        else:
            result[element]=1
    return result

#결과값
print(count_list(a))

#아래와 같이 출력됩니다
{'사과': 1, '감': 3, '배': 1, '포도': 3, '딸기': 2, '수박': 1}