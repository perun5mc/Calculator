import math
import re
import threading
from pynput import keyboard

from PyQt5 import QtCore, QtGui, QtWidgets

import clipboard

class Ui_Dialog(QtWidgets.QWidget):
    def setupUi(self, Dialog):
        self.setFocus()
        Dialog.setObjectName("Dialog")
        Dialog.resize(280, 280)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(280, 280))
        Dialog.setMaximumSize(QtCore.QSize(280, 280))
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(20, 20, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit.setFont(font)
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_9 = QtWidgets.QPushButton(Dialog)
        self.pushButton_9.setGeometry(QtCore.QRect(120, 120, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setAutoDefault(False)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_8 = QtWidgets.QPushButton(Dialog)
        self.pushButton_8.setGeometry(QtCore.QRect(70, 120, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setAutoDefault(False)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_7 = QtWidgets.QPushButton(Dialog)
        self.pushButton_7.setGeometry(QtCore.QRect(20, 120, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setAutoDefault(False)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_22 = QtWidgets.QPushButton(Dialog)
        self.pushButton_22.setGeometry(QtCore.QRect(120, 160, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        self.pushButton_22.setFont(font)
        self.pushButton_22.setAutoDefault(False)
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(70, 160, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setAutoDefault(False)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(20, 160, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setAutoDefault(False)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(120, 200, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setAutoDefault(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(70, 200, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_1 = QtWidgets.QPushButton(Dialog)
        self.pushButton_1.setGeometry(QtCore.QRect(20, 200, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setAutoDefault(False)
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_0 = QtWidgets.QPushButton(Dialog)
        self.pushButton_0.setGeometry(QtCore.QRect(20, 240, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        self.pushButton_0.setFont(font)
        self.pushButton_0.setAutoDefault(False)
        self.pushButton_0.setObjectName("pushButton_0")
        self.pushButton_dot = QtWidgets.QPushButton(Dialog)
        self.pushButton_dot.setGeometry(QtCore.QRect(120, 240, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        self.pushButton_dot.setFont(font)
        self.pushButton_dot.setAutoDefault(False)
        self.pushButton_dot.setObjectName("pushButton_dot")
        self.pushButton_div = QtWidgets.QPushButton(Dialog)
        self.pushButton_div.setGeometry(QtCore.QRect(170, 120, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        self.pushButton_div.setFont(font)
        self.pushButton_div.setAutoDefault(False)
        self.pushButton_div.setObjectName("pushButton_div")
        self.pushButton_mult = QtWidgets.QPushButton(Dialog)
        self.pushButton_mult.setGeometry(QtCore.QRect(170, 160, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        self.pushButton_mult.setFont(font)
        self.pushButton_mult.setAutoDefault(False)
        self.pushButton_mult.setObjectName("pushButton_mult")
        self.pushButton_sub = QtWidgets.QPushButton(Dialog)
        self.pushButton_sub.setGeometry(QtCore.QRect(170, 200, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        self.pushButton_sub.setFont(font)
        self.pushButton_sub.setAutoDefault(False)
        self.pushButton_sub.setObjectName("pushButton_sub")
        self.pushButton_add = QtWidgets.QPushButton(Dialog)
        self.pushButton_add.setGeometry(QtCore.QRect(170, 240, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        self.pushButton_add.setFont(font)
        self.pushButton_add.setAutoDefault(False)
        self.pushButton_add.setObjectName("pushButton_add")
        self.pushButton_equal = QtWidgets.QPushButton(Dialog)
        self.pushButton_equal.setGeometry(QtCore.QRect(220, 200, 41, 71))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        self.pushButton_equal.setFont(font)
        self.pushButton_equal.setAutoDefault(False)
        self.pushButton_equal.setObjectName("pushButton_equal")
        self.pushButton_sqrt = QtWidgets.QPushButton(Dialog)
        self.pushButton_sqrt.setGeometry(QtCore.QRect(220, 160, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        self.pushButton_sqrt.setFont(font)
        self.pushButton_sqrt.setAutoDefault(False)
        self.pushButton_sqrt.setObjectName("pushButton_sqrt")
        self.pushButton_factor = QtWidgets.QPushButton(Dialog)
        self.pushButton_factor.setGeometry(QtCore.QRect(220, 120, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        self.pushButton_factor.setFont(font)
        self.pushButton_factor.setAutoDefault(False)
        self.pushButton_factor.setObjectName("pushButton_factor")
        self.pushButton_back = QtWidgets.QPushButton(Dialog)
        self.pushButton_back.setGeometry(QtCore.QRect(20, 80, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Onyx")
        font.setPointSize(20)
        self.pushButton_back.setFont(font)
        self.pushButton_back.setAutoDefault(False)
        self.pushButton_back.setObjectName("pushButton_back")
        self.pushButton_ML = QtWidgets.QPushButton(Dialog)
        self.pushButton_ML.setGeometry(QtCore.QRect(120, 80, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        self.pushButton_ML.setFont(font)
        self.pushButton_ML.setAutoDefault(False)
        self.pushButton_ML.setObjectName("pushButton_ML")
        self.pushButton_MR = QtWidgets.QPushButton(Dialog)
        self.pushButton_MR.setGeometry(QtCore.QRect(170, 80, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        self.pushButton_MR.setFont(font)
        self.pushButton_MR.setAutoDefault(False)
        self.pushButton_MR.setObjectName("pushButton_MR")
        self.pushButton_clear = QtWidgets.QPushButton(Dialog)
        self.pushButton_clear.setGeometry(QtCore.QRect(70, 80, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        self.pushButton_clear.setFont(font)
        self.pushButton_clear.setAutoDefault(False)
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.pushButton_percent = QtWidgets.QPushButton(Dialog)
        self.pushButton_percent.setGeometry(QtCore.QRect(220, 80, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        self.pushButton_percent.setFont(font)
        self.pushButton_percent.setAutoDefault(False)
        self.pushButton_percent.setObjectName("pushButton_percent")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(170, 0, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.defaultValues()

        self.pushButton_1.clicked.connect(lambda: self.addNum(1))
        self.pushButton_2.clicked.connect(lambda: self.addNum(2))
        self.pushButton_3.clicked.connect(lambda: self.addNum(3))
        self.pushButton_6.clicked.connect(lambda: self.addNum(4))
        self.pushButton_5.clicked.connect(lambda: self.addNum(5))
        self.pushButton_22.clicked.connect(lambda: self.addNum(6))
        self.pushButton_7.clicked.connect(lambda: self.addNum(7))
        self.pushButton_8.clicked.connect(lambda: self.addNum(8))
        self.pushButton_9.clicked.connect(lambda: self.addNum(9))
        self.pushButton_0.clicked.connect(lambda: self.addNum(0))

        self.pushButton_add.clicked.connect(lambda: self.addMark("+", " ", " "))
        self.pushButton_sub.clicked.connect(lambda: self.addMark("-", " ", " "))
        self.pushButton_div.clicked.connect(lambda: self.addMark("/", " ", " "))
        self.pushButton_mult.clicked.connect(lambda: self.addMark("*", " ", " "))
        self.pushButton_factor.clicked.connect(lambda: self.addMark("^", "", "("))
        self.pushButton_percent.clicked.connect(lambda: self.addMark("%", "", ""))

        self.pushButton_ML.clicked.connect(lambda: self.addSymbol("(", "", ""))
        self.pushButton_MR.clicked.connect(lambda: self.addSymbol(")", "", ""))
        self.pushButton_sqrt.clicked.connect(lambda: self.addSymbol("√", "", "("))

        self.pushButton_dot.clicked.connect(self.addDot)

        self.pushButton_equal.clicked.connect(self.calculate)

        self.lineEdit.textChanged.connect(self.updateText)

        # ​, ‌

        # self.lineEdit.textChanged.connect(self.changeText)

        self.pushButton_clear.clicked.connect(self.clear)
        self.pushButton_back.clicked.connect(self.backSpace)

        t = threading.Thread(target=self.keys)
        t.daemon = True
        t.start()

    def keys(self):
        def on_press(key):
            if self.isActiveWindow():
                if str(key).replace("'", "") == "\\x16":
                    separators = ["+", "-", "/", "*"]
                    allowed = ["+", "-", "/", "*", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "%", "(", ")", "^", "√", "."]
                    text = clipboard.paste()
                    text = text.replace(",", ".")
                    print(text)

                    for j in range(0, len(text)):
                        curChar = text[j]
                        if not allowed.__contains__(curChar):
                            text = text.replace(curChar, " ")
                    text = text.replace(" ", "")
                    print(text)

                    splitText = re.split("([+/\-*])", text)
                    newText = ""
                    print(splitText)

                    for i in range(0, len(splitText)):
                        if separators.__contains__(splitText[i]):
                            newText = str(newText) + " " + str(splitText[i]) + " "
                        else:
                            newText = str(newText) + str(splitText[i])
                    print(newText)
                    self.lineEdit.setText(self.lineEdit.text() + newText)
                else:
                    self.keyboardInput(key)
        listener = keyboard.Listener(on_press=on_press)
        listener.start()

    def keyboardInput(self, key1):
        key1 = (str(key1).lower().replace("'", "").replace("s", "√"))
        if self.basicNums.__contains__(key1):
            self.addNum(key1)
        elif self.basicMarks.__contains__(key1):
            self.addMark(str(key1), " ", " ")
        elif self.basicSymbols.__contains__(key1):
            self.addSymbol(str(key1), "", "")
        else:
            if key1 == "^":
                self.addMark("^", "", "(")
            if key1 == "%":
                self.addMark("%", "", "")
            if key1 == "√":
                self.addSymbol("√", "", "(")
            if key1 == "=" or key1 == "key.enter":
                self.calculate()
            if key1 == ".":
                self.addDot()
            if key1 == "key.back√pace":
                self.backSpace()
            if key1 == "c":
                self.clear()


    def updateText(self):
        self.label.setHidden(True)

        splitText = re.split("([+/\-*])", self.lineEdit.text())
        # text = self.lineEdit.text()
        # text = text.replace(" ", "")
        # splitText2 = re.split("([+/\-*\^\(\)])", text)
        # print(splitText2)
        if str(splitText[len(splitText) - 1]).__contains__("."):
            self.dotsCount = 1
        else:
            self.dotsCount = 0

    def calculate(self):
        lastChar = self.lineEdit.text()[len(self.lineEdit.text()) - 1:]

        if lastChar == "" or lastChar == "(" or lastChar == " ":
            self.addNum(0)

        equation = self.lineEdit.text()

        MLcount = 0
        MRcount = 0
        for i in range(0, len(equation)):

            curChar = equation[i]
            if curChar == "(":
                MLcount += 1
            if curChar == ")":
                if MLcount > 0:
                    MLcount -= 1
                else:
                    MRcount += 1
        for i in range(0, MLcount):
            equation += ")"

        for i in range(0, MRcount):
            equation = "(" + equation

        self.lineEdit.setText(equation)

        equation = equation.replace(" ", "")
        #splitText2 = re.split("([+/\-*\^\(\)])", equation)
        splitText2 = re.split("([+/\-*\^\(])", equation)
        newText = ""

        for i in range(0, len(splitText2)):
            if str(splitText2[i]).__contains__("%"):
                newText = newText + "(" + str(splitText2[i]) + ")"
            else:
                newText = newText + str(splitText2[i])

        self.equation = newText
        self.equation = self.equation.replace("%", "*0.01")
        self.equation = self.equation.replace("√", "math.sqrt")
        self.equation = self.equation.replace("^", "**")

        try:
            self.ans = float(eval(self.equation))
            self.ans = round(self.ans, 11)
            if self.ans % 1 == 0:
                self.dotsCount = 0
            else:
                self.dotsCount = 1
            # print(self.ans)
            self.lineEdit.setText(str(self.ans))
            self.label.setHidden(True)
        except:
            self.label.setHidden(False)

    def backSpace(self):
        lastChar = self.lineEdit.text()[len(self.lineEdit.text()) - 1:]
        lastChar2 = (self.lineEdit.text()[len(self.lineEdit.text()) - 2: len(self.lineEdit.text()) - 1])
        if lastChar == "(":
            if lastChar2 == "√" or lastChar2 == "^":
                self.lineEdit.setText(str(str(self.lineEdit.text()).strip())[:-1])

        if self.basicMarks.__contains__(lastChar2):
            self.lineEdit.setText(str(str(self.lineEdit.text()).strip())[:-1].strip())
        else:
            self.lineEdit.setText(str(str(self.lineEdit.text()).strip())[:-1])

    def clear(self):
        self.lineEdit.setText("")
        self.dotsCount = 0

    def addDot(self):
        prevChar = self.lineEdit.text()[len(self.lineEdit.text()) - 1:]
        #print(self.dotsCount)

        if(self.dotsCount < 1):
            if self.nums.__contains__(prevChar):
                self.lineEdit.setText(str(self.lineEdit.text()) + str("."))
            else:
                self.addNum(0)
                self.lineEdit.setText(str(self.lineEdit.text()) + str("."))
            self.dotsCount = self.dotsCount + 1

    def addSymbol(self, symbol, prefix, suffix):
        prevChar = self.lineEdit.text()[len(self.lineEdit.text()) - 1:]
        #print("prevChar: " + str(prevChar))

        if symbol == ")":
            if prevChar == " " or prevChar == "" or prevChar == "(":
                self.lineEdit.setText(str(self.lineEdit.text()) + "0")

        if prevChar == ".":
            self.lineEdit.setText(str(self.lineEdit.text()) + "0")

        prevChar = self.lineEdit.text()[len(self.lineEdit.text()) - 1:]

        if symbol == "(" or symbol == "√":
            if self.nums2.__contains__(prevChar):
                self.addMark("*", " ", " ")
        self.lineEdit.setText(str(self.lineEdit.text()) + str(prefix) + str(symbol) + str(suffix))

    def addMark(self, symbol, prefix, suffix):
        prevChar = self.lineEdit.text()[len(self.lineEdit.text()) - 1:]
        self.dotsCount = 0

        if prevChar == "." or prevChar == "(":
            self.lineEdit.setText(str(self.lineEdit.text()) + "0")

        prevChar = self.lineEdit.text()[len(self.lineEdit.text()) - 1:]

        if prevChar == "":
            if symbol == "%":
                self.lineEdit.setText("1")
            else:
                self.lineEdit.setText("0")

        if prevChar == " ":
            self.backSpace()
            self.lineEdit.setText(str(self.lineEdit.text()) + str(prefix) + str(symbol) + str(suffix))
        else:
            self.lineEdit.setText(str(self.lineEdit.text()) + str(prefix) + str(symbol) + str(suffix))

    def addNum(self, num):
        lastChar = self.lineEdit.text()[len(self.lineEdit.text()) - 1:]

        if lastChar == ")" or lastChar == "%":
            self.addSymbol("*", " ", " ")
        if lastChar == "^" or lastChar == "√":
            self.addSymbol("(", "", "")
        self.lineEdit.setText(str(self.lineEdit.text()) + str(num))

    def defaultValues(self):
        self.nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "%"]
        self.nums2 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "%", ")"]
        self.basicNums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        self.basicMarks = ["+", "-", "/", "*"]
        self.basicSymbols = ["(", ")"]

        self.lineEdit.setText("")
        self.label.setHidden(True)
        self.label.setStyleSheet('color: red')
        self.label.setText("Error.")

        self.dotsCount = 0

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Calculator"))
        self.lineEdit.setText(_translate("Dialog", ""))
        self.pushButton_9.setText(_translate("Dialog", "9"))
        self.pushButton_8.setText(_translate("Dialog", "8"))
        self.pushButton_7.setText(_translate("Dialog", "7"))
        self.pushButton_22.setText(_translate("Dialog", "6"))
        self.pushButton_5.setText(_translate("Dialog", "5"))
        self.pushButton_6.setText(_translate("Dialog", "4"))
        self.pushButton_3.setText(_translate("Dialog", "3"))
        self.pushButton_2.setText(_translate("Dialog", "2"))
        self.pushButton_1.setText(_translate("Dialog", "1"))
        self.pushButton_0.setText(_translate("Dialog", "0"))
        self.pushButton_dot.setText(_translate("Dialog", ","))
        self.pushButton_div.setText(_translate("Dialog", "/"))
        self.pushButton_mult.setText(_translate("Dialog", "*"))
        self.pushButton_sub.setText(_translate("Dialog", "-"))
        self.pushButton_add.setText(_translate("Dialog", "+"))
        self.pushButton_equal.setText(_translate("Dialog", "="))
        self.pushButton_sqrt.setText(_translate("Dialog", "√"))
        self.pushButton_factor.setText(_translate("Dialog", "xʸ"))
        self.pushButton_back.setText(_translate("Dialog", "↩"))
        self.pushButton_ML.setText(_translate("Dialog", "("))
        self.pushButton_MR.setText(_translate("Dialog", ")"))
        self.pushButton_clear.setText(_translate("Dialog", "C"))
        self.pushButton_percent.setText(_translate("Dialog", "%"))
        self.label.setText(_translate("Dialog", "Invalid input!"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Dialog()
    ui.setupUi(ui)
    ui.show()
    sys.exit(app.exec_())