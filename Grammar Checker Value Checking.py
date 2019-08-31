import sys
from PyQt5.QtWidgets import QApplication,QTableWidget, QTableWidgetItem


app = QApplication(sys.argv)
table = QTableWidget()
sentenceIndivedual = ""
def countValue(sentenceList, InputSentence):
   count = 0
   for sentence in sentenceList:
       found = sentence.find(InputSentence, 0, len(sentence))
       if found != -1:
           count = count + 1
   return count

def modifySentence(sentenceList, number):
    number = number - 1
    start = ""
    end = ""
    for i in range (number):
        start += "START "
        end += " END"
    for index in range (len(sentenceList)) :
        sentenceList[index] =  start +sentenceList[index]+ end
    return sentenceList

def modifyPredict(sentence, number):
    number = number - 1
    start = ""
    end = ""
    for i in range(number):
        start += "START "
        end += " END"
    sentence = start + sentence + end
    return sentence
def nGram(sentenceList, predict, number,sentence,rows):
    test = predict.split()
    probability = 1.0
    for i in range(0, len(test)-number):
        predict_upper = test[i]
        predict_lower = test[i]
        for j in range(i+1,i+number-1):
            predict_lower += " "+test[j]
        for j in range(i+1, i+number):
            predict_upper += " "+test[j]

        print(predict_upper)
        print(predict_lower)
        upperCount = countValue(sentenceList, predict_upper)
        lowerCount = countValue(sentenceList, predict_lower)
        print(upperCount)
        print(lowerCount)
        if upperCount == 0 or lowerCount == 0:
            upperCount += 1
            lowerCount += 1
        probability *= (upperCount/lowerCount)
        print(upperCount/lowerCount)
        sentence += "P("+predict_upper+"|"+predict_lower+") = "+str(upperCount/lowerCount)+"\n";

    print(sentence)
    table.setItem(rows, 1, QTableWidgetItem(sentence))
    return probability





#file = open("C:\\Users\\osruh\\OneDrive\\Desktop\\Capston Project\\Dataset_mini-Sheet1.csv", "rb")
file = open(".\\main-dataset.txt", "rb")
#file = open("C:\\Users\\osruh\\OneDrive\\Desktop\\Capston Project\\Full data set.csv", "rb")
readFile = (file.read()).decode()
#sentenceList = readFile.split(",,,\r\n")
sentenceList = readFile.split("\r\n")
sentenceList[0] = sentenceList[0].replace("\ufeff", "")
#print("Please input number which gram do u want")
#number = input()
#number = int(number)



table.setWindowTitle("Bangla Grammar Checker")
table.setGeometry(0, 0, 1000, 800)

table.setColumnWidth(1, 2000)
table.resize(1000, 800)
table.setColumnCount(7)
table.horizontalHeader().setStyleSheet("""
QHeaderView::section {background-color: rgba(0,0,0,0.1)}
""")
table.setHorizontalHeaderItem(0, QTableWidgetItem("Sentence"))
table.setHorizontalHeaderItem(1, QTableWidgetItem("Individual Probability"))
table.setHorizontalHeaderItem(2, QTableWidgetItem("Total Probability"))
table.setHorizontalHeaderItem(3, QTableWidgetItem("Bigram"))
table.setHorizontalHeaderItem(4, QTableWidgetItem("Trigram"))
table.setHorizontalHeaderItem(5, QTableWidgetItem("Fourthgram"))
table.setHorizontalHeaderItem(6, QTableWidgetItem("Fifthgram"))


row = 0;
table.setRowCount(4)
for test in range(1):
    print("Plesae input predict Sentence")
    predict = input()
    table.setItem(test, 0, QTableWidgetItem(predict))

    for number in range(2,6):
     print("For "+str(number) + "-gram:\n")
     sentenceList = modifySentence(sentenceList,number)
     predict = modifyPredict(predict,number)
     predictValue = nGram(sentenceList, predict, number, sentenceIndivedual,row)
     print(predictValue)
     table.setItem(row, 2, QTableWidgetItem(str(predictValue)))
     if number == 2:
         table.setItem(row, 3, QTableWidgetItem(str(predictValue)))
     if number == 3:
         table.setItem(row, 4, QTableWidgetItem(str(predictValue)))
     if number == 4:
         table.setItem(row, 5, QTableWidgetItem(str(predictValue)))
     if number == 5:
         table.setItem(row, 6, QTableWidgetItem(str(predictValue)))
     row+=1

table.resizeColumnToContents(0)
table.resizeColumnToContents(1)
table.resizeColumnToContents(2)
table.resizeColumnToContents(3)
table.resizeColumnToContents(4)
table.resizeColumnToContents(5)
table.resizeColumnToContents(6)
table.setSpan(0,0,3,0)

table.resizeRowsToContents()
table.show()
sys.exit(app.exec_())




#root.mainloop()
