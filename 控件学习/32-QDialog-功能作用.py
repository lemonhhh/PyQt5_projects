from PyQt5.Qt import *
import sys


app = QApplication(sys.argv)


window = QWidget()

window.setWindowTitle("QDialog")
window.resize(500,500)

d = QDialog()
d.setWindowTitle("对话")
# d.exec()
d.open()

window.show()
sys.exit(app.exec_())