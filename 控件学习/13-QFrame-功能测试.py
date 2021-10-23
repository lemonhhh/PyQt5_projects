from PyQt5.Qt import *
import sys


app = QApplication(sys.argv)


window = QWidget()

window.setWindowTitle("QFrame功能测试")
window.resize(500,500)

frame = QFrame(window)
frame.resize(100,100)
frame.move(100,100)
frame.setStyleSheet("background-color:cyan;")
frame.setFrameStyle(QFrame.Bos | QFrame.Raised)
frame.setFrameRect(QRect(20,20))
window.show()
sys.exit(app.exec_())