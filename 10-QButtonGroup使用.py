from PyQt5.Qt import *
import sys


app = QApplication(sys.argv)


window = QWidget()

window.setWindowTitle("按钮组的使用")
window.resize(500,500)

#创建4个单选按钮
#男女
r_male = QRadioButton("男",window)
r_male.move(100,100)
r_female = QRadioButton("女",window)
r_female.move(100,120)
sex_group = QButtonGroup(window)

r_male.setChecked(True)
sex_group.addButton(r_male,1)
sex_group.addButton(r_female,2)
sex_group.setExclusive(True)

#是否

r_yes = QRadioButton("是",window)
r_yes.move(200,100)
r_no = QRadioButton("否",window)
r_no.move(200,120)
answer_group = QButtonGroup(window)
answer_group.addButton(r_yes)
answer_group.addButton(r_no)
answer_group.setId(r_yes,1)
answer_group.setId(r_no,2)

def test(val):
    print(sex_group.id(val))
sex_group.buttonClicked.connect(test)

window.show()
sys.exit(app.exec_())