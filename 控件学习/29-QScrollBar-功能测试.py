from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__() #调用父类的方法
        self.setWindowTitle("QScrollBar功能测试")
        self.resize(500,500)
        self.setup_ui()



    def setup_ui(self):
        sb2 = QScrollBar(self)
        sb2.resize(30,200)
        sb2.move(100,100)

        sb2 = QScrollBar(Qt.Horizontal,self)
        sb2.resize(200, 30)
        sb2.move(150, 100)
        

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

