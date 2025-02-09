from PyQt5.QtWidgets import*

import sys
from PyQt5.QtWidgets import*


app = QApplication(sys.argv)
window = QWidget()

input_text = QTextEdit()
autput_edit = QTextEdit()
button = QPushButton( "-> <-" )
button2 = QPushButton("Перекласти")

combo = QComboBox()
combo.addItem('Англійська')



combo2 = QComboBox()
combo2.addItem("Українська")

main_line = QHBoxLayout()


v_line = QVBoxLayout()
v_line.addWidget(combo)
v_line.addWidget(input_text)

v_line2 = QVBoxLayout()
v_line2.addWidget(combo2)
v_line2.addWidget(autput_edit)

main_line.addLayout(v_line)
main_line.addWidget(button)
main_line.addLayout(v_line2)
main_line.addWidget(button2)

window.setLayout(main_line)
window.show()
sys.exit(app.exec_())