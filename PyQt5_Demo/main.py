#导入类
from Login_Pane import LoginPane
from Register_Pane import RegisterPane
from Caculator_Pane import CaculatorPane
from PyQt5.Qt import *


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    login_pane = LoginPane()
    register_pane = RegisterPane(login_pane)
    register_pane.move(0, login_pane.height())
    register_pane.show()

    #全局变量
    caculator_pane = CaculatorPane()  # 没有父控件，顶层窗口

    def exit_register_pane():
        animation = QPropertyAnimation(register_pane)
        animation.setTargetObject(register_pane)
        animation.setPropertyName(b"pos")
        animation.setStartValue(QPoint(0, 0))
        animation.setEndValue(QPoint(login_pane.width(),0))
        animation.setDuration(200)
        animation.setEasingCurve(QEasingCurve.InBounce)
        animation.start(QAbstractAnimation.DeleteWhenStopped)  # 运行



    def show_register_pane():
        #设置动画
        animation = QPropertyAnimation(register_pane)
        animation.setTargetObject(register_pane)
        animation.setPropertyName(b"pos")
        animation.setStartValue(QPoint(0,login_pane.height()))
        animation.setEndValue(QPoint(0,0))
        animation.setDuration(200)
        animation.setEasingCurve(QEasingCurve.OutBounce)
        animation.start(QAbstractAnimation.DeleteWhenStopped) #运行


    def check_login(account,pwd):
        if (account == "1125408974" and pwd == "like"):
            print("登陆成功")

            caculator_pane.show()
            login_pane.hide() #隐藏

        else:
            login_pane.show_error_animation()


    #登陆界面
    login_pane.show_register_pane_singal.connect(show_register_pane)
    login_pane.check_login_single.connect(check_login)


    #注册界面发出的信号，
    register_pane.exit_signal.connect(exit_register_pane)
    register_pane.register_account_pwd_signal.connect(lambda account,pwd:print(account,pwd))

    login_pane.show()
    sys.exit(app.exec_())


