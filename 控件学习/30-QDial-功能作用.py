from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__() #调用父类的方法
        self.setWindowTitle("QDial")
        self.resize(500,500)
        self.setup_ui()



    def setup_ui(self):
        label = QLabel(self)
        label.move(200,100)
        label.setText("真好啊")
        # label.setStyleSheet("font-size:30px")
        dia = QDial(self)
        dia.setNotchesVisible(True)
        dia.setPageStep(5)
        dia.setWrapping(True)
        dia.valueChanged.connect(lambda val:label.setStyleSheet("font-size:{}px;".format(val)))


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

