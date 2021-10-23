from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__() #调用父类的方法
        self.setWindowTitle("QAbstractSlider的学习")
        self.resize(500,500)
        self.setup_ui()



    def setup_ui(self):
        label = QLabel(self)
        label.setText("0")
        label.move(200,200)
        label.resize(100,30)
        sd = QSlider(self)
        sd.move(100,100)
        sd.valueChanged.connect(lambda val:label.setText(str(val)))
        #设置数值范围
        sd.setMaximum(100)
        sd.setMinimum(10)
        #当前数值
        sd.setValue(88)
        #设置步长
        sd.setSingleStep(5)


        #是否追踪
        # sd.setTracking(False)

        #滑块位置
        sd.setSliderPosition(88)



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

