# This .py make sandglass
# 아침시간 Quiz

num = int(input("가장 윗 줄에 들어갈 *의 갯수를 입력하세요 : "))

i = 0			# for while-loop
num_of_space = 0	# control blank space
switch = False		# check if it passed middle point

while i < num:
    print(' ' * num_of_space + '*' * (num - (2 * num_of_space)) + ' ' * num_of_space)		# 공백 갯수에 초점을 맞춰 별 갯수를 조절
    if(switch is not True):										# 중간까지 안 갔다면
        if( num - (2 * (num_of_space+1)) > 0  ):								# 공백이 하나 더 늘어나도 별찍는게 문제가 없다면
            num_of_space += 1											# 공백 찍는 갯수 증가시키고
        else:													# 공백 하나 더 늘리면 별이 찍히지 않는다면
            num_of_space -= 1											# 공백을 하나 줄이고
            switch = True											# 이제는 끝날 때까지 공백을 하나씩 줄이자
            if(num - (2 * (num_of_space+1)) == 0):								# 그리고 혹시나 들어온게 짝수라서 라면 처리해주자
                i += 1
    else:												# 줄어드는 상황이라면(중간을 넘었다면)
        num_of_space -= 1
    i += 1
