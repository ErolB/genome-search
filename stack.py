from PyQt5 import QtCore, QtGui, QtWidgets
from modules import retrieval
from modules import search_tools
from modules import utils
from shutil import copyfile

class Ui_StackedWidget(object):
    def __init__(self):
        self.search_results = []
        self.candidates = []
        self.searches = []
        self.search_objects = {}

    # automatically generated by QtDesigner
    # DO NOT MODIFY MANUALLY
    def setupUi(self, StackedWidget):
        StackedWidget.setObjectName("StackedWidget")
        StackedWidget.resize(1068, 831)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setItalic(True)
        StackedWidget.setFont(font)
        StackedWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.file_page = QtWidgets.QWidget()
        self.file_page.setObjectName("file_page")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.file_page)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title = QtWidgets.QLabel(self.file_page)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.verticalLayout.addWidget(self.title)
        self.browse_button = QtWidgets.QPushButton(self.file_page)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setItalic(True)
        self.browse_button.setFont(font)
        self.browse_button.setObjectName("browse_button")
        self.verticalLayout.addWidget(self.browse_button)
        self.label_4 = QtWidgets.QLabel(self.file_page)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.file_list = QtWidgets.QListWidget(self.file_page)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.file_list.setFont(font)
        self.file_list.setObjectName("file_list")
        self.verticalLayout.addWidget(self.file_list)
        self.search_button = QtWidgets.QPushButton(self.file_page)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.search_button.setFont(font)
        self.search_button.setObjectName("search_button")
        self.verticalLayout.addWidget(self.search_button)
        self.search_bar = QtWidgets.QLineEdit(self.file_page)
        self.search_bar.setText("")
        self.search_bar.setObjectName("search_bar")
        self.verticalLayout.addWidget(self.search_bar)
        self.label_5 = QtWidgets.QLabel(self.file_page)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.file_selected = QtWidgets.QListWidget(self.file_page)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.file_selected.setFont(font)
        self.file_selected.setObjectName("file_selected")
        self.verticalLayout.addWidget(self.file_selected)
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.add_button = QtWidgets.QPushButton(self.file_page)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.add_button.setFont(font)
        self.add_button.setObjectName("add_button")
        self.verticalLayout.addWidget(self.add_button)
        self.remove_button = QtWidgets.QPushButton(self.file_page)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.remove_button.setFont(font)
        self.remove_button.setObjectName("remove_button")
        self.verticalLayout.addWidget(self.remove_button)
        self.continue_button = QtWidgets.QPushButton(self.file_page)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.continue_button.setFont(font)
        self.continue_button.setObjectName("continue_button")
        self.verticalLayout.addWidget(self.continue_button)
        StackedWidget.addWidget(self.file_page)
        self.search_menu = QtWidgets.QWidget()
        self.search_menu.setObjectName("search_menu")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.search_menu)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.title_3 = QtWidgets.QLabel(self.search_menu)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setItalic(True)
        self.title_3.setFont(font)
        self.title_3.setAlignment(QtCore.Qt.AlignCenter)
        self.title_3.setObjectName("title_3")
        self.gridLayout_3.addWidget(self.title_3, 0, 0, 1, 1)
        self.motif_button = QtWidgets.QPushButton(self.search_menu)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.motif_button.setFont(font)
        self.motif_button.setObjectName("motif_button")
        self.gridLayout_3.addWidget(self.motif_button, 3, 0, 1, 1)
        self.remove_search_button = QtWidgets.QPushButton(self.search_menu)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.remove_search_button.setFont(font)
        self.remove_search_button.setObjectName("remove_search_button")
        self.gridLayout_3.addWidget(self.remove_search_button, 6, 0, 1, 1)
        self.psi_button = QtWidgets.QPushButton(self.search_menu)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.psi_button.setFont(font)
        self.psi_button.setObjectName("psi_button")
        self.gridLayout_3.addWidget(self.psi_button, 4, 0, 1, 1)
        self.hmm_button = QtWidgets.QPushButton(self.search_menu)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.hmm_button.setFont(font)
        self.hmm_button.setObjectName("hmm_button")
        self.gridLayout_3.addWidget(self.hmm_button, 2, 0, 1, 1)
        self.search_genomes_button = QtWidgets.QPushButton(self.search_menu)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.search_genomes_button.setFont(font)
        self.search_genomes_button.setObjectName("search_genomes_button")
        self.gridLayout_3.addWidget(self.search_genomes_button, 7, 0, 1, 1)
        self.to_be_searched = QtWidgets.QListWidget(self.search_menu)
        self.to_be_searched.setObjectName("to_be_searched")
        self.gridLayout_3.addWidget(self.to_be_searched, 1, 0, 1, 1)
        StackedWidget.addWidget(self.search_menu)
        self.patric_page = QtWidgets.QWidget()
        self.patric_page.setObjectName("patric_page")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.patric_page)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.add_patric_button = QtWidgets.QPushButton(self.patric_page)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.add_patric_button.setFont(font)
        self.add_patric_button.setObjectName("add_patric_button")
        self.gridLayout_2.addWidget(self.add_patric_button, 7, 0, 1, 2)
        self.name_search_button = QtWidgets.QPushButton(self.patric_page)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.name_search_button.setFont(font)
        self.name_search_button.setObjectName("name_search_button")
        self.gridLayout_2.addWidget(self.name_search_button, 4, 0, 1, 1)
        self.continue_button_2 = QtWidgets.QPushButton(self.patric_page)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.continue_button_2.setFont(font)
        self.continue_button_2.setObjectName("continue_button_2")
        self.gridLayout_2.addWidget(self.continue_button_2, 9, 0, 1, 2)
        self.patric_remove_button = QtWidgets.QPushButton(self.patric_page)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.patric_remove_button.setFont(font)
        self.patric_remove_button.setObjectName("patric_remove_button")
        self.gridLayout_2.addWidget(self.patric_remove_button, 8, 0, 1, 2)
        self.taxon_search_button = QtWidgets.QPushButton(self.patric_page)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.taxon_search_button.setFont(font)
        self.taxon_search_button.setObjectName("taxon_search_button")
        self.gridLayout_2.addWidget(self.taxon_search_button, 4, 1, 1, 1)
        self.patric_search = QtWidgets.QLineEdit(self.patric_page)
        self.patric_search.setText("")
        self.patric_search.setObjectName("patric_search")
        self.gridLayout_2.addWidget(self.patric_search, 3, 0, 1, 2)
        self.title_2 = QtWidgets.QLabel(self.patric_page)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.title_2.setFont(font)
        self.title_2.setAlignment(QtCore.Qt.AlignCenter)
        self.title_2.setObjectName("title_2")
        self.gridLayout_2.addWidget(self.title_2, 0, 0, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.patric_page)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.patric_page)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 5, 0, 1, 2)
        self.patric_list = QtWidgets.QListWidget(self.patric_page)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.patric_list.setFont(font)
        self.patric_list.setObjectName("patric_list")
        self.gridLayout_2.addWidget(self.patric_list, 2, 0, 1, 2)
        self.patric_selected = QtWidgets.QListWidget(self.patric_page)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.patric_selected.setFont(font)
        self.patric_selected.setObjectName("patric_selected")
        self.gridLayout_2.addWidget(self.patric_selected, 6, 0, 1, 2)
        StackedWidget.addWidget(self.patric_page)
        self.start = QtWidgets.QWidget()
        self.start.setObjectName("start")
        self.gridLayout = QtWidgets.QGridLayout(self.start)
        self.gridLayout.setObjectName("gridLayout")
        self.patric_button = QtWidgets.QPushButton(self.start)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.patric_button.setFont(font)
        self.patric_button.setObjectName("patric_button")
        self.gridLayout.addWidget(self.patric_button, 7, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.start)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.fasta_button = QtWidgets.QPushButton(self.start)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.fasta_button.setFont(font)
        self.fasta_button.setObjectName("fasta_button")
        self.gridLayout.addWidget(self.fasta_button, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.start)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        StackedWidget.addWidget(self.start)

        self.retranslateUi(StackedWidget)
        self.wiring(StackedWidget)
        StackedWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(StackedWidget)

    # automatically generated by QtDesigner
    def retranslateUi(self, StackedWidget):
        _translate = QtCore.QCoreApplication.translate
        StackedWidget.setWindowTitle(_translate("StackedWidget", "StackedWidget"))
        self.title.setText(_translate("StackedWidget", "Load Data from File"))
        self.browse_button.setText(_translate("StackedWidget", "Browse"))
        self.label_4.setText(_translate("StackedWidget", "Genomes found in file"))
        self.search_button.setText(_translate("StackedWidget", "Search"))
        self.label_5.setText(_translate("StackedWidget", "Selected Genomes"))
        self.add_button.setText(_translate("StackedWidget", "Add"))
        self.remove_button.setText(_translate("StackedWidget", "Remove"))
        self.continue_button.setText(_translate("StackedWidget", "Continue"))
        self.title_3.setText(_translate("StackedWidget", "Search Genomes"))
        self.motif_button.setText(_translate("StackedWidget", "Add Motif Search"))
        self.remove_search_button.setText(_translate("StackedWidget", "Remove"))
        self.psi_button.setText(_translate("StackedWidget", "Add PSI-BLAST Search"))
        self.hmm_button.setText(_translate("StackedWidget", "Add HMM Search"))
        self.search_genomes_button.setText(_translate("StackedWidget", "Search Genomes"))
        self.add_patric_button.setText(_translate("StackedWidget", "Add"))
        self.name_search_button.setText(_translate("StackedWidget", "Search by Name"))
        self.continue_button_2.setText(_translate("StackedWidget", "Continue"))
        self.patric_remove_button.setText(_translate("StackedWidget", "Remove"))
        self.taxon_search_button.setText(_translate("StackedWidget", "Search by Taxon ID"))
        self.title_2.setText(_translate("StackedWidget", "Load Data from PATRIC"))
        self.label_3.setText(_translate("StackedWidget", "Genomes found in PATRIC"))
        self.patric_button.setText(_translate("StackedWidget", "PATRIC"))
        self.label_2.setText(_translate("StackedWidget", "Choose a source for genome data."))
        self.fasta_button.setText(_translate("StackedWidget", "FASTA file"))
        self.label.setText(_translate("StackedWidget", "Welcome to the Genome Search Tool 1.0"))

    # add functionality
    def wiring(self, stack):
        # add functionality for start screen
        self.fasta_button.clicked.connect(lambda: stack.setCurrentIndex(0))
        self.patric_button.clicked.connect(lambda: stack.setCurrentIndex(2))
        # add functionality to PATRIC search
        def patric_name_search():
            self.search_results = retrieval.search_by_name(self.patric_search.text())
            self.patric_list.clear()
            for item in self.search_results:
                name = item.organism
                self.patric_list.addItem(name)
        def patric_id_search():
            self.search_results = retrieval.search_by_id(self.patric_search.text())
            self.patric_list.clear()
            for item in self.search_results:
                name = item.organism
                self.patric_list.addItem(name)
        def add_patric():
            selected_item = self.patric_list.currentItem().text()
            for i in range(self.patric_selected.__len__()):
                entry = self.patric_selected.item(i).text()
                if entry == selected_item:
                    return
            self.patric_selected.addItem(selected_item)
            for item in self.search_results:
                if item.organism == selected_item:
                    self.candidates.append(item)
                    break
        def remove_patric():
            selected_index = self.patric_selected.currentRow()
            selected_item = self.patric_selected.currentItem()
            self.patric_selected.takeItem(selected_index)
            for item in self.candidates:
                if item.organism == selected_item:
                    self.candidates.remove(item)
                    break
            print([item.organism for item in self.candidates])
        # retrieve gene sequences from PATRIC
        def continue_patric():
            self.candidates = retrieval.retrieve_sequences(self.candidates)
            stack.setCurrentIndex(1)
        # add functionality for file search
        def select_file():
            genome_file = QtWidgets.QFileDialog.getOpenFileName(self.file_page)
            self.search_results = retrieval.read_genomes(genome_file[0])
            for item in self.search_results:
                self.file_list.addItem(item.organism)
        # add functionality to search button on file page
        def search_candidates():
            query = self.search_bar.text()
            self.file_list.clear()
            for item in self.search_results:
                if query.lower() in item.organism.lower():
                    self.file_list.addItem(item.organism)
        # add item to selected genomes (on file page)
        def add_selection_from_file():
            selection = self.file_list.currentItem().text()
            print(selection)
            print('working')
            for item in self.candidates:
                if item.organism == selection:
                    return
            for item in self.search_results:
                if item.organism == selection:
                    self.file_selected.addItem(selection)
                    self.candidates.append(item)
                    break
        def remove_selection_from_file():
            selection = self.file_selected.currentItem().text()
            selection_index = self.file_selected.currentRow()
            self.file_selected.takeItem(selection_index)
            for item in self.candidates:
                if item.organism == selection:
                    self.candidates.remove(item)

        # allow user to add search methods
        def add_hmm_search():
            hmm_file = QtWidgets.QFileDialog.getOpenFileName(self.search_menu)
            name = hmm_file[0].split('/')[-1]
            self.to_be_searched.addItem(name)
            self.search_objects[name] = search_tools.HMMSearch(hmm_file[0])

        def add_motif_search():
            motif_file = QtWidgets.QFileDialog.getOpenFileName(self.search_menu)
            name = motif_file[0].split('/')[-1]
            self.to_be_searched.addItem(name)
            self.search_objects[name] = search_tools.MotifSearch(motif_file[0])

        def add_psiblast_search():
            pssm_file = QtWidgets.QFileDialog.getOpenFileName(self.search_menu)
            name = pssm_file[0].split('/')[-1]
            self.to_be_searched.addItem(name)
            self.search_objects[name] = search_tools.PSIBlastSearch(pssm_file[0])

        def remove_selection_from_searches():
            selection = self.to_be_searched.currentItem().text()
            selection_index = self.to_be_searched.currentRow()
            self.to_be_searched.takeItem(selection_index)
            for item in self.search_objects:
                if item.pssm_file == selection:
                    self.search_objects.remove(item)

        # allow user to make searches
        def run_searches():
            # create empty dictionary
            results = [{'genome': genome.organism, 'genes': []} for genome in self.candidates]  # generate empty structure
            for item in self.search_objects:
                if isinstance(item, search_tools.HMMSearch):
                    copyfile(self.search_objects[item].file, 'temp_files/'+item)
                for i, genome in enumerate(self.candidates):
                    features = self.search_objects[item].run(genome)
                    links = [{'url': 'https://www.patricbrc.org/view/Feature/{}#view_tab=overview'.format(item), 'name': item} for item in features]
                    results[i]['genes'].append(links)
            utils.generate_page(results, headings=['organism']+list(self.search_objects.keys()))

        # connect buttons to functions
        self.name_search_button.clicked.connect(patric_name_search)
        self.taxon_search_button.clicked.connect(patric_id_search)
        self.add_patric_button.clicked.connect(add_patric)
        self.patric_remove_button.clicked.connect(remove_patric)
        self.browse_button.clicked.connect(select_file)
        self.search_button.clicked.connect(search_candidates)
        self.add_button.clicked.connect(add_selection_from_file)
        self.remove_button.clicked.connect(remove_selection_from_file)
        self.continue_button.clicked.connect(lambda: stack.setCurrentIndex(1))
        self.continue_button_2.clicked.connect(continue_patric)
        self.hmm_button.clicked.connect(add_hmm_search)
        self.motif_button.clicked.connect(add_motif_search)
        self.search_genomes_button.clicked.connect(run_searches)
        self.psi_button.clicked.connect(add_psiblast_search)
        self.remove_search_button.clicked.connect(remove_selection_from_searches)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StackedWidget = QtWidgets.QStackedWidget()
    ui = Ui_StackedWidget()
    ui.setupUi(StackedWidget)
    StackedWidget.show()
    sys.exit(app.exec_())
