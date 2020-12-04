#!/bin/python
import re

def isSuspicious(line):

    cpt = 0

    for i in range( 0, len(line) ):
        l = line[i]
        cpt += bool(re.search( '[0-9]|,|-|\.', l ))
    if( cpt > 10 ):
        return True
    return False



def isTitleLineCorrect(line):
    specials = bool(re.search( '\(|\)|\[|\]\*', line ))
    length = len(line)
    words = len( line.split() )

    return not( specials or ( length < 16 ) or words > 10 or isSuspicious(line))


def findTitleStartLine(text):

    text = text.split('\n')

    ret = False

    for i in range( 0, len(text) ):
        if isTitleLineCorrect( text[i] ):
            return i

    return -1


def findTitleEndLine(text):
    s = findTitleStartLine( text )
    text = text.split('\n')

    # Title are 2 lines max
    if( isTitleLineCorrect( text[s + 1] )): 
        return s + 1;
    return s;

def getTitle(text):
    s1 = findTitleStartLine(text)
    s2 = findTitleEndLine(text)

    text = text.split('\n')

    title = text[s1]
    if( s2 != s1 ):
        title += '\n' + text[s2]

    return title

# For tests purposes
a = "Karagiannis & Reimer (Eds.): Practical Aspects of Knowledge Management.\n\
c\n\
LNAI 2569, pp. 168-178, ISBN 3-540-00314-2, Springer\n\
2002.\n\
\n\
Analysis of Clustering Algorithms for Web-based Search\n\
Sven Meyer zu Eissen and Benno Stein"

#   print(findTitleStartLine( a )) 
#   print(findTitleEndLine( a ))
#   print(getTitle( a ))
