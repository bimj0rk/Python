def main():
    try:
        aFile = open('fileToRead.txt', 'r')
        fileContents = aFile.read().upper()
        bFile = open('fileToWrite.txt', 'r')
        bFile.write(fileContents)
        aFile.close()
        bFile.close()
    except FileNotFoundError:
        print("One of the files were not found.")
    
if __name__ == "__main__":
    main()