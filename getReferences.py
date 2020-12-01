#!/bin/python
import os
import glob
import re


     

def findReferenceParagraph( text ):
    text = text.split("\n\n")

    i = len( text ) - 1
    while( i >= 0 ):
        if( re.search( 'reference', text[i], re.IGNORECASE )):
                break
        i += -1 
    return i

def getReferences( text ):

    i = findReferenceParagraph( text )

    text = text.split("\n\n")

    par = text[i].split('References')

    references = '' 
    if( len( par )) > 1 :
        references = par[1]

    while( i < len( text ) ):
        references += text[i]
        i += 1

    return references

