from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

import sys

from pages.untitled import Ui_Form

class Window(QStackedWidget):

    def __init__(self):
        super(Window, self).__init__()
        self.home_screen = self.create_home_screen()
        self.patric_screen = self.create_patric_search_screen()
        self.addWidget(self.home_screen)
        self.setCurrentIndex(0)
        self.show()

    def create_home_screen(self):
        screen = QWidget()
        layout = QVBoxLayout()
        patric_button = QPushButton(text="Choose genomes from PATRIC")
        file_button = QPushButton(text="Choose a FASTA file")
        patric_button.clicked.connect(lambda: self.setCurrentIndex(1))
        file_button.clicked.connect(lambda: self.setCurrentIndex(2))
        layout.addWidget(patric_button)
        layout.addWidget(file_button)
        screen.setLayout(layout)
        return screen

    def create_patric_search_screen(self):
        screen = QWidget()
        layout = QVBoxLayout()
        field = QLineEdit()
        species_button = QPushButton(text="Search by species name")
        taxon_button = QPushButton(text="Search by taxon ID")
        layout.addWidget(field)
        layout.addWidget(species_button)
        layout.addWidget(taxon_button)
        screen.setLayout(layout)
        return screen

app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())

