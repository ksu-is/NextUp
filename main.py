
import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QHBoxLayout, QVBoxLayout, QLabel, QPushButton
)

# Start the application
app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("NextUp")
window.resize(1100, 700)

# Create the main layout
central_widget = QWidget()
window.setCentralWidget(central_widget)

main_layout = QHBoxLayout(central_widget)
main_layout.setContentsMargins(0, 0, 0, 0)
main_layout.setSpacing(0)

# Create the sidebar
sidebar = QWidget()
sidebar.setFixedWidth(220)
sidebar.setObjectName("sidebar")

sidebar_layout = QVBoxLayout(sidebar)
sidebar_layout.setContentsMargins(15, 20, 15, 20)
sidebar_layout.setSpacing(10)

# NextUp logo and subtitle
logo = QLabel("NextUp")
logo.setObjectName("logo")

subtitle = QLabel("BACKLOG TRACKER")
subtitle.setObjectName("subtitle")

sidebar_layout.addWidget(logo)
sidebar_layout.addWidget(subtitle)
sidebar_layout.addSpacing(20)

# Create the main content area
content = QWidget()
content_layout = QVBoxLayout(content)
content_layout.setContentsMargins(30, 30, 30, 30)

page_title = QLabel("My Library")
page_title.setObjectName("pageTitle")

page_description = QLabel("Your video game collection")
page_description.setObjectName("subtitle")

content_layout.addWidget(page_title)
content_layout.addWidget(page_description)
content_layout.addStretch()

# Change the current page
def change_page(page):
    page_title.setText(page)

# Create navigation buttons
pages = [
    "My Library",
    "Not Started",
    "Playing",
    "Completed",
    "Dropped"
]

for page in pages:
    button = QPushButton(page)
    button.clicked.connect(
        lambda checked, name=page: change_page(name)
    )
    sidebar_layout.addWidget(button)

# Push the Play Next button to the bottom
sidebar_layout.addStretch()

play_next = QPushButton("Play Next")
play_next.setObjectName("playNext")
play_next.clicked.connect(
    lambda: change_page("Play Next")
)

sidebar_layout.addWidget(play_next)

# Combine the sidebar and content area
main_layout.addWidget(sidebar)
main_layout.addWidget(content)

# Style the application
window.setStyleSheet("""
    QWidget {
        background-color: #15171e;
        color: #f0f1f5;
        font-family: Segoe UI;
        font-size: 14px;
    }

    QWidget#sidebar {
        background-color: #20232d;
    }

    QLabel {
        background-color: transparent;
    }

    QLabel#logo {
        color: #a6a2ff;
        font-size: 32px;
        font-weight: bold;
    }

    QLabel#subtitle {
        color: #9ca3af;
        font-size: 12px;
    }

    QLabel#pageTitle {
        font-size: 28px;
        font-weight: bold;
    }

    QPushButton {
        background-color: transparent;
        color: #b4b8c6;
        border: none;
        border-radius: 6px;
        padding: 12px;
        text-align: left;
    }

    QPushButton:hover {
        background-color: #37354f;
        color: #ffffff;
    }

    QPushButton#playNext {
        background-color: #7771dc;
        color: white;
        font-weight: bold;
        text-align: center;
    }

    QPushButton#playNext:hover {
        background-color: #8983ed;
    }
""")

# Display the application
window.show()

sys.exit(app.exec_())