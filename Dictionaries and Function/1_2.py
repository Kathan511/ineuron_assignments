def filter_long_words(lst,n):
    lst1=[]
    for i in lst:
        if len(i)>n:
            lst1.append(i)
    return lst1

print(filter_long_words(["aa","aaaa","aaaaaa",'a'],2)) 