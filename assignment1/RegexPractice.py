import re

#Ex1
def names():
    simple_string = """Amy is 5 years old, and her sister Mary is 2 years old. 
    Ruth and Peter, their parents, have 3 kids."""

    # YOUR CODE HERE
    pattern = "[A-Z][a-z]*"

    test_string = simple_string
    # result = re.match(pattern, test_string)
    result = re.findall(pattern, test_string)
    return result


#Ex2
def grades():
    with open("assets/grades.txt", "r") as file:
        grades = file.read()

    only_B_grades = re.findall("[A-Z][a-z]* [A-Z][a-z]*\: [B]", grades)
    person = [grade_B.split(':')[0] for grade_B in only_B_grades]
    return person



#Ex3
def logs():
    pattern = '(?P<host>(?:\d+\.){3}\d+)\s+(?:\S+)\s+(?P<user_name>\S+)\s+\[(?P<time>[-+\w\s:/]+)\]\s+"(?P<request>.+?.+?)"'
    with open("assets/logdata.txt", "r") as f:
        data = f.read()
    logs = []
    for m in re.finditer(pattern, data):
        logs.append(m.groupdict())
    return logs

# if __name__ == '__main__':
#     names()
#     print("person: " + str(grades()))
#     it = []
#     it.append(1)
#     print(len(logs()))
