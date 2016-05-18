import os
import shutil
# This script takes all the tif/xml files in a given directory and copies them into folders so that the total file size of each folder is less than 2 GB.
# Once all the tif/xml files have been copied to folders, the script then compresses the folders into zip files to be ingested into the digital archive.
# To use the script, simply put in the directory pathway in single quotations in the line below i.e. dir='PATH'. Then run the script in IDLE.
dir='H:\Digitization_Projects\Air_Photos\AirPhotos_1950_Hamilton\Code_Test\NEW_CODE_TEST' #Change this to the appropriate directory location where the photos are that you want to compress.
os.chdir(dir) #changes the directory to the above - where the script should look for the tif/xml files.
f=0 #this value will count file sizes
fzip=[] #this array will contain all files to be moved to a folder
xml=[] #this array will contain all the xml files in the directory
tif=[] #this array will contain all the tif files in the directory
for files in os.listdir(dir): #Look through every file in the given directory
    if files[-3:] == 'tif': #If the file extension is tif
        tif.append(files) #Add that file to the tif array
    elif files[-3:] == 'xml': #If the file extension is xml
        xml.append(files) #Add the file to the xml array
folder=[] #Creates an empty array for the files to be copied into a folder.
counter=0 #Counter acts as a check for the variable 't'. This allows us to fix an issue in an earlier version where, if a file would have pushed the folder file size over 2 GB, it would have been skipped over. Now that file is added to the next new folder.
endFlag=0 #sets a flag to end the looping
while (endFlag < 1): #At the beginning this is true so the loop goes through
    t=tif[counter] #The variable 't' is the nth position in the tif array where n is the counter number i.e. starting at the first tif file in the array
    findFlag=0 #another flag when looking for the matching xml file to the current tif file
    findcounter=0 #another counter to keep track of files.
    for x in xml: #loop through every xml file in the xml array
        findcounter=findcounter+1 #tick the counter 1 
        if t[:-4]==x[:-4]: #if the current tif file being looked at matches the xml file
            findFlag=1 #sets the findFlag to 1 which will be important later for the warning message
            folder.append(t) #make a copy of the current tif file in the new folder array
            folder.append(x) #make a copy of the matching xml file in the new folder array
            y=os.path.getsize(t) #calculate the file size of the tif file
            y=y+os.path.getsize(x) #add the file size of the xml file
            f=f+y #compute the cumulative file size
            if f<2.14e9: #the maximum file size allowed, just under 2 GB; if the current cumulative file size is less than the threshold then continue
                    folderName=folder[0] #name the folder after the first entry in the array
                    folderName=folderName[:-4] #this ignores the extension in the folder name
                    try:
                        os.makedirs(folderName) #made the out directory the current Dir to create folders
                    except OSError:
                        if os.path.exists(folderName): #do not create if it already exists
                            pass
                        else:
                            raise
                    shutil.copy(t, folderName) #makes the copy of the tif file in the new folder
                    shutil.copy(x, folderName) #makes the copy of the xml file in the new folder
                    counter=counter+1 #tick the counter by 1, this is important as it keeps track of the progress of the loop essentially.
                    if counter>=len(tif): #once the counter is past the maximum index of the tif array i.e. it has reached the last tif file
                        endFlag=1 #stops the loop as there are no more tif files
            elif f >=2.14e9: # if the cumulative file size is greater than 2 GB
                    f=0 #once the file size is met clear the file size tally
                    folder=[] #clear the folder array and begin a new one	
        else: 
            if findcounter>=len(xml) and findFlag < 1: #This says that if the loop has gone through the entire xml array and found no match
                print "No xml file found for " , t #prints an error message that there is no match
                counter=counter+1 #this continues ticking the counter so that the process doesn't stop if there is an error
                if counter>=len(tif):
                    endFlag=1
for item in os.listdir(dir): #Selects all folders in the directory
    if item[-3:]!='tif' and item[-3:]!='xml' and item[-3:]!='zip' and item[-2:]!='py':
        print item #this prints the folder we are going through to give us an idea of how much progress we've made
        shutil.make_archive(item, 'zip', item) #zips each folder to the location desired
