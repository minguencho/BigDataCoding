# 다수의 매개 변수 연산

def calculate(choice, *args):
    result = 0
    if choice == "plus":
        result = args[0]
        for i in args[1:]:
            result = result + i

    elif choice == "minus":
        result = args[0]
        for i in args[1:]:
            result = result - i
                
    elif choice == "multiple":
        result = args[0]
        for i in args[1:]:
            result = result*i
        
    elif choice == "devide":
        result = args[0]
        for i in args[1:]:
            result = result/i

    else:
        print("plz input \n plus \n minus \n multiple \n devide")

    print("result is %d" % result)
choice = input("input type of calculate :")
while (input == "stop"):
    input = input("input number : ")

calculate(choice,4,3)