from PyQt5.Qt import *
import sys


app = QApplication(sys.argv)


window = QWidget()

window.setWindowTitle("QCheckBox")
window.resize(500,500)

cb = QCheckBox("python",window)
cb.setIcon(QIcon("flower.png"))
cb.setIconSize(QSize(50,50))

cb.setCheckState(Qt.PartiallyChecked)
window.show()
sys.exit(app.exec_())