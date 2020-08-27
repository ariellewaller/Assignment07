#------------------------------------------#
# Title: CDInventory.py
# Desc: Working with classes and functions.
# Change Log: (Who, When, What)
# AWaller, 2020-August-19, Created File
# AWaller, 2020-August-19, Added cd_information function to class IO. 
# AWaller, 2020-August-19, Added add_cd function to class DataProcessor. 
# AWaller, 2020-August-19, Added delete_inventory method to class DataProcessor. 
# AWaller, 2020-August-19, Added write_file method to class FileProcessor. 
# AWaller, 2020-August-19, Added try-except error handling to write_file and
# read_file method in FileProcessor.
# AWaller, 2020-August-26, Modify the permanent data store to use binary data.
# AWaller, 2020-August-26, Add try-except error handling to cd_information method
# in class IO. 
# AWaller, 2020-August-26, Add try-except error handling for deleting a CD.
# Awaller, 2020-August-26, Change Github link. 

# Link to Github: https://github.com/ariellewaller/Assignment07

#------------------------------------------#

import pickle 

# -- DATA -- #
strChoice = '' # User input
lstTbl = []  # list of lists to hold data
dicRow = {}  # list of data row
strFileName = 'CDInventory.dat'  # data storage file (binary file)
objFile = None  # file object


# -- PROCESSING -- #
class DataProcessor:
    # TODONE: Added functions for processing here. 
    
    @staticmethod
    def add_cd(strID, strTitle, stArtist,table):
        """Add a CD to the current inventory table. 


        Args:
            strID: string that holds the CD ID.
            strTitle: string that holds the CD title.
            strArtist: string that holds the CD artist.
            table (list of dict): 2D data structure (list of dicts) that holds
            the data during runtime.

        Returns:
            table: 2D data structure (list of dicts) that holds the data
            during runtime. Modified to include the new CD. 

        """

        # 3.3.2 Add item to the table
        intID = int(strID)
        dicRow = {'ID': intID, 'Title': strTitle, 'Artist': stArtist}
        table.append(dicRow)
        return table 

    
    @staticmethod
    def delete_inventory(intIDDel, table): 
        """Deletes a CD from the current inventory table


        Args:
            intIDDel: the ID integer of the CD to be deleted 
            table (list of dict): 2D data structure (list of dicts) that holds
            the data during runtime.

        Returns:
            table (list of dict): 2D data structure (list of dicts) that holds
            the data during runtime. If intIDDel is found, this list is edited
            to remove the applicable dictionary. 

        """
        # 3.5.2 search thru table and delete CD
        intRowNr = -1
        blnCDRemoved = False
        for row in table:
            intRowNr += 1
            if row['ID'] == intIDDel:
                del table[intRowNr]
                blnCDRemoved = True
                break
        if blnCDRemoved:
            print('The CD was removed')
        else:
            print('Could not find this CD!')
        return table

class FileProcessor:
    """Processing the data to and from text file"""


    @staticmethod
    def read_file(file_name, table):
        """Function to manage data ingestion from file to a list of
        dictionaries

        Reads the data from file identified by file_name into a 2D table
        (list of dicts) table one line in the file represents one dictionary
        row in table.

        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds
            the data during runtime

        Returns:
            table (list of dict): 2D data structure (list of dicts) that holds
            the data during runtime. If intIDDel is found, this list is edited
            to remove the applicable dictionary. 
        """
        # Clear the existing data and allow to load data from file. 
        table.clear() 
        try: 
            # Open the binary data file in read mode. 
            objFile = open(file_name, 'rb')
        except IOError:
            print('File does not exist. Creating a new file...\n')
            # Create a new binary data file if it doesn't already exist.
            objFile = open(file_name, 'wb')
            # Close the file. 
            objFile.close()            
        else: 
            # Unpickle the list of dictionaries stored in the file and assign
            # this list of dictionaries back to table. 
            try:
                table = pickle.load(objFile)
            except EOFError: 
                print("Error! File is empty. You must write data to the file first.")
            # Close the file. 
            objFile.close()
            # Return the table.
            return table 
            

    @staticmethod
    def write_file(file_name, table):
        """Function to write data from the list of dictionaries to a file.
        
        Takes the data from the 2D table and represeents one dictionary row in
        the table as one line in the file. (The values of each dictionary row
        are reperesented as one line in the table)
        
        Args:
            file_name (string): name of file used to write the data to
            table (list of dict): 2D data structure (list of dicts) that holds
            the data during runtime
            table (list of dict): 2D data structure (list of dicts) that holds
            the data during runtime.
        Returns:
            None.
        
        """
        # Open the binary file in write mode and assign the file object to a variable.
        objFile = open(file_name, 'wb')
        # Pickle the list of dictionaries (table) and write it as one object to
        # the file. 
        pickle.dump(table, objFile)
        # Close the file. 
        objFile.close()



# -- PRESENTATION (Input/Output) -- #

class IO:
    """Handling Input / Output"""


    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit\n')


    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice


    @staticmethod
    def show_inventory(table):
        """Displays a CD from the current inventory table


        Args:
            table (list of dict): 2D data structure (list of dicts) that holds
            the data during runtime.

         Returns:
             None.

         """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print('{}\t{} (by:{})'.format(*row.values()))
        print('======================================')


    @staticmethod
    def cd_information():
        """Collect user input for CD information to add CD to the current
        inventory table. 
        
        Args:
            None. 

         Returns:
             strID: string that holds the new CD ID.
             strTitle: string that holds the new CD title.
             strArtist: string that holds the new CD artist.
            """
        # Prompt user for CD information. 
        # Initialize condition for while loop. 
        IDcheck = None
        while IDcheck == None:
            # Prompt user for CD ID. 
            strID = input('Enter ID: ').strip()
            try: 
                IDcheck = int(strID)
            except ValueError: 
                print('Sorry, that wasn\'t an integer. Please enter an integer.')
                # continue
        strTitle = input('What is the CD\'s title? ').strip()
        stArtist = input('What is the Artist\'s name? ').strip()
        # Return a tuple of the collected values. 
        return strID, strTitle, stArtist


# # 1. When program starts, read in the currently saved Inventory
FileProcessor.read_file(strFileName, lstTbl)

# 2. start main loop
while True:
    # 2.1 Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()
    # 3. Process menu selection
    # 3.1 process exit first
    if strChoice == 'x':
        break
    # 3.2 process load inventory
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the\
              Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. \
                          otherwise reload will be canceled')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            # Re-assign lstTbl to table returned from read_file method. 
            lstTbl = FileProcessor.read_file(strFileName, lstTbl)
            IO.show_inventory(lstTbl)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.3 process add a CD
    elif strChoice == 'a':
        # 3.3.1 Ask user for new ID, CD Title and Artist. TO-DONE: Moved IO code
        # into function.
        # # Unpack the tuple returned from the function. 
        cd_id, title, artist = IO.cd_information()
        # 3.3.2 Add CD to the table.
        # TO-DONE: Moved processing code into function.
        DataProcessor.add_cd(cd_id, title, artist, lstTbl)
        # Display the new inventory table. 
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.4 process display current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.5 process delete a CD
    elif strChoice == 'd':
        # 3.5.1 get Userinput for which CD to delete
        # 3.5.1.1 display Inventory to user
        IO.show_inventory(lstTbl)
        # 3.5.1.2 ask user which ID to remove.
        intIDDelcheck = None
        while intIDDelcheck == None:
            # Prompt user for CD ID. 
            intIDDel = input('Which ID would you like to delete? ').strip()
            try: 
                intIDDelcheck = int(intIDDel)
            except ValueError: 
                print('Sorry, that wasn\'t an integer. Please enter an integer.')
                # continue
        # 3.5.2 search thru table and delete CD.TO-DONE - Moved processing code
        # into function.
        DataProcessor.delete_inventory(intIDDelcheck, lstTbl)
        # Display the new CD inventory table.
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.6 process save inventory to file
    elif strChoice == 's':
        # 3.6.1 Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstTbl)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # 3.6.2 Process choice
        if strYesNo == 'y':
            # 3.6.2.1 save data
            # TO-DONE: Moved processing code into write_function.
            FileProcessor.write_file(strFileName, lstTbl)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    # 3.7 catch-all should not be possible, as user choice gets vetted in IO, but to be save:
    else:
        print('General Error')




