def getIntroduction(text):
    paragraphe=text.split("\n\n")
    position1=0
    position2=0
    test1=True
    test2=True
    a=""
    for m in range(0,len(paragraphe)):
        if(('Introduction' in paragraphe[m] or 'introduction' in paragraphe[m] or 'INTRODUCTION' in paragraphe[m]) and (test1==True)):
            position1=m
            test1=False

        if(('2. ' in paragraphe[m] or 'II' in paragraphe[m]) and (test2==True)):
            position2=m
            test2=False


    print(position2)
    for k in range(position1,position2+1):
        if(k==position1):
            part1=paragraphe[k].split(" ")
            for f in range(0,len(part1)):
                if('Introduction' in part1[f] or 'introduction' in part1[f] or 'INTRODUCTION' in part1[f]):
                    break
            for j in range(f,len(part1)):
                a+=part1[j]
                a+=" "
            k=k+1

        if(k==position2):
            part2=paragraphe[k].split(" ")

            for f in range(0,len(part2)):
                if('2.' in part2[f] or 'II' in part2[f]):
                    print(f)
                    break
            for j in range(0,f+1):
                a+=part2[j]
                a+=" "
            k=k+1

        a+=paragraphe[k]
    return(a)
