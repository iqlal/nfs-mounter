import subprocess
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

class NFSMountApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('NFS Mounter')
        self.setGeometry(300, 300, 400, 200)

        layout = QVBoxLayout()

        self.server_label = QLabel('NFS Server:')
        self.server_input = QLineEdit(self)
        self.server_input.setPlaceholderText('Enter NFS Server IP or Hostname')

        self.mount_point_label = QLabel('Mount Point:')
        self.mount_point_input = QLineEdit(self)
        self.mount_point_input.setPlaceholderText('Enter Local Mount Point')

        self.mount_button = QPushButton('Mount', self)
        self.mount_button.clicked.connect(self.mount)

        layout.addWidget(self.server_label)
        layout.addWidget(self.server_input)
        layout.addWidget(self.mount_point_label)
        layout.addWidget(self.mount_point_input)
        layout.addWidget(self.mount_button)

        self.setLayout(layout)

    def mount(self):
        server = self.server_input.text().strip()
        mount_point = self.mount_point_input.text().strip()

        if not server or not mount_point:
            QMessageBox.warning(self, 'Input Error', 'Please enter both NFS Server and Mount Point.')
            return

        command = f'sudo mount -t nfs {server}:/path/to/share {mount_point}'

        try:
            subprocess.run(command, shell=True, check=True)
            QMessageBox.information(self, 'Success', 'Mounting successful!')
        except subprocess.CalledProcessError as e:
            QMessageBox.critical(self, 'Error', f'Mounting failed. {e}')
