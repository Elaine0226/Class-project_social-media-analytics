print("This program displays info about links, hashtags, usernames, images, and vias.")
from load_data import *
file_name=input("Please enter the name of your data file:")
data = load_data(file_name)

nr=len([i for i in data if 'RT @' in i[1].upper()])



nlink = 0
rowslink = 0
for i in data:
    if 'http://' in i[1]:
        rowslink += 1
        nlink += i[1].count('http://')        
nrlink=len([i for i in data if 'http://' in i[1].lower() and "RT @" in i[1]])


nhashtag = 0
rowshashtag = 0
for i in data:
    if '#' in i[1]:
        rowshashtag += 1
        nhashtag += i[1].count('#')
nrhashtag=len([i for i in data if '#' in i[1].lower() and "RT @" in i[1]])


nusernameall = 0
rowsusername = 0
for i in data:
    if '@' in i[1]:
        rowsusername += 1
        nusernameall += i[1].count('@')

nusernameRT =0
rowsusernameRT=0
for i in data:
    if 'RT @' in i[1]:
        rowsusernameRT +=1
        nusernameRT += i[1].count('RT @')
        
nusername= nusernameall-nusernameRT

nrusername=0
for i in data:
    if 'RT @' in i[1]:
        a=0
        a+= i[1].count('@')
        if a>=2:
            nrusername+= 1


nimage = 0
rowsimage = 0
for i in data:
    if 'image' or '/photo/' in i[1]:
        rowsimage += 1
        nimage += i[1].count('image')
        nimage +=i[1].count('/photo')

nrimage=len([i for i in data if 'image' in i[1].lower() and "RT @" in i[1]])+len([i for i in data if '/photo/' in i[1].lower() and "RT @" in i[1]])


nvia = 0
rowsvia = 0
for i in data:
    if 'via @' in i[1]:
        rowsvia += 1
        nvia += i[1].count('via @')
nrvia=len([i for i in data if 'via @' in i[1].lower() and "RT @" in i[1]])



print("Total # links:",nlink,", Proportion of retweets containing link(s):",nrlink/nr)
print("Total # hashtags:",nhashtag,", Proportion of retweets containing hashtag(s):",nrhashtag/nr)
print("Total # usernames:",nusername,", Proportion of retweets containing username(s):",nrusername/nr)
print("Total # images:",nimage,", Proportion of retweets containing image(s):",nrimage/nr)
print("Total # via’s:", nvia,", Proportion of retweets containing via(s):",nrvia/nr)


