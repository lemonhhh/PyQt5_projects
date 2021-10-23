from PyQt5.Qt import *
import sys


app = QApplication(sys.argv)


window = QWidget()

window.setWindowTitle("最小最大尺寸的限定")
window.resize(300,300)
window.setMinimumSize(200,200)
window.setMaximumSize(500,500)

window.show()
sys.exit(app.exec_())