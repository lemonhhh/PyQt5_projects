from PyQt5.Qt import *
import math

class Btn(QPushButton):
    def hitButton(self, point):
        yuanxin_x =  self.width()/2
        yuanxin_y = self.height()/2

        hit_x = point.x()
        hit_y = point.y()

        r = self.width()/2

        distance = math.sqrt(math.pow(hit_x - yuanxin_x,2) + math.pow(hit_y-yuanxin_y,2))
        if (distance <= r):
            return True
        else:
            return False


    def paintevent(self,evt):
        super().paintevent(evt)
        painter = QPainter(self)
        painter.setPen(QPen(QColor(100,150,200),6))
        painter.drawEllipse(self.rect())


class Window(QWidget):
    def __init__(self):
        super().__init__() #调用父类的方法
        self.setWindowTitle("")
        self.resize(500,500)
        self.setup_ui()



    def setup_ui(self):
        btn = Btn("xxx",self)
        btn.resize(200,200)
        btn.move(100,100)



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

