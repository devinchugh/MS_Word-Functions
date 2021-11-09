# CODES FOR VARIOUS PROGRAMS FOR STRINGS

print('Enter the string on which you wish to execute all the programs:')
print('At last press enter keeping the last line empty')
string = ''
temp = 'run'

while(temp == 'run'):
    line = input()
    string += line+' '
    if line == '':
        temp = 'stop'

lis = string.split()

# 1- PROGRAM TO COUNT THE  TOTAL WORDS


print('1-The total number of words in the entered string are:', len(lis))
print('\n')

# 2- PROGRAM  TO FIND THE WORDS BEGINNING WITH CAPITAL LETTER

cptl = []
for i in lis:
    if ord(i[0]) > 64 and ord(i[0]) < 91:
        cptl.append(i)

print('2-The words beginning with capital letters in the entered string are:', cptl)
print('\n')

# 3- PROGRAM  TO FIND THE WORDS BEGINNING WITH SMALL LETTER

small = []
for i in lis:
    if ord(i[0]) > 96 and ord(i[0]) < 123:
        small.append(i)

print('3-The words beginning with small letters in the entered string are:', small)
print('\n')

# 4- PROGRAM TO FIND A PARTICUALAR WORD IS PRESENT IN ENTERED STRING OR NOT

find = input('4-Enter the word to be found:')

count = 0
for i in lis:
    if find == i:
        count += 1

if count != 0:
    print('Yes, the word is present and its occurence is:', count)
else:
    print('No, the word is not present')

print('\n')

# 5- PROGRAM TO REPLACE THE WORD

find = input('5-Enter the word to be replaced:')

count = 0
for i in lis:
    if find == i:
        count += 1

x = 0
if count != 0:
    print('The entered word is present', count, 'times')
    x = int(input('How many occurences of it you wish to replace:'))
    replace = input('Enter the word by which it is to be replaced:')
else:
    print('the word is not present')

string = ''
update = []
for i in lis:
    update.append(i)
for i in range(x):
    for j in range(len(update)):
        if update[j] == find:
            update[j] = replace
            break

print('The updated string is:', ' '.join(update))
print('\n')

# 6- PROGRAM TO CAPITALISE THE WHOLE STRING

cptl = []
for i in lis:
    str = ''
    for j in i:
        if ord(j) > 96 and ord(j) < 123:
            str += chr(ord(j)-32)
        else:
            str += j
    cptl.append(str)

print('The string  with all the words in capital letters is:')
print(' '.join(cptl))
print('\n')

# 7- PROGRAM TO CHANGE CAPITAL LETTERS TO SMALL FOR THE WHOLE STRING

small = []
for i in lis:
    str = ''
    for j in i:
        if ord(j) > 64 and ord(j) < 91:
            str += chr(ord(j)+32)
        else:
            str += j
    small.append(str)

print('The string  with all the words in small letters is:')
print(' '.join(small))
print('\n')

# 8- PROGRAM TO ARRANGE THE WORDS OF THE STRING IN ASCENDING ORDER

words = []
for i in lis:
    words.append(i)

for i in range(0, len(words)):
    min = words[i]
    temp = i
    for j in range(i, len(words)):
        if min > words[j]:
            min = words[j]
            temp = j
    (words[i], words[temp]) = (words[temp], words[i])

print('The string with words arranged in ascending order is:')
print(' '.join(words))
print('\n')


# 9- PROGRAM TO ARRANGE THE WORDS OF THE STRING IN DESCENDING ORDER


for i in range(0, len(words)):
    max = words[i]
    temp = i
    for j in range(i, len(words)):
        if max < words[j]:
            max = words[j]
            temp = j
    (words[i], words[temp]) = (words[temp], words[i])

print('The string arranged with words in descending order is:')
print(' '.join(words))
print('\n')

# 10-PROGRAM TO COUNT THE OCCURENCE OF EACH WORD

unq = []
countdic = {}
for i in lis:
    if i not in unq:
        unq.append(i)

for i in unq:
    count = 0
    for j in lis:
        if i == j:
            count += 1
    countdic[i] = count

print('The dictionery with the count of occurence of every word is:')
print(countdic)
print('\n')

# 11-PROGRAM TO COUNT THE OCCURENCE OF EACH VOWEL

vowels = 'aeiou'
smstring = ''.join(small)
countvwl = {}

for i in vowels:
    count = 0
    for j in smstring:
        if i == j:
            count += 1
    countvwl[i] = count

print('The count of the occurence of each vowel is:')
print(countvwl)
print('\n')

# 12-PROGRAM TO COUNT THE OCCURENCE OF EACH CONSONENT

countcon = {}

for i in range(ord('a'), ord('z')+1):
    count = 0
    for j in smstring:
        if chr(i) in vowels:
            break
        elif chr(i) == j:
            count += 1
    if chr(i) not in vowels:
        countcon[chr(i)] = count

print('The count of the occurence of each consonent is:')
print(countcon)
print('\n')

# 13- PROGRAM TO CHANGE LOWERCASE WORDS INTO UPPERCASE AND UPPERCASE WORDS TO LOWERCASE

newstr = ''

for i in lis:
    temp = ''
    for j in i:
        if ord(j) >= ord('a') and ord(j) <= ord('z'):
            temp += chr(ord(j)-32)
        elif ord(j) >= ord('A') and ord(j) <= ord('Z'):
            temp += chr(ord(j)+32)
        else:
            temp += j
    newstr += temp+' '

print('The string with lowercase letters changed to uppercase and upper case letters changed to lowercase is:')
print(newstr)
print('\n')

# 14-PROGRAM TO REVERSE THE WHOLE PARAGRAPH

revstr = ''

for i in range(len(lis)-1, -1, -1):
    revstr += lis[i]+' '

print('The whole paragraph in reverse order is:')
print(revstr)
print('\n')

# 15-PROGRAM TO REVERSE EACH WORD IN THE STRING

revword = ''

for i in lis:
    temp = ''
    for j in range(len(i)-1, -1, -1):
        temp += i[j]
    revword += temp+' '

print('The paragraph with all the words reversed is:')
print(revword)
print('\n')

# 16-PROGRAM TO REVERSE ONLY THOSE WORDS PRESENT AT EVEN INDEXES

reveven = ''

for i in range(0, len(lis)):
    temp = ''
    if i % 2 == 0:
        for j in range(len(lis[i])-1, -1, -1):
            temp += lis[i][j]
    else:
        temp += lis[i]
    reveven += temp+' '

print('The paragraph with the words at even position reversed is:')
print(reveven)
print('\n')

# 17-PROGRAM TO REVERSE ONLY THOSE WORDS PRESENT AT ODD INDEXES

revodd = ''

for i in range(0, len(lis)):
    temp = ''
    if i % 2 != 0:
        for j in range(len(lis[i])-1, -1, -1):
            temp += lis[i][j]
    else:
        temp += lis[i]
    revodd += temp+' '

print('The paragraph with the words at odd position reversed is:')
print(revodd)
print('\n')

# 18- PROGRAM TO REMOVE ALL THE SPACES FROM ENTERED STRING

spacefree = ''
for i in lis:
    spacefree += i

print('The string with all the spaces removed from the entered string:')
print(spacefree)
print('\n')

# 19- PROGRAM TO MAKE A STRING WHICH ONLY CONTAINS WORDS AT EVEN POSITION

evenstr = ''

for i in range(len(lis)):
    if i % 2 == 0:
        evenstr += lis[i]+' '

print('The string with only the words at even position from entered string is:')
print(evenstr)
print('\n')

# 20- PROGRAM TO MAKE A STRING WHICH ONLY CONTAINS WORDS AT ODD POSITION

oddstr = ''

for i in range(len(lis)):
    if i % 2 != 0:
        oddstr += lis[i]+' '

print('The string with only the words at odd position from entered string is:')
print(oddstr)
print('\n')

# 21- PROGRAM TO SORT THE WORDS ACCORDING TO THEIR LENGTH

sortlis = []

for i in lis:
    sortlis.append(i)

for i in range(len(sortlis)):
    min = len(sortlis[i])
    temp = i
    for j in range(i, len(sortlis)):
        if min > len(sortlis[j]):
            min = len(sortlis[j])
            temp = j
    (sortlis[i], sortlis[temp]) = (sortlis[temp], sortlis[i])

print('The string with the words sorted according to their length is:')
print(' '.join(sortlis))
print('\n')


# 22- PROGRAM TO REMOVE VOWELS FROM THE ENTERED STRING

remvov = ''
vowels = 'aeiou'

for i in lis:
    temp = ''
    for j in i:
        if j not in vowels:
            temp += j
    remvov += temp+' '

print('The string with all the vowels removed from entered string is:')
print(remvov)
print('\n')

# 23- PROGRAM TO SWAP THE ODD AND EVEN INDEXES WORDS

swaplis = []
for i in lis:
    swaplis.append(i)

for i in range(0, len(lis)-1, 2):
    (swaplis[i], swaplis[i+1]) = (swaplis[i+1], swaplis[i])

print('The string with the words at even indexes swapped with the words at odd indexes:')
print(' '.join(swaplis))
print('\n')


# 24- PROGRAM TO CHANGE A PARTICUALR WORD TO UPPERACASE TAKING USER INPUT

change = input('Enter the word that you want to change to uppercase:')

newstr = ''
for i in lis:
    if i == change:
        temp = ''
        for j in i:
            if ord(j) >= ord('a') and ord(j) <= ord('z'):
                temp += chr(ord(j)-32)
            else:
                temp += j
        newstr += temp+' '
    else:
        newstr += i+' '

print('The string with all the occurences of entered word changed to uppercase is:')
print(newstr)
print('\n')

# 25-PROGRAM TO PRINT THE WORD OCCURING MAXIMUM TIMES AND MINIMUM TIMES

wordcount = {}
uniqword = []

for i in lis:
    if i not in uniqword:
        uniqword.append(i)

for i in uniqword:
    count = 0
    for j in lis:
        if i == j:
            count += 1
    wordcount[i] = count

max = 0
min = count
maxstr = ''
minstr = ''

for j in wordcount.values():
    if j > max:
        max = j
    elif j < min:
        min = j

for i in wordcount.keys():
    if wordcount[i] == max:
        maxstr += i+', '
    elif wordcount[i] == min:
        minstr += i+', '

maxstr = maxstr[:len(maxstr)-2]
minstr = minstr[:len(minstr)-2]

print('The words that occurs,', max, '(maximum times) are:')
print(maxstr)
print('\n')
print('The words that occurs,', min, '(minimum times) are:')
print(minstr)
print('\n')

# 26-PROGRAM TO REPLACE ALL OCCURENCES OF A PARTICULAR ALPHABET TO UPPERCASE

letter = input(
    'Enter the letter which you want to change to uppercase(lowercase letter only):')

newlis = []

for i in lis:
    temp = ''
    for j in i:
        if j == letter:
            temp += chr(ord(j)-32)
        else:
            temp += j
    newlis.append(temp)


print('The string with the entered letter changed to uppercase is:')
print(' '.join(newlis))
print('\n')


# 27- PROGRAM TO FIND THE WORD HAVING 'K' DISTINCT CHARACTERS

k = int(input('Enter the number to find the word having that much distinct characters:'))
find = []

for i in lis:
    if len(i) < k:
        pass
    else:
        count = 0
        uniq = []
        for j in i:
            if j not in uniq:
                uniq.append(j)
        if len(uniq) == k:
            find.append(i)

print('The words with the entered number of distinct characters is:')
print(', '.join(find))
print('\n')

# 28-PROGRAM TO COUNT THE FREQUENCY OF EACH CHARACTER IN THE STRING

countchr = {}
uniqchr = []

for i in lis:
    for j in i:
        if j not in uniqchr:
            uniqchr.append(j)

for i in uniqchr:
    count = 0
    for j in lis:
        for k in j:
            if k == i:
                count += 1
    countchr[i] = count

print('The dictionery with the frequency of each character is:')
print(countchr)
print('\n')

# 29-PROGRAM TO FIND MAXIMUM AND MINIMUM OCCURING CHARACTER IN GIVEN STRING

max = 0
min = count
maxchr = ''
minchr = ''

for i in countchr.keys():
    if countchr[i] > max:
        max = countchr[i]
    elif countchr[i] < min:
        min = countchr[i]

for i in countchr.keys():
    if countchr[i] == max:
        maxchr += i+', '
    elif countchr[i] == min:
        minchr += i+', '

maxchr = maxchr[:len(maxchr)-2]
minchr = minchr[:len(minchr)-2]

print('The characters which occurs', max, '(maximum) times are:', maxchr)
print('\n')
print('The characters which occurs', min, '(minimum) times are:', minchr)
print('\n')


# 30- PROGRAM TO FIND AND PRINT THE SENTENCE WITH MAXIMUM NUMBER OF WORDS

lines = ' '.join(lis).split('.')

max = 0
for i in range(0, len(lines)):
    if len(lines[i].split()) > max:
        max = len(lines[i].split())
        temp = i

print('The sentence having', max, '(maximum) words is:')
print(lines[temp])
print('\n')
print('\n')

print('THE END')
