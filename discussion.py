from references import *

def findAknowledgementParagraph( text ):
    text = text.split("\n\n")

    i = len( text ) - 1
    while( i >= 0 ):
        if( re.search( 'Acknowledgments', text[i] ) or re.search( 'ACKNOWLEDGMENTS', text[i] ) ):
                break
        i += -1 
    return i

def findDiscussionParagraph( text ):
    text = text.split("\n\n")

    i = len( text ) - 1
    while( i >= 0 ):
        if( re.search( 'Discussion', text[i] ) or re.search( 'DISCUSSION', text[i] ) ):
                break
        i += -1 
    if( i <= 1 ):
        return 99999
    return i


def getDiscussion(text):
    target = "Discussion"
    if( not re.search( target, text )):
        target = "DISCUSSION"

    if( re.search( "Discussion", text ) or re.search( "DISCUSSION", text )):

        x = findDiscussionParagraph(text)
        y = findReferenceParagraph(text)
        z = findAknowledgementParagraph(text)

        y = min( y, z ) 

        text = text.split("\n\n")

        par = text[x].split( target )

        discussion = ''
        if( len(par) > 1 ):
            discussion = par[1]
        
        while( x < y ):
            discussion += text[x]
            x += 1

        return discussion
 
    else: # could not find discussion section
        return ''
  





