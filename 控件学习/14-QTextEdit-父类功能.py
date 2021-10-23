from PyQt5.Qt import *
import sys


app = QApplication(sys.argv)


window = QWidget()

window.setWindowTitle("QTextEdit父类功能测试")
window.resize(500,500)


t1 = QTextEdit("小猫真可爱",window)
t1.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
t1.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
window.show()
sys.exit(app.exec_())