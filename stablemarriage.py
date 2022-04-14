#You are given each man’s and woman’s preference lists. Given these lists find a stable matching, meaning #that
#there do not exist two man-woman-pairs (m 1 , w 1 ), (m 2 , w 2 ) such that w 2 is higher ranked on m 1 ’s #preference list
#than w 1 and simultaneously m 1 is higher ranked on w 2 ’s preference list than m 2 (thus that both m 1 and #w 2 would
#prefer to change partner).

#


from operator import index


def GS (listfromtest):
    W = [] #list of women
    inputlist = [int(x) for x in listfromtest.split()]
    peopleamount = inputlist.pop(0) # how many males/females we have - also preferences amount
    print ('asdfasdf')
    M = [inputlist[x:x+peopleamount + 1] for x in range (0, len(inputlist), peopleamount + 1) ] # split input into sublists and gradually move sublists into W
    
    for i in range (1,peopleamount +1):
        for val in M: 
            if val[0] == i:
                W.append(M.pop(M.index(val)))
                W[-1].pop(0)
                break
    for male in M:
        male.pop(0)
    
        #now men and women have pref lists in order in M, W

    for Woman in W:  #invert list
        inverselist = []
        for index in range(1,peopleamount+1):
           for i in range (0, peopleamount):
               if index == Woman[i]:
                   inverselist.append(i)
        W[W.index(Woman)] = inverselist
       

    unmarried = M
    married = [-1 for i in range(peopleamount)] #married is a list of women currently married to the index
    while -1 in married: #while some man has no woman
        for male in unmarried: #for each male in unmarried 
            indexofman = unmarried.index(male) #index 
            if married[indexofman] == -1: #if he is not married, we want to propose
                perfectgirl = male[0]
                if perfectgirl in married:
                    Whatshethinksofproposer = W[perfectgirl][indexofman]
                    Whatshethinksofhusband = W[perfectgirl][married.index(perfectgirl)]
                if perfectgirl not in married: #if his pref is not married
                    married[indexofman] = male.pop(0) #his pref is added to his married spot and removed from his preflist as no point in trying again
                elif Whatshethinksofproposer>Whatshethinksofhusband: #
                    married[married.index(perfectgirl)] = -1
                    married[unmarried.index(male)] = perfectgirl
                else:
                    male.pop(0)
    
    print (*married, sep='\n')
contents = []
while True:
    try:
        line = input()
    except EOFError:
        break
    contents.append(line)
listToStr = ' '.join([str(elem) for elem in contents])
#GS('2 1 1 2 1 2 1 2 2 1 2 1 2 ')
#GS('4 4 2 1 4 3 1 3 2 4 1 1 1 4 3 2 2 2 4 3 1 3 1 2 4 3 3 4 3 1 2 4 3 2 4 1 2 1 3 2 4')
#GS('10 5 9 4 3 1 5 8 2 6 10 7 1 3 1 9 2 8 5 10 6 7 4 7 8 2 7 4 9 10 1 5 3 6 9 10 1 5 7 8 3 9 4 6 2 4 5 2 8 9 4 6 3 7 1 10 7 3 7 2 6 8 4 5 1 9 10 10 10 7 6 4 2 8 5 9 3 1 3 7 8 2 10 3 5 9 6 1 4 6 10 9 7 1 3 2 4 8 6 5 1 2 9 5 1 10 8 4 6 7 3 8 2 9 4 8 7 6 10 1 3 5 6 1 10 9 5 4 3 2 8 7 6 4 6 2 8 7 10 3 5 9 1 4 2 10 1 7 5 6 8 3 2 4 9 2 7 1 8 3 2 9 4 6 10 5 3 7 9 2 10 5 8 4 6 1 3 9 5 3 7 2 10 1 6 4 9 8 10 4 9 8 7 3 5 6 1 2 10 5 5 8 7 3 9 2 1 10 4 6 8 9 8 5 3 6 7 2 1 4 10')
GS(listToStr)
  

            






