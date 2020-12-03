#!/bin/python
import pdftotext
import glob
import sys
import os
import re

from corps import *
from references import *

def getConclusion(text):
    position1 = findConclusionParagraph(text)#on recupere la position du paragraphe qui contient la conclusion
    positionR = findReferenceParagraph(text)#on recupere la position du paragraphe qui contient la reference
    positionA = findAknowledgementParagraph(text)#on recupere la position du paragraphe qui contient la Aknowledgement

    if(positionA!=99999):       #on choisit si on travaille avec la position de la reference ou de l Aknowledgement
        position2=positionA
        word1='Acknowledgments'
        word2='ACKNOWLEDGMENTS'

    else:
        position2=positionR
        word1='References'
        word2='REFERENCES'

    a=""
    paragraphe=text.split("\n\n")
    for k in range(position1,position2+1):

        if(k==position1):#on ajoute le texte à partir du mot conclusion
            part1=paragraphe[k].split(" ")
            for f in range(0,len(part1)):
                if( re.search( 'Conclusion', part1[f] ) or re.search( 'conclusion', part1[f] ) or re.search( 'CONCLUSION', part1[f] ) or re.search( 'Conclusions', part1[f] )):
                    break

            for j in range(f,len(part1)):

                a+=part1[j]
                a+=" "

        elif(k==position2):#on ajoute le texte avant le mot l Aknowledgement (ou la reference)
            part2=paragraphe[k].split(" ")
            for i in range(0,len(part2)):
                if( re.search( word1, part2[i] ) or re.search( word2, part2[i] ) ):
                    break
                a+=part2[i]
                a+=" "
        else:#on selectionne tous ce qui entre les deux mots
            a+=paragraphe[k]


    return a
