info= {
    "name":"D",
    "age" : 18,
    "marks": 100.0,
    "subject": ["java","c","python"],
    "topics": ("dictionary","set")
}
print(info["age"])
print(info)

info["name"]="Adarsh"  # to change
info["surname"]="Pratik" # To add
print(info)

# Nested Dictionary
student={
    "name":"Pranav",
    "subjects":{
        "physics":98,
        "Math":100,
        "Chemistry":96
    },
    "age":20
}
print(student)

#Methods in Dict
print(student.keys()) #Return all keys of dict expect nested
print(len(student)) #Print total No of keys value
print(student.values()) #Return all values
print(student.items()) #Return key & values in touple form
print(student.get("name"))# To get value
student.update({"city":"Radhanagari"}) # To update
print(student)