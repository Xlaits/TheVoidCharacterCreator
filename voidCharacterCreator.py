# voidCharacterCreator
# Andrew Roderigues
#
# Released under the Artistic License 2.0

from PyQt5.QtWidgets import (QWidget, QMainWindow, QApplication, QComboBox, 
QDialog, QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout, 
QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, 
QVBoxLayout, QStackedLayout, QAction, QTabWidget)
from PyQt5.QtCore import pyqtSlot
import sys, os
from pathlib import Path

class aboutWindow(QWidget):
    def __init__(self, parent = None):
        super().__init__()
        self.title = "About"
        self.initWindow()
        
    def initWindow(self):
        self.setWindowTitle(self.title)
        self.layout = QVBoxLayout()
        
        self.layout.addWidget(QLabel("The Void Character Creation Program"))
        self.layout.addWidget(QLabel("Code by Andrew Roderigues"))
        self.layout.addWidget(QLabel("The Void is copyright of Wildfire"))
        
        self.setLayout(self.layout)
        
class characterTabs(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.layout = QVBoxLayout()
        
        # Generate tabs bar.
        self.tabs = QTabWidget()
        # Stats, Health, FP, Speed, summary data
        self.statSheet = QWidget()
        # Skills
        self.skillsSheet = QWidget()
        # Gear
        self.equipSheet = QWidget()
        # Background, Talents, Qualities, Quirks
        self.qualitiesSheet = QWidget()
        # Armor & Weapons
        self.combatSheet = QWidget()
        
        #Adding tabs to the list
        self.tabs.addTab(self.statSheet, "Stats")
        self.tabs.addTab(self.skillsSheet, "Skills")
        self.tabs.addTab(self.equipSheet, "Gear")
        self.tabs.addTab(self.qualitiesSheet, "Qualities")
        self.tabs.addTab(self.combatSheet, "Combat")
        
        self.horizontalGroupBox = QGroupBox("Grid")
        
        #Stats Tab
        #Set statSheet layout
        self.statSheet.layout = QVBoxLayout()
        
        #Add content to layout of statSheet
        self.statSheet.layout.addWidget(QLabel("Character Name:"))
        self.statSheet.layout.addWidget(QLineEdit())
        
        #Skills Tab
        self.skillsSheet.layout = QGridLayout()
        
        #Add content to skillsSheet
        self.skillsSheet.layout.addWidget(QLabel("Skill Name:"))
        self.skillsSheet.layout.addWidget(QLineEdit())
        
        #Gear Tab
        self.equipSheet.layout = QGridLayout()
        
        #Qualities Tab
        self.qualitiesSheet.layout = QGridLayout()
        
        #Combat Tab
        self.combatSheet.layout = QGridLayout()
        
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

class mainWindow(QMainWindow):
    def __init__(self, parent = None):
        '''
        This initializes the main window of the program.
        '''
        super().__init__()
        self.title = 'The Void Character Creator'
        self.initUI()
        self.statusBar()
        
        # Initializing the Menubar
        mainMenu = self.menuBar() 
        fileMenu = mainMenu.addMenu('File')
        
        # New character option in File menu
        startCharacter = QAction('Start a New Character', self)
        startCharacter.setShortcut('Ctrl+N')
        startCharacter.setStatusTip('Start a new character file')
        #startCharacter.triggered.connect(self.newCharacter)
        fileMenu.addAction(startCharacter)
        
        # Load character option in File menu
        viewCharacter = QAction('View a Character', self)
        viewCharacter.setShortcut('Ctrl+V')
        viewCharacter.setStatusTip('View a character file')
        #viewCharacter.triggered.connect(self.loadCharacter)
        fileMenu.addAction(viewCharacter)
        
        # Exit option in file menu
        exitButton = QAction('Exit', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close)
        fileMenu.addAction(exitButton)
		
        # About button on menubar
        aboutButton = QAction('About', self)
        aboutButton.setStatusTip('More about the program')
        aboutButton.triggered.connect(self.aboutWin)
        mainMenu.addAction(aboutButton)
    
    def aboutWin(self):
        # call aboutWindow
        self.window = aboutWindow()
        self.window.show()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setFixedSize(800,800)
        self.central_wid = QWidget()
        self.layout_for_wid = QStackedLayout()
        
        self.tabs = characterTabs(self)
        self.setCentralWidget(self.tabs)
        
        # Show main window
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = mainWindow()
    sys.exit(app.exec_())
