from PyQt5.Qt import *
import sys


app = QApplication(sys.argv)


window = QWidget()

window.setWindowTitle("QLineEdit功能测试")
window.resize(500,500)

lea = QLineEdit(window)
lea.move(100,100)
leb = QLineEdit(window)
leb.move(100,200)
leb.setEchoMode(QLineEdit.NoEcho)

btn = QPushButton(window)
btn.move(100,300)
btn.setText("复制")

def copy_cao():
    #获取文本框a的内容
    context = lea.text()
    #复制b
    leb.setText(context)
btn.clicked.connect(copy_cao)
window.show()
sys.exit(app.exec_())