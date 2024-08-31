# ------------------------------- івафіваіф
from PyQt5.QtCore import Qt      
from PyQt5.QtWidgets import *  
# ------------------------------- 


app = QApplication([])

# ------------------------------- 
menu_win = QWidget()
menu_win.resize(400, 300)            
menu_win.setWindowTitle("Меню")
# ------------------------------- 

# Лінії для вводу нового запитання
txt_Question = QLineEdit('')
txt_Answer = QLineEdit('')
txt_Wrong1 = QLineEdit('')
txt_Wrong2 = QLineEdit('')
txt_Wrong3 = QLineEdit('')

# обєднання ліній та тексту
layout_form = QFormLayout()

layout_form.addRow('Питання:', txt_Question)
layout_form.addRow('Правильна відповідь:', txt_Answer)
layout_form.addRow('Правильна відповідь №1:', txt_Wrong1)
layout_form.addRow('Правильна відповідь №2', txt_Wrong2)
layout_form.addRow('Правильна відповідь №3:', txt_Wrong3)

# кнопки 
btn_back = QPushButton('Назад')
btn_add_q = QPushButton('Додати питання')
btn_clear = QPushButton('Очистити')

# Статистика
lbl_statistics = QLabel('Статистика:\nПравильних відповідей: 0\nЗагальна кількість спроб: 0') 

# гориз.лінія - макет
hbtn = QHBoxLayout()         
hbtn.addWidget(btn_back)
hbtn.addWidget(btn_add_q)
hbtn.addWidget(btn_clear)

# Макет для основного вікна
vline = QVBoxLayout()
vline.addLayout(layout_form)
vline.addLayout(hbtn)
vline.addWidget(lbl_statistics) 

menu_win.setLayout(vline) # макет на вікно



