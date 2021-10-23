from PyQt5.Qt import *
import sys


app = QApplication(sys.argv)


window = QWidget()

window.setWindowTitle("QToolButton使用")
window.resize(500,500)

tb = QToolButton(window)
tb.setText("工具")
tb.setIcon(QIcon("flower.png"))
tb.setIconSize(QSize(50,50))
tb.setToolTip("花")

window.show()
sys.exit(app.exec_())