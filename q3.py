question = input()
question = question.split(" ")
answer = ["-"] * 12
wrong = ""
def in_list(lst,val):
    try:
        return lst.index(val)
    except ValueError:
        return -1
for times in range(5):
    guess = input()
    if(in_list(question,guess)<0):
        wrong = wrong + guess +" "
    for i in range(12):
        if(guess==question[i]):
            answer[i] = guess
            print(answer[i]+" ", end="")
        else:
            print(answer[i]+" ",end="")
    print(wrong)
score = [ind for ind,value in enumerate(answer) if value=='-']
print(12-len(score))
