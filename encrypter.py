#Encrypter
#William Doyle

import matplotlib.image as img
import numpy as npy
import random as random

#=========================================#
#----------------FUNCTIONS----------------#
#=========================================#

#converts letter to val: a = 0... z = 25
def TSwitch(letter):
    return ((ord(letter) - 97) / 255)

#perfoms a ROT[num] shift to [message], returns encrypted message
def ROT(num, message):
    encryptedMsg = ''
    message = message.lower()
    for i in range(len(message)):
        letter = ord(list(message)[i]) - 97 + num
        if(letter > 25):
            letter -= 26
        encryptedMsg += chr(letter + 97)
    return encryptedMsg

#encrypts autokey cipher with key (REQUIRES TABULA RECTA)
def autokey(key, msg):
    encryptedMsg = ''
    for i in range(len(msg)):
        encryptedMsg += chr(table[ord(list(msg)[i])-97][ord(list(key)[i])-97]+97)
        key += msg[i]

    return encryptedMsg

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
msg = str(input('Enter your message: ')).lower()
msgArr = []
key = ''
rotMsg = ''
rotNum = 0
random.seed(int(targetImg[0][0][1] * 255 + 1))
SEED1 = random.randint(0, 999)
tempLetter = ''
index = 0
xCoord = 0
yCoord = 0

#=========================================#
#----------------MAIN---------------------#
#=========================================#

#generating ROT msg & num
for y in range(3):
    for z in range(1, 4):
        rotMsg += (tens2Letter(int((targetImg[width-1][height-1][y]) * (100 ** z))))

random.seed(SEED1)
rotNum = random.randrange(0, 25)

#performing ROT cipher
rotMsg = ROT(rotNum, rotMsg)

#performing autokey cipher
msg = autokey(rotMsg, msg)

#encrypted message conversion
for x in range(len(msg)):
    tempLetter = (bin(ord(list(msg)[x]))[2:].zfill(8))
    for y in range(8):
        msgArr.append(int(list(tempLetter)[y]))

#writing message to image
while(index < len(msgArr)):
    if(max(targetImg[xCoord][yCoord][0], targetImg[xCoord][yCoord][1], targetImg[xCoord][yCoord][2]) <= .85):
        if(msgArr[index] == 1):
            targetImg[xCoord][yCoord][3] = .999
        else:
            targetImg[xCoord][yCoord][3] = .995
        index += 1
        
    if(xCoord == width-1):
        xCoord = 0
        yCoord += 1
    else:
        xCoord += 1

#saving embedded image
img.imsave('target.png', targetImg)
