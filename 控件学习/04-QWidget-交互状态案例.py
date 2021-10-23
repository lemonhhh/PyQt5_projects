from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__() #调用父类的方法
        self.setWindowTitle("交互状态")
        self.resize(500,500)
        self.setup_ui()


    #追加子控件
    def setup_ui(self):
        label = QLabel(self)
        label.setText("标签")
        label.move(100,50)
        label.hide()

        le = QLineEdit(self)
        le.setText("文本框")
        le.move(100,100)

        btn = QPushButton(self)
        btn.setText("登陆")
        btn.move(100,150)
        btn.setEnabled(False)

        def text_cao(text):
            print("文本内容发生了改变",text)

            btn.setEnabled(len(text) > 0)

        le.textChanged.connect(text_cao)

        def check():
            # print("被点击了")
            # 获取文本框内容
            content = le.text()

            #判定是否是sz
            if content == "sz":
                label.setText("登录成功")

            else:
                label.show()


            label.show()
            label.adjustSize()
            #是的化 显示隐藏的标签
        btn.pressed.connect(check)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

