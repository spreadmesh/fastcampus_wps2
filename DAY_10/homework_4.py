## 4. 문자 갯수 세기
# 문자열의 리스트를 입력받아, 각각의 문자열에 대한 갯수를 세어 `{"문자열": 문자열_갯수, ...}` 를 반환함과 동시에 예쁘게 출력하는 프로그램을 작성하시오.
"""
라인 맞춰서 예쁘게 찍기를 하는데 문제가 있음
 - %6s 와 같은 포맷코드를 사용하고자 하는데 한글은 출력될 때 두 칸을 소모함
 - 그냥 직접 공백 문자를 찍기로 선회
"""
def histogram(words):
    # 스트링들이 담긴 리스트
    hist_dict = {}
    longest_word = words[0]
    for word in words:
        if len(longest_word) < len(word):
            longest_word = word
        buf = word
        chk = 0
        for word in words:
            if buf == word:
                chk += 1
        hist_dict[buf] = chk
        chk = 0

    for key, value in hist_dict.items():
        diff_len = (len(longest_word) - len(key)) * 2
        print(key, " " * diff_len, "=" * value)

histogram(["패스트", "캠퍼스", "패스트캠퍼스", "패스트", "트랙", "아시아"])
