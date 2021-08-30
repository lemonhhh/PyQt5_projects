

from PyQt5.Qt import *
import sys



app = QApplication(sys.argv)

window = QWidget()

window.setWindowTitle("QLabel的学习")
window.resize(500,500)

label = QLabel(window)
label.setText("xxx")

window.show()
sys.exit(app.exec_())


