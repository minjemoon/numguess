
# Generate the random number
from random import randint
answer = randint(1,100)

# User interaction
user_name = input("사용자 이름: ")
print('안녕, {}! 숫자를 맞춰봐'.format(user_name))
guess_answer = input("추측한 정답: ")

if answer == guess_answer:
    print("{}가 맞습니다.".format(guess_answer))
else:
    print("틀렸습니다.")
    print("정답은 {}입니다.".format(answer))
