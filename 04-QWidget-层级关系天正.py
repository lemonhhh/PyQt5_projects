from PyQt5.Qt import *
import sys

class Label(QLabel):
    def mousePressEvent(self, evt):
        self.raise_()
app = QApplication(sys.argv)


window = QWidget()

window.setWindowTitle("层级关系调整")
window.resize(500,500)

label1 = Label(window)
label1.setText("标签1")
label1.resize(200,200)
label1.setStyleSheet("background-color:red;")

label2 = Label(window)
label2.setText("标签2")
label2.resize(200,200)
label2.setStyleSheet("background-color:green;")
label2.move(50,50)

window.show()
sys.exit(app.exec_())