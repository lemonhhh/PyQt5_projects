from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__() #调用父类的方法
        self.setWindowTitle("QSlider")
        self.resize(500,500)
        self.setup_ui()



    def setup_ui(self):
        sd = QSlider(self)
        sd.move(100,100)
        sd.setTickPosition(QSlider.TicksRight)
        


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

