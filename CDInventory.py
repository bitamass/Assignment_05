#-----------------------------------------------------
#Title: CDInventory.py
#Desc: Script CDInventory to store CD Inventory data
#Change Log: (who, when, what)
#Bmassoudi, 2022-Nov-05, modified file to replace inner rows with dicts, add the 'l' and 'd' functionalities
#-----------------------------------------------------

#display menu allowing the user to choose: 'Add CD', 'Display Current INventory', 'Save Inventory to File' and 'Exit'.
#Add data to the table (2D list) each time the user wants to add data.
#Display the current data to the user each time the user wants to display the data.
#Save the data to the text file CDInventory.txt if the user chooses so.
#Exit the program if the user chooses so.


#display menu allowing the user to choose: 'Add CD', 'Display Current Inventory', 'Save Inventory to File' and 'Exit'.
CDInventory= []
dicTbl=[]
ID=0
while True:
    print('----------------------------')
    print('Welcome to the CD Inventory\n\nYour Menu for tonight:')
    print('[l] load\n[d] display\n[s] save\n[a] add\n[r] remove\n[x] exit')
    menuSelection = input('Enter Your Choice: ') 

#Load the data from the file 
    if menuSelection.lower() == 'l':
        objFile=None
        lstRow=[]
        print('load')
        CDInventory.clear()
        objFile=open('CDInventory.txt', 'r')
        for row in objFile:
            lstRow=row.strip().split(',')
            dicRow ={'ID': lstRow[0],'Artist':lstRow[1], 'Album':lstRow[2] }
            CDInventory.append(lstRow)
        objFile.close()

#Display the current data to the user each time the user wants to display the data.
    elif menuSelection.lower() == 'd':
        print('Display the CD Inventory contents')
        print('\nID', 'Title', 'Artist')
        print('___ _________ ________')
        for row in CDInventory:
            print(*row.values(), sep=',')

#Remove a row in the table as designated by the user    
    elif menuSelection.lower() == 'r':
        print('//////////////////////////////////\n')
        print('you have chosen to delete a row from CD Inventory\n')
        print('ID', 'Title', 'Artist')
        for row in CDInventory:
            print(*row.values(), sep=',')
        delRow = int(input('enter row # to delete: '))
        CDInventory.pop(delRow-1)
        print('Row ', delRow,' was removed. This is your new inventory:')
        print('\nID', 'Title', 'Artist')
        print('___ _________ ________')
        for row in CDInventory:
            print(*row.values(), sep=',')
            

#Add data to the table (2D list) each time the user wants to add data.
    elif menuSelection.lower() == 'a':
        ID= ID+1
        Title = input ('what is the title of your CD? ')
        Artist = input ('what is the artist name?')
        lstRow = (ID, Title, Artist)
        dicRow={'ID': ID, 'Title': Title, 'Artist': Artist}     #dictionary row
        CDInventory.append(dicRow)                              #list of dictionaries
        print("your CD is added. Don't forget to save your work!")
        
#save the file        
    elif menuSelection.lower() == 's':
        print('save')
        objFile=open('CDInventory.txt', 'w')        #open file
        for row in CDInventory:
            lstRow =''
            for item in row.values():               #select an item in the row
                lstRow+=str(item)+','               #add the item to the row
            objFile.write(lstRow)                   #write the row to the file
        objFile.close()                             #close the file
        print('Your CD list was saved. You may safely exit now.')
                
    elif menuSelection.lower() == 'x': 
        break  
    
    else:
        print('invalid choice. try again')
    print('CDInventory')
