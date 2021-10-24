from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__() #调用父类的方法
        self.setWindowTitle("QMessage")
        self.resize(500,500)
        self.setup_ui()



    def setup_ui(self):
        mb = QMessageBox(QMessageBox.Warning,"窗口标题","<h2>主标题</h2>",QMessageBox.Ok | QMessageBox.Discard,self)
        mb.open()
        

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

