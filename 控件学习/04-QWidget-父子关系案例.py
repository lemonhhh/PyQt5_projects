from PyQt5.Qt import *
import sys

# class Label(QLabel):
#     def mousePressEvent(self,QMouseEvent):
#         self.setStyleSheet("background-color:red;")

class Window(QWidget):
    def mousePressEvent(self,evt):
        local_x = evt.x()
        local_y = evt.y()
        #获取指定位置的控件
        sub_widget = self.childAt(local_x,local_y)
        if sub_widget is not None:
            sub_widget.setStyleSheet("background-color:red;")

app = QApplication(sys.argv)


window = Window()

window.setWindowTitle("")
window.resize(500,500)

for i in range(1,11):
    label = QLabel(window)
    label.setText("标签" + str(i))
    label.move(40*i,40*i)

window.show()
sys.exit(app.exec_())