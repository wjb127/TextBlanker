import random



# start program loop
while True:

    # open text file
    file_name = input('빈칸을 생성할 텍스트 파일명 입력 : ')
    file = open(file_name+'.txt','r',encoding='utf-8')

    # read one line, split with " " and store the length of words
    line = file.readline()
    char = line.split(' ')
    charlen = len(char)

    # make cache of blanked text and
    bsk = []
    oldbsk = []
    bskran = []

    # before the end of the text
    while line!='':

        # remove '\n' from end of word in list
        endchar = ''
        if charlen > 0:
            endchar = char[charlen-1]
        else :
            endchar = ''

        # collect words in bsk list
        endcharlen = len(endchar)
        bsk = bsk + char[0:charlen-1] + [endchar[0:endcharlen-1]] + ['\n']
        oldbsk = oldbsk + char[0:charlen - 1] + [endchar[0:endcharlen - 1]] + ['\n']


        # read one line, split with " " and store the length of words
        line = file.readline()
        char = line.split(' ')
        charlen = len(char)

    # make random numbers as many as words in the original text
    # with value of 0 as ratio 25% for not "" and '\n'
    for index in range(0,len(bsk)):
        if bsk[index] != '\n' and bsk[index] != '':
            num = random.randint(0,4)
        else:
            num = -1
        bskran.append(num)

    # make blank if the matched random number is 0
    for index in range(0,len(bsk)):

        if bsk[index]!='\n' and bsk[index]!='' and bskran[index]==0:
            bsk[index] = "_"*len(bsk[index])

    # print(bskran)
    # print(oldbsk)
    # print(bsk)

    # file close and start writing
    file.close()
    file = open(file_name+'_blanked.txt','w',encoding='utf-8')

    # write the text in the bsk variable
    i=0
    while i<len(bsk):

        # write appropriate space between words
        if bsk[i] == '\n':
            file.write(bsk[i])
        else:
            file.write(bsk[i] + ' ')

        i+=1

    # stop writing
    file.close()
    break





