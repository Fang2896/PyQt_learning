
import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon

# 我们创建了只有一个命令的菜单栏
# 这个命令就是终止应用。
# 同时也创建了一个状态栏。而且还能使用快捷键Ctrl+Q退出应用。
class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):               

        # QAction是菜单栏，工具栏或者快捷键的动作的组合。
        exitAct = QAction(QIcon('demo copy.jpg'), '&Exit', self)        
        exitAct.setShortcut('Ctrl+Q')
        # 创建了一个状态栏。鼠标悬停在菜单栏的时候，能够显示当前状态
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)

        self.statusBar()

        # 创建菜单栏。并在上面添加一个file菜单。并关联了点击退出应用的事件
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Simple menu')    
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())