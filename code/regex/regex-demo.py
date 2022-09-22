import re


def find_date(line):
    pattern = r"\d{1,2}/\d{1,2}/\d{2,4}"
    result = re.findall(pattern,line)

    pattern=r'(October|Oct|November|Nov)( [0-9]{1,2}, [0-9]{4})'
    result = result + re.findall(pattern,line)
    return result


f = open("datefile.dat")
for line in f.readlines():
    #print(line)
    result = find_date(line)
    if (len(result)>0):
        print(result)
