from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__() #调用父类的方法
        self.move_flag = False
        self.setWindowTitle("")
        self.resize(500,500)
        self.setup_ui()



    def setup_ui(self):
        pass

    def mousePressEvent(self,evt):
        self.move_flag = True
        self.mouse_x = evt.globalX()
        self.mouse_y = evt.globalY()

        #窗口原始位置
        self.origin_x = self.x()
        self.origin_y = self.y()

    def mouseMoveEvent(self,evt):
        if(self.move_flag):
        #计算的是移动的向量（相对刚点击的时候）
            move_x = evt.globalX() - self.mouse_x
            move_y = evt.globalY() - self.mouse_y

            dest_x = self.origin_x + move_x
            dest_y = self.origin_y + move_y
            self.move(dest_x,dest_y)


    def mouseReleaseEvent(self,evt):
        self.move_flag = False

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()

    sys.exit(app.exec_())

