from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__() #调用父类的方法
        self.setWindowTitle("QDoubleSpinBox")
        self.resize(500,500)
        self.setup_ui()



    def setup_ui(self):
        dsb = QDoubleSpinBox(self)
        dsb.move(100,100)
        dsb.resize(50,50)
        dsb.setMaximum(88.88)
        dsb.setMaximum(66.66)


        dsb.setPrefix("$")
        dsb.setSuffix("%")
        dsb.valueChanged.connect(lambda val:print(val))




if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

