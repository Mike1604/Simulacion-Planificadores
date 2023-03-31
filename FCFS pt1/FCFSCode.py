from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5 import QtTest
from PyQt5.QtCore import Qt
import random    

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1098, 770)
        MainWindow.setStyleSheet("background-color: #2C3333;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1081, 751))
        self.stackedWidget.setObjectName("stackedWidget")
        self.Principal = QtWidgets.QWidget()
        self.Principal.setObjectName("Principal")
        self.frame = QtWidgets.QFrame(self.Principal)
        self.frame.setGeometry(QtCore.QRect(10, 0, 1071, 751))
        self.frame.setStyleSheet("border :3px solid #A5C9CA;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(690, 350, 161, 61))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    font: 63 16pt \"Bahnschrift SemiBold SemiConden\";\n"
"    color: #E7F6F2;\n"
"    border :3px solid #2C3333;\n"
"    background-color: #395B64;\n"
"    border-radius: 10;\n"
"    \n"
"}\n"
"QPushButton:hover{\n"
"    font: 63 16pt \"Bahnschrift SemiBold SemiConden\";\n"
"    color: #E7F6F2;\n"
"    border :3px solid #2C3333;\n"
"    background-color: #A5C9CA;\n"
"    border-radius: 10;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.spinBox = QtWidgets.QSpinBox(self.frame)
        self.spinBox.setGeometry(QtCore.QRect(510, 340, 161, 71))
        self.spinBox.setStyleSheet("font: 63 30pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: #A5C9CA;\n"
"color: #2C3333;\n"
"border-radius: 5;")
        self.spinBox.setObjectName("spinBox")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(180, 330, 311, 81))
        self.label_2.setStyleSheet("font: 63 30pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: #E7F6F2;\n"
"border :3px solid #2C3333;")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(360, 190, 401, 61))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(32)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 63 32pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: #E7F6F2;\n"
"border :3px solid #2C3333;")
        self.label.setObjectName("label")
        self.stackedWidget.addWidget(self.Principal)
        self.Lotes = QtWidgets.QWidget()
        self.Lotes.setObjectName("Lotes")
        self.label_9 = QtWidgets.QLabel(self.Lotes)
        self.label_9.setGeometry(QtCore.QRect(410, 10, 311, 61))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("font: 63 26pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: #E7F6F2;")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.Lotes)
        self.label_10.setGeometry(QtCore.QRect(90, 60, 151, 51))
        self.label_10.setStyleSheet("font: 63 16pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: #E7F6F2;")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.Lotes)
        self.label_11.setGeometry(QtCore.QRect(260, 70, 51, 41))
        self.label_11.setStyleSheet("font: 63 25pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: #A5C9CA;\n"
"color: #2C3333;;\n"
"border-radius: 5;")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.tableWidget = QtWidgets.QTableWidget(self.Lotes)
        self.tableWidget.setGeometry(QtCore.QRect(80, 200, 241, 321))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("QHeaderView::section{\n"
"    padding: 5px;\n"
"    background-color: #A5C9CA;\n"
"    border: .5px solid #395B64;\n"
"    font: 87 13pt \"Arial Black\";\n"
"    color: #2C3333;\n"
"\n"
"}\n"
"QTableWidget{\n"
"    border: .5px solid #395B64;\n"
"}\n"
"QTableWidget::Item {\n"
"    font: 87 13pt \"Arial Black\";\n"
"    color: #E7F6F2;\n"
"    border:  .3px solid #395B64;\n"
"    background-color: 2C3333;\n"
"}\n"
"\n"
"")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(65)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.label_12 = QtWidgets.QLabel(self.Lotes)
        self.label_12.setGeometry(QtCore.QRect(170, 140, 51, 51))
        self.label_12.setStyleSheet("font: 63 16pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: #E7F6F2;")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.Lotes)
        self.label_13.setGeometry(QtCore.QRect(70, 610, 151, 51))
        self.label_13.setStyleSheet("font: 63 16pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: #E7F6F2;")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.Lotes)
        self.label_14.setGeometry(QtCore.QRect(250, 620, 51, 41))
        self.label_14.setStyleSheet("font: 63 25pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: #A5C9CA;\n"
"color: #2C3333;;\n"
"border-radius: 5;")
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.Lotes)
        self.tableWidget_2.setGeometry(QtCore.QRect(390, 200, 261, 191))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.tableWidget_2.setFont(font)
        self.tableWidget_2.setStyleSheet("QHeaderView::section{\n"
"    padding: 5px;\n"
"    background-color: #A5C9CA;\n"
"    border: .5px solid #395B64;\n"
"    font: 87 10pt \"Arial Black\";\n"
"    color: #2C3333;\n"
"\n"
"}\n"
"QTableWidget{\n"
"    border: .5px solid #395B64;\n"
"}\n"
"QTableWidget::Item {\n"
"    font: 87 13pt \"Arial Black\";\n"
"    color: #E7F6F2;\n"
"    border:  .3px solid #395B64;\n"
"    background-color: 2C3333;\n"
"}\n"
"")
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(4, item)
        self.tableWidget_2.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_2.horizontalHeader().setHighlightSections(True)
        self.tableWidget_2.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget_2.verticalHeader().setHighlightSections(False)
        self.tableWidget_2.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget_2.verticalHeader().setStretchLastSection(True)
        self.label_15 = QtWidgets.QLabel(self.Lotes)
        self.label_15.setGeometry(QtCore.QRect(440, 130, 181, 51))
        self.label_15.setStyleSheet("font: 63 16pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: #E7F6F2;")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.Lotes)
        self.label_16.setGeometry(QtCore.QRect(820, 70, 181, 51))
        self.label_16.setStyleSheet("font: 63 16pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: #E7F6F2;")
        self.label_16.setObjectName("label_16")
        self.pushButton_3 = QtWidgets.QPushButton(self.Lotes)
        self.pushButton_3.setGeometry(QtCore.QRect(420, 410, 161, 61))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"    font: 63 16pt \"Bahnschrift SemiBold SemiConden\";\n"
"    color: #E7F6F2;\n"
"    border :3px solid #2C3333;\n"
"    background-color: #395B64;\n"
"    border-radius: 10;\n"
"    \n"
"}\n"
"QPushButton:hover{\n"
"    font: 63 16pt \"Bahnschrift SemiBold SemiConden\";\n"
"    color: #E7F6F2;\n"
"    border :3px solid #2C3333;\n"
"    background-color: #A5C9CA;\n"
"    border-radius: 10;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.tableWidget_4 = QtWidgets.QTableWidget(self.Lotes)
        self.tableWidget_4.setGeometry(QtCore.QRect(700, 140, 371, 451))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.tableWidget_4.setFont(font)
        self.tableWidget_4.setStyleSheet("QHeaderView::section{\n"
"    padding: 5px;\n"
"    background-color: #A5C9CA;\n"
"    border: .5px solid #395B64;\n"
"    font: 87 13pt \"Arial Black\";\n"
"    color: #2C3333;\n"
"\n"
"}\n"
"QTableWidget{\n"
"    border: .5px solid #395B64;\n"
"}\n"
"QTableWidget::Item {\n"
"    font: 87 13pt \"Arial Black\";\n"
"    color: #E7F6F2;\n"
"    border:  .3px solid #395B64;\n"
"    background-color: 2C3333;\n"
"}\n"
"")
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(3)
        self.tableWidget_4.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, item)
        self.tableWidget_4.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_4.horizontalHeader().setDefaultSectionSize(65)
        self.tableWidget_4.horizontalHeader().setHighlightSections(True)
        self.tableWidget_4.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget_4.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_4.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_4.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget_4.verticalHeader().setMinimumSectionSize(25)
        self.tableWidget_3 = QtWidgets.QTableWidget(self.Lotes)
        self.tableWidget_3.setGeometry(QtCore.QRect(390, 550, 261, 191))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.tableWidget_3.setFont(font)
        self.tableWidget_3.setStyleSheet("QHeaderView::section{\n"
"    padding: 5px;\n"
"    background-color: #A5C9CA;\n"
"    border: .5px solid #395B64;\n"
"    font: 87 10pt \"Arial Black\";\n"
"    color: #2C3333;\n"
"\n"
"}\n"
"QTableWidget{\n"
"    border: .5px solid #395B64;\n"
"}\n"
"QTableWidget::Item {\n"
"    font: 87 13pt \"Arial Black\";\n"
"    color: #E7F6F2;\n"
"    border:  .3px solid #395B64;\n"
"    background-color: 2C3333;\n"
"}\n"
"")
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(2)
        self.tableWidget_3.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        self.tableWidget_3.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_3.horizontalHeader().setHighlightSections(True)
        self.tableWidget_3.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget_3.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_3.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget_3.verticalHeader().setHighlightSections(False)
        self.tableWidget_3.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget_3.verticalHeader().setStretchLastSection(True)
        self.label_18 = QtWidgets.QLabel(self.Lotes)
        self.label_18.setGeometry(QtCore.QRect(430, 490, 181, 51))
        self.label_18.setStyleSheet("font: 63 16pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: #E7F6F2;")
        self.label_18.setObjectName("label_18")
        self.pushButton_4 = QtWidgets.QPushButton(self.Lotes)
        self.pushButton_4.setGeometry(QtCore.QRect(820, 660, 161, 61))
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"    font: 63 16pt \"Bahnschrift SemiBold SemiConden\";\n"
"    color: #E7F6F2;\n"
"    border :3px solid #2C3333;\n"
"    background-color: #395B64;\n"
"    border-radius: 10;\n"
"    \n"
"}\n"
"QPushButton:hover{\n"
"    font: 63 16pt \"Bahnschrift SemiBold SemiConden\";\n"
"    color: #E7F6F2;\n"
"    border :3px solid #2C3333;\n"
"    background-color: #A5C9CA;\n"
"    border-radius: 10;\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.stackedWidget.addWidget(self.Lotes)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label_17 = QtWidgets.QLabel(self.page)
        self.label_17.setGeometry(QtCore.QRect(460, 20, 121, 61))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("font: 63 26pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: #E7F6F2;")
        self.label_17.setObjectName("label_17")
        self.tableWidget_6 = QtWidgets.QTableWidget(self.page)
        self.tableWidget_6.setGeometry(QtCore.QRect(20, 90, 1061, 651))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.tableWidget_6.setFont(font)
        self.tableWidget_6.setStyleSheet("QHeaderView::section{\n"
"    padding: 5px;\n"
"    background-color: #A5C9CA;\n"
"    border: .5px solid #395B64;\n"
"    font: 87 10pt \"Arial Black\";\n"
"    color: #2C3333;\n"
"\n"
"}\n"
"QTableWidget{\n"
"    border: .5px solid #395B64;\n"
"}\n"
"QTableWidget::Item {\n"
"    font: 87 13pt \"Arial Black\";\n"
"    color: #E7F6F2;\n"
"    border:  .3px solid #395B64;\n"
"    background-color: 2C3333;\n"
"}\n"
"")
        self.tableWidget_6.setObjectName("tableWidget_6")
        self.tableWidget_6.setColumnCount(10)
        self.tableWidget_6.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(9, item)
        self.tableWidget_6.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_6.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget_6.horizontalHeader().setHighlightSections(True)
        self.tableWidget_6.horizontalHeader().setMinimumSectionSize(39)
        self.tableWidget_6.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget_6.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_6.verticalHeader().setVisible(False)
        self.tableWidget_6.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_6.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget_6.verticalHeader().setHighlightSections(True)
        self.tableWidget_6.verticalHeader().setMinimumSectionSize(25)
        self.tableWidget_6.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget_6.verticalHeader().setStretchLastSection(False)
        self.pushButton_5 = QtWidgets.QPushButton(self.page)
        self.pushButton_5.setGeometry(QtCore.QRect(810, 20, 191, 61))
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"    font: 63 16pt \"Bahnschrift SemiBold SemiConden\";\n"
"    color: #E7F6F2;\n"
"    border :3px solid #2C3333;\n"
"    background-color: #395B64;\n"
"    border-radius: 10;\n"
"    \n"
"}\n"
"QPushButton:hover{\n"
"    font: 63 16pt \"Bahnschrift SemiBold SemiConden\";\n"
"    color: #E7F6F2;\n"
"    border :3px solid #2C3333;\n"
"    background-color: #A5C9CA;\n"
"    border-radius: 10;\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.stackedWidget.addWidget(self.page)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        
        """
        Inician instrucciones
        """
        self.pushButton_2.clicked.connect(lambda: self.numProcesos())
        self.tg=0;
        self.FPausa=False;
        self.FInterrupcion=False;
        self.FError=False;
        self.procesos = [];
        self.active=False;
        
        self.pushButton_3.clicked.connect(lambda: self.comenzar());
        MainWindow.keyPressEvent = self.keyPressEvent
        self.tableWidget.keyPressEvent = self.keyPressEvent
        self.pushButton_4.clicked.connect(lambda: self.showTimes());
        self.pushButton_5.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Lotes));
        
        
        

    def numProcesos(self):
        self.numProc = int(self.spinBox.text())
        if self.numProc == 0:
            self.msgError("No valido", "El numero de procesos debe ser mayor a 0");
        else:
            #Validaciones
            for i in range(self.numProc):
                Id = i+1;
                op1 = random.randint(1,1000);
                op2 = random.randint(1,1000);
                oper = random.randint(1,5);
                tiEs = random.randint(5, 16)
                if(oper==1):
                    operacion = "+"
                    res = int(op1) + int(op2);
                elif(oper==2):
                    operacion = "-"
                    res = int(op1) - int(op2);
                elif(oper==3):
                    operacion = "*"
                    res = int(op1) * int(op2);
                elif(oper==4):
                    operacion = "/"
                    res = int(op1) / int(op2);
                elif(oper==5):
                    operacion = "%"
                    res = int(op1) % int(op2);
                    
                operacion = str(op1) +" "+ operacion+ " " + str(op2)
                p = proceso(Id, operacion, str(res), tiEs)
                
                self.procesos.append(p);

                    
            self.stackedWidget.setCurrentWidget(self.Lotes)

        
            
    def comenzar(self):
        if self.active:
            return;
        self.done = []
        bloq = []
        numProc = self.numProc
        act = 0
        listos = []
        i=0
        self.active=True
        while (act)<numProc and i<4:
            listos.append(self.procesos[act])
            print(act)
            act+=1;
            i+=1
        while (numProc != len(self.done)):
            self.label_11.setText(str(numProc-act))
            print("YOOOOO "+str(numProc)+" "+str(len(self.done)))
            print("Listos: "+str(len(listos)))
            if (len(listos)>0):
                flag=True;
                j=listos[0]
                if j.Tt == 0:
                    j.tRespuesta = self.tg - j.tLlegada
                listos.pop(0)
                self.actualizarListos(listos)
                    
                self.tableWidget_2.setRowCount(5)
                self.tableWidget_2.setColumnCount(1)
                self.tableWidget_2.setItem(0,0,QTableWidgetItem(str(j.id)))
                self.tableWidget_2.setItem(1,0,QTableWidgetItem(str(j.operacion)))
                self.tableWidget_2.setItem(2,0,QTableWidgetItem(str(j.tiEs)))
                self.tableWidget_2.setItem(4,0,QTableWidgetItem(str(j.Tr)))
                    
                tp = int(j.Tr) 
                for k in range(tp):
                    self.actualizarListos(listos)
                    if self.FPausa:
                        while True:
                            if self.FPausa == False:
                                break;
                            QtTest.QTest.qWait(50)
                    
                    if self.FError:
                        j.res="ERROR";
                        self.FError=False;
                        break;
                        
                    if self.FInterrupcion:
                        j.Tb = 8
                        bloq.append(j)
                        
                        tablerow = 0
                        for row in bloq:
                            self.tableWidget_3.setRowCount(tablerow + 1)
                            self.tableWidget_3.setItem(tablerow,0,QTableWidgetItem(str(row.id)))
                            self.tableWidget_3.setItem(tablerow, 1, QTableWidgetItem(str(8-(row.Tb))))
                            tablerow+=1
                                
                        self.FInterrupcion=False;
                        flag=False;
                            
                        break;
                        
                    j.Tt+=1;
                    j.Tr-=1;
                    self.tg+=1;
                    self.tableWidget_2.setItem(3,0,QTableWidgetItem(str(j.Tt)))
                    self.tableWidget_2.setItem(4,0,QTableWidgetItem(str(j.Tr)))
                        
                    if len(bloq)!=0:
                        tablerow = 0
                        cont = 0
                        toDel=False;
                        while cont < len(bloq):
                            row = bloq[cont]
                            row.Tb -= 1
                            self.tableWidget_3.setRowCount(tablerow + 1)
                            self.tableWidget_3.setItem(tablerow, 0, QTableWidgetItem(str(row.id)))
                            self.tableWidget_3.setItem(tablerow, 1, QTableWidgetItem(str(8-(row.Tb))))
                            tablerow += 1
                            if row.Tb == 0:
                                Del = row;
                                toDel = True
                            cont += 1
                        if toDel:
                            listos.append(Del)
                            bloq.remove(Del)
                        
                    else:
                        self.tableWidget_3.setRowCount(0)
                        
                    self.label_14.setText(str(self.tg));
                    
                    QtTest.QTest.qWait(1000) 
                if flag:
                    j.tFinali = self.tg
                    j.tRetorno = j.tFinali-j.tLlegada;
                    j.tEspera = j.tFinali - j.tLlegada - j.Tt
                    self.done.append(j);
                    if(act<numProc) and (len(bloq)+len(listos) < 4):
                        self.procesos[act].tLlegada=self.tg;
                        listos.append(self.procesos[act])
                        act+=1;
                    
                tablerow2 = 0
                for rows in self.done:
                    self.tableWidget_4.setRowCount(tablerow2 + 1)
                    self.tableWidget_4.setItem(tablerow2,0,QTableWidgetItem(str(rows.id)))
                    self.tableWidget_4.setItem(tablerow2,1,QTableWidgetItem(str(rows.operacion)))
                    self.tableWidget_4.setItem(tablerow2,2,QTableWidgetItem(str(rows.res)))
                    tablerow2+=1
            
            elif (len(listos)==0) and (len(bloq)>0):
                self.tableWidget_2.setColumnCount(0)
                tablerow = 0
                cont = 0
                toDel=False;
                while cont < len(bloq):
                    row = bloq[cont]
                    row.Tb -= 1
                    self.tableWidget_3.setRowCount(tablerow + 1)
                    self.tableWidget_3.setItem(tablerow, 0, QTableWidgetItem(str(row.id)))
                    self.tableWidget_3.setItem(tablerow, 1, QTableWidgetItem(str(8-(row.Tb))))
                    tablerow += 1
                    if row.Tb == 0:
                        Del = row;
                        toDel = True
                    cont += 1
                    self.tg+=1;
                    self.label_14.setText(str(self.tg));
                if toDel:
                    listos.append(Del)
                    bloq.remove(Del)
                QtTest.QTest.qWait(1000) 
                
        self.tableWidget.setRowCount(0)  
        self.tableWidget_2.setColumnCount(0)
        self.active=False
        self.actTimes()
        self.msgError("Procesos Terminados", "Todos los procesos han sido terminados, ya es posible revisar los tiempos")
        self.stackedWidget.setCurrentWidget(self.page)
        
        
    def showTimes(self):
        if self.active:
            self.msgError("Procesos aun corriendo", "Todos los procesos deben de ser ejecutados antes de ver los tiempos finales")
        else:
            self.stackedWidget.setCurrentWidget(self.page)
    
    def actualizarListos(self, listos):
        tablerow = 0
        self.tableWidget.setRowCount(0)
              
        for row in listos:
            self.tableWidget.setRowCount(tablerow + 1)
            self.tableWidget.setItem(tablerow,0,QTableWidgetItem(str(row.id)))
            self.tableWidget.setItem(tablerow,1,QTableWidgetItem(str(row.tiEs)))
            self.tableWidget.setItem(tablerow,2,QTableWidgetItem(str(row.Tt)))
            tablerow+=1
    def actTimes(self):
        tablerow = 0
        
        doneSort = sorted(self.done, key=lambda p: p.id);
        self.tableWidget_6.setRowCount(0)
              
        for row in doneSort:
            self.tableWidget_6.setRowCount(tablerow + 1)
            self.tableWidget_6.setItem(tablerow,0,QTableWidgetItem(str(row.id)))
            self.tableWidget_6.setItem(tablerow,1,QTableWidgetItem(str(row.tiEs)))
            self.tableWidget_6.setItem(tablerow,2,QTableWidgetItem(str(row.tLlegada)))
            self.tableWidget_6.setItem(tablerow,3,QTableWidgetItem(str(row.tFinali)))
            self.tableWidget_6.setItem(tablerow,4,QTableWidgetItem(str(row.tRetorno)))
            self.tableWidget_6.setItem(tablerow,5,QTableWidgetItem(str(row.tRespuesta)))
            self.tableWidget_6.setItem(tablerow,6,QTableWidgetItem(str(row.tEspera)))
            self.tableWidget_6.setItem(tablerow,7,QTableWidgetItem(str(row.Tt)))
            self.tableWidget_6.setItem(tablerow,8,QTableWidgetItem(str(row.operacion)))
            self.tableWidget_6.setItem(tablerow,9,QTableWidgetItem(str(row.res)))
            tablerow+=1
       
    def keyPressEvent(self, event):
        if (event.key() == Qt.Key_Escape) and (self.active):
            self.close()
        elif (event.key() == Qt.Key_P) and (self.active):
            self.FPausa=True;
            print("Programa Pausado: "+str(self.FPausa))
        elif (event.key() == Qt.Key_C) and (self.active):
            self.FPausa=False;
            print("Tecla presionada C Programa continuado: ")
            
        elif (event.key()== Qt.Key_I) and (self.active):
            self.FInterrupcion=True;
            print("Tecla presionada I interrupcion ejecutada:")
        elif (event.key()==Qt.Key_E) and (self.active):
            self.FError=True;
            print("Tecla presionada E ERROR:")
            
        print("Presionaste la tecla: " + event.text())
    
    
            
    def msgError(self,msg1,msg2):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle(msg1)
        msg.setText(msg2)
        msg.setIcon(QtWidgets.QMessageBox.Information)
        
        x = msg.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "Aceptar"))
        self.label_2.setText(_translate("MainWindow", "Num de procesos:"))
        self.label.setText(_translate("MainWindow", "Simulador de procesos"))
        self.label_9.setText(_translate("MainWindow", "Simulador de procesos"))
        self.label_10.setText(_translate("MainWindow", "Nuevos procesos:"))
        self.label_11.setText(_translate("MainWindow", "0"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "TiEs"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "TT"))
        self.label_12.setText(_translate("MainWindow", "Listos"))
        self.label_13.setText(_translate("MainWindow", "Contador Global:"))
        self.label_14.setText(_translate("MainWindow", "0"))
        item = self.tableWidget_2.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Id"))
        item = self.tableWidget_2.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Operacion"))
        item = self.tableWidget_2.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Tiempo"))
        item = self.tableWidget_2.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "Tiempo Total"))
        item = self.tableWidget_2.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "Tiempo Restante"))
        self.label_15.setText(_translate("MainWindow", "Proceso en Ejecución"))
        self.label_16.setText(_translate("MainWindow", "Procesos Terminados"))
        self.pushButton_3.setText(_translate("MainWindow", "Iniciar"))
        item = self.tableWidget_4.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Id"))
        item = self.tableWidget_4.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Op"))
        item = self.tableWidget_4.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Res"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "TB"))
        self.label_18.setText(_translate("MainWindow", "Proceso bloqueados"))
        self.pushButton_4.setText(_translate("MainWindow", "Ver tiempos"))
        self.label_17.setText(_translate("MainWindow", "Tiempos"))
        item = self.tableWidget_6.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Id"))
        item = self.tableWidget_6.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "TME"))
        item = self.tableWidget_6.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "T.Llegada"))
        item = self.tableWidget_6.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "T.Finalizacion"))
        item = self.tableWidget_6.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "T.Retorno"))
        item = self.tableWidget_6.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "T.Respuesta"))
        item = self.tableWidget_6.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "T.Espera"))
        item = self.tableWidget_6.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "T.Servicio"))
        item = self.tableWidget_6.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Opoeracion"))
        item = self.tableWidget_6.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Resultado"))
        self.pushButton_5.setText(_translate("MainWindow", "Volver a simulador"))

class proceso(object):
    def __init__(self,Id,operacion,res,tiEs):
        self.id = Id
        self.operacion = operacion
        self.res = str(res)
        self.tiEs = tiEs
        self.tLlegada = 0;
        self.tFinali = 0;
        self.tRetorno = 0;
        self.tRespuesta = 0;
        self.tEspera =0;
        self.Tservicio = 0;
        self.Tt = 0;
        self.Tr = self.tiEs
        self.Tb = 0

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    
    MainWindow.keyPressEvent = ui.keyPressEvent
    MainWindow.installEventFilter(MainWindow)
    MainWindow.keyPressEvent = ui.keyPressEvent
    
    sys.exit(app.exec_())


