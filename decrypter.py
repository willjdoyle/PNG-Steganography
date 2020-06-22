#Decrypter
#William Doyle

import matplotlib.image as img
import numpy as npy
import random as random

#=========================================#
#----------------FUNCTIONS----------------#
#=========================================#

#converts val to letter: 0 = a... 25 = z
def inverseTSwitch(number):
    return chr(int(number * 255 + 97))

#decrypts a ROT[num] cipher with [encryptedMsg], returns unencrypted message
def inverseROT(num, encryptedMsg):
    message = ''
    encryptedMsg = encryptedMsg.lower()
    for i in range (len(encryptedMsg)):
        letter = ord(list(encryptedMsg)[i]) - 97 + num
        if(letter < 0):
            letter += 26
        message += chr(letter + 97)
    return message

#decrypts autokey cipher with key (REQUIRES TABULA RECTA)
def inverseAutokey(key, encryptedMsg):
    msg = ''
    for i in range(len(encryptedMsg)):
        keyLetter = list(key)[i]
        row = table[:][ord(keyLetter) - 97]
        for j in range(26):
            if(row[j] == ord(encryptedMsg[i]) - 97):
                msg += chr(j + 97)
                key += chr(j + 97)

    return msg

#converts two digit number to letter
def tens2Letter(num):
    if(num > 25):
        return chr(num % 25 + 97)
    else:
        return chr(num + 97)

#=========================================#
#----------------DEFINITIONS--------------#
#=========================================#

#---------------TABULA RECTA--------------#
table = [[0 for i in range(26)] for j in range(26)]
for i in range(0, 26):
    num = i
    for j in range(0, 26):
        if((num + j) > 25):
            table[i][j] = num + j - 26
        else:
            table[i][j] = num + j

#-------------VARIABLES-------------------#
targetImg = img.imread('target.png')
width, height = targetImg.shape[:2]
msgB = ''
msg = ''
random.seed(int(targetImg[0][0][1] * 255 + 1))
SEED1 = random.randint(0, 999)
rotNum = 0
rotMsg = ''
xCoord = 0
yCoord = 0

#=========================================#
#----------------MAIN---------------------#
#=========================================#

#read encrypted msg
while(yCoord < height):
    if(int(targetImg[xCoord][yCoord][3]*1000) == 996):
        msgB += '1'
    elif(int(targetImg[xCoord][yCoord][3]*1000) == 992):
        msgB += '0'
        
    if(xCoord == width-1):
        xCoord = 0
        yCoord += 1
    else:
        xCoord += 1

#convert from binary to alpha
for x in range(int(len(msgB) / 8)):
    msg += chr(int(msgB[:8], 2))
    msgB = msgB[8:]

#generating inverseROT msg & num
for y in range(3):
    for z in range(1, 4):
        rotMsg += (tens2Letter(int((targetImg[width-1][height-1][y]) * (100 ** z))))

random.seed(SEED1)
rotNum = random.randrange(0, 25)

#performing ROT cipher
rotMsg = inverseROT(rotNum, rotMsg)

#performing inverse autokey cipher
msg = inverseAutokey(rotMsg, msg)
print(msg)
