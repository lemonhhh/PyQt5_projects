from PyQt5.Qt import *

from resource.register import Ui_Form



class Window(QWidget,Ui_Form):
    def __init__(self):
        super().__init__() #调用父类的方法

        #如果没有这一行的话，就不会显示背景图片了
        self.setAttribute(Qt.WA_StyledBackground,True)
        self.setupUi(self)

        #动画目标控件
        self.animation_targets = [self.about_menue_btn,self.reset_menue_btn,self.exit_menue_btn]
        self.animation_targets_pos = [target.pos() for target in self.animation_targets] #循环

    def show_hide_menu(self,checked):
        # print("显示和隐藏",checked)

        #创建动画组
        animation_group = QSequentialAnimationGroup(self)

        for idx,target in enumerate(self.animation_targets):

            animation = QPropertyAnimation()

            #目标对象
            animation.setTargetObject(target)
            animation.setPropertyName(b"pos")

            animation.setStartValue(self.main_menu_button.pos())
            #结束的位置
            animation.setEndValue(self.animation_targets_pos[idx])

            animation.setDuration(200)
            animation.setEasingCurve(QEasingCurve.InOutBounce)
            animation_group.addAnimation(animation)

        #控制动画的方向
        if not checked:
            animation_group.setDirection(QAbstractAnimation.Forward)
        else:
            animation_group.setDirection(QAbstractAnimation.Backward)

        animation_group.start(QAbstractAnimation.DeleteWhenStopped)



    def tuichu_fun(self):
        print("退出")

    def guanyu_fun(self):
        QMessageBox.about(self,"百度","https://www.baidu.com")

    def chongzhi_fun(self):
        print("重置")

    def check_register(self):
        print("注册")



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

