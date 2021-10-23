from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__() #调用父类的方法
        self.setWindowTitle("布局管理")
        self.resize(500,500)
        self.setup_ui()



    def setup_ui(self):
        label1 = QLabel("标签1",self)
        label1.setStyleSheet("background-color:cyan;")
        label2 = QLabel("标签1", self)
        label2.setStyleSheet("background-color:yellow;")
        label3 = QLabel("标签1", self)
        label3.setStyleSheet("background-color:red;")

        #垂直排列



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

