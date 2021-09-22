from PyQt5.Qt import *
import sys

class Window(QWidget):
    def __init__(self):
        super().__init()
        self.setWindowTitle("鼠标操作")
        self.resize(500, 500)
        self.move(200, 200)


    def mouseMoveEvent(self, mv):
        print("鼠标移动",mv.localPos())
        label = self.findChild(QLabel)
        label.move(mv.localPos().x(),mv.localPos().y())

app = QApplication(sys.argv)


window = Window()



window.setMouseTracking(True)


pixmap = QPixmap("flower.png").scaled(50,50)
cursor = QCursor(pixmap)
window.setCursor(cursor)
label = QLabel(window)
label.setText("啊ddd")
label.move(100,100)
label.setStyleSheet("background-color:cyan;")


window.show()
sys.exit(app.exec_())