lst=[]
first_name=input('Enter your first name:')
lst.append(first_name)
last_name=input('Enter Last name')
lst.append(last_name)
reverse=' '.join(lst[::-1])
print(reverse)
