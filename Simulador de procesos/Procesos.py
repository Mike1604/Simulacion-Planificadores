from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QTableWidgetItem
from PyQt5 import QtTest
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(967, 615)
        MainWindow.setStyleSheet("background-color: #2C3333;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 10, 961, 611))
        self.stackedWidget.setObjectName("stackedWidget")
        self.Principal = QtWidgets.QWidget()
        self.Principal.setObjectName("Principal")
        self.label_4 = QtWidgets.QLabel(self.Principal)
        self.label_4.setGeometry(QtCore.QRect(690, 60, 181, 51))
        self.label_4.setStyleSheet("font: 63 16pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: #E7F6F2;")
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(self.Principal)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 151, 51))
        self.label_2.setStyleSheet("font: 63 16pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: #E7F6F2;")
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.Principal)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 70, 91, 41))
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
        self.label = QtWidgets.QLabel(self.Principal)
        self.label.setGeometry(QtCore.QRect(291, -10, 311, 61))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 63 26pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: #E7F6F2;")
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.Principal)
        self.frame.setGeometry(QtCore.QRect(20, 120, 931, 461))
        self.frame.setStyleSheet("border :3px solid #A5C9CA;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(130, 20, 201, 51))
        self.label_5.setStyleSheet("font: 63 16pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: #E7F6F2;\n"
"border :3px solid #2C3333;")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(30, 90, 211, 51))
        self.label_6.setStyleSheet("font: 63 16pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: #E7F6F2;\n"
"border :3px solid #2C3333;")
        self.label_6.setObjectName("label_6")
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(340, 20, 331, 41))
        self.textEdit.setStyleSheet("font: 63 16pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: #A5C9CA;\n"
"color: #2C3333;\n"
"border-radius: 5;")
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.frame)
        self.textEdit_2.setGeometry(QtCore.QRect(260, 130, 101, 51))
        self.textEdit_2.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: #A5C9CA;\n"
"color: #2C3333;\n"
"border-radius: 5;")
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.frame)
        self.textEdit_3.setEnabled(True)
        self.textEdit_3.setGeometry(QtCore.QRect(630, 130, 101, 51))
        self.textEdit_3.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: #A5C9CA;\n"
"color: #2C3333;\n"
"border-radius: 5;")
        self.textEdit_3.setObjectName("textEdit_3")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(460, 130, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("background-color: #395B64;\n"
"border :3px solid #2C3333;\n"
"color: #E7F6F2;\n"
"font: 63 25pt \"Bahnschrift SemiBold SemiConden\";")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(30, 220, 211, 51))
        self.label_7.setStyleSheet("font: 63 16pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: #E7F6F2;\n"
"border :3px solid #2C3333;")
        self.label_7.setObjectName("label_7")
        self.textEdit_4 = QtWidgets.QTextEdit(self.frame)
        self.textEdit_4.setGeometry(QtCore.QRect(260, 260, 101, 51))
        self.textEdit_4.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: #A5C9CA;\n"
"color: #2C3333;\n"
"border-radius: 5;")
        self.textEdit_4.setObjectName("textEdit_4")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(490, 210, 211, 51))
        self.label_8.setStyleSheet("font: 63 16pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: #E7F6F2;\n"
"border :3px solid #2C3333;")
        self.label_8.setObjectName("label_8")
        self.textEdit_5 = QtWidgets.QTextEdit(self.frame)
        self.textEdit_5.setGeometry(QtCore.QRect(630, 270, 101, 51))
        self.textEdit_5.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: #A5C9CA;\n"
"color: #2C3333;\n"
"border-radius: 5;")
        self.textEdit_5.setObjectName("textEdit_5")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(430, 360, 161, 61))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton{\n"
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
        self.pushButton.setObjectName("pushButton")
        self.spinBox = QtWidgets.QSpinBox(self.Principal)
        self.spinBox.setGeometry(QtCore.QRect(190, 80, 51, 31))
        self.spinBox.setStyleSheet("font: 63 16pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: #A5C9CA;\n"
"color: #2C3333;\n"
"border-radius: 5;")
        self.spinBox.setObjectName("spinBox")
        self.label_3 = QtWidgets.QLabel(self.Principal)
        self.label_3.setGeometry(QtCore.QRect(880, 70, 51, 41))
        self.label_3.setStyleSheet("font: 63 25pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: #A5C9CA;\n"
"color: #2C3333;\n"
"border-radius: 5;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_20 = QtWidgets.QLabel(self.Principal)
        self.label_20.setGeometry(QtCore.QRect(390, 60, 191, 51))
        self.label_20.setStyleSheet("font: 63 16pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: #E7F6F2;")
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.Principal)
        self.label_21.setGeometry(QtCore.QRect(600, 70, 51, 41))
        self.label_21.setStyleSheet("font: 63 25pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: #A5C9CA;\n"
"color: #2C3333;\n"
"border-radius: 5;")
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.stackedWidget.addWidget(self.Principal)
        self.Lotes = QtWidgets.QWidget()
        self.Lotes.setObjectName("Lotes")
        self.label_9 = QtWidgets.QLabel(self.Lotes)
        self.label_9.setGeometry(QtCore.QRect(320, 10, 311, 61))
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
        self.label_10.setGeometry(QtCore.QRect(30, 70, 151, 51))
        self.label_10.setStyleSheet("font: 63 16pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: #E7F6F2;")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.Lotes)
        self.label_11.setGeometry(QtCore.QRect(190, 70, 51, 41))
        self.label_11.setStyleSheet("font: 63 25pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: #A5C9CA;\n"
"color: #2C3333;;\n"
"border-radius: 5;")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.tableWidget = QtWidgets.QTableWidget(self.Lotes)
        self.tableWidget.setGeometry(QtCore.QRect(40, 200, 241, 321))
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
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.label_12 = QtWidgets.QLabel(self.Lotes)
        self.label_12.setGeometry(QtCore.QRect(90, 140, 151, 51))
        self.label_12.setStyleSheet("font: 63 16pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: #E7F6F2;")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.Lotes)
        self.label_13.setGeometry(QtCore.QRect(290, 550, 151, 51))
        self.label_13.setStyleSheet("font: 63 16pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: #E7F6F2;")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.Lotes)
        self.label_14.setGeometry(QtCore.QRect(460, 560, 51, 41))
        self.label_14.setStyleSheet("font: 63 25pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: #A5C9CA;\n"
"color: #2C3333;;\n"
"border-radius: 5;")
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.Lotes)
        self.tableWidget_2.setGeometry(QtCore.QRect(300, 200, 261, 191))
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
        self.label_15.setGeometry(QtCore.QRect(360, 140, 181, 51))
        self.label_15.setStyleSheet("font: 63 16pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: #E7F6F2;")
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.Lotes)
        self.label_16.setGeometry(QtCore.QRect(690, 80, 181, 51))
        self.label_16.setStyleSheet("font: 63 16pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: #E7F6F2;")
        self.label_16.setObjectName("label_16")
        self.pushButton_3 = QtWidgets.QPushButton(self.Lotes)
        self.pushButton_3.setGeometry(QtCore.QRect(350, 470, 161, 61))
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
        self.tableWidget_4.setGeometry(QtCore.QRect(580, 140, 371, 451))
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
        self.tableWidget_4.setColumnCount(5)
        self.tableWidget_4.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(4, item)
        self.tableWidget_4.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_4.horizontalHeader().setDefaultSectionSize(65)
        self.tableWidget_4.horizontalHeader().setHighlightSections(True)
        self.tableWidget_4.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget_4.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_4.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_4.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget_4.verticalHeader().setMinimumSectionSize(25)
        self.stackedWidget.addWidget(self.Lotes)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        
        """
        Inician instrucciones
        """
        self.pushButton_2.clicked.connect(lambda: self.numProcesos())
        self.pushButton.clicked.connect(lambda: self.agregar())
        self.numProc = 0;
        self.leftProc = 0;
        self.procDone=0;
        self.con = 0;
        self.numLote = 1;
        self.tt=0;
        
        self.procesos = [];
        
        self.pushButton_3.clicked.connect(lambda: self.comenzar());

    def numProcesos(self):
        if self.spinBox.text() == "0":
            self.msgError("No valido", "El numero de procesos debe ser mayor a 0");
        else:
            self.numProc = int(self.spinBox.text());
            self.label_21.setText(str(self.numProc));
            self.leftProc = self.numProc;
            self.label_3.setText("0");
            self.procesos.clear();
            self.procDone=0;
            self.con = 0;
            self.numLote = 1;
    
    def agregar(self):
        #Validaciones
        if(self.numProc == 0):
            self.msgError("No valido", "Primero debes de indicar el numero de procesos a ingresar");
            return;
        
        if(len(self.textEdit.toPlainText()) == 0):
            self.msgError("Falta de informacion", "Primero debes de ingresar un nombre de programador");
            return;
        elif(len(self.textEdit_2.toPlainText()) == 0) or (len(self.textEdit_3.toPlainText()) == 0):
            self.msgError("Falta de informacion", "Primero debes de ingresar dos operando");
            return;
        elif(len(self.textEdit_4.toPlainText()) == 0):
            self.msgError("Falta de informacion", "Primero debes de ingresar el tiempo estimado");
            return;
        elif(len(self.textEdit_5.toPlainText()) == 0):
            self.msgError("Falta de informacion", "Primero debes de ingresar el id del proceso");
            return;
            
        name = self.textEdit.toPlainText();
        try:
            op1 = int(self.textEdit_2.toPlainText());
            op2 = int(self.textEdit_3.toPlainText());
        except ValueError:
            self.msgError("Operadores incorrectos", "Debes ingresar valores numericos");
            return;
        tiEs = self.textEdit_4.toPlainText();
        Id = self.textEdit_5.toPlainText();
        operacion = self.comboBox.currentText();
            
        if(op1>0 and op2==0 and operacion=="/") or (op1==0 and op2>0 and operacion=="/"):
            self.msgError("Operacion incorrecta", "No es posible dividir entre 0");
            return;
        if(op1>0 and op2==0 and operacion=="%") or (op1==0 and op2>0 and operacion=="%"):
            self.msgError("Operacion incorrecta", "No es posible hacer modulo entre 0");
            return;
        for row in self.procesos:
            if(row[1] == Id):
                self.msgError("Id incorrecto", "El id ya ha sido ingresado");
                return;
            
        if(operacion == "+"):
            res = int(op1) + int(op2);
        elif(operacion == "-"):
            res = int(op1) - int(op2);
        elif(operacion == "*"):
            res = int(op1) * int(op2);
        elif(operacion == "/"):
            res = int(op1) / int(op2);
        elif(operacion == "%"):
            res = int(op1) % int(op2);
            
        operacion = str(op1) +" "+ operacion+ " " + str(op2)
        self.procesos.append([self.numLote,Id,name,operacion,res,tiEs]);
        self.leftProc -= 1;
        self.procDone += 1;
        self.con += 1;
        
        if(self.con == 4):
            self.con = 0;
            self.numLote += 1;
        
        self.label_21.setText(str(self.leftProc));
        self.label_3.setText(str(self.procDone))
        
        if (self.leftProc == 0) and (self.numProc != 0):
            self.stackedWidget.setCurrentWidget(self.Lotes)
            self.label_11.setText(str(self.numLote))
            
            
            
    def comenzar(self):
        done = []
        for i in range(self.numLote):
            aux = []
            tablerow = 0
            self.label_11.setText(str(self.numLote - (i+1)))
            for row in self.procesos:
                if row[0] == i+1:
                    aux.append(row);
                    
            actl = list(aux)
            
            for j in aux:
                
                tablerow = 0
                
                actl.remove(j)
                
                self.tableWidget.setRowCount(0)
                
                for row in actl:
                    self.tableWidget.setRowCount(tablerow + 1)
                    self.tableWidget.setItem(tablerow,0,QTableWidgetItem(str(row[2])))
                    self.tableWidget.setItem(tablerow,1,QTableWidgetItem(str(row[5])))
                    tablerow+=1
                
                self.tableWidget_2.setRowCount(5)
                self.tableWidget_2.setColumnCount(1)
                self.tableWidget_2.setItem(0,0,QTableWidgetItem(str(j[1])))
                self.tableWidget_2.setItem(1,0,QTableWidgetItem(str(j[2])))
                self.tableWidget_2.setItem(2,0,QTableWidgetItem(str(j[3])))
                self.tableWidget_2.setItem(4,0,QTableWidgetItem(str(j[5])))
                
                tp = int(j[5])
                auxtp=tp;
                
                for k in range(tp):
                    self.tt+=1;
                    auxtp-=1;
                    self.tableWidget_2.setItem(3,0,QTableWidgetItem(str(k+1)))
                    self.tableWidget_2.setItem(4,0,QTableWidgetItem(str(auxtp)))
    
                    self.label_14.setText(str(self.tt));
                    QtTest.QTest.qWait(1000) 
                    
                done.append(j);
                
                tablerow2 = 0
                for rows in done:
                    self.tableWidget_4.setRowCount(tablerow2 + 1)
                    self.tableWidget_4.setItem(tablerow2,0,QTableWidgetItem(str(rows[0])))
                    self.tableWidget_4.setItem(tablerow2,1,QTableWidgetItem(str(rows[1])))
                    self.tableWidget_4.setItem(tablerow2,2,QTableWidgetItem(str(rows[2])))
                    self.tableWidget_4.setItem(tablerow2,3,QTableWidgetItem(str(rows[3])))
                    self.tableWidget_4.setItem(tablerow2,4,QTableWidgetItem(str(rows[4])))
                    tablerow2+=1

        self.tableWidget.clear()
        self.tableWidget_2.clear()
        
                
            
    def msgError(self,msg1,msg2):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle(msg1)
        msg.setText(msg2)
        msg.setIcon(QtWidgets.QMessageBox.Information)
        
        x = msg.exec_()
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "Procesos ingresados:"))
        self.label_2.setText(_translate("MainWindow", "Num de procesos:"))
        self.pushButton_2.setText(_translate("MainWindow", "Aceptar"))
        self.label.setText(_translate("MainWindow", "Simulador de procesos"))
        self.label_5.setText(_translate("MainWindow", "Nombre programador:"))
        self.label_6.setText(_translate("MainWindow", "Ingresa la operacion:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "+"))
        self.comboBox.setItemText(1, _translate("MainWindow", "-"))
        self.comboBox.setItemText(2, _translate("MainWindow", "/"))
        self.comboBox.setItemText(3, _translate("MainWindow", "*"))
        self.comboBox.setItemText(4, _translate("MainWindow", "%"))
        self.label_7.setText(_translate("MainWindow", "Tiempo estimado:"))
        self.label_8.setText(_translate("MainWindow", "Id de proceso:"))
        self.pushButton.setText(_translate("MainWindow", "Agregar"))
        self.label_3.setText(_translate("MainWindow", "0"))
        self.label_20.setText(_translate("MainWindow", "Procesos por ingresar:"))
        self.label_21.setText(_translate("MainWindow", "0"))
        self.label_9.setText(_translate("MainWindow", "Simulador de procesos"))
        self.label_10.setText(_translate("MainWindow", "Lotes pendientes:"))
        self.label_11.setText(_translate("MainWindow", "0"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Tiempo"))
        self.label_12.setText(_translate("MainWindow", "Lote en Ejecución"))
        self.label_13.setText(_translate("MainWindow", "Contador Global:"))
        self.label_14.setText(_translate("MainWindow", "0"))
        item = self.tableWidget_2.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Id"))
        item = self.tableWidget_2.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.tableWidget_2.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Operacion"))
        item = self.tableWidget_2.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "Tiempo Ejecucion"))
        item = self.tableWidget_2.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "Tiempo restante"))
        self.label_15.setText(_translate("MainWindow", "Proceso en Ejecución"))
        self.label_16.setText(_translate("MainWindow", "Procesos Terminados"))
        self.pushButton_3.setText(_translate("MainWindow", "Iniciar"))
        item = self.tableWidget_4.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Lote"))
        item = self.tableWidget_4.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Id"))
        item = self.tableWidget_4.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget_4.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Op"))
        item = self.tableWidget_4.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Res"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

