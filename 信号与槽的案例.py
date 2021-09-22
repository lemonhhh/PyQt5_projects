from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__() #调用父类的方法
        self.setWindowTitle("")
        self.resize(500,500)
        self.setup_ui()



    def setup_ui(self):
        self.QObject_signal_operation()

    # def QObject_signal_operation(self):
    #     btn = QPushButton(self)
    #     btn.setText("点我点我点我")
    #
    #     def cao():
    #         print("干嘛点我～")
    #
    #     btn.clicked.connect(cao)

    pass

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    # window = Window()
    window = QWidget()
    window.setWindowTitle("Hello sz!")
    #连接窗口变化的信号
    def cao(title):
        window.windowTitleChanged.disconnect()
        window.setWindowTitle("喵"+title)

    window.windowTitleChanged.connect(cao)
    window.setWindowTitle("Hello sz2!")
    window.setWindowTitle("Hello sz3!")

    window.show()
    sys.exit(app.exec_())

