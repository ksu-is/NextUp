import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("NextUp")
window.resize(1100, 700)

window.setStyleSheet("background-color: #15171e;")

window.show()

sys.exit(app.exec_())