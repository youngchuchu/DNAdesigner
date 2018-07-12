# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'easyDietz.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QComboBox, QApplication, QGraphicsView, QGraphicsScene, QGraphicsItem, QGridLayout, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton)
from PyQt5.QtGui import QIcon, QPixmap


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(346, 272)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 0, 421, 231))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.twoTALgraphicsViewer = QtWidgets.QLabel(self.tab_1)
        self.twoTALgraphicsViewer.setGeometry(QtCore.QRect(160, 9, 161, 91))
        self.twoTALgraphicsViewer.setObjectName("twoTALgraphicsViewer")
        self.twoTALsequenceViewer = QtWidgets.QTextBrowser(self.tab_1)
        self.twoTALsequenceViewer.setGeometry(QtCore.QRect(160, 108, 161, 91))
        self.twoTALsequenceViewer.setObjectName("twoTALsequenceViewer")
        self.twoTALshowImageButton = QtWidgets.QPushButton(self.tab_1)
        self.twoTALshowImageButton.setGeometry(QtCore.QRect(10, 36, 141, 20))
        self.twoTALshowImageButton.setObjectName("twoTALshowImageButton")
        self.twoTALshowSequenceButton = QtWidgets.QPushButton(self.tab_1)
        self.twoTALshowSequenceButton.setGeometry(QtCore.QRect(10, 57, 141, 20))
        self.twoTALshowSequenceButton.setObjectName("twoTALshowSequenceButton")
        self.twoTALstructureSelector = QtWidgets.QComboBox(self.tab_1)
        self.twoTALstructureSelector.setGeometry(QtCore.QRect(10, 10, 140, 20))
        self.twoTALstructureSelector.setObjectName("twoTALstructureSelector")
        self.twoTALstructureSelector.addItem("")
        self.twoTALstructureSelector.addItem("")
        self.twoTALstructureSelector.addItem("")
        self.twoTALenzymeSpaceLabel = QtWidgets.QLabel(self.tab_1)
        self.twoTALenzymeSpaceLabel.setGeometry(QtCore.QRect(10, 115, 111, 10))
        self.twoTALenzymeSpaceLabel.setObjectName("twoTALenzymeSpaceLabel")
        self.twoTALdihedralAngleLabel = QtWidgets.QLabel(self.tab_1)
        self.twoTALdihedralAngleLabel.setGeometry(QtCore.QRect(10, 130, 111, 20))
        self.twoTALdihedralAngleLabel.setObjectName("twoTALdihedralAngleLabel")
        self.twoTALcalculateParametersButton = QtWidgets.QPushButton(self.tab_1)
        self.twoTALcalculateParametersButton.setGeometry(QtCore.QRect(10, 79, 141, 20))
        self.twoTALcalculateParametersButton.setObjectName("twoTALcalculateParametersButton")
        self.twoTALsequenceSizeLabel = QtWidgets.QLabel(self.tab_1)
        self.twoTALsequenceSizeLabel.setGeometry(QtCore.QRect(10, 150, 71, 20))
        self.twoTALsequenceSizeLabel.setObjectName("twoTALsequenceSizeLabel")
        self.twoTALdimerizabilityLabel = QtWidgets.QLabel(self.tab_1)
        self.twoTALdimerizabilityLabel.setGeometry(QtCore.QRect(10, 171, 71, 20))
        self.twoTALdimerizabilityLabel.setObjectName("twoTALdimerizabilityLabel")
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 346, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuTutorials = QtWidgets.QMenu(self.menubar)
        self.menuTutorials.setObjectName("menuTutorials")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionDocumentation = QtWidgets.QAction(MainWindow)
        self.actionDocumentation.setObjectName("actionDocumentation")
        self.actionContact = QtWidgets.QAction(MainWindow)
        self.actionContact.setObjectName("actionContact")
        self.menuTutorials.addAction(self.actionDocumentation)
        self.menuTutorials.addAction(self.actionContact)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuTutorials.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Recommended TAL structure generator"))
        self.twoTALshowImageButton.setText(_translate("MainWindow", "Show Image"))
        self.twoTALshowSequenceButton.setText(_translate("MainWindow", "Show Sequence"))
        self.twoTALstructureSelector.setItemText(0, _translate("MainWindow", "two-helix Type A"))
        self.twoTALstructureSelector.setItemText(1, _translate("MainWindow", "two-helix Type B"))
        self.twoTALstructureSelector.setItemText(2, _translate("MainWindow", "two-helix Type C"))
        self.twoTALenzymeSpaceLabel.setText(_translate("MainWindow", "Enzyme space:"))
        self.twoTALdihedralAngleLabel.setText(_translate("MainWindow", "Dihedral angle:"))
        self.twoTALcalculateParametersButton.setText(_translate("MainWindow", "Calculate parameters"))
        self.twoTALsequenceSizeLabel.setText(_translate("MainWindow", "Sequence size:"))
        self.twoTALdimerizabilityLabel.setText(_translate("MainWindow", "Dimerizability:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "2-TAL Structure"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "3-TAL Structure"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Arc Structures"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuTutorials.setTitle(_translate("MainWindow", "Tutorials"))
        self.actionDocumentation.setText(_translate("MainWindow", "Documentation"))
        self.actionContact.setText(_translate("MainWindow", "Contact"))

        # connect to actions in GUI
        self.twoTALshowSequenceButton.clicked.connect(self.showSequence)
        self.twoTALcalculateParametersButton.clicked.connect(self.calculateParameters)
        self.twoTALshowImageButton.clicked.connect(self.drawImage)
        # self.twoTALshowImageButton.clicked.connect(self.displayGraphic)
    
    def showSequence(self):
        # get data from the ComboBox in the GUI
        TALstructureType = str(self.twoTALstructureSelector.currentText())
        
        if TALstructureType == "two-helix Type A":
            primarySequence = "tCTGCTCGACGTAACTGACGTATACTGTGGAtCCAAGAGCGCTGATTACATTTGCGCAGTTACtCCGGTGAATCCACATTTACCATTCCTATACtTCTTCCATCCTGGATAGAGTGACATAGATAGtCCGGTCCGTGTTAGCGATGCGGAAAAGAGtTCAGTAGTACCGATAGTATCCAATTGGGCATtTCAGATGATCGCTGTCGTTCCTGGTTGCACtCGTGATAATTTGTGCGATCTCAGTCAGTAAAtATAAATGTCGGTTGCCGTCTTTGTCCATGCtACAGCGCACCTCTAATACCTCCTATCACAAGtTCGACGAAACGTTACGCCTCGGACTAACACtATTAAGCGCCGCGGTCCAGCAGAGGGTACCGCAGCCCTCCTTAGCATAGCTAGCCCTAAGTGAGCTTCAGGCCATGAGACAGCCAAGGGGTCAGTCGCAATAGTCGGATGAGCGTCAGGGGGTAGTGCGTGTGTGTTATACCAACGAGGTATCGACTGTAGATTCGTACGTGGGAGATTGTCGGAGCCAATCCTCCGATATAATGCCCGGGATCTGAGCCtCATAATTCATAGATCTCGAACAGTGGCTCAtCAATATCGATTCATCTGAATTCACCCGATAGtTACTATCGATTGATCTCGAACTTGATAGTTtCATCAGCGGATCATCTCGATTCGAGACAAAAtAGTTATACATGTACTGGTAACTCCACAAGAtAGCTAGTATTTCATCCAATACGGTCGTTGTAtTACAAGTGGCTCATTGGCGACTAAGCCGACtTGTCACTCACTAATGCAGGCGGCCAGCACCGtCAATACGCGAGCATTCTAGTTTTTTGAAGTtTTACAGTGATAAAATCTTACCAGTGGGGCGTtTCATGTTATAACGGACGGGTAAATAACGAAtCGTGAACCGACAACTCTTGA"
        elif TALstructureType == "two-helix Type B":
            primarySequence = "tCTGCTCGACGTAACTGACGTATACTGTGACCCGTCCGTTATAACATGAaGTTGCGCAGTTACtCCGGTGAATCCACATTTACCATTCCTATACTAGAATGCTCGCGTATTGaTGGACATAGATAGtCCGGTCCGTGTTAGCGATGCGGAAAAAGTCGCCAATGAGCCACTTGTAaCACAATTGGGCATtTCAGATGATCGCTGTCGTTCCTGGTTGCTTACCAGTACATGTATAACTaCTCAGTCAGTAAAtATAAATGTCGGTTGCCGTCTTTGTCCATTTCGAGATCAATCGATAGTAaGACCTATCACAAGtTCGACGAAACGTTACGCCTCGGACTAACTTCGAGATCTATGAATTATGaACAGAGGGTACCGCAGCCCTCCTTAGCATAGCTAGCCCTAAGTGAGCTTCAGGCCATGAGACAGCCAAGGGGTCAGTCGCAATAGTCGGATGAGCGTCAGGGGGTAGTGCGTGTGTGTTATACCAACGAGGTATCGACTGTAGATTCGTACGTGGGAGATTGTCGGAGCCAATCCTCCGATATAATGCCCGGGATCTGAGGCTGGACCGCGGCGCTTAATaCCCAGTGGCTCATtCAATATCGATTCATCTGAATCACCCGATAGGTATTAGAGGTGCGCTGTaGGCTTGATAGTTAtCATCAGCGGATCATCTCGATCGAGACAAAGATCGCACAAATTATCACGaAACTCCACAAGAAtAGCTAGTATTTCATCCAATAGGTCGTTGGATACTATCGGTACTACTGAaGCCTAAGCCGACAtTGTCACTCACTAATGCAGGCGCCAGCACACTCTATCCAGGATGGAAGAaACTTTTTGAAGTCtTTACAGTGATAAAATCTTACAGTGGGGCAATGTAATCAGCGCTCTTGGaCCAAATAACGAAAtCGTGAACCGACAACTCTTGA" 
        else:
            primarySequence = "tCTGCTCGACGTAACTGACGTATACTGTGGAATGTAATCAGCGCTCTTGGaTTGCGCAGTTACtCCGGTGAATCCACATTTACCATTCCTATAACTCTATCCAGGATGGAAGAaGGACATAGATAGtCCGGTCCGTGTTAGCGATGCGGAAAAAGAGATACTATCGGTACTACTGAaACAATTGGGCATtTCAGATGATCGCTGTCGTTCCTGGTTGCAAGATCGCACAAATTATCACGaTCAGTCAGTAAAtATAAATGTCGGTTGCCGTCTTTGTCCATGAGGTATTAGAGGTGCGCTGTaACCTATCACAAGtTCGACGAAACGTTACGCCTCGGACTAACAGCTGGACCGCGGCGCTTAATaCAGAGGGTACCGCAGCCCTCCTTAGCATAGCTAGCCCTAAGTGAGCTTCAGGCCATGAGACAGCCAAGGGGTCAGTCGCAATAGTCGGATGAGCGTCAGGGGGTAGTGCGTGTGTGTTATACCAACGAGGTATCGACTGTAGATTCGTACGTGGGAGATTGTCGGAGCCAATCCTCCGATATAATGCCCGGGATCTGAGCTTCGAGATCTATGAATTATGaCCAGTGGCTCATTtCAATATCGATTCATCTGAATACCCGATATTCGAGATCAATCGATAGTAaGCTTGATAGTTAAtCATCAGCGGATCATCTCGATGAGACAAATTACCAGTACATGTATAACTaACTCCACAAGAAAtAGCTAGTATTTCATCCAATAGTCGTTGTTCGCCAATGAGCCACTTGTAaCCTAAGCCGACATtTGTCACTCACTAATGCAGGCCCAGCACCACTAGAATGCTCGCGTATTGaCTTTTTGAAGTCCtTTACAGTGATAAAATCTTACGTGGGGCGACCCGTCCGTTATAACATGAaCAAATAACGAAAGtCGTGAACCGACAACTCTTGA"
        
        #Show the sequence in the text editor
        self.twoTALsequenceViewer.setText(primarySequence)       
        
    
    def calculateParameters(self):
        # get data from the ComboBox in the GUI
        TALstructureType = str(self.twoTALstructureSelector.currentText())
        
        if TALstructureType == "two-helix Type A":
            nmDistance = 12.2
            bpDistance = (str((nmDistance)/0.34))
            dihedralAngle = (((nmDistance)%10)/10)*360
            primarySequence = "tCTGCTCGACGTAACTGACGTATACTGTGGAtCCAAGAGCGCTGATTACATTTGCGCAGTTACtCCGGTGAATCCACATTTACCATTCCTATACtTCTTCCATCCTGGATAGAGTGACATAGATAGtCCGGTCCGTGTTAGCGATGCGGAAAAGAGtTCAGTAGTACCGATAGTATCCAATTGGGCATtTCAGATGATCGCTGTCGTTCCTGGTTGCACtCGTGATAATTTGTGCGATCTCAGTCAGTAAAtATAAATGTCGGTTGCCGTCTTTGTCCATGCtACAGCGCACCTCTAATACCTCCTATCACAAGtTCGACGAAACGTTACGCCTCGGACTAACACtATTAAGCGCCGCGGTCCAGCAGAGGGTACCGCAGCCCTCCTTAGCATAGCTAGCCCTAAGTGAGCTTCAGGCCATGAGACAGCCAAGGGGTCAGTCGCAATAGTCGGATGAGCGTCAGGGGGTAGTGCGTGTGTGTTATACCAACGAGGTATCGACTGTAGATTCGTACGTGGGAGATTGTCGGAGCCAATCCTCCGATATAATGCCCGGGATCTGAGCCtCATAATTCATAGATCTCGAACAGTGGCTCAtCAATATCGATTCATCTGAATTCACCCGATAGtTACTATCGATTGATCTCGAACTTGATAGTTtCATCAGCGGATCATCTCGATTCGAGACAAAAtAGTTATACATGTACTGGTAACTCCACAAGAtAGCTAGTATTTCATCCAATACGGTCGTTGTAtTACAAGTGGCTCATTGGCGACTAAGCCGACtTGTCACTCACTAATGCAGGCGGCCAGCACCGtCAATACGCGAGCATTCTAGTTTTTTGAAGTtTTACAGTGATAAAATCTTACCAGTGGGGCGTtTCATGTTATAACGGACGGGTAAATAACGAAtCGTGAACCGACAACTCTTGA"
            dimerizability = "High"
            
        elif TALstructureType == "two-helix Type B":
            nmDistance = 19.5
            bpDistance = (str((nmDistance)/0.34))
            dihedralAngle = (((nmDistance)%10)/10)*360
            primarySequence = "tCTGCTCGACGTAACTGACGTATACTGTGACCCGTCCGTTATAACATGAaGTTGCGCAGTTACtCCGGTGAATCCACATTTACCATTCCTATACTAGAATGCTCGCGTATTGaTGGACATAGATAGtCCGGTCCGTGTTAGCGATGCGGAAAAAGTCGCCAATGAGCCACTTGTAaCACAATTGGGCATtTCAGATGATCGCTGTCGTTCCTGGTTGCTTACCAGTACATGTATAACTaCTCAGTCAGTAAAtATAAATGTCGGTTGCCGTCTTTGTCCATTTCGAGATCAATCGATAGTAaGACCTATCACAAGtTCGACGAAACGTTACGCCTCGGACTAACTTCGAGATCTATGAATTATGaACAGAGGGTACCGCAGCCCTCCTTAGCATAGCTAGCCCTAAGTGAGCTTCAGGCCATGAGACAGCCAAGGGGTCAGTCGCAATAGTCGGATGAGCGTCAGGGGGTAGTGCGTGTGTGTTATACCAACGAGGTATCGACTGTAGATTCGTACGTGGGAGATTGTCGGAGCCAATCCTCCGATATAATGCCCGGGATCTGAGGCTGGACCGCGGCGCTTAATaCCCAGTGGCTCATtCAATATCGATTCATCTGAATCACCCGATAGGTATTAGAGGTGCGCTGTaGGCTTGATAGTTAtCATCAGCGGATCATCTCGATCGAGACAAAGATCGCACAAATTATCACGaAACTCCACAAGAAtAGCTAGTATTTCATCCAATAGGTCGTTGGATACTATCGGTACTACTGAaGCCTAAGCCGACAtTGTCACTCACTAATGCAGGCGCCAGCACACTCTATCCAGGATGGAAGAaACTTTTTGAAGTCtTTACAGTGATAAAATCTTACAGTGGGGCAATGTAATCAGCGCTCTTGGaCCAAATAACGAAAtCGTGAACCGACAACTCTTGA"             
            dimerizability = "Low"
        
        else:
            nmDistance = 15.1
            bpDistance = (str((nmDistance)/0.34))
            dihedralAngle = (((nmDistance)%10)/10)*360
            primarySequence = "tCTGCTCGACGTAACTGACGTATACTGTGGAATGTAATCAGCGCTCTTGGaTTGCGCAGTTACtCCGGTGAATCCACATTTACCATTCCTATAACTCTATCCAGGATGGAAGAaGGACATAGATAGtCCGGTCCGTGTTAGCGATGCGGAAAAAGAGATACTATCGGTACTACTGAaACAATTGGGCATtTCAGATGATCGCTGTCGTTCCTGGTTGCAAGATCGCACAAATTATCACGaTCAGTCAGTAAAtATAAATGTCGGTTGCCGTCTTTGTCCATGAGGTATTAGAGGTGCGCTGTaACCTATCACAAGtTCGACGAAACGTTACGCCTCGGACTAACAGCTGGACCGCGGCGCTTAATaCAGAGGGTACCGCAGCCCTCCTTAGCATAGCTAGCCCTAAGTGAGCTTCAGGCCATGAGACAGCCAAGGGGTCAGTCGCAATAGTCGGATGAGCGTCAGGGGGTAGTGCGTGTGTGTTATACCAACGAGGTATCGACTGTAGATTCGTACGTGGGAGATTGTCGGAGCCAATCCTCCGATATAATGCCCGGGATCTGAGCTTCGAGATCTATGAATTATGaCCAGTGGCTCATTtCAATATCGATTCATCTGAATACCCGATATTCGAGATCAATCGATAGTAaGCTTGATAGTTAAtCATCAGCGGATCATCTCGATGAGACAAATTACCAGTACATGTATAACTaACTCCACAAGAAAtAGCTAGTATTTCATCCAATAGTCGTTGTTCGCCAATGAGCCACTTGTAaCCTAAGCCGACATtTGTCACTCACTAATGCAGGCCCAGCACCACTAGAATGCTCGCGTATTGaCTTTTTGAAGTCCtTTACAGTGATAAAATCTTACGTGGGGCGACCCGTCCGTTATAACATGAaCAAATAACGAAAGtCGTGAACCGACAACTCTTGA"
            dimerizability = "Low"
            
        self.twoTALenzymeSpaceLabel.setText("Dist: "+str(nmDistance)+"nm, "+str(round(float(bpDistance),0))+"bp")
        self.twoTALdihedralAngleLabel.setText("Dihedral: " + str(round(dihedralAngle,1)) + "°")
        self.twoTALsequenceSizeLabel.setText("Length: " + str(len(primarySequence))+"bp")
        self.twoTALdimerizabilityLabel.setText("Dimers: " + str(dimerizability))
        
    def drawImage(self):
        TALstructureType = str(self.twoTALstructureSelector.currentText())
        
        if TALstructureType == "two-helix Type A":
            pixmap = QPixmap('2TALtypeA.png')
            
        elif TALstructureType == "two-helix Type B":
            pixmap = QPixmap('2TALtypeB.png')

        else:
            pixmap = QPixmap('2TALtypeC.png')           
    
        self.twoTALgraphicsViewer.setPixmap(pixmap)
    
    
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

# program has been debugged in Windows command line
