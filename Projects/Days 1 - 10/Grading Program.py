scores = {
    "harry" : 81, 
    "ron" : 78, 
    "hermione" : 99, 
    "draco" : 73, 
    "neville" : 62
}

pass_fail = {}

for key in scores:

    if scores[key] >= 91:
        pass_fail[key] = "Outstanding"
    elif 90 >= scores[key] >= 81:
        pass_fail[key] = "Exceeds Expectations"
    elif 81 > scores[key] > 71:
        pass_fail[key] = "Acceptable"
    elif 70 >= scores[key]:
        pass_fail[key] = "Fail"

print(pass_fail)