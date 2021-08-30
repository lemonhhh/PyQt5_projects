
#0。导入需要的包和模块
from PyQt5.Qt import *
import sys
from menu import Window

app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec_())