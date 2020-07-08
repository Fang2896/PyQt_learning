import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, 
    QPushButton, QApplication)
from PyQt5.QtGui import QFont    


class Example(QWidget):

    def __init__(self):
        super().__init__()
        # 从QWidget那里继承而来的initUI方法。创建一个GUI
        self.initUI()


    def initUI(self):
        # 设置提示框的字体
        QToolTip.setFont(QFont('SansSerif', 10))
        # 调用setTooltip()创建提示框可以使用富文本格式的内容。
        self.setToolTip('This is a <b>QWidget</b> widget')
        # 创建一个按钮，并且为按钮添加了一个提示框
        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        # 调整按钮大小，并让按钮在屏幕上显示出来，sizeHint()方法提供了一个默认的按钮大小。
        btn.resize(btn.sizeHint())
        btn.move(50, 50)       

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')    
        self.show()


if __name__ == '__main__':
    # 创建一个应用对象
    app = QApplication(sys.argv)
    # 调用Example里的所有方法 ?
    ex = Example()
    # 进入主循环。exit退出
    sys.exit(app.exec_())