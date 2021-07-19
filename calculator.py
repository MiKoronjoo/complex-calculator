from PyQt5 import QtCore, QtGui, QtWidgets

from utils import str_exp, str_pol, to_complex, str_rect, pol2rct


class Ui_MainWindow(object):
    def __init__(self):
        self.text = ''
        self.fontSize = 36

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 600)
        MainWindow.setStyleSheet("background-color: rgb(23, 23, 26);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.formLayout = QtWidgets.QFormLayout(self.frame)
        self.formLayout.setObjectName("formLayout")
        self.display = QtWidgets.QTextBrowser(self.frame)
        self.display.setObjectName("display")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.display)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setObjectName("gridLayout")
        self.n2Button = QtWidgets.QPushButton(self.frame_2)
        self.n2Button.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.n2Button.setFont(font)
        self.n2Button.setStyleSheet("background-color: rgb(46, 52, 54);\n"
                                    "color: rgb(238, 238, 236);")
        self.n2Button.setObjectName("n2Button")
        self.gridLayout.addWidget(self.n2Button, 6, 1, 1, 1)
        self.dotButton = QtWidgets.QPushButton(self.frame_2)
        self.dotButton.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.dotButton.setFont(font)
        self.dotButton.setStyleSheet("background-color: rgb(46, 52, 54);\n"
                                     "color: rgb(238, 238, 236);")
        self.dotButton.setObjectName("dotButton")
        self.gridLayout.addWidget(self.dotButton, 7, 2, 1, 1)
        self.mulButton = QtWidgets.QPushButton(self.frame_2)
        self.mulButton.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.mulButton.setFont(font)
        self.mulButton.setStyleSheet("background-color: rgb(204, 107, 0);\n"
                                     "color: rgb(238, 238, 236);")
        self.mulButton.setObjectName("mulButton")
        self.gridLayout.addWidget(self.mulButton, 7, 3, 1, 1)
        self.divButton = QtWidgets.QPushButton(self.frame_2)
        self.divButton.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.divButton.setFont(font)
        self.divButton.setStyleSheet("background-color: rgb(204, 107, 0);\n"
                                     "color: rgb(238, 238, 236);")
        self.divButton.setObjectName("divButton")
        self.gridLayout.addWidget(self.divButton, 6, 3, 1, 1)
        self.rectButton = QtWidgets.QPushButton(self.frame_2)
        self.rectButton.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.rectButton.setFont(font)
        self.rectButton.setStyleSheet("background-color: rgb(0, 255, 115);")
        self.rectButton.setObjectName("rectButton")
        self.gridLayout.addWidget(self.rectButton, 3, 1, 1, 1)
        self.iButton = QtWidgets.QPushButton(self.frame_2)
        self.iButton.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.iButton.setFont(font)
        self.iButton.setStyleSheet("background-color: rgb(46, 52, 54);\n"
                                   "color: rgb(238, 238, 236);")
        self.iButton.setObjectName("iButton")
        self.gridLayout.addWidget(self.iButton, 7, 0, 1, 1)
        self.n4Button = QtWidgets.QPushButton(self.frame_2)
        self.n4Button.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.n4Button.setFont(font)
        self.n4Button.setStyleSheet("background-color: rgb(46, 52, 54);\n"
                                    "color: rgb(238, 238, 236);")
        self.n4Button.setObjectName("n4Button")
        self.gridLayout.addWidget(self.n4Button, 5, 0, 1, 1)
        self.thetaSpinBox = QtWidgets.QDoubleSpinBox(self.frame_2)
        self.thetaSpinBox.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.thetaSpinBox.setFont(font)
        self.thetaSpinBox.setStyleSheet("background-color: rgb(46, 52, 54);\n"
                                        "color: rgb(238, 238, 236);")
        self.thetaSpinBox.setMinimum(-99999.99)
        self.thetaSpinBox.setMaximum(99999.99)
        self.thetaSpinBox.setObjectName("thetaSpinBox")
        self.gridLayout.addWidget(self.thetaSpinBox, 1, 1, 1, 1)
        self.equButton = QtWidgets.QPushButton(self.frame_2)
        self.equButton.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.equButton.setFont(font)
        self.equButton.setStyleSheet("background-color: rgb(0, 255, 115);")
        self.equButton.setObjectName("equButton")
        self.gridLayout.addWidget(self.equButton, 8, 0, 1, 1)
        self.clearButton = QtWidgets.QPushButton(self.frame_2)
        self.clearButton.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.clearButton.setFont(font)
        self.clearButton.setStyleSheet("background-color: rgb(40, 0, 0);\n"
                                       "color: rgb(204, 0, 0);")
        self.clearButton.setObjectName("clearButton")
        self.gridLayout.addWidget(self.clearButton, 0, 3, 1, 1)
        self.calculateButton = QtWidgets.QPushButton(self.frame_2)
        self.calculateButton.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.calculateButton.setFont(font)
        self.calculateButton.setStyleSheet("background-color: rgb(0, 0, 50);\n"
                                           "color: rgb(50, 50, 236);")
        self.calculateButton.setObjectName("calculateButton")
        self.gridLayout.addWidget(self.calculateButton, 1, 2, 1, 1)
        self.n3Button = QtWidgets.QPushButton(self.frame_2)
        self.n3Button.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.n3Button.setFont(font)
        self.n3Button.setStyleSheet("background-color: rgb(46, 52, 54);\n"
                                    "color: rgb(238, 238, 236);")
        self.n3Button.setObjectName("n3Button")
        self.gridLayout.addWidget(self.n3Button, 6, 2, 1, 1)
        self.polarButton = QtWidgets.QPushButton(self.frame_2)
        self.polarButton.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.polarButton.setFont(font)
        self.polarButton.setStyleSheet("background-color: rgb(0, 255, 115);")
        self.polarButton.setObjectName("polarButton")
        self.gridLayout.addWidget(self.polarButton, 3, 2, 1, 1)
        self.n9Button = QtWidgets.QPushButton(self.frame_2)
        self.n9Button.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.n9Button.setFont(font)
        self.n9Button.setStyleSheet("background-color: rgb(46, 52, 54);\n"
                                    "color: rgb(238, 238, 236);")
        self.n9Button.setObjectName("n9Button")
        self.gridLayout.addWidget(self.n9Button, 4, 2, 1, 1)
        self.openPButton = QtWidgets.QPushButton(self.frame_2)
        self.openPButton.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.openPButton.setFont(font)
        self.openPButton.setStyleSheet("background-color: rgb(46, 52, 54);\n"
                                       "color: rgb(238, 238, 236);")
        self.openPButton.setObjectName("openPButton")
        self.gridLayout.addWidget(self.openPButton, 8, 2, 1, 1)
        self.powButton = QtWidgets.QPushButton(self.frame_2)
        self.powButton.setEnabled(True)
        self.powButton.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.powButton.setFont(font)
        self.powButton.setStyleSheet("background-color: rgb(204, 107, 0);\n"
                                     "color: rgb(238, 238, 236);")
        self.powButton.setFlat(False)
        self.powButton.setObjectName("powButton")
        self.gridLayout.addWidget(self.powButton, 3, 3, 1, 1)
        self.n6Button = QtWidgets.QPushButton(self.frame_2)
        self.n6Button.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.n6Button.setFont(font)
        self.n6Button.setStyleSheet("background-color: rgb(46, 52, 54);\n"
                                    "color: rgb(238, 238, 236);")
        self.n6Button.setObjectName("n6Button")
        self.gridLayout.addWidget(self.n6Button, 5, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(238, 238, 236);")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.subButton = QtWidgets.QPushButton(self.frame_2)
        self.subButton.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.subButton.setFont(font)
        self.subButton.setStyleSheet("background-color: rgb(204, 107, 0);\n"
                                     "color: rgb(238, 238, 236);")
        self.subButton.setObjectName("subButton")
        self.gridLayout.addWidget(self.subButton, 5, 3, 1, 1)
        self.plusButton = QtWidgets.QPushButton(self.frame_2)
        self.plusButton.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.plusButton.setFont(font)
        self.plusButton.setStyleSheet("background-color: rgb(204, 107, 0);\n"
                                      "color: rgb(238, 238, 236);")
        self.plusButton.setObjectName("plusButton")
        self.gridLayout.addWidget(self.plusButton, 4, 3, 1, 1)
        self.n1Button = QtWidgets.QPushButton(self.frame_2)
        self.n1Button.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.n1Button.setFont(font)
        self.n1Button.setStyleSheet("background-color: rgb(46, 52, 54);\n"
                                    "color: rgb(238, 238, 236);")
        self.n1Button.setObjectName("n1Button")
        self.gridLayout.addWidget(self.n1Button, 6, 0, 1, 1)
        self.n7Button = QtWidgets.QPushButton(self.frame_2)
        self.n7Button.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.n7Button.setFont(font)
        self.n7Button.setStyleSheet("background-color: rgb(46, 52, 54);\n"
                                    "color: rgb(238, 238, 236);")
        self.n7Button.setAutoDefault(False)
        self.n7Button.setDefault(False)
        self.n7Button.setFlat(False)
        self.n7Button.setObjectName("n7Button")
        self.gridLayout.addWidget(self.n7Button, 4, 0, 1, 1)
        self.eButton = QtWidgets.QPushButton(self.frame_2)
        self.eButton.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.eButton.setFont(font)
        self.eButton.setStyleSheet("background-color: rgb(46, 52, 54);\n"
                                   "color: rgb(238, 238, 236);")
        self.eButton.setObjectName("eButton")
        self.gridLayout.addWidget(self.eButton, 8, 1, 1, 1)
        self.rhoSpinBox = QtWidgets.QDoubleSpinBox(self.frame_2)
        self.rhoSpinBox.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.rhoSpinBox.setFont(font)
        self.rhoSpinBox.setStyleSheet("background-color: rgb(46, 52, 54);\n"
                                      "color: rgb(238, 238, 236);")
        self.rhoSpinBox.setWrapping(False)
        self.rhoSpinBox.setFrame(True)
        self.rhoSpinBox.setMinimum(-99999.99)
        self.rhoSpinBox.setMaximum(99999.99)
        self.rhoSpinBox.setObjectName("rhoSpinBox")
        self.gridLayout.addWidget(self.rhoSpinBox, 1, 0, 1, 1)
        self.n5Button = QtWidgets.QPushButton(self.frame_2)
        self.n5Button.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.n5Button.setFont(font)
        self.n5Button.setStyleSheet("background-color: rgb(46, 52, 54);\n"
                                    "color: rgb(238, 238, 236);")
        self.n5Button.setObjectName("n5Button")
        self.gridLayout.addWidget(self.n5Button, 5, 1, 1, 1)
        self.expButton = QtWidgets.QPushButton(self.frame_2)
        self.expButton.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.expButton.setFont(font)
        self.expButton.setStyleSheet("background-color: rgb(0, 255, 115);")
        self.expButton.setObjectName("expButton")
        self.gridLayout.addWidget(self.expButton, 3, 0, 1, 1)
        self.n8Button = QtWidgets.QPushButton(self.frame_2)
        self.n8Button.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.n8Button.setFont(font)
        self.n8Button.setStyleSheet("background-color: rgb(46, 52, 54);\n"
                                    "color: rgb(238, 238, 236);")
        self.n8Button.setObjectName("n8Button")
        self.gridLayout.addWidget(self.n8Button, 4, 1, 1, 1)
        self.n0Button = QtWidgets.QPushButton(self.frame_2)
        self.n0Button.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.n0Button.setFont(font)
        self.n0Button.setStyleSheet("background-color: rgb(46, 52, 54);\n"
                                    "color: rgb(238, 238, 236);")
        self.n0Button.setObjectName("n0Button")
        self.gridLayout.addWidget(self.n0Button, 7, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(238, 238, 236);")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.closePButton = QtWidgets.QPushButton(self.frame_2)
        self.closePButton.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.closePButton.setFont(font)
        self.closePButton.setStyleSheet("background-color: rgb(46, 52, 54);\n"
                                        "color: rgb(238, 238, 236);")
        self.closePButton.setObjectName("closePButton")
        self.gridLayout.addWidget(self.closePButton, 8, 3, 1, 1)
        self.backspaceButton = QtWidgets.QPushButton(self.frame_2)
        self.backspaceButton.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.backspaceButton.setFont(font)
        self.backspaceButton.setStyleSheet("background-color: rgb(40, 0, 0);\n"
                                           "color: rgb(204, 0, 0);")
        self.backspaceButton.setObjectName("backspaceButton")
        self.gridLayout.addWidget(self.backspaceButton, 1, 3, 1, 1)
        self.verticalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.fontSpinBox = QtWidgets.QSpinBox(self.frame)
        self.fontSpinBox.setObjectName("fontSpinBox")
        self.fontSpinBox.setStyleSheet("background-color: rgb(46, 52, 54);\n"
                                       "color: rgb(238, 238, 236);")
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.fontSpinBox.setFont(font)
        self.fontSpinBox.setMinimum(1)
        self.fontSpinBox.setMaximum(999)
        self.fontSpinBox.setValue(36)

        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.fontSpinBox)
        MainWindow.setStatusBar(self.statusbar)
        self.fontSpinBox.valueChanged.connect(self.on_font_size_change)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Complex Calculator"))
        self.label.setText(_translate("MainWindow", "r"))
        self.label_2.setText(_translate("MainWindow", "θ"))
        self.n0Button.setText(_translate("MainWindow", "0"))
        self.n0Button.clicked.connect(lambda: self.append('0'))
        self.n1Button.setText(_translate("MainWindow", "1"))
        self.n1Button.clicked.connect(lambda: self.append('1'))
        self.n2Button.setText(_translate("MainWindow", "2"))
        self.n2Button.clicked.connect(lambda: self.append('2'))
        self.n3Button.setText(_translate("MainWindow", "3"))
        self.n3Button.clicked.connect(lambda: self.append('3'))
        self.n4Button.setText(_translate("MainWindow", "4"))
        self.n4Button.clicked.connect(lambda: self.append('4'))
        self.n5Button.setText(_translate("MainWindow", "5"))
        self.n5Button.clicked.connect(lambda: self.append('5'))
        self.n6Button.setText(_translate("MainWindow", "6"))
        self.n6Button.clicked.connect(lambda: self.append('6'))
        self.n7Button.setText(_translate("MainWindow", "7"))
        self.n7Button.clicked.connect(lambda: self.append('7'))
        self.n8Button.setText(_translate("MainWindow", "8"))
        self.n8Button.clicked.connect(lambda: self.append('8'))
        self.n9Button.setText(_translate("MainWindow", "9"))
        self.n9Button.clicked.connect(lambda: self.append('9'))
        self.powButton.setText(_translate("MainWindow", "pow"))
        self.powButton.clicked.connect(lambda: self.append('^'))
        self.plusButton.setText(_translate("MainWindow", "➕"))
        self.plusButton.clicked.connect(lambda: self.append('+'))
        self.subButton.setText(_translate("MainWindow", "➖"))
        self.subButton.clicked.connect(lambda: self.append('-'))
        self.divButton.setText(_translate("MainWindow", "➗"))
        self.divButton.clicked.connect(lambda: self.append('/'))
        self.mulButton.setText(_translate("MainWindow", "✖"))
        self.mulButton.clicked.connect(lambda: self.append('*'))
        self.openPButton.setText(_translate("MainWindow", "("))
        self.openPButton.clicked.connect(lambda: self.append('('))
        self.closePButton.setText(_translate("MainWindow", ")"))
        self.closePButton.clicked.connect(lambda: self.append(')'))
        self.dotButton.setText(_translate("MainWindow", "."))
        self.dotButton.clicked.connect(lambda: self.append('.'))
        self.eButton.setText(_translate("MainWindow", "e"))
        self.eButton.clicked.connect(lambda: self.append('e'))
        self.iButton.setText(_translate("MainWindow", "i"))
        self.iButton.clicked.connect(lambda: self.append('i'))
        self.clearButton.setText(_translate("MainWindow", "C"))
        self.clearButton.clicked.connect(self.clear)
        self.backspaceButton.setText(_translate("MainWindow", "⬅"))
        self.backspaceButton.clicked.connect(self.pop)
        self.calculateButton.setText(_translate("MainWindow", "cal"))
        self.calculateButton.clicked.connect(self.calculate)
        self.rectButton.setText(_translate("MainWindow", "rect"))
        self.rectButton.clicked.connect(self.rect)
        self.polarButton.setText(_translate("MainWindow", "polar"))
        self.polarButton.clicked.connect(self.polar)
        self.expButton.setText(_translate("MainWindow", "exp"))
        self.expButton.clicked.connect(self.exp)
        self.equButton.setText(_translate("MainWindow", "equ"))
        self.equButton.clicked.connect(self.equ)

    def on_font_size_change(self):
        if self.fontSpinBox.value() > 99:
            self.fontSpinBox.setValue(99)
            return
        self.fontSize = self.fontSpinBox.value()
        self._update_display()

    def _update_display(self):
        _translate = QtCore.QCoreApplication.translate
        self.display.setHtml(
            _translate("MainWindow",
                       "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                       "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                       "p, li { white-space: pre-wrap; }\n"
                       "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
                       f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:{self.fontSize}pt; font-weight:600; color:#eeeeec;\">{self.text}</span></p></body></html>"))

    def calculate(self):
        rho = self.rhoSpinBox.value()
        theta = self.thetaSpinBox.value()
        cn = pol2rct(rho, theta)
        self.set(str_rect(cn))

    def rect(self):
        if not self.text:
            return
        cn = to_complex(self.text)
        if cn is None:
            self.error()
            return
        self.set(str_rect(cn))

    def exp(self):
        if not self.text:
            return
        cn = to_complex(self.text)
        if cn is None:
            self.error()
            return
        self.set(str_exp(cn))

    def polar(self):
        if not self.text:
            return
        cn = to_complex(self.text)
        if cn is None:
            self.error()
            return
        self.set(str_pol(cn))

    def equ(self):
        tmp = self.text
        self.text = 'I love maths!'
        self._update_display()
        self.text = tmp

    def append(self, txt: str):
        if self.text == '0' and txt != '.':
            self.text = txt
        elif self.text and self.text[-1] in '-+/*^' and txt in '-+/*^':
            self.text = self.text[:-1] + txt
        else:
            self.text += txt
        self._update_display()

    def clear(self):
        self.text = ''
        self._update_display()

    def pop(self):
        self.text = self.text[:-1]
        self._update_display()

    def set(self, txt: str):
        self.text = txt
        self._update_display()

    def error(self):
        self.text = 'Error'
        self._update_display()
        self.text = ''


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
