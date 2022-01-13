from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor
from Randomizers import Encounters, Evolutions, Trainers, UndergroundEncounters, Levels, Shop, TM, Starters, TMCompat, Ability, FldItems, Moves
from Randomizers.dialog import Ui_MainWindow
from Utilities import GlobalGameManager
from os import error, path, remove, getcwd, chdir
import shutil
import sys
import traceback

class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnRandomize.clicked.connect(self.buttonClicked)
    
    def buttonClicked(self):
        #setup directory where romFS Tok modify is. 
        dialog = QFileDialog()
        global romFSPath
        romFSPath = dialog.getExistingDirectory(self, 'Select ROMFS path')
        
        if path.exists(path.join(romFSPath, "Data")):
            romFSPath = path.join(romFSPath, "Data")
            
        self.ui.tbLog.append("RomFS Directory set to " + romFSPath)
        
        self.ui.tbLog.append("Output folder set to {}".format(path.join(getcwd(), "mods")))
        
        #Deletes remnamts of old randomizer
        if path.exists('mods'):
            shutil.rmtree('mods')
        chdir(getcwd())
        
        try:
            
            if self.ui.cbStarters.isChecked():
                Starters.RandomizeStarters(self.ui.tbLog, romFSPath)
        
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
                Encounters.RandomizeEncounters(self.ui.tbLog,self.ui.cbLegends.isChecked(), generations, self.ui.cbSafari.isChecked(), romFSPath)
                
            if self.ui.cbMoves.isChecked():
                self.ui.tbLog.append('Randomizing Movesets!')
                Moves.RandomizerMoves(self.ui.tbLog, romFSPath)
                self.ui.tbLog.append('Updating Trainer Movesets!')
                Trainers.updateMovesets(self.ui.tbLog, romFSPath)
                
            if self.ui.cbTrainers.isChecked():
                self.ui.tbLog.append('Randomizing Trainers!')
                Trainers.RandomizeTrainers(self.ui.tbLog, 0, 0, romFSPath, scaleWithLevel=False)
                
            if self.ui.cbTimeSkip.isChecked() or self.ui.cb60FPS.isChecked():
                self.ui.tbLog.append('Applying Utilities!')
                GlobalGameManager.ApplyUtilities(self.ui.cb60FPS.isChecked(), self.ui.sbTimeStep.value(), self.ui.tbLog, romFSPath)
            
            if self.ui.cbUnderground.isChecked():
                self.ui.tbLog.append('Randomizing Underground Pokemon!')
                UndergroundEncounters.RandomizeUG(self.ui.tbLog, romFSPath)
                
            if self.ui.cbEvolutions.isChecked():
                self.ui.tbLog.append('Randomizing Evolutions!')
                Evolutions.RandomizeEvolutions(self.ui.tbLog, romFSPath)
            
            if self.ui.cbTM.isChecked():
                self.ui.tbLog.append('Randomizing TMs!')
                TM.RandomizeTMs(self.ui.tbLog, romFSPath)
            
            if self.ui.cbShops.isChecked():
                self.ui.tbLog.append('Randomizing Shops!')
                Shop.RandomizeShops(self.ui.tbLog, romFSPath)
            
            if self.ui.cbTMCompat.isChecked():
                TMCompat.RandomizeCompat(self.ui.tbLog, romFSPath)
            
            if self.ui.cbAbilities.isChecked():
                Ability.RandomizeAbilities(self.ui.tbLog, romFSPath)
            
            if self.ui.cbFieldItems.isChecked():
                FldItems.RandomizeFieldItems(self.ui.tbLog, romFSPath)          
                
            ##Deletes temp files at the end
            moves = "Resources//tempMoveIndex.txt"
            
            tempFileList = [moves]
            for file in tempFileList:
                if path.exists(file):
                    remove(file)
                
        except Exception: 
            self.ui.tbLog.append("An Error has occured: ")
            self.ui.tbLog.append(traceback.format_exc())
            # self.ui.tbLog.append(str(type(inst.args)))
        #if self.ui.cbLevels.isChecked():
        #    self.ui.tbLog.append('Randomizing Levels!')
        #    if self.ui.rbFlat.isChecked():
        #        Levels.RandomizeLevels(self.ui.tbLog,1, self.ui.sbMin.value(), self.ui.sbMax.value())
        #    else:
        #        Levels.RandomizeLevels(self.ui.tbLog,0, self.ui.sbMin.value(), self.ui.sbMax.value())

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

