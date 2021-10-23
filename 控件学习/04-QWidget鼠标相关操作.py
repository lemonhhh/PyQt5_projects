from PyQt5.Qt import *
import sys

class MyWindow(QWidget):
    def mouseMoveEvent(self, me):
        print("鼠标移动了")

app = QApplication(sys.argv)


window = MyWindow()
window.setWindowTitle("鼠标操作")
window.resize(500,500)
window.setMouseTracking(True)

'''
pixmap = QPixmap("flower.png")
pixmap = pixmap.scaled(50,50)
cursor = QCursor(pixmap,0,0)
window.setCursor(cursor)
window.unsetCursor()
label = QLabel(window)
label.setText("喵")
label.resize(100,100)
label.setStyleSheet("background-color:cyan;")

'''







window.show()
sys.exit(app.exec_())