from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5 import QtTest
from PyQt5.QtCore import Qt
import random    


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1452, 641)
        MainWindow.setStyleSheet("background-color: rgb(26, 26, 26);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(580, 30, 291, 61))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("font: 63 26pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: whitesmoke;")
        self.label_9.setObjectName("label_9")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(1160, 110, 181, 181))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Images/dj.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 120, 181, 181))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Images/wifi.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(150, 50, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("font: 63 26pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: whitesmoke;")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(1170, 40, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("font: 63 26pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: whitesmoke;")
        self.label_11.setObjectName("label_11")
        self.StatusProductor = QtWidgets.QLabel(self.centralwidget)
        self.StatusProductor.setGeometry(QtCore.QRect(110, 310, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.StatusProductor.setFont(font)
        self.StatusProductor.setStyleSheet("font: 63 26pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: whitesmoke;")
        self.StatusProductor.setAlignment(QtCore.Qt.AlignCenter)
        self.StatusProductor.setObjectName("StatusProductor")
        self.StatusConsumidor = QtWidgets.QLabel(self.centralwidget)
        self.StatusConsumidor.setGeometry(QtCore.QRect(1140, 300, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.StatusConsumidor.setFont(font)
        self.StatusConsumidor.setStyleSheet("font: 63 26pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: whitesmoke;")
        self.StatusConsumidor.setAlignment(QtCore.Qt.AlignCenter)
        self.StatusConsumidor.setObjectName("StatusConsumidor")
        self.Cont1 = QtWidgets.QLabel(self.centralwidget)
        self.Cont1.setGeometry(QtCore.QRect(20, 380, 111, 101))
        self.Cont1.setStyleSheet("background-color: #002B5B;")
        self.Cont1.setText("")
        self.Cont1.setScaledContents(True)
        self.Cont1.setObjectName("Cont1")
        self.Cont2 = QtWidgets.QLabel(self.centralwidget)
        self.Cont2.setGeometry(QtCore.QRect(150, 380, 111, 101))
        self.Cont2.setStyleSheet("background-color: #002B5B;")
        self.Cont2.setText("")
        self.Cont2.setScaledContents(True)
        self.Cont2.setObjectName("Cont2")
        self.Cont3 = QtWidgets.QLabel(self.centralwidget)
        self.Cont3.setGeometry(QtCore.QRect(280, 380, 111, 101))
        self.Cont3.setStyleSheet("background-color: #002B5B;")
        self.Cont3.setText("")
        self.Cont3.setScaledContents(True)
        self.Cont3.setObjectName("Cont3")
        self.Cont4 = QtWidgets.QLabel(self.centralwidget)
        self.Cont4.setGeometry(QtCore.QRect(410, 380, 111, 101))
        self.Cont4.setStyleSheet("background-color: #002B5B;")
        self.Cont4.setText("")
        self.Cont4.setScaledContents(True)
        self.Cont4.setObjectName("Cont4")
        self.Cont5 = QtWidgets.QLabel(self.centralwidget)
        self.Cont5.setGeometry(QtCore.QRect(540, 380, 111, 101))
        self.Cont5.setStyleSheet("background-color: #002B5B;")
        self.Cont5.setText("")
        self.Cont5.setScaledContents(True)
        self.Cont5.setObjectName("Cont5")
        self.Cont6 = QtWidgets.QLabel(self.centralwidget)
        self.Cont6.setGeometry(QtCore.QRect(670, 380, 111, 101))
        self.Cont6.setStyleSheet("background-color: #002B5B;")
        self.Cont6.setText("")
        self.Cont6.setScaledContents(True)
        self.Cont6.setObjectName("Cont6")
        self.Cont10 = QtWidgets.QLabel(self.centralwidget)
        self.Cont10.setGeometry(QtCore.QRect(1190, 380, 111, 101))
        self.Cont10.setStyleSheet("background-color: #002B5B;")
        self.Cont10.setText("")
        self.Cont10.setScaledContents(True)
        self.Cont10.setObjectName("Cont10")
        self.Cont9 = QtWidgets.QLabel(self.centralwidget)
        self.Cont9.setGeometry(QtCore.QRect(1060, 380, 111, 101))
        self.Cont9.setStyleSheet("background-color: #002B5B;")
        self.Cont9.setText("")
        self.Cont9.setScaledContents(True)
        self.Cont9.setObjectName("Cont9")
        self.Cont11 = QtWidgets.QLabel(self.centralwidget)
        self.Cont11.setGeometry(QtCore.QRect(1320, 380, 111, 101))
        self.Cont11.setStyleSheet("background-color: #002B5B;")
        self.Cont11.setText("")
        self.Cont11.setScaledContents(True)
        self.Cont11.setObjectName("Cont11")
        self.Cont8 = QtWidgets.QLabel(self.centralwidget)
        self.Cont8.setGeometry(QtCore.QRect(930, 380, 111, 101))
        self.Cont8.setStyleSheet("background-color: #002B5B;")
        self.Cont8.setText("")
        self.Cont8.setScaledContents(True)
        self.Cont8.setObjectName("Cont8")
        self.Cont7 = QtWidgets.QLabel(self.centralwidget)
        self.Cont7.setGeometry(QtCore.QRect(800, 380, 111, 101))
        self.Cont7.setStyleSheet("background-color: #002B5B;")
        self.Cont7.setText("")
        self.Cont7.setScaledContents(True)
        self.Cont7.setObjectName("Cont7")
        self.Cont17 = QtWidgets.QLabel(self.centralwidget)
        self.Cont17.setGeometry(QtCore.QRect(670, 500, 111, 101))
        self.Cont17.setStyleSheet("background-color: #002B5B;")
        self.Cont17.setText("")
        self.Cont17.setScaledContents(True)
        self.Cont17.setObjectName("Cont17")
        self.Cont20 = QtWidgets.QLabel(self.centralwidget)
        self.Cont20.setGeometry(QtCore.QRect(1060, 500, 111, 101))
        self.Cont20.setStyleSheet("background-color: #002B5B;")
        self.Cont20.setText("")
        self.Cont20.setScaledContents(True)
        self.Cont20.setObjectName("Cont20")
        self.Cont22 = QtWidgets.QLabel(self.centralwidget)
        self.Cont22.setGeometry(QtCore.QRect(1320, 500, 111, 101))
        self.Cont22.setStyleSheet("background-color: #002B5B;")
        self.Cont22.setText("")
        self.Cont22.setScaledContents(True)
        self.Cont22.setObjectName("Cont22")
        self.Cont15 = QtWidgets.QLabel(self.centralwidget)
        self.Cont15.setGeometry(QtCore.QRect(410, 500, 111, 101))
        self.Cont15.setStyleSheet("background-color: #002B5B;")
        self.Cont15.setText("")
        self.Cont15.setScaledContents(True)
        self.Cont15.setObjectName("Cont15")
        self.Cont14 = QtWidgets.QLabel(self.centralwidget)
        self.Cont14.setGeometry(QtCore.QRect(280, 500, 111, 101))
        self.Cont14.setStyleSheet("background-color: #002B5B;")
        self.Cont14.setText("")
        self.Cont14.setScaledContents(True)
        self.Cont14.setObjectName("Cont14")
        self.Cont19 = QtWidgets.QLabel(self.centralwidget)
        self.Cont19.setGeometry(QtCore.QRect(930, 500, 111, 101))
        self.Cont19.setStyleSheet("background-color: #002B5B;")
        self.Cont19.setText("")
        self.Cont19.setScaledContents(True)
        self.Cont19.setObjectName("Cont19")
        self.Cont21 = QtWidgets.QLabel(self.centralwidget)
        self.Cont21.setGeometry(QtCore.QRect(1190, 500, 111, 101))
        self.Cont21.setStyleSheet("background-color: #002B5B;")
        self.Cont21.setText("")
        self.Cont21.setScaledContents(True)
        self.Cont21.setObjectName("Cont21")
        self.Cont16 = QtWidgets.QLabel(self.centralwidget)
        self.Cont16.setGeometry(QtCore.QRect(540, 500, 111, 101))
        self.Cont16.setStyleSheet("background-color: #002B5B;")
        self.Cont16.setText("")
        self.Cont16.setScaledContents(True)
        self.Cont16.setObjectName("Cont16")
        self.Cont18 = QtWidgets.QLabel(self.centralwidget)
        self.Cont18.setGeometry(QtCore.QRect(800, 500, 111, 101))
        self.Cont18.setStyleSheet("background-color: #002B5B;")
        self.Cont18.setText("")
        self.Cont18.setScaledContents(True)
        self.Cont18.setObjectName("Cont18")
        self.Cont13 = QtWidgets.QLabel(self.centralwidget)
        self.Cont13.setGeometry(QtCore.QRect(150, 500, 111, 101))
        self.Cont13.setStyleSheet("background-color: #002B5B;")
        self.Cont13.setText("")
        self.Cont13.setScaledContents(True)
        self.Cont13.setObjectName("Cont13")
        self.Cont12 = QtWidgets.QLabel(self.centralwidget)
        self.Cont12.setGeometry(QtCore.QRect(20, 500, 111, 101))
        self.Cont12.setStyleSheet("background-color: #002B5B;")
        self.Cont12.setText("")
        self.Cont12.setScaledContents(True)
        self.Cont12.setObjectName("Cont12")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(630, 190, 161, 61))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"    font: 63 16pt \"Bahnschrift SemiBold SemiConden\";\n"
"    color: #E7F6F2;\n"
"    border :3px solid #2C3333;\n"
"    background-color: rgb(76, 174, 254);\n"
"    border-radius: 10;\n"
"    \n"
"}\n"
"QPushButton:hover{\n"
"    font: 63 16pt \"Bahnschrift SemiBold SemiConden\";\n"
"    color: #E7F6F2;\n"
"    border :3px solid #2C3333;\n"
"    background-color:  rgb(4, 237, 254);\n"
"    border-radius: 10;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        
        """
        Aqui empiezan las funciones
        """
        self.Running=False;
        self.pushButton_3.clicked.connect(lambda: self.iniciar())
        
    def iniciar(self):
        self.StatusProductor.setText("Status")
        self.StatusProductor.setStyleSheet("font: 63 26pt \"Bahnschrift SemiBold SemiConden\"; color: whitesmoke;");
        self.StatusConsumidor.setText("Status")
        self.StatusConsumidor.setStyleSheet("font: 63 26pt \"Bahnschrift SemiBold SemiConden\"; color: whitesmoke;");
        labels = [self.Cont1, self.Cont2,self.Cont3,self.Cont4,self.Cont5,self.Cont6,self.Cont7,self.Cont8,self.Cont9,self.Cont10,self.Cont11,self.Cont12,
                  self.Cont13,self.Cont14,self.Cont15,self.Cont16,self.Cont17,self.Cont18,self.Cont19,self.Cont20,self.Cont21,self.Cont22];
        for i, num in enumerate(labels):
            labels[i].setStyleSheet("background-color: #002B5B;")
            pixmap = QPixmap(None)
            labels[i].setPixmap(pixmap)
            
        self.Running=True;
        ConsumerPointer=0;
        ProducerPointer=0;
        content = [0] * 22;
        last="";
        
        while self.Running == True:
            numconsum = random.randint(1,1000);
            numprod = random.randint(1,1000);
            while numconsum == numprod:
                numconsum = random.randint(1,1000);
                numprod = random.randint(1,1000);
            #Recorrido del productor
            if numprod > numconsum:
                last="Productor"
                numprod = random.randint(3,6);
                for i in range(numprod):
                    if self.Running == False:
                        break;
                    if content[ProducerPointer]==1:
                        self.StatusProductor.setStyleSheet("font: 63 26pt \"Bahnschrift SemiBold SemiConden\"; color: whitesmoke;background-color: rgb(255, 170, 34);");
                        self.StatusProductor.setText("Intentando")
                        QtTest.QTest.qWait(1000) 
                        break;
                    else:
                        self.StatusProductor.setStyleSheet("font: 63 26pt \"Bahnschrift SemiBold SemiConden\"; color: whitesmoke;background-color: rgb(95, 208, 104);");
                        self.StatusProductor.setText("Produciendo")
                        content[ProducerPointer]=1;
                        pixmap = QPixmap('Images/vinilo.png')
                        labels[ProducerPointer].setStyleSheet("")
                        labels[ProducerPointer].setPixmap(pixmap)
                    ProducerPointer+=1;
                    if ProducerPointer==22:
                        ProducerPointer=0;
                    QtTest.QTest.qWait(1000) 
                
                
            else:
                last="Consumidor"
                numconsum = random.randint(3,6);
                for i in range(numconsum):
                    if self.Running == False:
                        break;
                    if content[ConsumerPointer]==0:
                        self.StatusConsumidor.setStyleSheet("font: 63 26pt \"Bahnschrift SemiBold SemiConden\"; color: whitesmoke;background-color: rgb(255, 170, 34);");
                        self.StatusConsumidor.setText("Intentando")
                        QtTest.QTest.qWait(1000) 
                        break;
                    else:
                        self.StatusConsumidor.setStyleSheet("font: 63 26pt \"Bahnschrift SemiBold SemiConden\"; color: whitesmoke;background-color: rgb(95, 208, 104);");
                        self.StatusConsumidor.setText("Consumiendo")
                        content[ConsumerPointer]=0;
                        pixmap = QPixmap('Images/vinilo.png')
                        labels[ConsumerPointer].setStyleSheet("background-color: #002B5B;")
                        pixmap = QPixmap(None)
                        labels[ConsumerPointer].setPixmap(pixmap)
                    ConsumerPointer+=1;
                    if ConsumerPointer==22:
                        ConsumerPointer=0;
                    QtTest.QTest.qWait(1000) 
            
            if last=="Productor":
                self.StatusProductor.setStyleSheet("font: 63 26pt \"Bahnschrift SemiBold SemiConden\"; color: whitesmoke;background-color: rgb(255, 26, 26);");
                self.StatusProductor.setText("Durmiendo")
            else:
                self.StatusConsumidor.setStyleSheet("font: 63 26pt \"Bahnschrift SemiBold SemiConden\"; color: whitesmoke;background-color: rgb(255, 26, 26);");
                self.StatusConsumidor.setText("Durmiendo")
            QtTest.QTest.qWait(1500) 
            
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_9.setText(_translate("MainWindow", "Producto Consumidor"))
        self.label_10.setText(_translate("MainWindow", "Productor"))
        self.label_11.setText(_translate("MainWindow", "Consumidor"))
        self.StatusProductor.setText(_translate("MainWindow", "Status"))
        self.StatusConsumidor.setText(_translate("MainWindow", "Status"))
        self.pushButton_3.setText(_translate("MainWindow", "Iniciar"))
        
    def keyPressEvent(self, event):
        if (event.key() == Qt.Key_Escape):
            self.Running=False;
            
        print("Presionaste la tecla: " + event.text())
    
    
            
    def msgError(self,msg1,msg2):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle(msg1)
        msg.setText(msg2)
        msg.setIcon(QtWidgets.QMessageBox.Information)
        
        x = msg.exec_()    
    

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


