from load_data import *
data = load_data('data_sample.csv')#load twitter data from a csv file into python
print("This program displays summary information about Twitter data.")
input("Please enter the name of your data file: ")
key=input("Enter a keyword: ")
[i[1] for i in data if key in i[1]]
number = len([i[1] for i in data if key in i[1].lower()])#number of tweets that include the keyword that users typed in
print("The keyword",key, "is present in", number,"of", len(data)," tweets")
print("Which is ",number/len(data)*100,"% of all tweets",sep="")
answer = input("Show all keyword tweets? (y/n):")
if answer == "y":
    [print(i[1])for i in data if key in i[1].lower()]#print all the tweets that include the keyword, in separate lines
else:
    print()
    
