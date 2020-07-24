"""This function To find number of character"""

def countcharter(reptitionchar):
    """create hash table for Alphabet"""
    hashingtable={}
    val=97
    for i in range(0,26):
        hashingtable[chr(val)]=0
        val+=1
    """this for count the reptition charater"""
    for i in reptitionchar:
        hashingtable[i]+=1
    print("To know the number of repetition of a character:")
    #print(hashingtable)
    val=97
    for i in range(0,26):
        if hashingtable[chr(val)]!=0:
            print(chr(val),hashingtable[chr(val)])
        val+=1


"""This function To find number of word"""
def countword(reptitionword):
    print("To know the number of repetition of a word:")
    dic={}
    for i in reptitionword:
        try:
            dic[i]+=1
        except:
            dic[i]=1
    print(dic)


"""This function find number of conversation"""
def countconversation(conversation):
    print("To know the length of conversation:")
    if conversation%2==0:
        print(conversation//2)
    else:
        print(conversation//2+1)






"""/ Geting input from the user/"""


print("Pleale enter the input this format. like `A:ping`")
print("if you want to stop enter the input please enter `quit`")

reptitionchar=''
reptitionword=[]
conversation=0

while(1):
    try:
        s1,s2=input().split(':')
        conversation +=1
        reptitionchar+=s2
        reptitionword.append(s2)     
    except:
        break
"""Function call"""
countcharter(reptitionchar)
countword(reptitionword)
countconversation(conversation)







        
    
