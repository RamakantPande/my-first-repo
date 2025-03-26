import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QSizePolicy, QToolBar, QAction, QLineEdit, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView

class WebBrowser(QMainWindow):
    def __init__(self):
        super().__init__()

        # Initialize the browser window
        self.browser = QWebEngineView()
        self.browser.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.browser.setSizeIncrement(1, 1)
        self.browser.setUrl(QUrl('https://www.google.com'))

        # Create a navigation toolbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        # Add navigation actions
        back_btn = QAction('Back', self)
        back_btn.setStatusTip('Back to previous page')
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction('Forward', self)
        forward_btn.setStatusTip('Forward to the next page')
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction('Reload', self)
        reload_btn.setStatusTip('Reload page')
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        home_btn = QAction('Home', self)
        home_btn.setStatusTip('Go home')
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        # Add a URL bar
        self.urlbar = QLineEdit()
        self.urlbar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.urlbar)

        stop_btn = QAction('Stop', self)
        stop_btn.setStatusTip('Stop loading current page')
        stop_btn.triggered.connect(self.browser.stop)
        navbar.addAction(stop_btn)

        # Create a central widget to contain the browser
        container = QWidget()
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.browser)
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Set main window properties
        self.setWindowTitle("Web Browser")
        self.setGeometry(100, 100, 1024, 768)

    def navigate_home(self):
        self.browser.setUrl(QUrl('https://www.google.com'))

    def navigate_to_url(self):
        q = self.urlbar.text()
        if not q.startswith('http://') and not q.startswith('https://'):
            q = 'http://' + q
        url = QUrl(q)
        self.browser.setUrl(url)

app = QApplication(sys.argv)
QApplication.setApplicationName("Web Browser")
window = WebBrowser()
window.show()
app.exec_()
