student_data={
    "id1": {"name": "Sara", "class": "V", "subject_integration": "english, math, science"},
    "id2": {"name": "David", "class": "V", "subject_integration": "english, math, science"},
    "id3": {"name": "Sara", "class": "V", "subject_integration": "english, math, science"},
    "id1": {"name": "Surya", "class": "V", "subject_integration": "english, math, science"},
}

result={}
seen=set()

for student_id, details in student_data.items():
    unique_key=(details["name"], details["class"], details["subject_integration"])
    if unique_key not in seen:
        seen.add(unique_key)
        result[student_id]=details


for k,v in result.items():
    print(k,":",v)