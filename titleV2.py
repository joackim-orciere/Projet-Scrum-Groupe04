#!/bin/python
import pdftotext
import glob
import sys
import os
import re

def GetTitle(text):
    a=''
    ligne=text.split('\n')
    idEndTitle=#fct joack
    a+=line[idEndTitle+1]
    a+=" "
    position=idEndTitle+2

    if(position=='\n'):
        position++
        while(len(line[position])<30):
            a+=line[position]
            a+=" "
            position++
