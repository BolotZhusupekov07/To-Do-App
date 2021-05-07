import os
import sys
from gtts import gTTS
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QListWidgetItem, QFileDialog


class UiMainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1377, 737)
        MainWindow.setStyleSheet("\n"
                                 "background-color: rgb(33, 42, 70);")
        MainWindow.setWindowIcon(QtGui.QIcon('icon.ico'))
        font_widget = QtGui.QFont()
        font_widget.setFamily("Microsoft JhengHei UI Light")
        font_widget.setPointSize(12)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI Light")
        font.setPointSize(10)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(68, 50, 321, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setStyleSheet("color: rgb(255,255,255);")
        self.lineEdit.setText("Add a task")
        self.lineEdit.setFont(font)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(50, 100, 400, 521))
        self.listWidget.setStyleSheet("color:rgb(255,255,255);")
        self.listWidget.setFont(font_widget)
        self.listWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setSpacing(3)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(410, 50, 31, 31))
        self.pushButton.setStyleSheet("background-color: rgb(91, 164, 207);\n"
                                      "color: rgb(0, 0, 0);\n"
                                      "border-radius: 15px;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.add_task)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(530, 650, 100, 30))
        self.pushButton_2.setStyleSheet("\n"
                                        "background-color: rgb(254, 174, 63);\n"
                                        "color: rgb(0, 0, 0);\n"
                                        "font: 10pt \"Ebrima\";\n"
                                        "border-radius: 7px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.done_task)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(270, 650, 100, 30))
        self.pushButton_3.clicked.connect(self.skip)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(254, 174, 63);\n"
                                        "font: 10pt \"Ebrima\";\n"
                                        "color: rgb(0, 0, 0);\n"
                                        "border-radius: 7px;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(100, 10, 121, 23))
        self.pushButton_4.setStyleSheet("background-color: rgb(123, 200, 108);\n"
                                        "color: rgb(0, 0, 0);\n"
                                        "border-style: outset;\n"
                                        "border-radius:10px;    ")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.saveAs)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(270, 10, 121, 23))
        self.pushButton_5.setStyleSheet("background-color: rgb(123, 200, 108);\n"
                                        "color: rgb(0, 0, 0);\n"
                                        " border-style: outset;\n"
                                        "border-radius:10px;    ")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.openFile)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(95, 650, 100, 30))
        self.pushButton_6.setStyleSheet("background-color: rgb(254, 174, 63);;\n"
                                        "border-right-color: rgb(0, 0, 0);\n"
                                        "color:rgb(0, 0, 0);\n"
                                        "border-top-color: rgb(0, 0, 0);\n"
                                        "font: 10pt \"Ebrima\";\n"
                                        "border-radius: 7px;\n"
                                        "")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.doing)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(510, 50, 361, 20))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setStyleSheet("color:rgb(255,255,255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(980, 60, 311, 20))
        self.label_2.setStyleSheet("color:rgb(255,255,255);")
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(720, 650, 100, 30))
        self.pushButton_7.setStyleSheet("background-color: rgb(254, 174, 63);\n"
                                        "color: rgb(0, 0, 0);\n"
                                        "\n"
                                        "font: 10pt \"Ebrima\";\n"
                                        "border-radius: 7px;")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.doItLater)
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(490, 100, 400, 521))
        self.listWidget_2.setObjectName("listWidget_2")
        self.listWidget_2.setFont(font_widget)
        self.listWidget_2.setSpacing(3)
        self.listWidget_2.setStyleSheet("color:rgb(255,255,255);")
        self.listWidget_3 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_3.setGeometry(QtCore.QRect(930, 100, 400, 521))
        self.listWidget_3.setObjectName("listWidget_3")
        self.listWidget_3.setFont(font_widget)
        self.listWidget_3.setSpacing(3)
        self.listWidget_3.setStyleSheet("color:rgb(255,255,255);")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(1065, 650, 100, 30))
        self.pushButton_8.setStyleSheet("background-color: rgb(254, 174, 63);\n"
                                        "color: rgb(0, 0, 0);\n"
                                        "\n"
                                        "font: 10pt \"Ebrima\";\n"
                                        "border-radius: 7px;")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(self.clear)
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(1200, 10, 100, 23))
        self.pushButton_9.setStyleSheet("background-color: rgb(239, 117, 100);\n"
                                        "color: rgb(255, 255, 255);\n"
                                        " border-style: outset;\n"
                                        "border-radius:10px;    ")
        self.pushButton_9.setObjectName("pushButton_5")
        self.pushButton_9.clicked.connect(self.play)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def doing(self):
        row = self.listWidget.currentRow()
        if row == -1:
            pass
        else:
            line = self.listWidget.item(row).text()
            item = QListWidgetItem(line)
            item.setTextAlignment(4)
            self.listWidget_2.addItem(item)
            self.listWidget.takeItem(row)

    def doItLater(self):
        row = self.listWidget_2.currentRow()
        if row == -1:
            pass
        else:
            line = self.listWidget_2.item(row).text()
            item = QListWidgetItem(line)
            item.setTextAlignment(4)
            self.listWidget.addItem(item)
            self.listWidget_2.takeItem(row)

    def clear(self):
        self.listWidget_3.clear()

    def openFile(self):
        self.listWidget.clear()
        file = QFileDialog.getOpenFileName()[0]
        first = False
        second = False
        third = False
        if file:
            with open(file, "r") as f:
                for line in f.readlines():
                    if line.strip() == "ToDo":
                        first = True
                    elif line.strip() == "Doing":
                        second = True
                        first = False
                    elif line.strip() == "Done":
                        third = True
                        second = False

                    if first:
                        if line.strip() == "ToDo" or line.strip() == "":
                            continue
                        item = QListWidgetItem(line.strip())
                        item.setTextAlignment(4)
                        self.listWidget.addItem(item)
                    if second:
                        if line.strip() == "Doing" or line.strip() == "":
                            continue
                        item = QListWidgetItem(line.strip())
                        item.setTextAlignment(4)
                        self.listWidget_2.addItem(item)
                    if third:
                        if line.strip() == "Done" or line.strip() == "" \
                                or line.strip() == "This is the list":
                            continue
                        item = QListWidgetItem(line.strip())
                        item.setTextAlignment(4)
                        self.listWidget_3.addItem(item)

    def saveAs(self):
        filedialog = QtWidgets.QFileDialog()
        filedialog.setDefaultSuffix("cal")
        filedialog.setNameFilter("Text Files (*.txt);; files (*.*)")
        filedialog.setAcceptMode(QtWidgets.QFileDialog.AcceptSave)
        selected = filedialog.exec()
        l = []
        if selected:
            file = filedialog.selectedFiles()[0]
        else:
            return
        if file:
            a = []
            for i in range(self.listWidget.count()):
                a.append(self.listWidget.item(i).text())
            l.append(a)
            b = []
            for i in range(self.listWidget_2.count()):
                b.append(self.listWidget_2.item(i).text())
            l.append(b)
            c = []
            for i in range(self.listWidget_3.count()):
                c.append(self.listWidget_3.item(i).text())
            l.append(c)
            s = ["Doing", "Done", "This is the list"]

            with open(file, "w") as f:
                f.write('ToDo' + '\n')
                index = 0
                for row in l:

                    for line in row:
                        f.write(line + '\n')
                    f.write('\n' + s[index] + '\n')
                    index += 1

    def add_task(self):
        line = self.lineEdit.text()
        if line == "Add a task":
            pass
        elif len(line) > 0:
            item = QListWidgetItem(line)
            item.setTextAlignment(4)

            self.listWidget.addItem(item)
            self.lineEdit.clear()
        else:
            pass

    def done_task(self):
        row = self.listWidget_2.currentRow()
        if row == -1:
            pass
        else:
            line = self.listWidget_2.item(row).text()
            item = QListWidgetItem(line)
            item.setTextAlignment(4)
            self.listWidget_3.addItem(item)
            self.listWidget_2.takeItem(row)

    def skip(self):
        row = self.listWidget.currentRow()
        if row == -1:
            pass
        else:
            self.listWidget.takeItem(row)

    def play(self):
        language = 'en'
        text_ = "Things you need to do,"

        try:
            if self.listWidget.count() == 0 and\
                    self.listWidget_2.count() == 0 and self.listWidget_3.count() == 0:
                pass
            else:

                for i in range(self.listWidget.count()):
                    text_ += self.listWidget.item(i).text() + ","
                text_ += ",Things you are doing currently, "
                for i in range(self.listWidget_2.count()):
                    text_ += self.listWidget_2.item(i).text() + ","
                text_ += ",Things you have finished, " + ","
                for i in range(self.listWidget_3.count()):
                    text_ += self.listWidget_3.item(i).text() + ","
                audio = gTTS(text=text_, lang=language, slow=True)
                audio.save('T22S.wav')
                os.system('T22S.wav')
        except AssertionError:
            pass

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Productivity", "Productivity"))
        self.listWidget.setToolTip(
            _translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.listWidget.setWhatsThis(
            _translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "+"))
        self.pushButton_2.setText(_translate("MainWindow", "Done"))
        self.pushButton_3.setText(_translate("MainWindow", "Skip"))
        self.pushButton_4.setText(_translate("MainWindow", "Save"))
        self.pushButton_5.setText(_translate("MainWindow", "Open"))
        self.pushButton_6.setText(_translate("MainWindow", "Doing"))
        self.label.setText(_translate("MainWindow", "DOING"))
        self.label_2.setText(_translate("MainWindow", "DONE"))
        self.pushButton_7.setText(_translate("MainWindow", "Do Later"))
        self.pushButton_8.setText(_translate("MainWindow", "Clear"))
        self.pushButton_9.setText(_translate("MainWindow", "Speak"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UiMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
