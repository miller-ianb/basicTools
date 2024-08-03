import os


# Function to copy string to clipboard
def copyToClipBoard(text):
    command = 'echo ' + text.strip() + '| clip'
    os.system(command)


# Function to remove empty lines
def removeEmptyLines(text):
    lines = text.split('\n')
    cleanedLines = [line for line in lines if line.strip()]
    cleanedText = ' '.join(cleanedLines)
    return cleanedText


# Collect multi-line input from the user
while True:
    print('Enter Text (ENTER two-empty lines to input): ')
    userInput = []
    emptyLineCount = 0
    while True:
        line = input()
        if line == '':
            emptyLineCount += 1
        else:
            emptyLineCount = 0
        if emptyLineCount == 2:
            break
        userInput.append(line)
    inputText = '\n'.join(userInput)

    # Process the text, copy to clipboard, and print the result
    cleanedText = removeEmptyLines(inputText)
    copyToClipBoard(cleanedText)
    print(cleanedText)
    print('')

    reLoop = input('Type ENTER to continue, or QUIT to stop: ')
    print('')
    if reLoop != '':
        break
