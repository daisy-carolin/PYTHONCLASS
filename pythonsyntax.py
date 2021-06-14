s="I love Akirachix"
print(s)
x=[2,1,4,5]
y=[4,5,6]
z=[4,7,89]
t=x+y+z
print(t)


fruits=["mango","banana","Orange","melon","apple"]
print(fruits[1:3])

print(fruits)
fruits_from_groceries=["kiwi","ovacado","guava"]
fruits.extend(fruits_from_groceries)
print(fruits)

fruits=["tomato","pawpaw","beatroot","jacaranda"]
fruits.sort()
print (fruits)

Books=["Born a crime","The Originals","Crawling out of Darkness","Betrayal in the City"]
Books.insert(2,"The river and the Source")
print(Books)

Books=["Born a crime","The originals","Crawling out of Darkness","Bettrayal in the City"]
Books.remove("Born a crime")
print(Books)


Books=["Born a crime","The Originals","Crawling out of Darkness","Betrayal in the City"]
Books.pop(3)
print(Books)

# Iteration in python
i=1
while(i<100):
    print(i)
    i +=1
   
def add(a,b):
    answer= a+b
    return answer 
x=add(3,4)
y=add(1000,5000)
z=add(1200,1500)  

print(x)
print(y)
print(z)

def subtract(c,d):
    answer=c+d
    return answer
w=subtract(1000,300)
v=subtract(1200,400)
s=subtract(300,150)

print(w)
print(v)
print(s)

def year_of_birth(name,age):
    year=2021-age
    print("Hello {} you were born in year {}".format(name))
year_of_birth(name="Lynne",age=15)
year_of_birth(name="Christine",age=55)


