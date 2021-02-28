# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Demo of error handling and pickling in python
# ChangeLog (Who,When,What):
# Hubert Ogier,2/25/2021,Created script and complete assignment
# ---------------------------------------------------------------------------- #


##############
#Pickling demo
##############
import pickle

#Create a row of data in a dictionary
dicEmployee = {"First_Name": "Mike","Job": "Manager","Start_date": "01/19/2020"}
#This is the output before pickling
print("This is the Dictionary BEFORE serialization: ")
print(dicEmployee,"\n")
#Start serialization
pickle_fileA = open("Pickle_DumpP5.txt", "wb")
pickle_fileB = open("Pickle_DumpP2.txt", "wb")
pickle.dump(dicEmployee,pickle_fileA,5)
pickle.dump(dicEmployee,pickle_fileB,2)
pickle_fileA.close()
pickle_fileB.close()
#This is output after serialization
non_pickle_fileA = open("Pickle_DumpP5.txt","r")
non_pickle_fileB = open("Pickle_DumpP2.txt","r")
print("This is the Dictionary AFTER serialization with protocol 5: ")
print(non_pickle_fileA.readlines(),"\n")
print("This is the Dictionary AFTER serialization with protocol 2: ")
print(non_pickle_fileB.readlines(),"\n")
#Start deserialization
pickle_fileA = open ("Pickle_DumpP5.txt", "rb")
pickle_fileB = open ("Pickle_DumpP2.txt", "rb")
pickle_contentA = pickle.load(pickle_fileA)
pickle_contentB = pickle.load(pickle_fileB)
print("This is the Dictionary AFTER Deserialization of the file serialized with protocol 5: ")
print(pickle_contentA,"\n")
print("This is the Dictionary AFTER Deserialization of the file serialized with protocol 2: ")
print(pickle_contentB,"\n")
#####################
#Error handling demo#
#####################
#Starting a try statement to trap exception
try:
    # Create a FileNotFoundError as I mispell the file name
    pickle_file = open ("Pickle_DumpS.txt", "rb")
#Customize the error message
except FileNotFoundError as e:
    print("You probably mispelled the file name")
#This is what you get otherwise
    print("This is what python will return by default: ")
    print(e)
    print("This is document provided by python:")
    print(e.__doc__)
