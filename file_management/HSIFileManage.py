# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 12:33:17 2020

@author: nick.viner
"""

import os
from PyQt5 import QtCore, QtWidgets, Qt
from PyQt5.QtWidgets import QAction
import sys
import HSIFileView_ui

class manage_Hsi(QtWidgets.QMainWindow, HSIFileView_ui.Ui_MainWindow):
    
    def __init__(self, parent=None):
        
        super().__init__()
        
        #Setup initial GUI
        self.setupUi(self)
        
        #Create filetree and table objects
        self.fileTreeView = file_Tree()
        self.batchTable = batch_Table()
        
        #Layout for buttons
        self.button_layout = QtWidgets.QVBoxLayout()
        
        #Add filetree and table to layout
        self.layout.addWidget(self.fileTreeView)
        self.layout.addWidget(self.batchTable)
        self.layout.addLayout(self.button_layout)
                
        #Initialize pushbutton for setting export directory
        self.set_output_directory = QtWidgets.QPushButton()
        self.set_output_directory.setText("Set Export")
        self.button_layout.addWidget(self.set_output_directory)
        
        #Job name text box
        self.job_name = QtWidgets.QLineEdit()
        self.job_name.setText("Job Name")
        self.button_layout.addWidget(self.job_name)
        
        #Session Number
        self.session_number = QtWidgets.QLineEdit()
        self.session_number.setText("Session Number")
        self.button_layout.addWidget(self.session_number)

        #Initialize pushbutton for the build_directory function
        self.build_file_structure = QtWidgets.QPushButton()
        self.build_file_structure.setText("Build Directory")
        self.button_layout.addWidget(self.build_file_structure)
        
        #Initialize pushbutton for moving files into proper directory structure
        self.move_files = QtWidgets.QPushButton()
        self.move_files.setText("Move Files")
        self.button_layout.addWidget(self.move_files)
        
        #Set inital states to false.
        self.build_file_structure.setEnabled(False)
        self.fileTreeView.setEnabled(False)
        self.batchTable.setEnabled(False)
        self.move_files.setEnabled(True)
        
        #Connect Signals
        self.reset.triggered.connect(self.reset_Gui)
        self.set_output_directory.clicked.connect(self.set_export_dir)
        self.fileTreeView.fileSelect.connect(self.batchTable._file_to_list)
        self.build_file_structure.clicked.connect(self.build_directory)
        self.remove_Rows.triggered.connect(self.remove_files)
        self.move_files.clicked.connect(self.move_files_to_cgp_structure)
        
        #Export Directory
        self.outdir = None
        self.session_folder = None
    
    def move_files_to_cgp_structure(self):
        
        for f in self.fileTreeView.files_for_batch:

            #Target files
            hdr_data_origin = f + "/capture/%s.hdr" % f.split("/")[-1]
            raw_data_origin = f + "/capture/%s.raw" % f.split("/")[-1]
            nav_data_origin = f + "/capture/%s.nav" % f.split("/")[-1]
                        
            print(hdr_data_origin)
            print(raw_data_origin)
            print(nav_data_origin)
            
            #Move target files to:
            data_target = self.session_folder + "/%s" % f.split("/")[-1]
            hdr_data_target = data_target + "/%s.hdr" % f.split("/")[-1]
            raw_data_target = data_target + "/%s.raw" % f.split("/")[-1]
            nav_data_target = data_target + "/%s.nav" % f.split("/")[-1]
            
            print(hdr_data_target)
            print(raw_data_target)
            print(nav_data_target)
            
            try:
                os.mkdir(data_target)
                os.rename(hdr_data_origin, hdr_data_target)
                os.rename(nav_data_origin, nav_data_target)
                os.rename(raw_data_origin, raw_data_target)
                
            except Exception as e:
                
                print(e)
            
    def remove_files(self):
        
        to_delete = self.batchTable.item(self.batchTable.currentRow(), 0).text()
        
        self.batchTable.remove_selected_item()
        
    def reset_Gui(self):
        
        self.build_file_structure.setEnabled(False)
        self.fileTreeView.setEnabled(False)
        self.batchTable.setEnabled(False)
        self.move_files.setEnabled(False)
        self.fileTreeView.clear_batch()
        
    def set_export_dir(self):
        
        self.outdir = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Base directory to build file structure in"))
        
        if self.outdir == None:
            
            pass
        
        else:
                        
            self.build_file_structure.setEnabled(True)
            self.fileTreeView.setEnabled(True)
            self.batchTable.setEnabled(True)
            self.batchTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        
    def build_directory(self):
        
        jobFolder = os.path.join(self.outdir, self.job_name.text())
        self.session_folder = os.path.join(jobFolder, "sess" + self.session_number.text())
        
        os.mkdir(jobFolder)
        os.mkdir(self.session_folder)
        
        os.chdir(self.session_folder)
        
        for file in ['CAL', 'NAV', 'DEM', 'OUTPUT', 'OPT']:
            
            os.mkdir(file)
        
        for x in self.fileTreeView.files_for_batch:
            
            print(x.split("/")[-1] + ".dat")
            print(x)
            print(os.path.join(x, "/capture/"))
            
        self.move_files.setEnabled(True)
        
               
class batch_Table(QtWidgets.QTableWidget):
    
    #fileAdd = QtCore.pyqtSignal(str)
    fileDeleted = QtCore.pyqtSignal(str)
    
    def __init__(self):
        
        super(batch_Table, self).__init__()
        
        self.setColumnCount(1)
        self.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        header_Horizontal = self.horizontalHeader()
        header_Horizontal.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header_Horizontal.hide()
        
        header_Vertical = self.verticalHeader()
        header_Vertical.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        header_Vertical.hide()
        
        self.setShowGrid(True)
        self.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        
        self.row = 0
        
        self.add_item("Batch Files")
        
        self.selectedCell = None
            
    def remove_selected_item(self):
        
        to_delete = self.item(self.currentRow(), 0).text()
        
        self.removeRow(self.currentRow())
        
        if self.row > 0:
            
            self.row -= 1
            
        self.fileDeleted.emit(to_delete)
            
        
    def add_item(self, val):
        
        self.insertRow(self.row)
        
        self.setItem(self.row,0, QtWidgets.QTableWidgetItem(val))
        
        self.row += 1
        
    #Signal slot to recieve filename string signals and add them to a list
    def _file_to_list(self, file):
        
        #print("message from file tree: %s" % str(file))
        
        self.add_item(QtWidgets.QTableWidgetItem(str(file)))
        

class file_Tree(QtWidgets.QTreeView):
    
    fileSelect = QtCore.pyqtSignal(str)
    
    def __init__(self, base_directory = ''):
        
        super(file_Tree, self).__init__()
        
        self.model = QtWidgets.QFileSystemModel()
        
        self.model.setRootPath("N:/")
        
        self.model.setFilter(QtCore.QDir.AllDirs|QtCore.QDir.NoDotAndDotDot)
        
        self.model.setReadOnly(True)
        
        self.proxy_model = QtCore.QSortFilterProxyModel(filterRole = QtWidgets.QFileSystemModel.FileNameRole)
        
        self.proxy_model.setSourceModel(self.model)
        
        self.setModel(self.proxy_model)
        
        self.setRootIndex(self.model.index("N:/"))
        
        self.setAnimated(True)
        
        self.setIndentation(20)
        
        self.setSortingEnabled(True)
        
        self.cwd = None
        
        self.active_file = None
        
        self.active_filepath = None
        
        self.doubleClicked.connect(self._on_Click)
        
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        
        self.customContextMenuRequested.connect(self._open_Menu)
        
        self.files_for_batch = []
        
    def clear_batch(self):
        
        self.files_for_batch = []

    def _open_Menu(self, pos):
        
        menu = QtWidgets.QMenu()
        
        add_Files_to_Batch = menu.addAction("Add Directory to Batch", self._on_file_select())

        action = menu.exec_(self.mapToGlobal(pos))
        
    #Signal Slot
    def _on_file_select(self):
        
        if self.active_file != None:
        
            self.fileSelect.emit(self.active_filepath)
            
        else:
            
            pass
        
    @QtCore.pyqtSlot(QtCore.QModelIndex)
    def _on_Click(self, index):
        
        source = self.proxy_model.mapToSource(index)
        
        item = self.model.index(source.row(), 0, source.parent())
        
        self.active_file = self.model.fileName(item)
        
        self.active_filepath = self.model.filePath(item)
        
        self.files_for_batch.append(self.active_filepath)
        
        self.fileSelect.emit(self.active_filepath)
            
        #print(self.model.fileName(item), self.model.filePath(item))
        
def make_file_structure(file_path, mission_id):
    
    os.chdir(file_path)
    
    os.mkdir(mission_id)
    
    FILES = ['DARK', 'DEM', 'OUTPUT', 'CAL']
    
    for file in FILES:
        
        os.mkdir("%s/%s" % (mission_id, file))
    
#make_file_structure('.','test')

def _pull_hsi_from_line(day_path):
    
    for session in os.listdir(day_path):
        
        print(session)
    
def move_hsi_data(origin_file_path, destination_file_path):
    
    pass

app = QtWidgets.QApplication(sys.argv)

window = manage_Hsi()

window.show()

app.exec_()
 
