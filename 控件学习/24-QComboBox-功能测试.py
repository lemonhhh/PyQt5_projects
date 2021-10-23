from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__() #调用父类的方法
        self.setWindowTitle("QComboBox")
        self.resize(500,500)
        self.setup_ui()



    def setup_ui(self):
        cd = QComboBox(self)
        cd.addItems(["1","2","3"])
        cd.setItemIcon(2,QIcon("flower.png"))
    

        

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

