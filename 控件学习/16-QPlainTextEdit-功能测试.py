from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__() #调用父类的方法
        self.setWindowTitle("QPlainTextEdit学习")
        self.resize(500,500)
        self.setup_ui()



    def setup_ui(self):
        pte = QPlainTextEdit(self)
        pte.resize(300,300)
        pte.move(100,100)
        

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

