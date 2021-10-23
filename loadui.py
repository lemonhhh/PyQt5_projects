from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__() #调用父类的方法
        self.setWindowTitle("ui学习")

        self.resize(500,500)
        self.setup_ui()



    def setup_ui(self):
        loadUi()


        

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    print(dir(window))

    sys.exit(app.exec_())

