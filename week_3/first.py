################ 변수 선언 #################
# a = 3
# b = a
# a = a + 1

# num1 = a*b
# num2 = 99


################ 데이터 타입 (튜플에서는 desstructuring 가능) #################

# name = 'bob'
# num = 12

# is_number = True

# a=['사과','배','감']
# print(a[0]) #사과


# a= {}
# a= {'name':'paul','age':24}
# print("hello world!")

################ 함수 #################
# def f(x):
# 	return 2*x+3

# y = f(2)
# print(y)


################ 루프 #################
fruits = ["apple", "banana", "cherry"]

for num in fruits:
    print(num)

for i in range(5):
    print(i)

# enumerate 는 index 를 가져올수 있게 힘
for i, fruit in enumerate(fruits):
    print(i, fruit)

################ 조건문 #################
age = 25

if age > 20:
    print("성인입니다")
else:
    print("청소년입니다")

for item in fruits:
    if item == "apple":
        print("apple")
    elif item == "banana":
        print("banana")
    else:
        print("other fruits")

################ venv 설치 #################
