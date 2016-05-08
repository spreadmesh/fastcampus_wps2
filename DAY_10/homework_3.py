# 3. 2016년 오늘은 무슨 요일?
"""
 풀이 과정

 7로 나눈 나머지를 이용한다.
 1월 1일이면 1%7 => 1 => 금요일
 5월 9일이면 31 + 28 + 31 + 30 + 9 ( 근데 윤년이니까 28이 아니고 29 )
 첫 번째 파라미터는 그 전달까지의 날짜 합산용
 두 번째 파라미터는 그 달의 날짜
 둘을 더해서 mod 7
"""
def get_day_of_week(month, day):

	totalday = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# 편하게 쓰기 위해 인덱스의 숫자와 month의 숫자를 맵핑
	what_day_is_it = ["목", "금", "토", "일", "월", "화", "수"]
	year = 2016
	days = 0

	if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
		totalday[2] = 29

	for i in range(month):
		days += totalday[i]

	days += day

	print("{}요일".format(what_day_is_it[days % 7]))


get_day_of_week(5, 9)
