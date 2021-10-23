from PyQt5.Qt import *
import sys
import math

app = QApplication(sys.argv)


window = QWidget()

window.setWindowTitle("按钮功能测试-抽象类")
window.resize(500,500)



#**********文本操作***********
# btn = QPushButton(window)
# def plus_one():
#     print("+")
#     num = int(btn.text())+1
#     btn.setText(str(num))
#
#
# btn.setText("1")
# btn.pressed.connect(plus_one)
#**********文本操作***********

#**********图标设置***********

# icon = QIcon("flower.png")
# btn.setIcon(icon)
#
# size = QSize(50,50)
# btn.setIconSize(size)
# print(btn.iconSize())
#**********图标设置***********


#**********快捷键***********
#方式1
# btn.setText("&abc")
# btn.pressed.connect(lambda :print("按钮被点击了"))

#方式2
# btn.setShortcut("option+a")
#**********快捷键***********


#**********z自动重复***********
# btn.setText("花儿")
# btn.pressed.connect(lambda :print("花儿为什么这样红"))
# btn.setAutoRepeat(True)
# btn.setAutoRepeatDelay(2000)
# print(btn.autoRepeat())
#**********z自动重复***********


#****状态******
# push_button = QPushButton(window)
# push_button.setText("这是QPushButton")
# push_button.move(100,100)
#
# radio_button = QRadioButton(window)
# radio_button.setText("这是一个radio")
# radio_button.move(100,150)
#
# check_box = QCheckBox(window)
# check_box.setText("这是一个check box")
# check_box.move(100,200)
#
# push_button.setDown(True)
# radio_button.setDown(True)
# check_box.setDown(True)
#
# push_button.setStyleSheet("QPushButton:press {background-color:green}")
#
# def cao():
#     push_button.setChecked(not push_button.isChecked())
#****状态******


#*****排他性********
# for i in range(0,3):
#
#     btn = QRadioButton(window)
#     # btn = QCheckBox(window)
#
#     btn.setText("btn"+str(i))
#     btn.move(50*i,50*i)
#     btn.setAutoExclusive(True)
#     print(btn.autoExclusive())
#     print(btn.isCheckable())
#     btn.setCheckable(True)
#
# btn = QPushButton(window)
# btn.move(200,200)
# btn.setText("hi")
# btn.setCheckable(True)
# btn.setAutoExclusive(False)


#*****排他性********



#*******按钮模拟点击
# btn = QPushButton(window)
# btn.setText("这是按钮")
# btn.move(200,200)
# btn.pressed.connect(lambda :print("点击按钮"))
# #方法1
# btn.click()
# #方法2
# # btn.animateClick(2000)
#
# btn2 = QPushButton(window)
# btn2.setText("按钮2")
# def test():
#     btn.click()
# btn2.pressed.connect(test)

#*******按钮模拟点击



#*******有效区域
class Btn(QPushButton):
    def hitButton(self, point):
        yuanxin_x =  self.width()/2
        yuanxin_y = self.height()/2

        hit_x = point.x()
        hit_y = point.y()

        r = self.width()/2

        distance = math.sqrt(math.pow(hit_x - yuanxin_x,2) + math.pow(hit_y-yuanxin_y,2))
        if (distance <= r):
            return True
        else:
            return False


    def paintevent(self,QPaintEvent):
        painter = QPainter(self)
        painter.setPen(QPen(QColor(100,150,200),6))
        painter.drawEllipse(self.rect())





btn = Btn(window)
btn.move(200,200)
btn.setText("点击")
btn.pressed.connect(lambda :print("按钮被点击了"))
#*******有效区域
window.show()
sys.exit(app.exec_())