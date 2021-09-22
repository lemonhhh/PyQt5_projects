from PyQt5.Qt import *
import sys

class Window(QWidget):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        # 公共那个数据
        self.top_margin = 10
        self.btn_w = 80
        self.btn_h = 40

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.resize(500, 500)
        self.setWindowOpacity(0.9)
        self.setup_ui()




    def setup_ui(self):


        self.close_btn = QPushButton(self)
        self.close_btn.setText("关闭")
        self.close_btn.resize(self.btn_w, self.btn_h)


        self.max_btn = QPushButton(self)
        self.max_btn.setText("最大化")
        self.max_btn.resize(self.btn_w, self.btn_h)


        self.min_btn = QPushButton(self)
        self.min_btn.setText("最小化")
        self.min_btn.resize(self.btn_w, self.btn_h)


        def max_normal():
            if (self.isMaximized()):
                self.showNormal()
                self.max_btn.setText("最大化")
            else:
                self.showMaximized()
                self.max_btn.setText("恢复")


        self.close_btn.pressed.connect(self.close)
        self.max_btn.pressed.connect(max_normal)
        self.min_btn.pressed.connect(self.showMinimized)

    #监听大小改变
    def resizeEvent(self,QResizeEvent):
        close_btn_w = self.btn_w
        window_w = self.width()
        close_btn_x = window_w - self.btn_w
        close_btn_y = self.top_margin
        self.close_btn.move(close_btn_x, close_btn_y)

        max_btn_x = close_btn_x - self.btn_w
        max_btn_y = self.top_margin
        self.max_btn.move(max_btn_x, max_btn_y)

        min_btn_x = max_btn_x - self.btn_w
        min_btn_y = self.top_margin
        self.min_btn.move(min_btn_x, min_btn_y)

    def mousePressEvent(self, QMouseEvent):
        #判断是否是左键
        #在此处设计一个标记，用作判断是否需要移动
        #窗口的原始坐标
        #鼠标按下的点

        #鼠标按下的点
    def mouseMoveEvent(self,QMouseEvent):
        #如果窗口移动标记==True
        #根据鼠标按下的点计算移动向量
        #根据移动向量和窗口原始坐标=最新坐标
    def mouseReleaseEvent(self,QMouseEvent):
        #把标记重置成False







app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())