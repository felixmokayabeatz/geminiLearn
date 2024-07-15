import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QTextEdit
from PyQt5.QtCore import Qt
import google.generativeai as genai
import os
from dotenv import load_dotenv

class ChatApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setup_genai()

    def initUI(self):
        self.setWindowTitle('ChatBot App')
        self.setGeometry(100, 100, 600, 400)

        # Layouts
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Text display area
        self.text_display = QTextEdit()
        self.text_display.setReadOnly(True)
        layout.addWidget(self.text_display)

        # Input area
        input_layout = QHBoxLayout()
        layout.addLayout(input_layout)

        self.input_field = QLineEdit()
        input_layout.addWidget(self.input_field)

        send_button = QPushButton('Send')
        send_button.clicked.connect(self.send_message)
        input_layout.addWidget(send_button)

    def setup_genai(self):
        dotenv_path = 'G:/geminiLearn/geminiLearn/API_KEY_GEMINI/.env'
        load_dotenv(dotenv_path)
        API_KEY = os.getenv('API_KEY_GEMINI')

        if API_KEY is None:
            print("No API_KEY Found!")
            return

        genai.configure(api_key=API_KEY)
        self.model = genai.GenerativeModel('gemini-pro')

    def send_message(self):
        message = self.input_field.text().strip()
        if message:
            response = self.model.generate_content(message)
            self.display_message(f"You: {message}")
            self.display_message(f"ChatBot: {response.text}")
        self.input_field.clear()

    def display_message(self, message):
        self.text_display.append(message)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    chat_app = ChatApp()
    chat_app.show()
    sys.exit(app.exec_())
