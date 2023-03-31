from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5 import QtTest
from PyQt5.QtCore import Qt
import random    

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
        self.frame = QtWidgets.QFrame(self.Principal)
        self.frame.setGeometry(QtCore.QRect(10, 0, 941, 591))
        self.frame.setStyleSheet("border :3px solid #A5C9CA;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(610, 280, 161, 61))
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
        self.spinBox.setGeometry(QtCore.QRect(410, 260, 161, 71))
        self.spinBox.setStyleSheet("font: 63 30pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: #A5C9CA;\n"
"color: #2C3333;\n"
"border-radius: 5;")
        self.spinBox.setObjectName("spinBox")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(70, 250, 311, 81))
        self.label_2.setStyleSheet("font: 63 30pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: #E7F6F2;\n"
"border :3px solid #2C3333;")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(290, 90, 401, 61))
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
        self.tableWidget_4.setColumnCount(4)
        self.tableWidget_4.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(3, item)
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
        self.numLote = 1;
        self.tg=0;
        self.FPausa=False;
        self.FInterrupcion=False;
        self.FError=False;
        self.procesos = [];
        self.active=False;
        self.pushButton_3.clicked.connect(lambda: self.comenzar());
        MainWindow.keyPressEvent = self.keyPressEvent
        self.tableWidget.keyPressEvent = self.keyPressEvent
        
        

    def numProcesos(self):
        self.numProc = int(self.spinBox.text())
        if self.numProc == 0:
            self.msgError("No valido", "El numero de procesos debe ser mayor a 0");
        else:
            #Validaciones
            con = 0;
            for i in range(self.numProc):
                Id = i+1;
                op1 = random.randint(1,1000);
                op2 = random.randint(1,1000);
                oper = random.randint(1,5);
                tiEs = random.randint(1, 16)
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
                p = proceso(self.numLote, Id, operacion, str(res), tiEs)
                
                self.procesos.append(p);
                
                con += 1;
                
                if(con == 4):
                    con = 0;
                    self.numLote += 1;
                    
            self.stackedWidget.setCurrentWidget(self.Lotes)
            self.label_11.setText(str(self.numLote))

        
            
            
            
    def comenzar(self):
        if self.active:
            return;
        done = []
        for i in range(self.numLote):
            self.active=True
            aux = []
            tablerow = 0
            self.label_11.setText(str(self.numLote - (i+1)))
            for row in self.procesos:
                if row.lote == i+1:
                    aux.append(row);
                    
            actl = list(aux)
            for j in aux:
                er=j;
                flag=True;
                tablerow = 0
                actl.remove(j)
                
                self.tableWidget.setRowCount(0)
                  
                for row in actl:
                    self.tableWidget.setRowCount(tablerow + 1)
                    self.tableWidget.setItem(tablerow,0,QTableWidgetItem(str(row.id)))
                    self.tableWidget.setItem(tablerow,1,QTableWidgetItem(str(row.Tr)))
                    self.tableWidget.setItem(tablerow,2,QTableWidgetItem(str(row.tiEs)))
                    tablerow+=1
                
                self.tableWidget_2.setRowCount(5)
                self.tableWidget_2.setColumnCount(1)
                self.tableWidget_2.setItem(0,0,QTableWidgetItem(str(j.id)))
                self.tableWidget_2.setItem(1,0,QTableWidgetItem(str(j.operacion)))
                self.tableWidget_2.setItem(2,0,QTableWidgetItem(str(j.tiEs)))
                self.tableWidget_2.setItem(4,0,QTableWidgetItem(str(j.Tr)))
                
                tp = int(j.Tr) 
                
                for k in range(tp):
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
                        aux.append(j);
                        actl.append(j);
                        self.FInterrupcion=False;
                        flag=False;
                        break;
                    
                    j.Tt+=1;
                    j.Tr-=1;
                    self.tg+=1;
                    self.tableWidget_2.setItem(3,0,QTableWidgetItem(str(j.Tt)))
                    self.tableWidget_2.setItem(4,0,QTableWidgetItem(str(j.Tr)))

                    self.label_14.setText(str(self.tg));
                        
                    QtTest.QTest.qWait(1000) 
                if flag:
                    done.append(j);
                
                tablerow2 = 0
                for rows in done:
                    self.tableWidget_4.setRowCount(tablerow2 + 1)
                    self.tableWidget_4.setItem(tablerow2,0,QTableWidgetItem(str(rows.lote)))
                    self.tableWidget_4.setItem(tablerow2,1,QTableWidgetItem(str(rows.id)))
                    self.tableWidget_4.setItem(tablerow2,2,QTableWidgetItem(str(rows.operacion)))
                    self.tableWidget_4.setItem(tablerow2,3,QTableWidgetItem(str(rows.res)))
                    tablerow2+=1
                
        self.tableWidget.setRowCount(0)  
        self.tableWidget_2.setColumnCount(0)
        self.active=False
        
                
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
        self.label_10.setText(_translate("MainWindow", "Lotes pendientes:"))
        self.label_11.setText(_translate("MainWindow", "0"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "TR"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "TT"))
        self.label_12.setText(_translate("MainWindow", "Lote en Ejecución"))
        self.label_13.setText(_translate("MainWindow", "Contador Global:"))
        self.label_14.setText(_translate("MainWindow", "0"))
        item = self.tableWidget_2.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Id"))
        item = self.tableWidget_2.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Operacion"))
        item = self.tableWidget_2.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Tiempo Total"))
        item = self.tableWidget_2.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "Tiempo Ejecucion"))
        item = self.tableWidget_2.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "Tiempo Restante"))
        self.label_15.setText(_translate("MainWindow", "Proceso en Ejecución"))
        self.label_16.setText(_translate("MainWindow", "Procesos Terminados"))
        self.pushButton_3.setText(_translate("MainWindow", "Iniciar"))
        item = self.tableWidget_4.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Lote"))
        item = self.tableWidget_4.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Id"))
        item = self.tableWidget_4.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Op"))
        item = self.tableWidget_4.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Res"))

class proceso(object):
    def __init__(self,lote,Id,operacion,res,tiEs):
        self.lote = lote
        self.id = Id
        self.operacion = operacion
        self.res = str(res)
        self.tiEs = tiEs
        self.Tt = 0;
        self.Tr = self.tiEs

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

    

