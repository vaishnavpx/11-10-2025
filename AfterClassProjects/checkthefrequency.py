test_dict={"Codingal": 3, "is": 2, "best": 2, "for": 2, "coding": 2}
print("The original dictionary : "+ str(test_dict))
K=int(input("Enter a value: "))
res=0
for key in test_dict:
    if test_dict[key]==K:
        res=res+1
print("frequency of your value is : "+ str(res))