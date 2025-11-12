import sys
import os
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QFrame
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIcon

class MouseLauncher(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gesture Mouse Launcher")
        self.setGeometry(600, 300, 400, 300)
        self.setWindowIcon(QIcon("mouse_icon.png"))
        self.process = None

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        title = QLabel("🖱️ Gesture Mouse Controller")
        title.setFont(QFont("Segoe UI", 16, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        layout.addWidget(line)

        self.label = QLabel("Click below to start Gesture Mouse.")
        self.label.setFont(QFont("Segoe UI", 11))
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        self.start_gesture = QPushButton("▶ Run Gesture Mouse")
        self.stop_button = QPushButton("⏹ Stop Gesture Mouse")
        self.start_normal = QPushButton("▶ Run Normal Mode")

        self.start_gesture.clicked.connect(self.run_gesture_mouse)
        self.start_normal.clicked.connect(self.run_normal_mode)
        self.stop_button.clicked.connect(self.stop_gesture_mouse)

        layout.addWidget(self.start_gesture)
        layout.addWidget(self.start_normal)
        layout.addWidget(self.stop_button)

        self.setLayout(layout)
        self.apply_styles()

    def apply_styles(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #1e1e2f;
                color: #f2f2f2;
            }
            QLabel {
                color: #e0e0e0;
            }
            QPushButton {
                background-color: #2d89ef;
                color: white;
                border-radius: 8px;
                padding: 10px;
                font-size: 13px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #1e65c2;
            }
            QPushButton:pressed {
                background-color: #164c91;
            }
        """)

    def run_gesture_mouse(self):
        if self.process is None:
            base_dir = os.path.dirname(os.path.abspath(__file__))
            python_executable = os.path.join(base_dir, "../venv/Scripts/python.exe")
            ai_mouse_script = os.path.join(base_dir, "../core/AI_virtual_Mouse.py")

            if not os.path.exists(python_executable):
                self.label.setText("❌ Python executable not found!")
                return
            if not os.path.exists(ai_mouse_script):
                self.label.setText("❌ AI_virtual_Mouse.py not found!")
                return

            self.process = subprocess.Popen([python_executable, ai_mouse_script])
            self.label.setText("✅ Gesture Mouse is running!")
        else:
            self.label.setText("⚙️ Gesture Mouse is already running!")

    def run_normal_mode(self):
        if self.process is None:
            base_dir = os.path.dirname(os.path.abspath(__file__))
            python_executable = os.path.join(base_dir, "../venv/Scripts/python.exe")
            normal_script = os.path.join(base_dir, "../core/normal_mode.py")

            if not os.path.exists(python_executable):
                self.label.setText("❌ Python executable not found!")
                return
            if not os.path.exists(normal_script):
                self.label.setText("❌ normal_mode.py not found!")
                return

            self.process = subprocess.Popen([python_executable, normal_script])
            self.label.setText("✅ Normal Mode is running!")
        else:
            self.label.setText("⚙️ A mode is already running!")

    def stop_gesture_mouse(self):
        if self.process is not None:
            self.process.terminate()
            self.process = None
            self.label.setText("🛑 Process stopped.")
        else:
            self.label.setText("⚠️ No process is currently running.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MouseLauncher()
    window.show()
    sys.exit(app.exec_())
