import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout, QLabel
import os

class MouseLauncher(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gesture Mouse Launcher")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()
        self.label = QLabel("Click the button to run Gesture Mouse")
        layout.addWidget(self.label)

      
        self.start_button = QPushButton("Run Gesture Mouse")
        self.start_button.clicked.connect(self.run_gesture_mouse)
        layout.addWidget(self.start_button)

    
        self.stop_button = QPushButton("Stop Gesture Mouse")
        self.stop_button.clicked.connect(self.stop_gesture_mouse)
        layout.addWidget(self.stop_button)

        self.setLayout(layout)
 
        self.process = None

    def run_gesture_mouse(self):
        if self.process is None:
            base_dir = os.path.dirname(os.path.abspath(__file__))
            python_executable = os.path.join(base_dir, "../venv/Scripts/python.exe")
            ai_virtual_mouse_script = os.path.join(base_dir, "../core/AI_virtual_Mouse.py")

            self.process = subprocess.Popen([python_executable, ai_virtual_mouse_script])
            self.label.setText("Gesture Mouse is running!")
        else:
            self.label.setText("Gesture Mouse is already running!")

    def stop_gesture_mouse(self):
        if self.process is not None:
           
            self.process.terminate()
            self.process = None
            self.label.setText("Gesture Mouse stopped.")
        else:
            self.label.setText("Gesture Mouse is not running.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MouseLauncher()
    window.show()
    sys.exit(app.exec_())