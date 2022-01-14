# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1033, 619)
        MainWindow.setWindowTitle("BDSP Randomizer")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("BDSP.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 2, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setEnabled(True)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.cbGen1 = QtWidgets.QCheckBox(self.groupBox_2)
        self.cbGen1.setChecked(True)
        self.cbGen1.setObjectName("cbGen1")
        self.gridLayout_3.addWidget(self.cbGen1, 0, 0, 1, 1)
        self.cbGen2 = QtWidgets.QCheckBox(self.groupBox_2)
        self.cbGen2.setChecked(True)
        self.cbGen2.setObjectName("cbGen2")
        self.gridLayout_3.addWidget(self.cbGen2, 0, 1, 1, 1)
        self.cbGen3 = QtWidgets.QCheckBox(self.groupBox_2)
        self.cbGen3.setChecked(True)
        self.cbGen3.setObjectName("cbGen3")
        self.gridLayout_3.addWidget(self.cbGen3, 1, 0, 1, 1)
        self.cbGen4 = QtWidgets.QCheckBox(self.groupBox_2)
        self.cbGen4.setChecked(True)
        self.cbGen4.setObjectName("cbGen4")
        self.gridLayout_3.addWidget(self.cbGen4, 1, 1, 1, 1)
        self.cbLegends = QtWidgets.QCheckBox(self.groupBox_2)
        self.cbLegends.setChecked(True)
        self.cbLegends.setObjectName("cbLegends")
        self.gridLayout_3.addWidget(self.cbLegends, 2, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 3, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 0, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.cbStarters = QtWidgets.QCheckBox(self.groupBox)
        self.cbStarters.setObjectName("cbStarters")
        self.verticalLayout.addWidget(self.cbStarters)
        self.cbPokemon = QtWidgets.QCheckBox(self.groupBox)
        self.cbPokemon.setObjectName("cbPokemon")
        self.verticalLayout.addWidget(self.cbPokemon)
        self.cbSafari = QtWidgets.QCheckBox(self.groupBox)
        self.cbSafari.setObjectName("cbSafari")
        self.verticalLayout.addWidget(self.cbSafari)
        self.cbUnderground = QtWidgets.QCheckBox(self.groupBox)
        self.cbUnderground.setObjectName("cbUnderground")
        self.verticalLayout.addWidget(self.cbUnderground)
        self.cbEvolutions = QtWidgets.QCheckBox(self.groupBox)
        self.cbEvolutions.setObjectName("cbEvolutions")
        self.verticalLayout.addWidget(self.cbEvolutions)
        self.cbTrainers = QtWidgets.QCheckBox(self.groupBox)
        self.cbTrainers.setObjectName("cbTrainers")
        self.verticalLayout.addWidget(self.cbTrainers)
        self.cbShops = QtWidgets.QCheckBox(self.groupBox)
        self.cbShops.setObjectName("cbShops")
        self.verticalLayout.addWidget(self.cbShops)
        self.cbTM = QtWidgets.QCheckBox(self.groupBox)
        self.cbTM.setObjectName("cbTM")
        self.verticalLayout.addWidget(self.cbTM)
        self.cbTMCompat = QtWidgets.QCheckBox(self.groupBox)
        self.cbTMCompat.setObjectName("cbTMCompat")
        self.verticalLayout.addWidget(self.cbTMCompat)
        self.cbAbilities = QtWidgets.QCheckBox(self.groupBox)
        self.cbAbilities.setEnabled(True)
        font = QtGui.QFont()
        font.setStrikeOut(False)
        self.cbAbilities.setFont(font)
        self.cbAbilities.setObjectName("cbAbilities")
        self.verticalLayout.addWidget(self.cbAbilities)
        self.cbFieldItems = QtWidgets.QCheckBox(self.groupBox)
        self.cbFieldItems.setEnabled(True)
        font = QtGui.QFont()
        font.setStrikeOut(False)
        self.cbFieldItems.setFont(font)
        self.cbFieldItems.setObjectName("cbFieldItems")
        self.verticalLayout.addWidget(self.cbFieldItems)
        self.cbMoves = QtWidgets.QCheckBox(self.groupBox)
        self.cbMoves.setEnabled(True)
        font = QtGui.QFont()
        font.setStrikeOut(False)
        self.cbMoves.setFont(font)
        self.cbMoves.setObjectName("cbMoves")
        self.verticalLayout.addWidget(self.cbMoves)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setEnabled(False)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.cbLevels = QtWidgets.QCheckBox(self.groupBox)
        self.cbLevels.setEnabled(False)
        font = QtGui.QFont()
        font.setStrikeOut(True)
        self.cbLevels.setFont(font)
        self.cbLevels.setObjectName("cbLevels")
        self.verticalLayout.addWidget(self.cbLevels)
        self.gridLayout.addWidget(self.groupBox, 0, 2, 3, 1, QtCore.Qt.AlignLeft)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setEnabled(True)
        self.groupBox_3.setMinimumSize(QtCore.QSize(131, 141))
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.rbFlat = QtWidgets.QCheckBox(self.groupBox_3)
        self.rbFlat.setChecked(True)
        self.rbFlat.setObjectName("rbFlat")
        self.gridLayout_2.addWidget(self.rbFlat, 0, 0, 1, 1)
        self.sbLevel = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.sbLevel.setMinimum(-50.0)
        self.sbLevel.setMaximum(500.0)
        self.sbLevel.setSingleStep(1.0)
        self.sbLevel.setProperty("value", 0.0)
        self.sbLevel.setObjectName("sbLevel")
        self.gridLayout_2.addWidget(self.sbLevel, 3, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_3, 1, 1, 1, 1)
        self.tbLog = QtWidgets.QTextEdit(self.centralwidget)
        self.tbLog.setReadOnly(True)
        self.tbLog.setPlaceholderText("")
        self.tbLog.setObjectName("tbLog")
        self.gridLayout.addWidget(self.tbLog, 2, 0, 3, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.cb60FPS = QtWidgets.QCheckBox(self.groupBox_4)
        self.cb60FPS.setObjectName("cb60FPS")
        self.verticalLayout_2.addWidget(self.cb60FPS)
        self.cbTimeSkip = QtWidgets.QCheckBox(self.groupBox_4)
        self.cbTimeSkip.setObjectName("cbTimeSkip")
        self.verticalLayout_2.addWidget(self.cbTimeSkip)
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_5.setEnabled(True)
        self.groupBox_5.setObjectName("groupBox_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(self.groupBox_5)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.sbTimeStep = QtWidgets.QDoubleSpinBox(self.groupBox_5)
        self.sbTimeStep.setSingleStep(0.1)
        self.sbTimeStep.setProperty("value", 1.0)
        self.sbTimeStep.setObjectName("sbTimeStep")
        self.horizontalLayout.addWidget(self.sbTimeStep)
        self.verticalLayout_2.addWidget(self.groupBox_5)
        self.gridLayout.addWidget(self.groupBox_4, 2, 1, 2, 1)
        self.groupBox_6 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.cbIronLocke = QtWidgets.QCheckBox(self.groupBox_6)
        font = QtGui.QFont()
        font.setStrikeOut(True)
        self.cbIronLocke.setFont(font)
        self.cbIronLocke.setText("IronLocke")
        self.cbIronLocke.setObjectName("cbIronLocke")
        self.verticalLayout_3.addWidget(self.cbIronLocke)
        self.cbPokemon_3 = QtWidgets.QCheckBox(self.groupBox_6)
        font = QtGui.QFont()
        font.setStrikeOut(True)
        self.cbPokemon_3.setFont(font)
        self.cbPokemon_3.setObjectName("cbPokemon_3")
        self.verticalLayout_3.addWidget(self.cbPokemon_3)
        self.cbSafari_3 = QtWidgets.QCheckBox(self.groupBox_6)
        font = QtGui.QFont()
        font.setStrikeOut(True)
        self.cbSafari_3.setFont(font)
        self.cbSafari_3.setText("Nuzlocke")
        self.cbSafari_3.setObjectName("cbSafari_3")
        self.verticalLayout_3.addWidget(self.cbSafari_3)
        self.gridLayout.addWidget(self.groupBox_6, 3, 2, 1, 1)
        self.btnRandomize = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.btnRandomize.setFont(font)
        self.btnRandomize.setText("Randomize")
        self.btnRandomize.setObjectName("btnRandomize")
        self.gridLayout.addWidget(self.btnRandomize, 4, 1, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1033, 17))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.groupBox_2.setTitle(_translate("MainWindow", "Pokemon Options"))
        self.cbGen1.setText(_translate("MainWindow", "Gen 1"))
        self.cbGen2.setText(_translate("MainWindow", "Gen 2"))
        self.cbGen3.setText(_translate("MainWindow", "Gen 3"))
        self.cbGen4.setText(_translate("MainWindow", "Gen 4"))
        self.cbLegends.setText(_translate("MainWindow", "Keep Legendarys"))
        self.label_2.setText(_translate("MainWindow", "*This only effects\n"
" encounters"))
        self.groupBox.setTitle(_translate("MainWindow", "Randomizers"))
        self.cbStarters.setText(_translate("MainWindow", "Randomize Starters"))
        self.cbPokemon.setText(_translate("MainWindow", "Randomize Encounters"))
        self.cbSafari.setText(_translate("MainWindow", "Randomize Safari"))
        self.cbUnderground.setText(_translate("MainWindow", "Randomize Underground"))
        self.cbEvolutions.setText(_translate("MainWindow", "Randomize Evolutions"))
        self.cbTrainers.setText(_translate("MainWindow", "Randomize Trainers"))
        self.cbShops.setText(_translate("MainWindow", "Randomize Shops"))
        self.cbTM.setText(_translate("MainWindow", "Randomize TMs"))
        self.cbTMCompat.setText(_translate("MainWindow", "Randomize TM Compat"))
        self.cbAbilities.setText(_translate("MainWindow", "Randomize Abilities"))
        self.cbFieldItems.setText(_translate("MainWindow", "Randomize Field Items"))
        self.cbMoves.setText(_translate("MainWindow", "Randomize Movesets"))
        self.label_5.setText(_translate("MainWindow", "Coming Soon"))
        self.cbLevels.setText(_translate("MainWindow", "Randomize Levels"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Level Options"))
        self.rbFlat.setText(_translate("MainWindow", "Level Multiplier"))
        self.sbLevel.setSuffix(_translate("MainWindow", "%"))
        self.label_3.setText(_translate("MainWindow", "\n"
"\n"
"\n"
"\n"
"Increase%"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Utilities"))
        self.cb60FPS.setText(_translate("MainWindow", "60FPS Mod"))
        self.cbTimeSkip.setText(_translate("MainWindow", "Speed Multiplier"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Timestep"))
        self.label_4.setText(_translate("MainWindow", "Speedup\n"
"Amount"))
        self.groupBox_6.setTitle(_translate("MainWindow", "*Lockes"))
        self.cbPokemon_3.setText(_translate("MainWindow", "Mega RandomLocke"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAbout.setTitle(_translate("MainWindow", "Help"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionAbout.setText(_translate("MainWindow", "About"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
