import sys
letters = input().split(" ")
alpha_matrix = []
for i in range(len(letters)):
    alpha_matrix.append(list(map(int, input().split(" "))))

queries = []
for i in range(int(input())):
    queries.append(input().split(" "))


def dynamic_matrix(s1, s2, penalty): # O(n*m), n = letters in word1, m = letters in word2
    n = len(s1) 
    m = len(s2)
    
    opt = [[0 for i in range(m+1)] for i in range(n+1)] #n+1 sub arrays containing m+1 zeroes. ex. n+1=4, m+1=4 [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for i in range(n+1):
        opt[i][0] = i * penalty
    for j in range(m+1):
        opt[0][j] = j * penalty
    # [[0, -4, -8, -12], [-4, 0, 0, 0], [-8, 0, 0, 0], [-12, 0, 0, 0]]
    for i in range(1, n+1):
        for j in range(1, m+1):
            opt[i][j] = max(opt[i-1][j-1] + alpha_matrix[letters.index(s1[i-1])][letters.index(s2[j-1])], opt[i-1][j] + penalty, opt[i][j-1] + penalty)
            #alpha + opt(i-1,j-1) = equal, penalty + opt(i, j-1) = s1 lacks a letter or penalty + opt(i-1, j) = s2 lacks a letter.
            # Goes from left to right which is why we pick max to then reverse later.
    return opt


def opt_alignment(s1, s2, alpha_matrix, penalty): # O(n+m)
    alignment = []
    n = len(s1)
    m = len(s2)
    while n > 0 and m > 0:
        letter_1 = s1[n-1] if n > 0 else "*"
        letter_2 = s2[m-1] if m > 0 else "*"
        if opt[n - 1][m - 1] + alpha_matrix[letters.index(s1[n-1])][letters.index(s2[m-1])] == opt[n][m]: # if letters are the same
            alignment.append((letter_1, letter_2))
            n -= 1
            m -= 1

        elif opt[n-1][m] + penalty == opt[n][m]: # s2 lacks a letter
            alignment.append((letter_1, "*"))
            n -= 1

        else:
            alignment.append(("*", letter_2)) # s1 lacks a letter
            m -= 1

    while n > 0:
        alignment.append((s1[n-1] if n > 0 else "*", "*")) # these two loops add on the rest
        n -= 1

    while m > 0:
        alignment.append(("*", s2[m-1] if m > 0 else "*"))
        m -= 1
    
    alignment.reverse() # now reverse the list
    
    return alignment

# main
for s1, s2 in queries:
    opt = dynamic_matrix(s1, s2, -4)
    readyList = opt_alignment(s1, s2, alpha_matrix, -4)
    firstWord, secondWord = ''.join(list(zip(*readyList))[0]), ''.join(list(zip(*readyList))[1])
    print(firstWord + ' ' + secondWord)
    
# Measure-Command{.\check_solution.bat python3 gorilla.py | Out-Default}