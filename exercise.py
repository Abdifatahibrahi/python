"""
sample `questions.txt` file:
1+1=2
2+2=4
8-4=4
task description:
- read from `questions.txt`
- for each question, print out the question and and wait for the user's answer
    for example, for the first question, print out: `1+1=`
- after the user answers all the questions, calculate her score and write it to the `result.txt` file
    the result should be in such format: `Your final score is n/m.`
    where n and m are the number of correct answers and the maximum score respectively
"""

# questions = open("questions.txt", "r")

# question_list = [line.strip() for line in questions.readlines()]
# questions.close()

# total = len(question_list)
# grade = 0

# for line in question_list:
#     q,a = line.split("=")

#     ans = input(f"{q} = ")

#     if a==ans:
#         grade = grade + 1

# result = open("result.txt", "w")
# final_grade = grade/total
# result.writelines(f"Your final score is {final_grade}")


questions = open('questions.txt', 'r')
question_list = [line.strip() for line in questions]
questions.close()

score = 0
total = len(question_list)


for line in question_list:
    q,a = line.split("=")
    
    
    ans = input(f"{q}= ")
    
    if a == ans:
        score = score + 1
        
result = open("result.txt", "w")  # open result.txt
# write final score to result.txt
result.write(f"Your final score is {score}/{total}.")
result.close()
