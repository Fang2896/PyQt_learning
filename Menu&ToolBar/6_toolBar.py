
import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon


# 我们创建了一个工具栏。这个工具栏只有一个退出应用的动作。

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):               
        # 使用了一个行为对象。绑定了ICon,和快捷键。和一个标签Exit
        exitAct = QAction(QIcon('demo copy.jpg'), 'Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        # 行为被触发的时候会调用QtGui.QMainWindow的quit方法退出应用
        exitAct.triggered.connect(qApp.quit)

        # 展示工具栏
        self.toolbar = self.addToolBar('Exit')
        # 为工具栏添加行为
        self.toolbar.addAction(exitAct)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Toolbar')    
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())