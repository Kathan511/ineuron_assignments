from random import randrange


class find_triangle:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        self.s= (a+b+c) / 2

    def total(self):
        total=(self.s*(self.s-self.a)*(self.s-self.b)*(self.s-self.c)) ** 0.5
        return f"Your area of triangle is {total}"


a=int(input(f"Enter length of 1st side: "))
b=int(input(f"Enter length of 2nd side: "))
c=int(input(f"Enter length of 3rd side: "))

tri=find_triangle(a,b,c)
print(tri.total())

