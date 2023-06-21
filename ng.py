import random
from source.db import *
from source.db import female_names
from ui.nickgen_ui import Ui_Form
from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QApplication

Form, Window = uic.loadUiType('C:/dev/projects/nickgenerator/ui/nickgen.ui')

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()

def nick(name, fam): # generate nickname's by S-Mamashin and BH Community 
    gen_f_name = random.SystemRandom().choice(name)
    gen_l_name = random.SystemRandom().choice(fam)

    s_nick =  gen_f_name + (' ' if form.checkBox.isChecked() == True else '_') + gen_l_name 

    exhaust = str( f"{s_nick}" )
    nick = form.lineEdit.setText( exhaust )
    gen = ( f"Последний сгенерированный ник: {s_nick}" )
    r_gen = form.label.setText( gen )

    return nick

form.pushButton.clicked.connect(lambda: nick(names_list, last_names) ) # male
form.pushButton_3.clicked.connect(lambda: nick(female_names, last_names) ) # female

app.exec()

