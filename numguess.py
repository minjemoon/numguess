
# Generate the random number
from random import randint
from time import sleep

answer = randint(1,100)

# User interaction
print('test 용도: ',  answer)
user_name = input("사용자 이름: ")
print('안녕, {}! 숫자를 맞춰보세요'.format(user_name))
guess = int(input("추측한 정답: "))
print('{}라고 작성하셨습니다.'.format(guess))

if answer == guess:
    print("************3*************")
    sleep(1)
    print("************2*************")
    sleep(1)
    print("************1*************")
    sleep(1)

    print("{}가 맞습니다. 축하합니다!".format(guess))
elif guess > answer:
    print('숫자가 너무 큽니다. {}'.format(guess))
elif guess < answer:
    print('숫자가 너무 작습니다. {}'.format(guess))
elif answer != guess:
    print("틀렸습니다.")
    print("정답은 {}입니다.".format(answer))


