def getPosition(text):
    paragraphe=text.split("\n\n")
    position1=0
    position2=0
    test1=True
    test2=True
    for m in range(0,len(paragraphe)):
        if(('Introduction' in paragraphe[m] or 'introduction' in paragraphe[m] or 'INTRODUCTION' in paragraphe[m] or 'I. 'in paragraphe[m]) and (test1==True)):
            position1=m
            test1=False

        if(('2. ' in paragraphe[m] or 'II.' in paragraphe[m] or paragraphe[m]=='2' or '2.1 ' in paragraphe[m]) and (test2==True) and (test1==False)):
            position2=m
            test2=False
    return[position1,position2]




def getIntroduction(text):
    a=""
    result = getPosition(text)
    position1=result[0]
    position2=result[1]
    paragraphe=text.split("\n\n")
    for k in range(position1,position2+1):

        if(k==position1):
            part1=paragraphe[k].split(" ")
            for f in range(0,len(part1)):
                if('Introduction' in part1[f] or 'introduction' in part1[f] or 'INTRODUCTION' in part1[f] or '1 ' in part1[f] or 'I. 'in paragraphe[f]):
                    break
            for j in range(f,len(part1)):
                a+=part1[j]
                a+=" "
        elif(k==position2):
            part2=paragraphe[k].split(" ")
            for f in range(0,len(part2)):
                if('2.' in part2[f] or 'II.' in part2[f] or part2[f]=='2' or '2 ' in part2[f] or '2.1' in part2[f]):
                    break
            for j in range(0,f+1):
                a+=part2[j]
                a+=" "

        else:
            a+=paragraphe[k]
    return(a)
