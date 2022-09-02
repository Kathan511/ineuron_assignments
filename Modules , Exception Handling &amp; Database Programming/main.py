
#Task 1

def HandlingExecption():
    try:
        x = 5 / 0
    except ZeroDivisionError:
        return f"Division of any number by zero gives infinity!"



subjects = ["Americans","Indians"]
verbs = ["play","watch"]
objects = ["Baseball","Cricket"]

sentence=[]
for s in subjects:
    for v in verbs:
        for o in objects:
            sentence.append(s+' '+v+' '+o)

for i in sentence:
    print(i)