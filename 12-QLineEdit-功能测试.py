from PyQt5.Qt import *
import sys


app = QApplication(sys.argv)


window = QWidget()

window.setWindowTitle("QLineEdit功能测试")
window.resize(500,500)

window.show()
sys.exit(app.exec_())