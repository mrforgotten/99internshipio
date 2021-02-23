answer=list()
textList=list()
number=int(input())
for i in range(number):
    textList.append(input())

def find_all(text):
    while(True):
        if(text.find(" ")<0):
            yield(("", text[0])[text[0].isupper()])
            break
        yield(("", text[0])[text[0].isupper()])
        text=text[text.find(" ")+1:]

for i in range(number):
    newText=""
    for j in find_all(textList[i]):
        y1 = j
        newText= newText + (y1)
    answer.append( ("",newText)[len(newText) > 0] )

answer.sort()
for i in range(number):
    print(answer.pop(
        answer.index(
            max(answer,key=len)
            )
        )
    )


