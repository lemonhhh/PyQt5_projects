from PyQt5.Qt import *
import sys


app = QApplication(sys.argv)


window = QWidget()

window.setWindowTitle("焦点控制")
window.resize(500,500)

le1 = QLineEdit(window)
le1.move(50,50)

le2 = QLineEdit(window)
le2.move(50,100)

le3 = QLineEdit(window)
le3.move(50,150)

le1.clearFocus()
# le2.setFocusPolicy(Qt.ClickFocus)
le2.setFocusPolicy(Qt.StrongFocus)
window.show()
sys.exit(app.exec_())