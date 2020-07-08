import sys
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):               
        
        # 创建一个文本编辑区域。并把它放到QMainWindow的中间区域
        # 这个组件或占满所有剩余的区域。
        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)

        # 创建一个行为。绑定icon，exit标签。和一个退出快捷键
        exitAct = QAction(QIcon('demo copy.py'), 'Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        # 这个行为和QMainWindow的quit行为绑定
        exitAct.triggered.connect(self.close)

        self.statusBar()

        # 创建一个名字叫File的menuBar.
        # 菜单下有一个行为exitAct，用addAction绑定
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)

        # 创建一个工具栏。Exit。行为和exitAct绑定
        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAct)

        # 主窗口设置
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Main window')    
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())