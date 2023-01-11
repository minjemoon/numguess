# Generate the random number
from random import randint
from time import sleep

# User interaction
def login():
  user = input("사용자 이름일 입력하세요 >> ")
  print(f"{user}로 입장하셨습니다.")

def game_start():
  print("설정한 횟수 안에 랜덤으로 생성된 숫자를 맞추는 게임입니다.")
  times = int(input("최대 횟수를 지정하십시오 >> "))

  print("1~100 사이에서 숫자가 랜덤 생성중...")
  answer = randint(1,100)
  sleep(1)
  print("랜덤 숫자가 생성되었습니다.")

  while(times >= 0):
    guess = int(input("추측한 숫자를 입력하십시오 >> "))

    if answer == guess:
      print("*************************")
      sleep(1)
      print(f"{guess}이 맞습니다. {user}님 축하합니다!")
      print("*************************")
      break
    elif guess > answer:
      print(f"{guess}보다 작습니다.")
    elif guess < answer:
      print(f"{guess}보다 큽니다.")
    times -= 1
  
  if times == 0:
    print("아쉽게도 지정하신 횟수 안에 맞추지 못하셨습니다.")
    print(f"{answer}가 정답이었습니다.")
  
  restart = input("게임을 다시 시작하시겠습니까?(yes or no) >> ")

  if restart == 'yes':
    print("게임을 다시 시작합니다.")
    game_start()
  else:
    return

login()
game_start()

