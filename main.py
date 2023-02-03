# print("Hello World!")
# print(1+5)
# print(1*5)
# print(5/2)
# print(5%2)
#
# professor = "Sungchul Choi"
# print(professor)
#
# # 주석표시 (ctrl + /) or (#)
#
# a = 7
# b = 5
# print(a + b)
# print(a - b)
# print("a + b")
# print(a * b)
# print(a / b)
# print(a % b)
#
# a = 1
# b = 1
# print(a, b)
#
# a = 1.5
# b = 3.5
# print(a, b)
#
# a = "ABC"
# b = "101010"
# print(a, b)
#
# a = True
# b = False
# print(a, b)
#
# print(3 * 3 * 3 * 3 * 3)
# print(3 ** 5)
#
# print(7 // 2)
# print(7 % 2)
#
# a = 1
# a = a + 1
# print(a)
# a += 1 #증가 연산
#
# b = 1
# b = b - 1
# print(b)
# b -= 1 #감소 연산
# print(b)
#
# a = input()
# b = input()
# num1 = int(a)
# num2 = int(b)
# print(num1 + num2)
# # print(type(a))
# print(num1 * num2)
# print(num1 / num2)
# print(num1 % num2)
# print(num1 - num2)
# print(num1 // num2)
# print(num1 ** num2)
# a = "1.5"
# b = 4
# print(a * b)
#
# a = 20
# b = '10'
# print(a!=int(b))
#
# a = 53
# b = 10
# print(53 % 10)
#
# a = 572
# print(type(a))
#
# a = "10"
# b = "40"
# print(type(float(a / b)))

# print("본 프로그램은 섭씨온도를 화씨온도로 변환하는 프로그램입니다.")
# print("변환하고 싶은 섭씨 온도를 입력하세요.")
#
# celsius = input()
# fahrenheit = (float(celsius) * 1.8) + 32
#
# print("섭씨온도", celsius)
# print("화씨온도", fahrenheit)

# a = 'red'
# b = 'blue'
# c = 'green'
#
# colors = ['red', 'blue', 'green']
# print(colors[0])
# print(colors[2])
# print(len(colors))
#
# colors = [a, b, c]
# print(colors[1])

# cities = ['서울', '부산', '인천', '대구', '대전', '광주', '울산', '수원']
# print(cities[0:6])
# print(cities[3])
# print(cities[5:])
# print(cities[-1])

# print("Enter your name:")
# somebody = input()
# print("Hi", somebody, "How are you today?")

# temperature = float(input("온도를 입력하세요:"))
# print(temperature)

# ct = input()
# ft=(float(ct) * 1.8) + 32
# print("섭씨온도",ct)
# print("화씨온도",ft)

# color = ['red', 'blue', 'green']
# color2 = ['orange', 'black', 'white']
# print(len(color))
# total_color = color + color2
# print(total_color)
#
# print('blue' in color)
# print('blue' in color2)
#
# color = ['red', 'blue', 'green']
# # color.append('white')
# # color.extend(['black', 'purple'])
# color.insert(0,'orange')
# color.remove('red')
# print(color)

# 패킹 언패킹
# t = [1, 2, 3]
# a, b, c = t
#
# print(a, b, c)
# print(t, a, b, c)

# a_list = [1, 2, 3]
# b_list = [4, 5, 6]
# c_list = [a_list, b_list]
# print(c_list)
# print(c_list[0])
# print(c_list[1])


# kor_score = [49, 79, 20, 100, 80]
# math_score = [46, 59, 85, 30, 90]
# eng_score = [49, 79, 48, 60, 100]
# midterm_score = [kor_score, math_score, eng_score]
# print(midterm_score[0][2])


# print("I eat %d apples" % 3) #정수 넣기
# print("I eat %s apples" % "five") #문자열 넣기
# number = 3
# print("I eat %d apples" % number) #변수 넣기
# print("I eat %0.2f apples" % 1.456465) #소수점 자리수 지정
# print("%10s" % "hi") #공백주기
# print("%-10sjane" % "hi")

# kor_score = [49, 79, 20, 100, 80]
# math_score = [46, 59, 85, 30, 90]
# eng_score = [49, 79, 48, 60, 100]
#
# midterm_score = [kor_score, math_score, eng_score]
# math_score[0] = 1000
# print(math_score)
# print(midterm_score)
# print(midterm_score[1][2])

name = []
kor = [85, 85, 85]
eng = [80, 75, 90]
math = [65, 95, 80]

print("%15s" % "성적표")
print('---------------------------------')
print("     국어  영어  수학  파이썬  평균")




