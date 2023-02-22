# Import necessary libraries
import os
from collections import Counter

# Define a function to get all filenames in a directory
def get_filenames(dirname):
    filenames = []
    # Use os.walk() function to traverse all files and directories under dirname
    for root, dirs, files in os.walk(dirname):
        for file in files:
            # Split the filename and extension, and add the filename to the list of filenames
            filename, ext = os.path.splitext(file)  #file name without extension
            filenames.append(filename.lower())      #case insensitive
    return filenames


# If the script is run as the main program
if __name__ == '__main__':
    # Get the current working directory as the input directory
    dirname = os.getcwd()

    '''or you can input your own path'''
    #dirname = input('lease enter the folder path：')

    # Get all filenames in the input directory, and count their occurrences
    filenames = get_filenames(dirname)
    counter = Counter(filenames)

    # Print the filenames and their occurrence counts, sorted by count in descending order
    for filename, count in counter.most_common():
        # more than 2 occurrences should be reported
        if count >=2:
            print(f'{filename.ljust(16)}{count}')
