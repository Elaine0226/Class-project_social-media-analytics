print("This program displays info about the most popular dates in Twitter datasets.")
from load_data import *
file_name=input("Please enter the name of your data file:")
data = load_data(file_name)
print('Data loaded from file "',file_name,'".')

dates=[]
for i in data:
    dates.append(i[2].split("T")[0])
   
print("This dataset includes",len(set(dates)),"unique dates.")

import collections
topdates=[]
topdates=collections.Counter(dates).most_common(3)
print("The top three dates by tweet volume are:")
print(topdates[0][0],":")
print(topdates[0][1],"total tweets")

top1=[]
top1_link=[]
top1_link1=[]
top1_hashtag=[]
top1_hashtag1=[]
top1_user=[]
top1_user1=[]

for i in data:
    top1=i[1].split(" ")
    for j in top1:
        if '://' in j and topdates[0][0] in i[2]:
            top1_link.append(j)

    for h in top1:
        h=h.lower()
        if '#intothebadlands' != h and "#" in h and topdates[0][0] in i[2]:
            top1_hashtag.append(h)

    for k in top1:
        k=k.lower()
        if "@" in k and topdates[0][0] in i[2]:
            if k[-1] == ':':
                top1_user.append(k[:-1])
            else:
                top1_user.append(k)
            
top1_link1=collections.Counter(top1_link).most_common()
top1_hashtag1=collections.Counter(top1_hashtag).most_common()
top1_user1=collections.Counter(top1_user).most_common()
   
print("Top web link:",top1_link1[0])
print("Top hashtag:",top1_hashtag1[0])
print("Top user:",top1_user1[0])


#top 2
print(topdates[1][0],":")
print(topdates[1][1],"total tweets")


top2=[]
top2_link=[]
top2_link1=[]
top2_hashtag=[]
top2_hashtag1=[]
top2_user=[]
top2_user1=[]

for i in data:
    top2=i[1].split(" ")
    for j in top2:
        if '://' in j and topdates[1][0] in i[2]:
            top2_link.append(j)

    for h in top2:
        h=h.lower()
        if '#intothebadlands' != h and "#" in h and topdates[1][0] in i[2]:
            top2_hashtag.append(h)

    for k in top2:
        k=k.lower()
        if "@" in k and topdates[1][0] in i[2]:
            if k[-1] == ':':
                top2_user.append(k[:-1])
            else:
                top2_user.append(k)
 
top2_link1=collections.Counter(top2_link).most_common()
top2_hashtag1=collections.Counter(top2_hashtag).most_common()
top2_user1=collections.Counter(top2_user).most_common()
   
print("Top web link:",top2_link1[0])
print("Top hashtag:",top2_hashtag1[0])
print("Top user:",top2_user1[0])

#top3
print(topdates[2][0],":")
print(topdates[2][1],"total tweets")


top3=[]
top3_link=[]
top3_link1=[]
top3_hashtag=[]
top3_hashtag1=[]
top3_user=[]
top3_user1=[]

for i in data:
    top3=i[1].split(" ")
    for j in top3:
        if '://' in j and topdates[2][0] in i[2]:
            top3_link.append(j)

    for h in top3:
        h=h.lower()
        if '#intothebadlands' != h and "#" in h and topdates[2][0] in i[2]:
             top3_hashtag.append(h)

    for k in top3:
        k=k.lower()
        if "@" in k and topdates[2][0] in i[2]:
             if k[-1] == ':':
                top3_user.append(k[:-1])
             else:
                top3_user.append(k)
            
top3_link1=collections.Counter(top3_link).most_common()
top3_hashtag1=collections.Counter(top3_hashtag).most_common()
top3_user1=collections.Counter(top3_user).most_common()
   
print("Top web link:",top3_link1[0])
print("Top hashtag:",top3_hashtag1[0])
print("Top user:",top3_user1[0])


        
