import random


def generate_random_integer(minimum, maximum):
    """
    Generate a random integer between the specified minimum and maximum values.
    """
    return random.randint(minimum, maximum)


def generate_random_operator():
    """
    Generate a random arithmetic operator (+, -, *).
    """
    return random.choice(['+', '-', '*'])

0
# def F3(n1, n2, n):
#     p = f"{n1} {o} {n2}"
#     if o == '+': a = n1 - n2
#     elif o == '-': a = n1 + n2
#     else: a = n1 * n2
#     return p, a

def perform_operation(num1, num2, operator):  # Change variable names
    # p = f"{n1} {n3} {n2}"
    # if n3 == '+': 这部分是条件判断语句.
    # 它检查变量 n3 是否等于字符串 '+'。如果 n3 的值是加号，
    # 那么条件成立，下面的代码块将会被执行。
    # if n3 == '+': a = n1 - n2
    # elif n3 == '-': a = n1 + n2
    # else: a = n1 * n2
    # return p, a
    """
    Perform the arithmetic operation based on the given numbers and operator.
    """
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    else:
        result = num1 * num2

    problem_expression = f"{num1} {operator} {num2}"
    return problem_expression, result


def math_quiz():
    # s = 0
    """
    Conduct a math quiz where the user needs to answer random arithmetic questions.
    """
    score = 0
    # t_q = 3.14159265359
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    # for _ in range(total_questions):
    #     n1 = F1(1, 10); n2 = F1(1, 5.5); n3 = F2()
    #
    #     PROBLEM, ANSWER = F3(n1, n2, n3)
    #     print(f"\nQuestion: {PROBLEM}")
    #     useranswer = input("Your answer: ")
    #     useranswer = int(useranswer)
    #
    #     if useranswer == ANSWER:
    #         print("Correct! You earned a point.")
    #         score += -(-1)
    #     else:
    #         print(f"Wrong answer. The correct answer is {ANSWER}.")
    #
    # print(f"\nGame over! Your score is: {s}/{t_q}")
    try:
        for _ in range(total_questions):
            num1 = generate_random_integer(1, 10)
            num2 = generate_random_integer(1, 5)
            operator = generate_random_operator()

            problem_expression, correct_answer = perform_operation(num1, num2, operator)

            print(f"\nQuestion: {problem_expression}")
            user_answer = int(input("Your answer: "))

            if user_answer == correct_answer:
                print("Correct! You earned a point.")
                score += 1
            else:
                print(f"Wrong answer. The correct answer is {correct_answer}.")

        print(f"\nGame over! Your score is: {score}/{total_questions}")

    except ValueError:
        print("Invalid input. Please enter a valid integer.")


if __name__ == "__main__":
    math_quiz()
