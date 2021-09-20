import sys

dict = {}
inputs = input()

while inputs != 'quit':
    
    #we first cut at the first space, if the first word is remove, it will only have two words
    first_cut = inputs.split(' ',1)
    if first_cut[0] == 'remove':
        if first_cut[1] in dict:
            del dict[first_cut[1]]
        print(dict)

        #load a new line after print the dictionary
        inputs = input()
        continue
    
    #we do a second cut, this time the command is cut to three parts
    second_cut = inputs.split(' ',2)
    if second_cut[0] == 'add':
        dict[second_cut[1]] = int(second_cut[2])
        print(dict)

        #load a new line after print the dictionary
        inputs = input()
        continue

    if second_cut[0] == 'edit':
        if second_cut[1] in dict:
            dict[second_cut[1]] = int(second_cut[2])
        print(dict)

        #load a new line after print the dictionary
        inputs = input()
        continue

#The while will end until it meets a quit, then we print a new line and exit the program
print()
sys.exit(0)    





