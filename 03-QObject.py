from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()  # 调用父类的方法
        self.setWindowTitle("QObject")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        self.QObject_type_judge()

    def QObject_structure_test(self):
        mros = QObject.mro()
        for mro in mros:
            print(mro)

    def QObject_name_object(self):
        # 测试API
        # obj = QObject()
        # obj.setObjectName("notice")
        # print(obj.objectName())
        #
        # obj.setProperty("notice_level1","error")
        # obj.setProperty("notice_level2","warning")
        # print(obj.property("notice_level1"))
        #
        # print(obj.dynamicPropertyNames())

        # 案例
        with open("QObject.qss", "r") as f:
            qApp.setStyleSheet(f.read())

        label1 = QLabel(self)
        label1.setText("喵喵")

        label2 = QLabel(self)
        label2.setText("汪汪")
        label2.move(100, 100)

    def QObject_father_son(self):
        # 测试API
        # obj0 = QObject()
        # obj1 = QObject()
        # obj2 = QObject()
        # obj3 = QObject()
        # obj4 = QObject()
        # obj5 = QObject()
        #
        # label = QLabel()
        #
        # print("obj0",obj0)
        # print("obj1",obj1)
        # print("obj2",obj2)
        # print("obj3",obj3)
        # print("obj4",obj4)
        # print("obj5",obj5)
        #
        # obj1.setParent(obj0)
        # obj2.setParent(obj0)
        # obj3.setParent(obj1)
        # obj4.setParent(obj2)
        # obj5.setParent(obj2)
        #
        # label.setParent(obj0)
        #
        # # print(obj4.parent())
        # # print(obj0.children())
        #
        # print(obj0.findChild(QLabel))

        obj1 = QObject()
        self.obj1 = obj1
        obj2 = QObject()

        obj2.setParent(obj2)

        obj2.destroyed.connect(lambda: print("obj2被释放了"))
        del self.obj1

    def QObject_signal_operation(self):
        self.obj = QObject()
        # obj.destroyed()
        # obj.objectNameChanged()

        def destroy_cao(obj):
            print("对象被释放了", obj)

        def obj_name_cao(name):
            print("对象名称发生了改变", name)

        self.obj.destroyed.connect(destroy_cao)
        self.obj.objectNameChanged.connect(obj_name_cao)
        self.obj.setObjectName("xxx")
        self.obj.objectNameChanged.disconnect()
        self.obj.setObjectName("ooo")
        self.obj.objectNameChanged.connect(obj_name_cao)
        self.obj.setObjectName("xxxooo")
        del self.obj

    def QObject_type_judge(self):
        # obj = QObject()
        # w = QWidget()
        # btn = QPushButton()
        # label = QLabel()
        #
        # objs = [obj,w,btn,label]
        # for o in objs:
        #     print(o.isWidgetType())

        # 案例
        label1 = QLabel(self)
        label1.setText("喵喵")
        label1.move(100, 100)
        label2 = QLabel(self)
        label2.setText("汪汪")
        label2.move(150, 150)

        btn = QPushButton(self)
        btn.setText("点我")
        btn.move(200, 200)

        # for widget in self.findChildren(QLabel):
        #     print(widget)
        for widget in self.children():
            if widget.inherits("QLabel"):
                widget.setStyleSheet("background-color:cyan;")

    def QObject_del(self):
        obj1 = QObject()
        self.obj = obj1
        obj2 = QObject()
        obj3 = QObject()
        obj3.setParent(obj2)
        obj2.setParent(obj1)

        obj1.destroyed.connect(lambda :print("obj1被释放了"))
        obj2.destroyed.connect(lambda :print("obj2被释放了"))
        obj3.destroyed.connect(lambda :print("obj3被释放了"))

        obj2.deleteLater()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
