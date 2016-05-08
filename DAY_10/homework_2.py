## 2. replace 함수의 구현 - 문자열을 치환하는 Python 내장 함수인 replace 를 직접 구현하세요.
"""
    해결 방법
 1. while문으로 직접 위치제어를 하자
 2. 비교할 위치의 문자 갯수가 다르면 곤란한데 그냥 반복문이 끝나고 나머지 부분을 붙이는 형태로 정리
"""
def word_replace(string, before, after):
    output=""
    index=0
    while index < len(string)-len(before)+1:
        if before != string[0+index:len(before)+index]:
            output += string[index]
        else:
            output += after
            index += len(before)-1
        index += 1
    output += string[index:]

    print(output)

print('''input => word_replace("패스트캠퍼스", "패스트", "Fast")''')
print("output => ", end="")
word_replace("패스트캠퍼스", "패스트", "fast")
print('''\ninput => word_replace("웹 프로그래밍 스쿨과 데이터 사이언스 스쿨", "스쿨", "SCHOOL")''')
print("output => ", end="")
word_replace("웹 프로그래밍 스쿨과 데이터 사이언스 스쿨", "스쿨", "SCHOOL")
