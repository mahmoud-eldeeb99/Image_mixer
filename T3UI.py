# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'T3UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1353, 724)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 330, 1331, 20))
        self.line.setLineWidth(2)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(650, 10, 21, 651))
        self.line_2.setLineWidth(2)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 360, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(700, 360, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(1040, 360, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(700, 10, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.comboBox_img1 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_img1.setGeometry(QtCore.QRect(400, 20, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_img1.setFont(font)
        self.comboBox_img1.setObjectName("comboBox_img1")
        self.comboBox_img1.addItem("")
        self.comboBox_img1.addItem("")
        self.comboBox_img1.addItem("")
        self.comboBox_img1.addItem("")
        self.comboBox_img1.addItem("")
        self.comboBox_img2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_img2.setGeometry(QtCore.QRect(400, 360, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_img2.setFont(font)
        self.comboBox_img2.setObjectName("comboBox_img2")
        self.comboBox_img2.addItem("")
        self.comboBox_img2.addItem("")
        self.comboBox_img2.addItem("")
        self.comboBox_img2.addItem("")
        self.comboBox_img2.addItem("")
        self.component1_image_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.component1_image_comboBox.setGeometry(QtCore.QRect(900, 80, 171, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.component1_image_comboBox.setFont(font)
        self.component1_image_comboBox.setObjectName("component1_image_comboBox")
        self.component1_image_comboBox.addItem("")
        self.component1_image_comboBox.addItem("")
        self.component1_image_comboBox.addItem("")
        self.component2_image_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.component2_image_comboBox.setGeometry(QtCore.QRect(900, 170, 171, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.component2_image_comboBox.setFont(font)
        self.component2_image_comboBox.setObjectName("component2_image_comboBox")
        self.component2_image_comboBox.addItem("")
        self.component2_image_comboBox.addItem("")
        self.component2_image_comboBox.addItem("")
        self.component2_image_comboBox.addItem("")
        self.component2_image_comboBox.setItemText(3, "")
        self.component1_component_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.component1_component_comboBox.setGeometry(QtCore.QRect(900, 120, 431, 22))
        self.component1_component_comboBox.setObjectName("component1_component_comboBox")
        self.component1_component_comboBox.addItem("")
        self.component1_component_comboBox.addItem("")
        self.component1_component_comboBox.addItem("")
        self.component1_component_comboBox.addItem("")
        self.component1_component_comboBox.addItem("")
        self.component1_component_comboBox.addItem("")
        self.component1_component_comboBox.addItem("")
        self.component2_component_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.component2_component_comboBox.setGeometry(QtCore.QRect(900, 210, 431, 22))
        self.component2_component_comboBox.setObjectName("component2_component_comboBox")
        self.component2_component_comboBox.addItem("")
        self.component2_component_comboBox.addItem("")
        self.component2_component_comboBox.addItem("")
        self.component2_component_comboBox.addItem("")
        self.component2_component_comboBox.addItem("")
        self.component2_component_comboBox.addItem("")
        self.component2_component_comboBox.addItem("")
        self.component1_Percentage = QtWidgets.QSlider(self.centralwidget)
        self.component1_Percentage.setGeometry(QtCore.QRect(1110, 80, 221, 22))
        self.component1_Percentage.setOrientation(QtCore.Qt.Horizontal)
        self.component1_Percentage.setObjectName("component1_Percentage")
        self.component2_Percentage = QtWidgets.QSlider(self.centralwidget)
        self.component2_Percentage.setGeometry(QtCore.QRect(1110, 170, 221, 22))
        self.component2_Percentage.setOrientation(QtCore.Qt.Horizontal)
        self.component2_Percentage.setObjectName("component2_Percentage")
        self.comboBox_output = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_output.setGeometry(QtCore.QRect(900, 10, 431, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_output.setFont(font)
        self.comboBox_output.setObjectName("comboBox_output")
        self.comboBox_output.addItem("")
        self.comboBox_output.addItem("")
        self.comboBox_output.addItem("")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(700, 80, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(700, 170, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.showImage_button = QtWidgets.QPushButton(self.centralwidget)
        self.showImage_button.setGeometry(QtCore.QRect(150, 20, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.showImage_button.setFont(font)
        self.showImage_button.setObjectName("showImage_button")
        self.showImage2_button = QtWidgets.QPushButton(self.centralwidget)
        self.showImage2_button.setGeometry(QtCore.QRect(140, 360, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.showImage2_button.setFont(font)
        self.showImage2_button.setObjectName("showImage2_button")
        self.applyChanges_Button = QtWidgets.QPushButton(self.centralwidget)
        self.applyChanges_Button.setGeometry(QtCore.QRect(700, 280, 621, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.applyChanges_Button.setFont(font)
        self.applyChanges_Button.setObjectName("applyChanges_Button")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(680, 50, 661, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(680, 150, 661, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(680, 250, 661, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(310, 690, 501, 20))
        self.label_8.setObjectName("label_8")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(10, 670, 1331, 20))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 60, 631, 261))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.image1_graphicsView = PlotWidget(self.layoutWidget)
        self.image1_graphicsView.setObjectName("image1_graphicsView")
        self.horizontalLayout.addWidget(self.image1_graphicsView)
        self.components_graphicsView = PlotWidget(self.layoutWidget)
        self.components_graphicsView.setObjectName("components_graphicsView")
        self.horizontalLayout.addWidget(self.components_graphicsView)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 400, 631, 261))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.image1_graphicsView_2 = PlotWidget(self.layoutWidget1)
        self.image1_graphicsView_2.setObjectName("image1_graphicsView_2")
        self.horizontalLayout_2.addWidget(self.image1_graphicsView_2)
        self.components_graphicsView2 = PlotWidget(self.layoutWidget1)
        self.components_graphicsView2.setObjectName("components_graphicsView2")
        self.horizontalLayout_2.addWidget(self.components_graphicsView2)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(680, 400, 661, 261))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.output1_graphicsView = PlotWidget(self.layoutWidget2)
        self.output1_graphicsView.setObjectName("output1_graphicsView")
        self.horizontalLayout_3.addWidget(self.output1_graphicsView)
        self.output2_graphicsView = PlotWidget(self.layoutWidget2)
        self.output2_graphicsView.setObjectName("output2_graphicsView")
        self.horizontalLayout_3.addWidget(self.output2_graphicsView)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1353, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Image 1"))
        self.label_2.setText(_translate("MainWindow", "Image 2"))
        self.label_3.setText(_translate("MainWindow", "Output 1"))
        self.label_4.setText(_translate("MainWindow", "output 2"))
        self.label_5.setText(_translate("MainWindow", "Mixer output to :"))
        self.comboBox_img1.setItemText(0, _translate("MainWindow", "Mag, phase, Real, Imag"))
        self.comboBox_img1.setItemText(1, _translate("MainWindow", "Magnitude"))
        self.comboBox_img1.setItemText(2, _translate("MainWindow", "Phase"))
        self.comboBox_img1.setItemText(3, _translate("MainWindow", "Real"))
        self.comboBox_img1.setItemText(4, _translate("MainWindow", "Imag"))
        self.comboBox_img2.setItemText(0, _translate("MainWindow", "Mag, phase, Real, Imag"))
        self.comboBox_img2.setItemText(1, _translate("MainWindow", "Magnitude"))
        self.comboBox_img2.setItemText(2, _translate("MainWindow", "Phase"))
        self.comboBox_img2.setItemText(3, _translate("MainWindow", "Real"))
        self.comboBox_img2.setItemText(4, _translate("MainWindow", "Imag"))
        self.component1_image_comboBox.setItemText(0, _translate("MainWindow", "Img1, Img 2"))
        self.component1_image_comboBox.setItemText(1, _translate("MainWindow", "Image1"))
        self.component1_image_comboBox.setItemText(2, _translate("MainWindow", "Image2"))
        self.component2_image_comboBox.setItemText(0, _translate("MainWindow", "Img1, Img 2"))
        self.component2_image_comboBox.setItemText(1, _translate("MainWindow", "Image1"))
        self.component2_image_comboBox.setItemText(2, _translate("MainWindow", "Image2"))
        self.component1_component_comboBox.setItemText(0, _translate("MainWindow", "Mag, Real, Imag, uniMag, uniPhase"))
        self.component1_component_comboBox.setItemText(1, _translate("MainWindow", "Magnitude"))
        self.component1_component_comboBox.setItemText(2, _translate("MainWindow", "Phase"))
        self.component1_component_comboBox.setItemText(3, _translate("MainWindow", "Real"))
        self.component1_component_comboBox.setItemText(4, _translate("MainWindow", "Imag"))
        self.component1_component_comboBox.setItemText(5, _translate("MainWindow", "Uni_Mag"))
        self.component1_component_comboBox.setItemText(6, _translate("MainWindow", "Uni_Phase"))
        self.component2_component_comboBox.setItemText(0, _translate("MainWindow", "Mag, Real, Imag, uniMag, uniPhase"))
        self.component2_component_comboBox.setItemText(1, _translate("MainWindow", "Magnitude"))
        self.component2_component_comboBox.setItemText(2, _translate("MainWindow", "Phase"))
        self.component2_component_comboBox.setItemText(3, _translate("MainWindow", "Real"))
        self.component2_component_comboBox.setItemText(4, _translate("MainWindow", "Imag"))
        self.component2_component_comboBox.setItemText(5, _translate("MainWindow", "Uni_Mag"))
        self.component2_component_comboBox.setItemText(6, _translate("MainWindow", "Uni_Phase"))
        self.comboBox_output.setItemText(0, _translate("MainWindow", "Output 1, Output 2"))
        self.comboBox_output.setItemText(1, _translate("MainWindow", "Output1"))
        self.comboBox_output.setItemText(2, _translate("MainWindow", "Output2"))
        self.label_6.setText(_translate("MainWindow", "component 1 :"))
        self.label_7.setText(_translate("MainWindow", "component 2 :"))
        self.showImage_button.setText(_translate("MainWindow", "load image "))
        self.showImage2_button.setText(_translate("MainWindow", "load image "))
        self.applyChanges_Button.setText(_translate("MainWindow", "<<        Apply        >>"))
        self.label_8.setText(_translate("MainWindow", "TextLabel"))
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
