from PyQt5.Qt import *
import sys

class Btn(QAbstractButton):
    def paintEvent(self,evt):

        #绘制
        #创建一个画家
        painter = QPainter(self)
        #创建一个笔
        pen = QPen(QColor(111,200,20),6)
        #设置这个笔
        painter.setPen(pen)
        #指明区域
        painter.drawText(25,40,self.text())
        painter.drawEllipse(0,0,100,100)


app = QApplication(sys.argv)


window = QWidget()

window.setWindowTitle("QPushButton")
window.resize(500,500)

btn = Btn(window)
btn.resize(100,100)
btn.setText("xxx")
btn.pressed.connect(lambda :print("点击"))
window.show()
sys.exit(app.exec_())