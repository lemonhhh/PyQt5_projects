from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__() #调用父类的方法
        self.setWindowTitle("QTextEdit学习")
        self.resize(500,500)
        self.setup_ui()



    def setup_ui(self):
        te = QTextEdit("xxx",self)
        te.move(50,50)
        te.remove(300,300)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

