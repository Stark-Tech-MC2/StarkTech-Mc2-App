import os
import shutil
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QFileDialog, QTextBrowser, QCheckBox, \
    QWidget, QVBoxLayout, QHBoxLayout,QFrame,QMessageBox
from PyQt5.QtCore import Qt

from get_data import get_data

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)
        self.setWindowTitle("IO Maker")
        self.setGeometry(100, 100, 500, 800)  # Set window size

        

        self.button_open_dialog = QPushButton("Add A Spreadsheet", self)
        
        self.button_open_dialog.clicked.connect(self.openFileDialog)

        self.button_submit_data = QPushButton("Submit Data", self)
        self.button_submit_data.clicked.connect(self.submitData)

        self.text_edit_frame = QFrame(self)
        self.text_edit_frame.setMaximumHeight(0) 
        self.text_edit_frame.setMaximumWidth(0)
        self.text_edit_frame.setFrameShape(QFrame.Panel)  # Set frame shape
        self.text_edit_frame.setFrameShadow(QFrame.Sunken)  # Set frame shadow

        self.text_edit = QTextBrowser(self.text_edit_frame)  # Add QTextBrowser to the frame
        self.text_edit.setMinimumHeight(600) 
        self.text_edit.setMaximumWidth(900)


        self.text_edit_frame1 = QFrame(self)
        self.text_edit_frame1.setMaximumHeight(0) 
        self.text_edit_frame1.setMaximumWidth(0)
        self.text_edit_frame1.setFrameShape(QFrame.Panel)  # Set frame shape
        self.text_edit_frame1.setFrameShadow(QFrame.Sunken)  # Set frame shadow
        
        self.text_edit1 = QTextBrowser(self.text_edit_frame1)  # Add QTextBrowser to the frame
        self.text_edit1.setMinimumHeight(600) 
        self.text_edit1.setMaximumWidth(900)
        self.text_edit1.setOpenExternalLinks(True)  # Allow opening links

        self.text_edit1.anchorClicked.connect(self.download_file)

        self.main_layout.addWidget(self.text_edit_frame1)
        self.directory1 = os.path.join(os.path.expanduser("~"), r"IO Creator\CreatedIO")
        self.show_files_in_directory(self.directory1)
        self.directory = os.path.join(os.path.expanduser("~"), r"IO Creator\SpreadSheets")
        

        self.setupLayout()

        self.showMaximized()

    def setupLayout(self):
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.button_open_dialog)
        button_layout.addWidget(self.button_submit_data)
        textlayout = QHBoxLayout()
       
        
        textlayout.addWidget(self.text_edit)
        textlayout.addWidget(self.text_edit1)
        
        self.checkbox_layout = QVBoxLayout()
        self.main_layout.addLayout(button_layout)
        
        self.main_layout.addLayout(textlayout)
        self.main_layout.addLayout(self.checkbox_layout)
        self.main_layout.addStretch(1)
        self.viewFiles()

    def openFileDialog(self):
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.ExistingFiles)
        if file_dialog.exec_():
            files = file_dialog.selectedFiles()
            for file in files:
                filename = os.path.basename(file)
                destination = os.path.join(self.directory, filename)
                os.rename(file, destination)

            self.directory = os.path.join(os.path.expanduser("~"), r"IO Creator\SpreadSheets")  # Update self.directory
            self.viewFiles()
            print("openFileDialog method called")

    def submitData(self):
        checked_files = [checkbox.text() for checkbox in self.checkboxes if checkbox.isChecked()]
        if checked_files:
            for filename in checked_files:
                data = get_data(filename)

                if data:
                    text = ''
                    for item in data:
                        for key, value in item.items():
                            # Replace commas with newlines in each value
                            modified_value = str(value).replace(',', '\n')
                            text += f"{key}: {modified_value}\n"  # Append key-value pair
                        text += '\n'  # Add a newline between each dictionary
                    self.text_edit.append(text.strip())  # Remove trailing newline
                    self.directory1 = os.path.join(os.path.expanduser("~"), r"IO Creator\CreatedIO")
                    self.show_files_in_directory(self.directory1)
                else:
                    self.text_edit.append("No data available for {}".format(filename))




                self.printMessage(filename)


    def printMessage(self, filename):
        print("Button clicked for file:", filename)

    def viewFiles(self):
        # Clear existing checkboxes
        for i in reversed(range(self.checkbox_layout.count())):
            self.checkbox_layout.itemAt(i).widget().setParent(None)

        files = os.listdir(self.directory)
        print("Files in directory:", files)

        # Add new checkboxes
        self.checkboxes = []
        for file in files:
            checkbox = QCheckBox(file, self)
            checkbox.toggled.connect(self.updateCheckBoxes)
            self.checkbox_layout.addWidget(checkbox)
            self.checkboxes.append(checkbox)
        self.checkbox_layout.parentWidget().setMinimumHeight(max(len(files) * 25, 200)) 

    def clearCheckBoxes(self):
        for checkbox in self.checkboxes:
            checkbox.deleteLater()
        self.checkboxes.clear()

    def updateCheckBoxes(self, checked):
        sender_checkbox = self.sender()
        if checked:
            for checkbox in self.checkboxes:
                if checkbox != sender_checkbox:
                    checkbox.setChecked(False)
    def show_files_in_directory(self, directory):
        file_list = os.listdir(directory)
        file_links = [f"<a href='file://{os.path.join(directory, file)}'>{file}</a>" for file in file_list]
        file_html = "<br>".join(file_links)
        self.text_edit1.setHtml(file_html)

    def download_file(self):
        try:
            if os.path.exists(self.directory1):
                os.startfile(self.directory1)  # Open the folder
                
            else:
                QMessageBox.warning(self, "Folder Not Found", "The specified folder does not exist.")
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Error opening folder: {str(e)}")