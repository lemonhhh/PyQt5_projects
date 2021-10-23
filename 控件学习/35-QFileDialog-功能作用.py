from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__() #调用父类的方法
        self.setWindowTitle("File")
        self.resize(500,500)
        self.setup_ui()



    def setup_ui(self):
        result = QFileDialog.getOpenFileName(self,"选择一个py文件","./","All(*.*);;Images(*.png *.jpg);;Python文件(*.py)")


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

