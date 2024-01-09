import sys
from PyQt5.QtWidgets import QApplication
from nfs_mount_ui import NFSMountApp

if __name__ == '__main__':
    app = QApplication(sys.argv)
    nfs_mount_app = NFSMountApp()
    nfs_mount_app.show()
    sys.exit(app.exec_())
