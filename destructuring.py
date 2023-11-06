t=5,11
x,y=t
print(x,y)

student_attendence={"bob":90,"rolf":80,"Anne":85}

print(list(student_attendence.items()))
for student ,attedance in student_attendence.items():
    print(f"{student},{attedance}")

people=[("bob",42,"mechanic"),("james",42,"artist"),("harry",32,"trainer")]
for name,age,profession in people:
    print(f"name :{name},age:{age},profession{profession}")
for person in people:
    print(f"name : {person[0]} ,age :{person[1]},profession ,{people[2]}")

person=("bob",42,"mechanic")
name,_,profession=person=person # _ will be ignored from the files 
print(name,profession)

*head,tail=[1,2,3,4,5] # Head have frist value  * will collect all remaining values in and packed in others 
print(head)
print(tail)
print(*head)
# * has importancein the values 