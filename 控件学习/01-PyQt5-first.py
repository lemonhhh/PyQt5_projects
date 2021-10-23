from PyQt5.Qt import *


import sys

#创建应用程序对象
app = QApplication(sys.argv)

#空间操作
window = QWidget()
window.setWindowTitle("This is my first try")
window.resize(500,500)
window.move(400,200)

label = QLabel(window)
label.setText("Hello world!")
label.move(200,200)
window.show()

#开始执行应用程序，并进入消息循环
sys.exit(app.exec_())