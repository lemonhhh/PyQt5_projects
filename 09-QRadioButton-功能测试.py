from PyQt5.Qt import *
import sys


app = QApplication(sys.argv)


window = QWidget()

window.setWindowTitle("QRadioButton测试")
window.resize(500,500)

rb_nan = QRadioButton('男',window)
rb_nan.move(100,100)
rb_nv = QRadioButton('女',window)
rb_nv.move(100,120)
rb_nv.setIcon(QIcon("flower.png"))
rb_nv.setIconSize(QSize(60,60))
rb_nv.toggled.connect(lambda isChecked: print(isChecked))

window.show()
sys.exit(app.exec_())