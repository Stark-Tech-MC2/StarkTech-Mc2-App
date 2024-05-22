from UI.UI import MainWindow
from get_data import get_data
from AddIOP import AddIOP
import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi

def main():
    # Your main code here
    #filename = r"C:\Users\ponced\IO Creator\SpreadSheets\IO Test.csv"
    #get_data(filename)
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()
