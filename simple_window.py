from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

def janela():
    window = QWidget()
    layout = QVBoxLayout()
    layout.addWidget(QPushButton('Top'))
    layout.addWidget(QPushButton('Bottom'))
    window.setLayout(layout)
    return window


app = QApplication([])
window = janela()
window.show()
app.exec_()
