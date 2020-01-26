##ASSIGNMENT 4
##Name: Mohid Ali Gill
##Roll Number: 21-10842


##Q1

def stripEnds(s):
    """ (str) -> str

    Return a new string based on s in which all letters have been
    converted to lowercase and punctuation characters have been stripped 
    from both ends. Inner punctuation is left untouched. 

    >>> clean_up('Happy Birthday!!!')
    'happy birthday'
    >>> clean_up("-> It's on your left-hand side.")
    " it's on your left-hand side"
    """

    lower=s.lower()
    string=lower.strip(".-?)([!"',;:]<>*#\n\t\r'"")
    return string
string1=input("enter string")
print(stripEnds(string1))

##Q2

def avgLength(s):
    """ (str) -> float

    Precondition: string is non-empty and ends with \n and
    contains at least one word.

    Return the average length of all words in s.

    >>> text = 'James Fennimore Cooper! Peter, Paul and Mary\n'
    >>> avgLength(text)
    5.142857142857143
    """
    total=0
    avg=0
    stripEnds(s)
    b=s.split()
    for i in range (len(b)):
        y= stripEnds(b[i])
        total=total+len(y)
    avg=total/len(b)
    return avg
x=input("enter string")
print(avgLength(x))       
   
##Q3

def avgWordLength(text):
    """ (list of str) -> float

    Precondition: text is non-empty. Each str in text ends with \n and
    text contains at least one word.

    Return the average length of all words in text. 
    

    >>> text = ['James Fennimore Cooper\n', 'Peter, Paul and Mary\n']
    >>> avg_word_length(text)
    5.142857142857143 
    """
    x=int(input("how many strings will you enter"))
    for i in range(x):
        y=input("enter string")
        list=[y]
    a=len(list)
    for j in range(a):
        z=avgLength(list[j])
    return z
        
    
##Q4

def typeTokenRatio(text):
    """ (list of str) -> float

    Precondition: text is non-empty. Each str in text ends with \n and
    text contains at least one word.

    Return the Type Token Ratio (TTR) for this text. TTR is the number of
    different words divided by the total number of words.

    >>> text = ['James Fennimore Cooper\n', 'Peter, Paul, and Mary\n',
        'James Gosling\n']
    >>> type_token_ratio(text)
    0.8888888888888888
    """
    list=[]
    z=int(input("how many strings will you enter"))
    for i in range(0,z,1):
          y=input("enter string")
          list=list+[y]
    a=len(list)
    sum=0
    for i in range(0,a,1):
        sum=sum+len(list[i])
        stripEnds(list[i])
    b=0
    mydict={}
    for j in range(0,a,1):
        for k in range(0,len(list[j]),1):
                mydict[j]=list[j]
    print (mydict)
    print(mydict.values())
    for n in range(0,len(mydict),1):
        for p in range(0, len(mydict[n]),1):
            if mydict[p] != "":
                word=mydict[p]
            
        

    # To do: Fill in this function's body to meet its specification.

##Q6
    
def split_on_seperators(original, seperator):
    """ (str, str) -> list of str

    Return a list of non-empty, non-blank strings from original,
    determined by splitting original on any of the separators.
    separators is a string of single-character separators.

    >>> split_on_separators("Hooray! Finally, we're done.", "!,")
    ['Hooray', ' Finally', " we're done."]
    """
    # To do: Fill in this function's body to meet its specification.
    list=[]
    x=""
    for i in range(len(original)):
        if i < (len(original)):
            if original[i] == seperator:
                a= original[len(x):i]
                list.append(a)
                x=x+""+a
            if i == (len(original)-1) and original[i] not in seperator:
                b= original[len(x):i+1]
                list.append(b)
    return list
string=input("enter string")
seperator=input("enter seperator")
print(split_on_seperators(string,seperator))
    
            


