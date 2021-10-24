from PyQt5.Qt import *

from resource.login import Ui_Form

#艹函数是写在此文件中的
#只做界面相关的东西

class LoginPane(QWidget,Ui_Form):

    #自定义的信号
    show_register_pane_singal = pyqtSignal()
    check_login_single = pyqtSignal(str,str)
    #判定工作交给外部

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        #如果没有这一行的话，就不会显示背景图片了
        self.setAttribute(Qt.WA_StyledBackground,True)
        self.setupUi(self)

        #用来加载gif
        movie = QMovie(":/login/images/e.gif")
        movie.setScaledSize(QSize(160,160))

        self.login_top_bg_label.setMovie(movie)
        movie.start()

    def show_register_pane(self):
        # print("ooo ")
        #发射信号
        self.show_register_pane_singal.emit()


    #实现槽！
    def open_qq_link(self):
        link = "https://qm.qq.com/cgi-bin/qm/qr?k=jhz-EmOshuee1GTbcFXZJKCY50v44ipz&jump_from=webapi"
        QDesktopServices.openUrl(QUrl(link))

    def enable_login_btn(self):
        account = self.account_cb.currentText()
        pwd = self.pwd_le.text()
        if(len(account) > 0 and len(pwd) > 0):
            self.login_btn.setEnabled(True)
        else:
            self.login_btn.setEnabled(False)

    def check_loign(self):
        account = self.account_cb.currentText()
        pwd = self.pwd_le.text()
        self.check_login_single.emit(account,pwd)

    def auto_login(self,checked):
        # print(checked)
        if checked:
            self.remember_pwd_cb.setChecked(True)

    def remember_pwd(self,checked):
        if not checked:
            self.auto_login_cb.setChecked(False)
        # print(checked)

    def show_error_animation(self):
        #左右抖动的效果
        animation = QPropertyAnimation(self)
        animation.setTargetObject(self.login_bottom)
        animation.setPropertyName(b"pos")
        animation.setKeyValueAt(0,self.login_bottom.pos())
        animation.setKeyValueAt(0.2,self.login_bottom.pos() + QPoint(15,0))
        animation.setKeyValueAt(0.5,self.login_bottom.pos())
        animation.setKeyValueAt(0.7,self.login_bottom.pos() + QPoint(-15,0))
        animation.setKeyValueAt(1,self.login_bottom.pos())
        animation.setDuration(200)
        animation.setLoopCount(3)
        animation.start(QAbstractAnimation.DeleteWhenStopped)




if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = LoginPane()
    window.show()
    sys.exit(app.exec_())

