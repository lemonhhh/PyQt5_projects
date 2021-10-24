from PyQt5.Qt import *

from resource.register import Ui_Form



class RegisterPane(QWidget,Ui_Form):

    exit_signal = pyqtSignal()
    #两个参数，账号和密码
    register_account_pwd_signal = pyqtSignal(str,str)

    def __init__(self,parent=None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs) #调用父类的方法

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
        self.exit_signal.emit()

    def guanyu_fun(self):
        QMessageBox.about(self,"百度","https://www.baidu.com")

    def chongzhi_fun(self):
        print("重置")
        self.account_le.clear()
        self.passward_le.clear()
        self.confirm_pwd_le.clear()

    def check_register(self):
        account_txt = self.account_le.text()
        passward_txt = self.passward_le.text()
        #发出信号
        self.register_account_pwd_signal.emit(account_txt,passward_txt)

    def enable_register_btn(self):
        account_txt = self.account_le.text()
        passward_txt = self.passward_le.text()
        cp_txt = self.confirm_pwd_le.text()

        if len(account_txt) > 0 and len(passward_txt)>0 and len(cp_txt)>0  and passward_txt == cp_txt:

            self.register_button.setEnabled(True)
        else:
            self.register_button.setEnabled(False)



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = RegisterPane()
    window.exit_signal.connect(lambda :print("退出了"))
    window.register_account_pwd_signal.connect(lambda a,p:print(a,p))
    window.show()
    sys.exit(app.exec_())

