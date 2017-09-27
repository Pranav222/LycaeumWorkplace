import math
def ari(filename):
    file = open(f"F:/fileopen/{filename}.txt", "r+") # enter your file path
    a = file.read()
    file.close()
    b= a.split()
    d= 0
    c=0
    q= (a.split(".")[:-1])
    p = 0
    L = len(a)
    for words in b:
        c += 1
    for sentence in q:
        p += 1
    ari = 4.71*(L/c)+0.5*(c/p)-21.43
    score = math.ceil(ari)
    reading_level={ 1: 'Kintergarden',
                    2: 'First grade',
                    3: 'second grade',
                    4: 'third grade',
                    5: 'fourth grade',
                    6: 'fifth grade',
                    7: 'sith grade',
                    8: 'seventh grade',
                    9: 'eigth grade',
                    10: 'nineth grade',
                    11: 'tenth grade',
                    12: 'eleventh grade',
                    13: 'tewelveth grade',
                    14: 'college'}
    level = reading_level[score]
    if score > 14:
        print("ARI value is 14 or more. So the book is for Adults")
    else:
        print(f"This book is for {level} students")
