from PyQt5.Qt import *
import sys


app = QApplication(sys.argv)


window = QWidget()

window.setWindowTitle("内容边距的设定")
window.resize(500,500)

label = QLabel(window)
label.setText('早上好')
label.resize(300,300)
label.setStyleSheet("background-color:AliceBlue;")
label.setContentsMargins(100,200,0,0)
window.show()
sys.exit(app.exec_())