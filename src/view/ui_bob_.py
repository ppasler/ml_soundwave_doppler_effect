# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_bob.ui'
#
# Created: Tue Jan 21 11:56:33 2014
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1378, 783)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.qwtPlot_1 = Qwt5.QwtPlot(self.centralwidget)
        self.qwtPlot_1.setEnabled(False)
        self.qwtPlot_1.setGeometry(QtCore.QRect(0, 0, 171, 150))
        self.qwtPlot_1.setObjectName(_fromUtf8("qwtPlot_1"))
        self.class3_bt = QtGui.QPushButton(self.centralwidget)
        self.class3_bt.setGeometry(QtCore.QRect(920, 700, 81, 23))
        self.class3_bt.setStyleSheet(_fromUtf8("QCheckBox, QComboBox, QSpinBox {\n"
"    color: red;\n"
"    background-color: white;\n"
"    font: bold;\n"
"}"))
        self.class3_bt.setObjectName(_fromUtf8("class3_bt"))
        self.k_lb = QtGui.QLabel(self.centralwidget)
        self.k_lb.setGeometry(QtCore.QRect(800, 610, 21, 21))
        self.k_lb.setObjectName(_fromUtf8("k_lb"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 640, 86, 80))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.initCalibration_sb = QtGui.QSpinBox(self.layoutWidget)
        self.initCalibration_sb.setMaximum(99999)
        self.initCalibration_sb.setProperty("value", 5000)
        self.initCalibration_sb.setObjectName(_fromUtf8("initCalibration_sb"))
        self.verticalLayout.addWidget(self.initCalibration_sb)
        self.initCalibration_bt = QtGui.QPushButton(self.layoutWidget)
        self.initCalibration_bt.setObjectName(_fromUtf8("initCalibration_bt"))
        self.verticalLayout.addWidget(self.initCalibration_bt)
        self.calibration_bt = QtGui.QPushButton(self.layoutWidget)
        self.calibration_bt.setObjectName(_fromUtf8("calibration_bt"))
        self.verticalLayout.addWidget(self.calibration_bt)
        self.learnKMeans_bt = QtGui.QPushButton(self.centralwidget)
        self.learnKMeans_bt.setGeometry(QtCore.QRect(800, 680, 91, 23))
        self.learnKMeans_bt.setObjectName(_fromUtf8("learnKMeans_bt"))
        self.openFile_bt = QtGui.QPushButton(self.centralwidget)
        self.openFile_bt.setGeometry(QtCore.QRect(650, 600, 121, 21))
        self.openFile_bt.setObjectName(_fromUtf8("openFile_bt"))
        self.class4_bt = QtGui.QPushButton(self.centralwidget)
        self.class4_bt.setGeometry(QtCore.QRect(1030, 610, 81, 23))
        self.class4_bt.setStyleSheet(_fromUtf8("QCheckBox, QComboBox, QSpinBox {\n"
"    color: red;\n"
"    background-color: white;\n"
"    font: bold;\n"
"}"))
        self.class4_bt.setObjectName(_fromUtf8("class4_bt"))
        self.class0_bt = QtGui.QPushButton(self.centralwidget)
        self.class0_bt.setGeometry(QtCore.QRect(920, 610, 81, 23))
        self.class0_bt.setStyleSheet(_fromUtf8("QCheckBox, QComboBox, QSpinBox {\n"
"    color: red;\n"
"    background-color: white;\n"
"    font: bold;\n"
"}"))
        self.class0_bt.setObjectName(_fromUtf8("class0_bt"))
        self.qwtPlot_8 = Qwt5.QwtPlot(self.centralwidget)
        self.qwtPlot_8.setEnabled(False)
        self.qwtPlot_8.setGeometry(QtCore.QRect(1190, 0, 171, 150))
        self.qwtPlot_8.setObjectName(_fromUtf8("qwtPlot_8"))
        self.qwtPlot_13 = Qwt5.QwtPlot(self.centralwidget)
        self.qwtPlot_13.setEnabled(False)
        self.qwtPlot_13.setGeometry(QtCore.QRect(680, 150, 171, 150))
        self.qwtPlot_13.setObjectName(_fromUtf8("qwtPlot_13"))
        self.qwtPlot_21 = Qwt5.QwtPlot(self.centralwidget)
        self.qwtPlot_21.setEnabled(False)
        self.qwtPlot_21.setGeometry(QtCore.QRect(680, 300, 171, 150))
        self.qwtPlot_21.setObjectName(_fromUtf8("qwtPlot_21"))
        self.layoutWidget1 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(280, 640, 123, 74))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_6.setMargin(0)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.skipFrames_lb = QtGui.QLabel(self.layoutWidget1)
        self.skipFrames_lb.setObjectName(_fromUtf8("skipFrames_lb"))
        self.verticalLayout_4.addWidget(self.skipFrames_lb)
        self.skipFrames_sb = QtGui.QSpinBox(self.layoutWidget1)
        self.skipFrames_sb.setMaximum(2048)
        self.skipFrames_sb.setSingleStep(32)
        self.skipFrames_sb.setObjectName(_fromUtf8("skipFrames_sb"))
        self.verticalLayout_4.addWidget(self.skipFrames_sb)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.showAnyX_lb = QtGui.QLabel(self.layoutWidget1)
        self.showAnyX_lb.setObjectName(_fromUtf8("showAnyX_lb"))
        self.verticalLayout_5.addWidget(self.showAnyX_lb)
        self.showAnyX_sb = QtGui.QSpinBox(self.layoutWidget1)
        self.showAnyX_sb.setMinimum(1)
        self.showAnyX_sb.setMaximum(2048)
        self.showAnyX_sb.setProperty("value", 1)
        self.showAnyX_sb.setObjectName(_fromUtf8("showAnyX_sb"))
        self.verticalLayout_5.addWidget(self.showAnyX_sb)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.showRecord_bt = QtGui.QPushButton(self.layoutWidget1)
        self.showRecord_bt.setObjectName(_fromUtf8("showRecord_bt"))
        self.verticalLayout_6.addWidget(self.showRecord_bt)
        self.qwtPlot_29 = Qwt5.QwtPlot(self.centralwidget)
        self.qwtPlot_29.setEnabled(False)
        self.qwtPlot_29.setGeometry(QtCore.QRect(680, 450, 171, 150))
        self.qwtPlot_29.setObjectName(_fromUtf8("qwtPlot_29"))
        self.qwtPlot_32 = Qwt5.QwtPlot(self.centralwidget)
        self.qwtPlot_32.setEnabled(False)
        self.qwtPlot_32.setGeometry(QtCore.QRect(1190, 450, 171, 150))
        self.qwtPlot_32.setObjectName(_fromUtf8("qwtPlot_32"))
        self.qwtPlot_30 = Qwt5.QwtPlot(self.centralwidget)
        self.qwtPlot_30.setEnabled(False)
        self.qwtPlot_30.setGeometry(QtCore.QRect(850, 450, 171, 150))
        self.qwtPlot_30.setObjectName(_fromUtf8("qwtPlot_30"))
        self.qwtPlot_2 = Qwt5.QwtPlot(self.centralwidget)
        self.qwtPlot_2.setEnabled(False)
        self.qwtPlot_2.setGeometry(QtCore.QRect(170, 0, 171, 150))
        self.qwtPlot_2.setObjectName(_fromUtf8("qwtPlot_2"))
        self.qwtPlot_3 = Qwt5.QwtPlot(self.centralwidget)
        self.qwtPlot_3.setEnabled(False)
        self.qwtPlot_3.setGeometry(QtCore.QRect(340, 0, 171, 150))
        self.qwtPlot_3.setObjectName(_fromUtf8("qwtPlot_3"))
        self.qwtPlot_4 = Qwt5.QwtPlot(self.centralwidget)
        self.qwtPlot_4.setEnabled(False)
        self.qwtPlot_4.setGeometry(QtCore.QRect(510, 0, 171, 150))
        self.qwtPlot_4.setObjectName(_fromUtf8("qwtPlot_4"))
        self.qwtPlot_5 = Qwt5.QwtPlot(self.centralwidget)
        self.qwtPlot_5.setEnabled(False)
        self.qwtPlot_5.setGeometry(QtCore.QRect(680, 0, 171, 150))
        self.qwtPlot_5.setObjectName(_fromUtf8("qwtPlot_5"))
        self.qwtPlot_7 = Qwt5.QwtPlot(self.centralwidget)
        self.qwtPlot_7.setEnabled(False)
        self.qwtPlot_7.setGeometry(QtCore.QRect(1020, 0, 171, 150))
        self.qwtPlot_7.setObjectName(_fromUtf8("qwtPlot_7"))
        self.records_pb = QtGui.QProgressBar(self.centralwidget)
        self.records_pb.setGeometry(QtCore.QRect(190, 640, 81, 23))
        self.records_pb.setProperty("value", 0)
        self.records_pb.setObjectName(_fromUtf8("records_pb"))
        self.checkKMeans_bt = QtGui.QPushButton(self.centralwidget)
        self.checkKMeans_bt.setGeometry(QtCore.QRect(800, 700, 91, 23))
        self.checkKMeans_bt.setObjectName(_fromUtf8("checkKMeans_bt"))
        self.qwtPlot_11 = Qwt5.QwtPlot(self.centralwidget)
        self.qwtPlot_11.setEnabled(False)
        self.qwtPlot_11.setGeometry(QtCore.QRect(340, 150, 171, 150))
        self.qwtPlot_11.setObjectName(_fromUtf8("qwtPlot_11"))
        self.qwtPlot_19 = Qwt5.QwtPlot(self.centralwidget)
        self.qwtPlot_19.setEnabled(False)
        self.qwtPlot_19.setGeometry(QtCore.QRect(340, 300, 171, 150))
        self.qwtPlot_19.setObjectName(_fromUtf8("qwtPlot_19"))
        self.loadLearnArray_bt = QtGui.QPushButton(self.centralwidget)
        self.loadLearnArray_bt.setGeometry(QtCore.QRect(650, 620, 121, 21))
        self.loadLearnArray_bt.setObjectName(_fromUtf8("loadLearnArray_bt"))
        self.qwtPlot_12 = Qwt5.QwtPlot(self.centralwidget)
        self.qwtPlot_12.setEnabled(False)
        self.qwtPlot_12.setGeometry(QtCore.QRect(510, 150, 171, 150))
        self.qwtPlot_12.setObjectName(_fromUtf8("qwtPlot_12"))
        self.qwtPlot_20 = Qwt5.QwtPlot(self.centralwidget)
        self.qwtPlot_20.setEnabled(False)
        self.qwtPlot_20.setGeometry(QtCore.QRect(510, 300, 171, 150))
        self.qwtPlot_20.setObjectName(_fromUtf8("qwtPlot_20"))
        self.layoutWidget2 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(110, 670, 77, 51))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.binaryPlot_dsb = QtGui.QDoubleSpinBox(self.layoutWidget2)
        self.binaryPlot_dsb.setMaximum(1000.0)
        self.binaryPlot_dsb.setSingleStep(0.05)
        self.binaryPlot_dsb.setObjectName(_fromUtf8("binaryPlot_dsb"))
        self.verticalLayout_2.addWidget(self.binaryPlot_dsb)
        self.binaryPlot_bt = QtGui.QPushButton(self.layoutWidget2)
        self.binaryPlot_bt.setObjectName(_fromUtf8("binaryPlot_bt"))
        self.verticalLayout_2.addWidget(self.binaryPlot_bt)
        self.kNumber_sb = QtGui.QSpinBox(self.centralwidget)
        self.kNumber_sb.setGeometry(QtCore.QRect(830, 610, 61, 22))
        self.kNumber_sb.setProperty("value", 2)
        self.kNumber_sb.setObjectName(_fromUtf8("kNumber_sb"))
        self.qwtPlot_23 = Qwt5.QwtPlot(self.centralwidget)
        self.qwtPlot_23.setEnabled(False)
        self.qwtPlot_23.setGeometry(QtCore.QRect(1020, 300, 171, 150))
        self.qwtPlot_23.setObjectName(_fromUtf8("qwtPlot_23"))
        self.maxIteration_sb = QtGui.QSpinBox(self.centralwidget)
        self.maxIteration_sb.setGeometry(QtCore.QRect(830, 630, 61, 22))
        self.maxIteration_sb.setMaximum(10000)
        self.maxIteration_sb.setProperty("value", 10)
        self.maxIteration_sb.setObjectName(_fromUtf8("maxIteration_sb"))
        self.class1_bt = QtGui.QPushButton(self.centralwidget)
        self.class1_bt.setGeometry(QtCore.QRect(920, 640, 81, 23))
        self.class1_bt.setStyleSheet(_fromUtf8("QCheckBox, QComboBox, QSpinBox {\n"
"    color: red;\n"
"    background-color: white;\n"
"    font: bold;\n"
"}"))
        self.class1_bt.setObjectName(_fromUtf8("class1_bt"))
        self.qwtPlot_31 = Qwt5.QwtPlot(self.centralwidget)
        self.qwtPlot_31.setEnabled(False)
        self.qwtPlot_31.setGeometry(QtCore.QRect(1020, 450, 171, 150))
        self.qwtPlot_31.setObjectName(_fromUtf8("qwtPlot_31"))
        self.layoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(650, 642, 121, 61))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.skipFramesLA_lb = QtGui.QLabel(self.layoutWidget_2)
        self.skipFramesLA_lb.setObjectName(_fromUtf8("skipFramesLA_lb"))
        self.verticalLayout_7.addWidget(self.skipFramesLA_lb)
        self.skipFramesLA_sb = QtGui.QSpinBox(self.layoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.skipFramesLA_sb.sizePolicy().hasHeightForWidth())
        self.skipFramesLA_sb.setSizePolicy(sizePolicy)
        self.skipFramesLA_sb.setMaximum(2048)
        self.skipFramesLA_sb.setSingleStep(1)
        self.skipFramesLA_sb.setObjectName(_fromUtf8("skipFramesLA_sb"))
        self.verticalLayout_7.addWidget(self.skipFramesLA_sb)
        self.horizontalLayout_2.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.arrayIdxLF_lb = QtGui.QLabel(self.layoutWidget_2)
        self.arrayIdxLF_lb.setObjectName(_fromUtf8("arrayIdxLF_lb"))
        self.verticalLayout_8.addWidget(self.arrayIdxLF_lb)
        self.arrayIdxLF_sb = QtGui.QSpinBox(self.layoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(7)
        sizePolicy.setHeightForWidth(self.arrayIdxLF_sb.sizePolicy().hasHeightForWidth())
        self.arrayIdxLF_sb.setSizePolicy(sizePolicy)
        self.arrayIdxLF_sb.setMinimum(1)
        self.arrayIdxLF_sb.setMaximum(2048)
        self.arrayIdxLF_sb.setProperty("value", 1)
        self.arrayIdxLF_sb.setObjectName(_fromUtf8("arrayIdxLF_sb"))
        self.verticalLayout_8.addWidget(self.arrayIdxLF_sb)
        self.horizontalLayout_2.addLayout(self.verticalLayout_8)
        self.calibration_pb = QtGui.QProgressBar(self.centralwidget)
        self.calibration_pb.setGeometry(QtCore.QRect(20, 610, 101, 23))
        self.calibration_pb.setProperty("value", 0)
        self.calibration_pb.setObjectName(_fromUtf8("calibration_pb"))
        self.showPlot_bt = QtGui.QPushButton(self.centralwidget)
        self.showPlot_bt.setGeometry(QtCore.QRect(430, 670, 171, 41))
        self.showPlot_bt.setObjectName(_fromUtf8("showPlot_bt"))
        self.initKMeans_bt = QtGui.QPushButton(self.centralwidget)
        self.initKMeans_bt.setGeometry(QtCore.QRect(800, 660, 91, 23))
        self.initKMeans_bt.setObjectName(_fromUtf8("initKMeans_bt"))
        self.qwtPlot_24 = Qwt5.QwtPlot(self.centralwidget)
        self.qwtPlot_24.setEnabled(False)
        self.qwtPlot_24.setGeometry(QtCore.QRect(1190, 300, 171, 150))
        self.qwtPlot_24.setObjectName(_fromUtf8("qwtPlot_24"))
        self.qwtPlot_14 = Qwt5.QwtPlot(self.centralwidget)
        self.qwtPlot_14.setEnabled(False)
        self.qwtPlot_14.setGeometry(QtCore.QRect(850, 150, 171, 150))
        self.qwtPlot_14.setObjectName(_fromUtf8("qwtPlot_14"))
        self.qwtPlot_22 = Qwt5.QwtPlot(self.centralwidget)
        self.qwtPlot_22.setEnabled(False)
        self.qwtPlot_22.setGeometry(QtCore.QRect(850, 300, 171, 150))
        self.qwtPlot_22.setObjectName(_fromUtf8("qwtPlot_22"))
        self.qwtPlot_25 = Qwt5.QwtPlot(self.centralwidget)
        self.qwtPlot_25.setEnabled(False)
        self.qwtPlot_25.setGeometry(QtCore.QRect(0, 450, 171, 150))
        self.qwtPlot_25.setObjectName(_fromUtf8("qwtPlot_25"))
        self.qwtPlot_26 = Qwt5.QwtPlot(self.centralwidget)
        self.qwtPlot_26.setEnabled(False)
        self.qwtPlot_26.setGeometry(QtCore.QRect(170, 450, 171, 150))
        self.qwtPlot_26.setObjectName(_fromUtf8("qwtPlot_26"))
        self.class2_bt = QtGui.QPushButton(self.centralwidget)
        self.class2_bt.setGeometry(QtCore.QRect(920, 670, 81, 23))
        self.class2_bt.setStyleSheet(_fromUtf8("QCheckBox, QComboBox, QSpinBox {\n"
"    color: red;\n"
"    background-color: white;\n"
"    font: bold;\n"
"}"))
        self.class2_bt.setObjectName(_fromUtf8("class2_bt"))
        self.qwtPlot_27 = Qwt5.QwtPlot(self.centralwidget)
        self.qwtPlot_27.setEnabled(False)
        self.qwtPlot_27.setGeometry(QtCore.QRect(340, 450, 171, 150))
        self.qwtPlot_27.setObjectName(_fromUtf8("qwtPlot_27"))
        self.qwtPlot_28 = Qwt5.QwtPlot(self.centralwidget)
        self.qwtPlot_28.setEnabled(False)
        self.qwtPlot_28.setGeometry(QtCore.QRect(510, 450, 171, 150))
        self.qwtPlot_28.setObjectName(_fromUtf8("qwtPlot_28"))
        self.qwtPlot_16 = Qwt5.QwtPlot(self.centralwidget)
        self.qwtPlot_16.setEnabled(False)
        self.qwtPlot_16.setGeometry(QtCore.QRect(1190, 150, 171, 150))
        self.qwtPlot_16.setObjectName(_fromUtf8("qwtPlot_16"))
        self.qwtPlot_6 = Qwt5.QwtPlot(self.centralwidget)
        self.qwtPlot_6.setEnabled(False)
        self.qwtPlot_6.setGeometry(QtCore.QRect(850, 0, 171, 150))
        self.qwtPlot_6.setObjectName(_fromUtf8("qwtPlot_6"))
        self.qwtPlot_9 = Qwt5.QwtPlot(self.centralwidget)
        self.qwtPlot_9.setEnabled(False)
        self.qwtPlot_9.setGeometry(QtCore.QRect(0, 150, 171, 150))
        self.qwtPlot_9.setObjectName(_fromUtf8("qwtPlot_9"))
        self.qwtPlot_17 = Qwt5.QwtPlot(self.centralwidget)
        self.qwtPlot_17.setEnabled(False)
        self.qwtPlot_17.setGeometry(QtCore.QRect(0, 300, 171, 150))
        self.qwtPlot_17.setObjectName(_fromUtf8("qwtPlot_17"))
        self.qwtPlot_15 = Qwt5.QwtPlot(self.centralwidget)
        self.qwtPlot_15.setEnabled(False)
        self.qwtPlot_15.setGeometry(QtCore.QRect(1020, 150, 171, 150))
        self.qwtPlot_15.setObjectName(_fromUtf8("qwtPlot_15"))
        self.qwtPlot_10 = Qwt5.QwtPlot(self.centralwidget)
        self.qwtPlot_10.setEnabled(False)
        self.qwtPlot_10.setGeometry(QtCore.QRect(170, 150, 171, 150))
        self.qwtPlot_10.setObjectName(_fromUtf8("qwtPlot_10"))
        self.qwtPlot_18 = Qwt5.QwtPlot(self.centralwidget)
        self.qwtPlot_18.setEnabled(False)
        self.qwtPlot_18.setGeometry(QtCore.QRect(170, 300, 171, 150))
        self.qwtPlot_18.setObjectName(_fromUtf8("qwtPlot_18"))
        self.k_lb_2 = QtGui.QLabel(self.centralwidget)
        self.k_lb_2.setGeometry(QtCore.QRect(800, 630, 31, 21))
        self.k_lb_2.setObjectName(_fromUtf8("k_lb_2"))
        self.layoutWidget3 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget3.setGeometry(QtCore.QRect(190, 670, 77, 51))
        self.layoutWidget3.setObjectName(_fromUtf8("layoutWidget3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.frames_sb = QtGui.QSpinBox(self.layoutWidget3)
        self.frames_sb.setMaximum(9999999)
        self.frames_sb.setProperty("value", 32)
        self.frames_sb.setObjectName(_fromUtf8("frames_sb"))
        self.verticalLayout_3.addWidget(self.frames_sb)
        self.record_bt = QtGui.QPushButton(self.layoutWidget3)
        self.record_bt.setObjectName(_fromUtf8("record_bt"))
        self.verticalLayout_3.addWidget(self.record_bt)
        self.class5_bt = QtGui.QPushButton(self.centralwidget)
        self.class5_bt.setGeometry(QtCore.QRect(1030, 640, 81, 23))
        self.class5_bt.setStyleSheet(_fromUtf8("QCheckBox, QComboBox, QSpinBox {\n"
"    color: red;\n"
"    background-color: white;\n"
"    font: bold;\n"
"}"))
        self.class5_bt.setObjectName(_fromUtf8("class5_bt"))
        self.class6_bt = QtGui.QPushButton(self.centralwidget)
        self.class6_bt.setGeometry(QtCore.QRect(1030, 670, 81, 23))
        self.class6_bt.setStyleSheet(_fromUtf8("QCheckBox, QComboBox, QSpinBox {\n"
"    color: red;\n"
"    background-color: white;\n"
"    font: bold;\n"
"}"))
        self.class6_bt.setObjectName(_fromUtf8("class6_bt"))
        self.class7_bt = QtGui.QPushButton(self.centralwidget)
        self.class7_bt.setGeometry(QtCore.QRect(1030, 700, 81, 23))
        self.class7_bt.setStyleSheet(_fromUtf8("QCheckBox, QComboBox, QSpinBox {\n"
"    color: red;\n"
"    background-color: white;\n"
"    font: bold;\n"
"}"))
        self.class7_bt.setObjectName(_fromUtf8("class7_bt"))
        self.testKMeans_bt = QtGui.QPushButton(self.centralwidget)
        self.testKMeans_bt.setGeometry(QtCore.QRect(1160, 610, 75, 23))
        self.testKMeans_bt.setObjectName(_fromUtf8("testKMeans_bt"))
        self.cutSides_sb = QtGui.QSpinBox(self.centralwidget)
        self.cutSides_sb.setGeometry(QtCore.QRect(440, 620, 75, 20))
        self.cutSides_sb.setMaximum(64)
        self.cutSides_sb.setProperty("value", 20)
        self.cutSides_sb.setObjectName(_fromUtf8("cutSides_sb"))
        self.cutSides_lb = QtGui.QLabel(self.centralwidget)
        self.cutSides_lb.setGeometry(QtCore.QRect(440, 600, 54, 13))
        self.cutSides_lb.setObjectName(_fromUtf8("cutSides_lb"))
        self.showLearnArray_bt = QtGui.QPushButton(self.centralwidget)
        self.showLearnArray_bt.setGeometry(QtCore.QRect(650, 700, 121, 21))
        self.showLearnArray_bt.setObjectName(_fromUtf8("showLearnArray_bt"))
        self.bufferedPlot_rb = QtGui.QRadioButton(self.centralwidget)
        self.bufferedPlot_rb.setGeometry(QtCore.QRect(440, 650, 111, 17))
        self.bufferedPlot_rb.setObjectName(_fromUtf8("bufferedPlot_rb"))
        self.picToRecordArray_bt = QtGui.QPushButton(self.centralwidget)
        self.picToRecordArray_bt.setGeometry(QtCore.QRect(610, 630, 31, 91))
        self.picToRecordArray_bt.setStyleSheet(_fromUtf8("QPushButton {\n"
"\n"
"    background-color: red;\n"
"    font: bold;\n"
"}"))
        self.picToRecordArray_bt.setObjectName(_fromUtf8("picToRecordArray_bt"))
        self.saveFile_bt = QtGui.QPushButton(self.centralwidget)
        self.saveFile_bt.setGeometry(QtCore.QRect(1160, 640, 75, 23))
        self.saveFile_bt.setObjectName(_fromUtf8("saveFile_bt"))
        self.showCluster_bt = QtGui.QPushButton(self.centralwidget)
        self.showCluster_bt.setGeometry(QtCore.QRect(1160, 670, 75, 23))
        self.showCluster_bt.setObjectName(_fromUtf8("showCluster_bt"))
        self.c0_cb = QtGui.QCheckBox(self.centralwidget)
        self.c0_cb.setGeometry(QtCore.QRect(1260, 610, 31, 17))
        self.c0_cb.setObjectName(_fromUtf8("c0_cb"))
        self.c1_cb = QtGui.QCheckBox(self.centralwidget)
        self.c1_cb.setGeometry(QtCore.QRect(1260, 640, 31, 17))
        self.c1_cb.setObjectName(_fromUtf8("c1_cb"))
        self.c2_cb = QtGui.QCheckBox(self.centralwidget)
        self.c2_cb.setGeometry(QtCore.QRect(1260, 670, 31, 17))
        self.c2_cb.setObjectName(_fromUtf8("c2_cb"))
        self.c3_cb = QtGui.QCheckBox(self.centralwidget)
        self.c3_cb.setGeometry(QtCore.QRect(1260, 700, 31, 17))
        self.c3_cb.setObjectName(_fromUtf8("c3_cb"))
        self.c4_cb = QtGui.QCheckBox(self.centralwidget)
        self.c4_cb.setGeometry(QtCore.QRect(1300, 610, 31, 17))
        self.c4_cb.setObjectName(_fromUtf8("c4_cb"))
        self.c6_cb = QtGui.QCheckBox(self.centralwidget)
        self.c6_cb.setGeometry(QtCore.QRect(1300, 670, 31, 17))
        self.c6_cb.setObjectName(_fromUtf8("c6_cb"))
        self.c5_cb = QtGui.QCheckBox(self.centralwidget)
        self.c5_cb.setGeometry(QtCore.QRect(1300, 640, 31, 17))
        self.c5_cb.setObjectName(_fromUtf8("c5_cb"))
        self.c7_cb = QtGui.QCheckBox(self.centralwidget)
        self.c7_cb.setGeometry(QtCore.QRect(1300, 700, 31, 17))
        self.c7_cb.setObjectName(_fromUtf8("c7_cb"))
        self.mulFiles_cb = QtGui.QCheckBox(self.centralwidget)
        self.mulFiles_cb.setGeometry(QtCore.QRect(540, 600, 61, 17))
        self.mulFiles_cb.setObjectName(_fromUtf8("mulFiles_cb"))
        self.skipFrames_sb_2 = QtGui.QSpinBox(self.centralwidget)
        self.skipFrames_sb_2.setGeometry(QtCore.QRect(280, 610, 54, 20))
        self.skipFrames_sb_2.setMaximum(2048)
        self.skipFrames_sb_2.setSingleStep(1)
        self.skipFrames_sb_2.setProperty("value", 1)
        self.skipFrames_sb_2.setObjectName(_fromUtf8("skipFrames_sb_2"))
        self.rotateArray_sb = QtGui.QSpinBox(self.centralwidget)
        self.rotateArray_sb.setGeometry(QtCore.QRect(540, 650, 54, 20))
        self.rotateArray_sb.setMaximum(32)
        self.rotateArray_sb.setSingleStep(1)
        self.rotateArray_sb.setProperty("value", 1)
        self.rotateArray_sb.setObjectName(_fromUtf8("rotateArray_sb"))
        self.rotateArr_lb = QtGui.QLabel(self.centralwidget)
        self.rotateArr_lb.setGeometry(QtCore.QRect(540, 630, 54, 13))
        self.rotateArr_lb.setObjectName(_fromUtf8("rotateArr_lb"))
        self.rotArray_cb = QtGui.QCheckBox(self.centralwidget)
        self.rotArray_cb.setGeometry(QtCore.QRect(610, 600, 70, 17))
        self.rotArray_cb.setObjectName(_fromUtf8("rotArray_cb"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1378, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.class3_bt.setText(_translate("MainWindow", "Class 3", None))
        self.k_lb.setText(_translate("MainWindow", "k", None))
        self.initCalibration_bt.setText(_translate("MainWindow", "initial calibration", None))
        self.calibration_bt.setText(_translate("MainWindow", "calibrate", None))
        self.learnKMeans_bt.setText(_translate("MainWindow", "learn k-means", None))
        self.openFile_bt.setText(_translate("MainWindow", "open file", None))
        self.class4_bt.setText(_translate("MainWindow", "Class 4", None))
        self.class0_bt.setText(_translate("MainWindow", "Class 0", None))
        self.skipFrames_lb.setText(_translate("MainWindow", "skip frames", None))
        self.showAnyX_lb.setText(_translate("MainWindow", "show any x", None))
        self.showRecord_bt.setText(_translate("MainWindow", "show record", None))
        self.checkKMeans_bt.setText(_translate("MainWindow", "check k-means", None))
        self.loadLearnArray_bt.setText(_translate("MainWindow", "load array", None))
        self.binaryPlot_bt.setText(_translate("MainWindow", "binary plot", None))
        self.class1_bt.setText(_translate("MainWindow", "Class 1", None))
        self.skipFramesLA_lb.setText(_translate("MainWindow", "skip frames", None))
        self.arrayIdxLF_lb.setText(_translate("MainWindow", "array idx", None))
        self.showPlot_bt.setText(_translate("MainWindow", "show plot", None))
        self.initKMeans_bt.setText(_translate("MainWindow", "init k-means", None))
        self.class2_bt.setText(_translate("MainWindow", "Class 2", None))
        self.k_lb_2.setText(_translate("MainWindow", "max it", None))
        self.record_bt.setText(_translate("MainWindow", "record frames", None))
        self.class5_bt.setText(_translate("MainWindow", "Class 5", None))
        self.class6_bt.setText(_translate("MainWindow", "Class 6", None))
        self.class7_bt.setText(_translate("MainWindow", "Class 7", None))
        self.testKMeans_bt.setText(_translate("MainWindow", "test kMeans", None))
        self.cutSides_lb.setText(_translate("MainWindow", "cut sides", None))
        self.showLearnArray_bt.setText(_translate("MainWindow", "show array", None))
        self.bufferedPlot_rb.setText(_translate("MainWindow", "bufferred plot", None))
        self.picToRecordArray_bt.setText(_translate("MainWindow", "R", None))
        self.saveFile_bt.setText(_translate("MainWindow", "save file", None))
        self.showCluster_bt.setText(_translate("MainWindow", "show cluster", None))
        self.c0_cb.setText(_translate("MainWindow", "0", None))
        self.c1_cb.setText(_translate("MainWindow", "1", None))
        self.c2_cb.setText(_translate("MainWindow", "2", None))
        self.c3_cb.setText(_translate("MainWindow", "3", None))
        self.c4_cb.setText(_translate("MainWindow", "4", None))
        self.c6_cb.setText(_translate("MainWindow", "6", None))
        self.c5_cb.setText(_translate("MainWindow", "5", None))
        self.c7_cb.setText(_translate("MainWindow", "7", None))
        self.mulFiles_cb.setText(_translate("MainWindow", "mul files", None))
        self.rotateArr_lb.setText(_translate("MainWindow", "rotate Arr", None))
        self.rotArray_cb.setText(_translate("MainWindow", "rot", None))

from PyQt4 import Qwt5