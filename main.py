import random


def generate_numbers():
    numbers = []
    while len(numbers) < 3:
        new_number = random.randint(0, 9)
        if new_number not in numbers:
            numbers.append(new_number)

    return numbers


def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")

    new_guess = []
    # 코드를 작성하세요.
    while len(new_guess) < 3:
        number = int(input("{}째 숫자를 입력하세요: ".format(len(new_guess) + 1)))
        if number < 0 or number > 9:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
        elif number in new_guess:
            print("중복되는 숫자입니다. 다시 입력하세요.")
        elif number not in new_guess:
            new_guess.append(number)

    return new_guess


def get_score(guess, solution):
    strike_count = 0
    ball_count = 0

    # 코드를 작성하세요.
    i = 0
    while i < len(solution):
        if guess[i] == solution[i]:
            strike_count += 1
        elif guess[i] in solution:
            ball_count += 1
        i += 1

    return strike_count, ball_count


ANSWER = generate_numbers()
tries = 0
while True:
    S, B = get_score(take_guess(), ANSWER)
    tries += 1
    print(f"{S}S {B}B\n")
    if S == 3:
        break

# 코드를 작성하세요.

print("축하합니다. {}번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.".format(tries))
