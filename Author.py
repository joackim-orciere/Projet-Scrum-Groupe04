#!/bin/python
import pdftotext
import glob
import sys
import os
import re
from title import *

def getAuthorV2(text):
    a=''
    line=text.split('\n')
    idEndTitle=findTitleEndLine(text)
    print()
    a+=line[idEndTitle+1]
    a+=" "
    position=idEndTitle+2
    while(len(line[position])==0):
        position=position+1
        if(len(line[position+1])!=0):
            break
        a+=line[position]
        position=position+1




    return a