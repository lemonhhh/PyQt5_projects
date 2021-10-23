from PyQt5.Qt import *
import sys

class Window(QWidget):
    def painEvent(self,evt):
        print("窗口被绘制了")
        return super().paintEvent(evt)


class Btn(QPushButton):
    def paintEvent(self,evt):
        print("按钮被绘制了")
        return super().paintEvent(evt)


app = QApplication(sys.argv)


window = Window()

window.setWindowTitle("交互状态[*]")
window.resize(500,500)
window.setWindowModified(True)

# btn = Btn(window)
# btn.setText("小按钮")
# btn.pressed.connect(lambda:print("按钮被点击啦"))
# btn.pressed.connect(lambda :btn.setVisible(False))


btn = Btn(window)
btn.setText("按钮")
btn.setAttribute(Qt.WA_DeleteOnClose,True)
btn.close()

window.show()
sys.exit(app.exec_())