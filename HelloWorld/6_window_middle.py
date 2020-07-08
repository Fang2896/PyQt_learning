
import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):               

        self.resize(250, 150)
        # 调用下面那个函数，居中
        self.center()

        self.setWindowTitle('Center')    
        self.show()


    def center(self):
        # 获得主窗口所在的框架
        qr = self.frameGeometry()
        # QtGui.QDesktopWidget提供了用户的桌面信息，包括屏幕的大小。
        # 获取显示器的分辨率，得到屏幕中间点的位置
        cp = QDesktopWidget().availableGeometry().center()
        # 移动到中心
        qr.moveCenter(cp)
        # 通过move函数把主窗口的左上角移动到其框架的左上角，这样就把窗口居中了。
        self.move(qr.topLeft())


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())