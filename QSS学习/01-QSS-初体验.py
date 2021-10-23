from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__() #调用父类的方法
        self.setWindowTitle("QSS初体验")
        self.resize(500,500)
        self.setup_ui()



    def setup_ui(self):
        box1 = QWidget(self)
        box2 = QWidget(self)
        v_layout = QVBoxLayout()
        self.setLayout(v_layout)
        v_layout.addWidget(box1)
        v_layout.addWidget(box2)
        # box1.setStyleSheet( "QPushButton { background-color:orange;}")
        # box2.setStyleSheet("background-color:yellow")

        label1 = QLabel("label1",box1)
        label1.setObjectName("l1")
        label1.move(50,50)
        btn1 = QPushButton("button1",box1)
        btn1.move(150,50)

        label2 = QLabel("label2", box2)
        label2.move(50, 50)
        btn2 = QPushButton("button2", box2)
        btn2.move(150, 50)


if __name__ == '__main__':
    import sys
    from Tool import QSSTool
    app = QApplication(sys.argv)
    window = Window()
    QSSTool.setQsstoObj("test.qss",app)
    window.show()
    sys.exit(app.exec_())

