from PyQt5.Qt import *
import sys


app = QApplication(sys.argv)


window = QWidget()

window.resize(500,500)
# icon = QIcon("flower.png")
# window.setWindowIcon(icon)
#
window.setWindowTitle("hi")
# print(window.windowTitle())
#
# window.setWindowOpacity(0.9)
# print(window.windowOpacity())




print(window.windowState() == Qt.WindowNoState)
window.setWindowState(Qt.WindowMaximized)
window.show()


w2 = QWidget()
w2.setWindowTitle("第二个")
w2.show()


sys.exit(app.exec_())