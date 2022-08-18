#Task 1
word="xyz"
output_1=[x*n for x in list(word) for n in range(1,5)]
print("Output:")
print(output_1)

#Task 2

output_2=[n*i for i in range(1,5) for n in list(word)]
print("Output:")
print(output_2)

#Section 3
number=[2,3,4]
number_1=[[x+n] for x in number for n in range(0,3)]
print(number_1)

#Section 4
number_2=[2,3,4,5]
number_3=[[x+n for n in range(0,4)] for x in number_2 ]
print(number_3)

#Section 5
number_4=[1,2,3]
number_5= [(b,a) for a in number_4 for b in number_4]
print(number_5)