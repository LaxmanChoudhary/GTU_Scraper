#Working with OS packages #2

'''
The program uses the os.path class, functions realpath, split.
And object attribute __file__

The script creates a directory of name "test" at the root directory of wherever the script
is located and executed

'''
import os

if __name__ == "__main__":
    #get current python script path relative to the terminal
    full_path = os.path.realpath(__file__)
    
    #spliting the script path and script name
    path, filename = os.path.split(full_path)
    
    #Set for the new directory
    new_path = path+"/test"
    
    #try to make the directory if it doesn't exist, else throw error
    try:
        os.mkdir(new_path)
    except OSError as e:
        print("Error occured : ",e)

        #hold error
        input()