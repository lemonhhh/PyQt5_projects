from PyQt5.Qt import *
import sys


app = QApplication(sys.argv)


window = QWidget()

window.setWindowTitle("按钮的功能")
window.resize(500,500)


btn = QPushButton(window)
btn.setText("xxx")
btn.setIcon(QIcon("flower.png"))

#菜单设置
menu = QMenu()
#子菜单 最近打开
open_recent_menu = QMenu(menu)
open_recent_menu.setTitle("最近打开")


#行为动作 新建 打开 分割线 退出
new_action = QAction()
new_action.setText("新建")
new_action.setIcon(QIcon("flower.png"))
new_action.triggered.connect(lambda :print("新建文件"))

open_action = QAction("打开",menu)
open_action.triggered.connect(lambda :print("打开文件"))


exit_action = QAction("退出",menu)
exit_action.triggered.connect(lambda :print("退出程序"))

file_action = QAction("python-GUI-PyQt5")
menu.addAction(new_action)
menu.addAction(open_action)
open_recent_menu.addAction()
menu.addMenu(open_recent_menu)
menu.addSeparator()
menu.addAction(exit_action)

btn.setMenu(menu)
btn.show(menu)
#*******


window.show()
sys.exit(app.exec_())

