from PyQt5.QtWidgets import QAction, QWidget, QTextEdit, QCheckBox, QGroupBox, QMenu, QPushButton, QRadioButton, QLabel, QSpinBox, QMenuBar,QStatusBar, QMainWindow, QApplication
from PyQt5.QtCore import Qt, QRect, QCoreApplication, QMetaObject
from PyQt5.QtGui import QPixmap, QKeySequence, QPalette, QColor
from Randomizers import Encounters, Evolutions, Trainers, UndergroundEncounters, Levels
from Randomizers.dialog import Ui_MainWindow
import sys

class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnRandomize.clicked.connect(self.buttonClicked)
    
    def buttonClicked(self):
        if self.ui.cbPokemon.isChecked():
            self.ui.tbLog.append('Randomizing Pokemon!')
            generations = []
            if self.ui.cbGen1.isChecked():
                generations.append(1)
            if self.ui.cbGen2.isChecked():
                generations.append(2)
            if self.ui.cbGen3.isChecked():
                generations.append(3)
            if self.ui.cbGen4.isChecked():
                generations.append(4)
            #Fixed added safari -- sangawku
            Encounters.RandomizeEncounters(self.ui.tbLog,self.ui.cbLegends.isChecked(), generations, self.ui.cbSafari.isChecked())
        if self.ui.cbTrainers.isChecked():
            self.ui.tbLog.append('Randomizing Trainers!')
            Trainers.RandomizeTrainers(self.ui.tbLog)
        
        
        
        if self.ui.cbUnderground.isChecked():
            self.ui.tbLog.append('Randomizing Underground Pokemon!')
            UndergroundEncounters.RandomizeUG(self.ui.tbLog)
            
        if self.ui.cbEvolutions.isChecked():
            self.ui.tbLog.append('Randomizing Evolutions!')
            Evolutions.RandomizeEvolutions(self.ui.tbLog)
            
        if self.ui.cbLevels.isChecked():
            self.ui.tbLog.append('Randomizing Levels!')
            if self.ui.rbFlat.isChecked():
                Levels.RandomizeLevels(self.ui.tbLog,1, self.ui.sbMin.value(), self.ui.sbMax.value())
            else:
                Levels.RandomizeLevels(self.ui.tbLog,0, self.ui.sbMin.value(), self.ui.sbMax.value())

app = QApplication(sys.argv)

# Set our style, We don't want mismatched themes 
app.setStyle("Fusion")

# Now make them bitches dark as night:
palette = QPalette()
palette.setColor(QPalette.Window, QColor(53, 53, 53))
palette.setColor(QPalette.WindowText, Qt.white)
palette.setColor(QPalette.Base, QColor(25, 25, 25))
palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
palette.setColor(QPalette.ToolTipBase, Qt.white)
palette.setColor(QPalette.ToolTipText, Qt.white)
palette.setColor(QPalette.Text, Qt.white)
palette.setColor(QPalette.Button, QColor(53, 53, 53))
palette.setColor(QPalette.ButtonText, Qt.white)
palette.setColor(QPalette.BrightText, Qt.red)
palette.setColor(QPalette.Link, QColor(42, 130, 218))
palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
palette.setColor(QPalette.HighlightedText, Qt.black)
app.setPalette(palette)
app.setApplicationName("BDSP Randomizer")

w = AppWindow()
w.show()
sys.exit(app.exec_())

w = AppWindow()
w.show()
app.exec_()

