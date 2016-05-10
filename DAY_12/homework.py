# 3. calendar과제

def is_leap_year(year):
	return True if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else False

def get_calendar(year, month):

        default_year = 1900
        totalday = [0, 31, 28+is_leap_year(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        what_day_is_it = ["일", "월", "화", "수", "목", "금", "토"]
        days = (year - default_year) * 365
        for i in range(default_year, year):
            days += is_leap_year(i)
        for i in range(0, month):
                days += totalday[i]

        days += 1 # 첫 번째 날짜 계산


# 그리는 부분
        print("      {month}월 {year}".format(month=month, year=year))
        print("일 월 화 수 목 금 토")        
        print("   " * (days % 7), end = "")

        for i in range(1, totalday[month]+1):

            if len(str(i)) == 1:
                print(" {i} ".format(i=i), end="")
            else:
                print("{i} ".format(i=i), end="")
            if (days+i) % 7 == 0:
                print()

        print("\n")

get_calendar(2016, 6)
