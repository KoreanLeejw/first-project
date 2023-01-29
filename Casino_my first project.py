import random
import time
print("""\
####################################################################################################################
#                                                                                                                  #
#                                                                                                                  #
#                                                                                                                  #
#                                                                                                                  #
#                                                   game start                                                     #
#                                                                                                                  #
#                                                                                                                  #
#                                                                                                                  #
#                                                                                                                  #
####################################################################################################################


""")
check = input("게임을 계속하려면 enter을 눌러 주세요 >>> ")
for i in range(5):
    if check == "":
        break
    else:
        print(f"5회 실패 시 프로그램이 자동 종료됩니다 Error : ({i+1}/5)\n ")
        if i ==4:
            print("당신은 게임을 이용할 수 없습니다. 3초 후 게임을 자동 종료합니다.")
            time.sleep(3)
            exit()
        check = input("게임을 계속하려면 enter을 눌러 주셔야 합니다 >>> ")
time.sleep(0.5)
show = input("\n게임의 모든 실행 결과를 투명하게 보기를 원하십니까? (o/x) ")
time.sleep(1)
check_list = ["o", "O", "YES", "Yes", "yes", "ok", "OK", "ㅇ", "True", "yep", "true", "of course", "right", "넵", "네", "sp", "넹"]
print("\n당신이 입력한 수의 절반 이내에 럭키 7 이 나오면 당신의 승리입니다")
a = int(input("수의 범위를 입력하세요(자연수 범위가 아닐 시 게임이 자동 종료 됩니다) >>> "))


count = 0
time1 = 1
while True:
    k = random.randint(1,a)
    if show in check_list:
        print(f"{time1}번째 실행 : {k}")
    count+=1
    time1+=1
    if k == 7:
        
        break
print(f"\n{count}번째에 7이 나왔습니다!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
if count >= (a//2):
    print("\n♠♠♠당신의 패배입니다♠♠♠")
    time.sleep(50)
else:
    print("\n♣♣♣승리하셨습니다♣♣♣")
    time.sleep(50)

