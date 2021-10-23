from PyQt5.Qt import *
import sys


app = QApplication(sys.argv)


window = QWidget()

window.setWindowTitle("父子关系学习")

window.resize(500,500)


label1 = QLabel(window)
label1.setText("标签1")

label2 = QLabel(window)
label2.setText("标签1")
label2.move(50,50)
print(label2.parentWidget())

label3 = QLabel(window)
label3.setText("标签1")
label3.move(100,100)

window.show()
sys.exit(app.exec_())