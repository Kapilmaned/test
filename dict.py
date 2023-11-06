friend_ages={"Rolf":24,"Adam":30,"Anne":27}

friend_ages["Bob"] =20

print(friend_ages)

friends=[
    {"name":"Rolf" ,"age":34},
    {"name":"Adam" ,"age":40},
    {"name":"Anne" ,"age":50},
]
print(friends[1]["name"]) # Provide the indexno and dictonery name 

student_attendence={"Rolf":90,"Adam":80,"Anne":85}

for student in student_attendence:
    # print(student) # Print the keys 
    print(f"{student}:{student_attendence[student]}")

student_attendence={"bob":90,"Adam":80,"Anne":85}

if "bob" in student_attendence:
    print(f"bob: {student_attendence["bob"]}")
else:
    print("bob is not student of the class") # Getting value  in the print 

attendence_values=student_attendence.values()
print(attendence_values)