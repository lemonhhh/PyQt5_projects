from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__() #调用父类的方法
        self.setWindowTitle("QFontDialog")
        self.resize(500,500)
        self.setup_ui()



    def setup_ui(self):
        fd = QFontDialog(self)
        font = QFont()
        font.setFamily("宋体")
        font.setPointSize(36)
        btn = QPushButton(self)
        btn.setText("按钮")
        btn.move(100,100)
        btn.clicked.connect(lambda :fd.open())


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

