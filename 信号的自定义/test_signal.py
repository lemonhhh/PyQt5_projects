from PyQt5.Qt import *

class Btn(QPushButton):
    rightClicked = pyqtSignal()

    def mousePressEvent(self,evt) -> None:
        super().mousePressEvent(evt)
        if evt.button() == Qt.RightButton:
            print("右击")

class Window(QWidget):
    def __init__(self):
        super().__init__() #调用父类的方法
        self.setWindowTitle("test_signal")
        self.resize(500,500)
        self.setup_ui()



    def setup_ui(self):
        btn = Btn("xx",self)
        btn.rightClicked.connect(lambda: print("click"))



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

