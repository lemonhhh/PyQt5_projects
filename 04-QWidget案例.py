import sys
from PyQt5.Qt import *

app = QApplication(sys.argv)



window = QWidget()
window.resize(500,500)
window.move(300,300)

#总控件的个数
widget_count = 100
#一行有多少列
count_column = 5
widget_width = window.width() / count_column
#多商行
row_count = (widget_count -1) // count_column + 1
widget_height = window.height() / row_count

for i in range(widget_count):
    w = QWidget(window)
    widget_x = (i % count_column ) * widget_width
    widget_y = (i // count_column) * widget_height
    w.move(widget_x,widget_y)
    w.resize(widget_width,widget_height)
    w.setStyleSheet("background-color:red;border:1px solid black;")

window.show()


sys.exit(app.exec_())