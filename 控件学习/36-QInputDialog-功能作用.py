from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__() #调用父类的方法
        self.setWindowTitle("QInputDialog")
        self.resize(500,500)
        self.setup_ui()



    def setup_ui(self):
        result = QInputDialog.getInt(self,"标题","标签",888,step=8)
        result = QInputDialog.getDouble(self,"标题","标签",888.88,decimals=2)
        result = QInputDialog.getText(self,"标题","标签",echo=QLineEdit.Password)
        result = QInputDialog.getMultiLineText(self,"标题","标签","default")
        result = QInputDialog.getItem(self,"标题","标签",["1","2","3"],2,True)
        print(result)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

