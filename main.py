import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from views.ui_main_window import MainWindow

def main():
    
    app = QApplication(sys.argv)

    window = QMainWindow()

    ui = MainWindow()
    ui.setupUi(window)

    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()