from PyQt5.Qt import *
import sys


app = QApplication(sys.argv)


window = QWidget()

window.setWindowTitle("QCommondLinkButton")
window.resize(500,500)

window.show()
sys.exit(app.exec_())