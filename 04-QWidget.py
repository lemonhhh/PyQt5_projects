from PyQt5.Qt import *
import sys




app = QApplication(sys.argv)




window = QWidget()
window.move(200,200)
window.resize(500,500)

label = QLabel(window)
label.setText("嘿呀嘿呀")
label.move(100,100)
label.setStyleSheet("background-color:cyan;")

def changeCao():
    new_content = label.text() + "巴扎黑"
    label.setText(new_content)
    # label.resize(label.width()+100,label.height())
    label.adjustSize()

btn = QPushButton(window)
btn.setText("增加内容")
btn.move(100,300)
btn.clicked.connect(changeCao)


window.show()

sys.exit(app.exec_())

