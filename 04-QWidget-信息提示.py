from PyQt5.Qt import *
import sys


app = QApplication(sys.argv)


window = QMainWindow()
#组合控件（有状态栏）
#懒加载：用到的时候才创建
window.statusBar()
window.setStatusTip("这是窗口")

window.setWindowTitle("信息提示案例")
window.resize(500,500)
window.setWindowFlags(Qt.WindowContextHelpButtonHint)
#当鼠标停留在窗口控件身上，在信息提示拦显示文本

label = QLabel(window)
label.setText("社会啊")
label.setStatusTip("这是标签")
label.setToolTip("这是一个提示标签")
label.setToolTipDuration(2000)
label.setWhatsThis("这是啥")
print(label.toolTip())

window.show()
sys.exit(app.exec_())