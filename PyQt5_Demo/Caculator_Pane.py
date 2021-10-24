from PyQt5.Qt import *

from resource.caculator import Ui_Form

#艹函数是写在此文件中的
#只做界面相关的东西

class CaculatorPane(QWidget,Ui_Form):

    #自定义的信号
    show_register_pane_singal = pyqtSignal()
    check_login_single = pyqtSignal(str,str)
    #判定工作交给外部

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        #如果没有这一行的话，就不会显示背景图片了
        self.setAttribute(Qt.WA_StyledBackground,True)
        self.setupUi(self)


    #实现slot
    def get_key(self,title,role):
        print(title,role)




if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = CaculatorPane()
    window.show()
    sys.exit(app.exec_())

