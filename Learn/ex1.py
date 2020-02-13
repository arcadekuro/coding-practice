def user_problem(user_answer, correct_answer):
    if user_answer == correct_answer:
        print("Correct!")
    else:
        print('Incorrect!')
    return user_problem


user_problem(2, 3)
user_problem(3, 5)
user_problem(3, 3)
