
import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QApplication

# 创建了一个行为菜单。这个动作/行为可以切换状态栏显示或者隐藏

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):         

        self.statusbar = self.statusBar()
        self.statusbar.showMessage('Ready')

        menubar = self.menuBar()
        viewMenu = menubar.addMenu('View')

        # 用checkable选项创建了一个能选中的菜单.
        viewStatAct = QAction('View statusbar', self, checkable=True)
        viewStatAct.setStatusTip('View statusbar')
        # 默认为选中状态
        viewStatAct.setChecked(True)
        # 与toggleMenu函数关联
        viewStatAct.triggered.connect(self.toggleMenu)

        viewMenu.addAction(viewStatAct)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Check menu')    
        self.show()
    
    # 根据选中状态切换状态栏的显示与否
    def toggleMenu(self, state):

        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())