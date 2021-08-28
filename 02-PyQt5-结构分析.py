
#0。导入需要的包和模块
from PyQt5.Qt import *
import sys

'''
代码的执行方式
1.在pycharm中执行
2.命令行执行
'''
#1.创建应用程序对象
app = QApplication(sys.argv)


#2.控件的操作
#创建控件，设置控件，事件、信号的处理
#2.1 创建控件
'''
当创建一个控件之后，如果这个控件没有父控件，则把它当成顶层顶尖
系统会自动给窗口添加一些装饰，窗口控件具备一些特性
'''
window = QWidget()

#2.2 设置控件
window.setWindowTitle("This is my first try")

'''
大小不包括标题栏
'''
window.resize(500,500)
window.move(400,200)

'''
控件也可以作为一个容器，承载其他控件
刚创建好一个控件之后（没有父控件），默认情况不会展示，只有手动调用show()才可以
'''
label = QLabel(window)
label.setText("Hello world!")
label.setWindowTitle("This is a title")
label.move(200,200)

'''
如果控件是有父控件的，那么父控件显示了就行
'''
# label.show()


window.show()

#3.应用程序的执行，进入到消息循环
sys.exit(app.exec_())


