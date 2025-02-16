from PyQt5.QtWidgets import*

import sys
from PyQt5.QtWidgets import*
from googletrans import Translator



app = QApplication(sys.argv)
window = QWidget()
translator = Translator()


text_to_translate = "Hello, how are you?"

langs = {
   "Англійська": "en",
   "Українська": "uk",
   "Японська": "ja",
   "Азейбарджанська": "az",
   "Казахстанська": "kk",
   "Німецька": "de",
   "Французька": "fr",
   "Польська": "pl",
   "Китайська": "zh-tw",
}

input_text = QTextEdit()
autput_edit = QTextEdit()
button = QPushButton("-> <-")
button2 = QPushButton("Перекласти")

combo = QComboBox()
combo.addItem('Англійська')
combo.addItem('Японська')
combo.addItem('Азейбарджанська')
combo.addItem('Казахстанська')
combo.addItem('Німецька')
combo.addItem('Французька')
combo.addItem('Польська')
combo.addItem('Китайська')




combo2 = QComboBox()
combo2.addItem("Українська")
combo2.addItem('Японська')
combo2.addItem('Азейбарджанська')
combo2.addItem('Казахстанська')
combo2.addItem('Німецька')
combo2.addItem('Французька')
combo2.addItem('Польська')
combo2.addItem('Китайська')



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

def print_text():
   a = input_text.toPlainText()
   translated_text = translator.translate(a, src=langs[combo.currentText()], dest=langs[combo2.currentText()])
   print(f"Original Text: {text_to_translate}")
   print(f"Translated Text: {translated_text.text}")
   autput_edit.setText(translated_text.text)
button.clicked.connect(print_text)

window.setLayout(main_line)
window.show()
sys.exit(app.exec_())