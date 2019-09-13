import aqgFunction


# Main Function
def main():
    # Create AQG object
    aqg = aqgFunction.AutomaticQuestionGenerator()

    inputTextPath = "C:/Users/DELL/Desktop/sairam_main_project/DB/db.txt"
    readFile = open(inputTextPath, 'r+')
    #readFile = open(inputTextPath, 'r+', encoding="utf8", errors = 'ignore')

    inputText = readFile.read()

    questionList = aqg.aqgParse(inputText)
    aqg.display(questionList)

    aqg.DisNormal(questionList)

    return 0


# Call Main Function
if __name__ == "__main__":
    main()

