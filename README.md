# **Hand Gesture Controlled Virtual Mouse**

This project implements a **gesture-controlled virtual mouse** using computer vision and hand tracking. It allows users to control the mouse pointer, perform clicks, drag-and-drop, and other actions using hand gestures detected via a webcam.

---

## **Features**
- **Mouse Movement**: Move the mouse pointer by moving your hand.
- **Click Actions**: Perform left-click, right-click, and double-click using specific hand gestures.
- **Drag-and-Drop**: Drag and drop files or objects by holding gestures.
- **Gesture Recognition**: Detects hand gestures in real-time using the webcam.
- **GUI Launcher**: A PyQt5-based graphical interface to start and stop the gesture-controlled mouse.

---

## **Technologies Used**
- **Python**: Core programming language.
- **OpenCV**: For real-time video processing and capturing webcam input.
- **MediaPipe**: For hand tracking and gesture recognition.
- **PyQt5**: For creating the graphical user interface (GUI).
- **AutoPy**: For controlling the mouse programmatically.
- **NumPy**: For numerical operations and smooth mouse movement.

---

## **Project Structure**
```
HandGesturesProject/
├── frontend/
│   ├── launcher.py          # GUI launcher for the application
│   ├── assets/              # (Optional) Static files like icons or images
├── core/
│   ├── AI_virtual_Mouse.py  # Main script for gesture-based mouse control
│   ├── HandTrackingModule.py # Hand tracking utility module
├── tests/
│   ├── test_hand_tracking.py # Unit tests for HandTrackingModule
│   ├── test_mouse_control.py # Unit tests for AI_virtual_Mouse
├── venv/                    # Virtual environment (ignored in .gitignore)
├── requirements.txt         # List of dependencies
├── .gitignore               # Git ignore file
├── README.md                # Project documentation

```

---

## **Setup Instructions**

### **1. Clone the Repository**
```bash
git clone <repository-url>
cd HandGesturesProject
```

### **2. Create and Activate a Virtual Environment**
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Run the Application**
To launch the GUI:
```bash
python frontend/launcher.py
```

---

## **How It Works**
1. **Hand Tracking**:
   - The webcam captures video frames.
   - MediaPipe detects the hand landmarks in real-time.
2. **Gesture Recognition**:
   - Specific gestures (e.g., index finger up, thumb down) are mapped to mouse actions.
3. **Mouse Control**:
   - The detected gestures are translated into mouse movements and actions using `autopy` and `pyautogui`.

---

## **Hand Gestures**
| **Gesture**                  | **Action**                |
|------------------------------|---------------------------|
| Index finger up              | Move the mouse pointer    |
| Thumb and index finger touch | Left-click               |
| All fingers down             | Drag-and-drop            |
| All fingers up               | Release drag             |
| Index and middle finger up   | Double-click             |

---

## **Testing**
Unit tests are included in the [`tests`](tests ) directory. To run the tests:
```bash
python -m unittest discover tests
```

---

## **Future Improvements**
- Add support for right-click gestures.
- Improve gesture recognition accuracy.
- Add support for multi-hand gestures.
- Optimize performance for low-end systems.

---

## **License**
This project is licensed under the MIT License.

---

## **Contributing**
Contributions are welcome! If you'd like to contribute, please fork the repository and submit a pull request.

---

## **Acknowledgments**
- [MediaPipe](https://mediapipe.dev/) for hand tracking.
- [OpenCV](https://opencv.org/) for video processing.
- [PyQt5](https://riverbankcomputing.com/software/pyqt/intro) for the GUI framework.

---

## **Contact**
For any questions or feedback, feel free to reach out:
- **Name**: Chinthaka
- **Email**: [your-email@example.com]
