from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__() #调用父类的方法
        self.setWindowTitle("QSpinBox学习")
        self.resize(500,500)
        self.setup_ui()



    def setup_ui(self):
        sb = QSpinBox(self)
        self.sb = sb
        sb.resize(100,25)
        sb.move(100,100)
        self.max_min()
    def max_min(self):
        self.sb.setMaximum(180)
        self.sb.setMinimum(18)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

