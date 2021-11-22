# checking for name .
def greeting(username,vowel):
    commonletters=[]
    for t in vowel:
        for a in username:
            if a==t :
                commonletters.append(t)
    singulisecommonletters=set(commonletters)
    if len(singulisecommonletters) > 1:
        print(f'Good {username} ,what a nice name u have!')
    else :
        print(f'{username} ,I neaver hear that name ')     


username=input('what is your name  : ')
greeting(username,'a e i ou')        




    
        
                