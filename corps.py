#!/bin/python
import pdftotext
import glob
import sys
import os
import re

from discussion import *
from introduction import *

def findConclusionParagraph( text ):
    text = text.split("\n\n")

    i = len( text ) - 1
    while( i >= 0 ):
        if( re.search( 'Conclusion', text[i] ) or re.search( 'CONCLUSION', text[i] ) ):
                break
        i += -1
    if( i <= 1 ):
        return 00000
    return i


def getCorps(text):
    positionD = findDiscussionParagraph(text)#on recupere la position du paragraphe qui contient la discussion
    result=getPosition(text)#on recupere la position du paragraphe qui contient la partie 2
    positionC = findConclusionParagraph( text )#on recupere la position du paragraphe qui contient la conclusion
    position1=result[1]
    a=""
    if(positionD!=99999):       #on choisit si on travaille avec la discussion ou la conclusion
        position2=positionD
        word1='Discussion'
        word2='DISCUSSION'

    else:
        position2=positionC
        word1='Conclusion'
        word2='CONCLUSION'


    paragraphe=text.split("\n\n")
    if(position2!=99999):
        for k in range(position1,position2+1):

            if(k==position1):#on selectionne le texte à partir de la partie 2
                part2=paragraphe[k].split(" ")
                for f in range(0,len(part2)):
                    if('2.' in part2[f] or 'II.' in part2[f] or part2[f]=='2' or '2 ' in part2[f] or '2.1' in part2[f]):
                        break
                for j in range(f+1,len(part2)):
                    a+=part2[j]
                    a+=" "

            elif(k==position2):#on selectionne le texte avant la discusssion (ou la conclusion)
                part1=paragraphe[k].split(" ")
                for i in range(0,len(part1)):
                    if( re.search( word1, part1[i] ) or re.search( word2, part1[i] ) ):
                        break
                    a+=part1[i]
                    a+=" "
            else:#on selectionne tous ce qui entre la partie 2 et la discussion (ou la conclusion)
                a+=paragraphe[k]

    return a
