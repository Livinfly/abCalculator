from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from Resource.UI.abCalcUI import Ui_mainWindow as abCalcUI
import keyboard

# PySide6-uic DemoUI.ui -o DemoUI.py
# from DemoUI import DemoUI

# self.ui.__Action__.triggered.connect(__Function__)
#           Button   clicked
#           ComboBox currentIndexChanged
#           SpinBox  valueChanged
# 自定义函数.属性名.connect

# 此窗口是否活跃
# self.window().isActiveWindow()
# self.window().isMinimized()

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = abCalcUI()
        self.ui.setupUi(self)
        # 启动移到指定位置
        # self.ToPlace()

        self.dict = {
            self.ui.Button0: '0', self.ui.Button1: '1', self.ui.Button2: '2',
            self.ui.Button3: '3', self.ui.Button4: '4', self.ui.Button5: '5',
            self.ui.Button6: '6', self.ui.Button7: '7', self.ui.Button8: '8',
            self.ui.Button9: '9', self.ui.ButtonPoint: '.', self.ui.ButtonPlus: '+',
            self.ui.ButtonSub: '-', self.ui.ButtonMul: '*', self.ui.ButtonDiv: '/',
            self.ui.ButtonEqual: '=', self.ui.ButtonClear: 'C', self.ui.ButtonBackspace: 'B',
        }
        self.course = str('0')
        self.error = False

        ButtonList = self.findChildren(QPushButton)
        for btn in ButtonList:
            btn.clicked.connect(self.Band)
    # def ToPlace(self):
    #     screen = QGuiApplication.primaryScreen().geometry()
    #     size = self.geometry()
    #
    #     Left = (screen.width() - size.width()) / 5
    #     Top = (screen.height() - size.height()) * 3 / 5
    #     self.move(Left, Top)
    def Band(self):
        def DelLeadingZeros(str):
            ok = False
            for i, x in enumerate(str):
                if not ok and x == '0' and (i+1 < len(str) and (str[i+1].isdigit() or str[i+1] not in {'.', '+', '-', '*', '/'})):
                    str = str[:i]+str[i+1:]
                elif x.isdigit():
                    ok = True
                elif x in {'+', '-', '*', '/'}:
                    ok = False
            return str
        def DelMorePoints(str):
            ok = True
            for i, x in enumerate(str):
                if x == '.':
                    if ok:
                        ok = False
                    else:
                        if i+1 < len(str):
                            str = str[:i]+str[i+1:]
                        else:
                            str = str[:i]
                elif x in {'+', '-', '*', '/'}:
                    ok = True
            return str
        val = self.dict[self.sender()]
        if self.error:
            if val == 'C':
                self.course = str('0')
                self.ui.Result.setText('0')
                self.error = False
        elif val == '=':
            if self.course[-1].isdigit():
                try:
                    ans = str(round(eval(self.course), 15))
                except Exception as e:
                    ans = str(e)
                    self.error = True
                self.ui.Result.setText(ans)
                if not self.error:
                    self.course = ans
                else:
                    self.course = 'Click C to reset'
        elif val == 'C':
            self.course = str('0')
            self.ui.Result.setText('0')
        elif val == 'B':
            if len(self.course) > 1:
                self.course = self.course[:-1]
            elif len(self.course) == 1:
                self.course = str('0')
        elif val.isdigit():
            self.course += val
        elif val in {'+', '-', '*', '/'}:
            if self.course[-1].isdigit():
                self.course += val
            elif self.course[-1] in {'+', '-', '*', '/'}:
                self.course = self.course[:-1]+val
        elif val == '.':
            if self.course[-1].isdigit():
                self.course += val
        self.course = DelLeadingZeros(self.course)
        self.course = DelMorePoints(self.course)
        self.ui.Course.setText(self.course[-min(32, len(self.course)):-1]+self.course[-1])

def Actived(func):
    if mainWindow.window().isActiveWindow():
        func()
def KeyboardInput():
    keyboard.add_hotkey('esc', lambda : Actived(app.exit))

    keyboard.add_hotkey('alt', lambda: Actived(mainWindow.ui.Button0.click))
    keyboard.add_hotkey('z', lambda : Actived(mainWindow.ui.Button1.click))
    keyboard.add_hotkey('x', lambda: Actived(mainWindow.ui.Button2.click))
    keyboard.add_hotkey('c', lambda: Actived(mainWindow.ui.Button3.click))
    keyboard.add_hotkey('a', lambda: Actived(mainWindow.ui.Button4.click))
    keyboard.add_hotkey('s', lambda: Actived(mainWindow.ui.Button5.click))
    keyboard.add_hotkey('d', lambda: Actived(mainWindow.ui.Button6.click))
    keyboard.add_hotkey('q', lambda: Actived(mainWindow.ui.Button7.click))
    keyboard.add_hotkey('w', lambda: Actived(mainWindow.ui.Button8.click))
    keyboard.add_hotkey('e', lambda: Actived(mainWindow.ui.Button9.click))
    keyboard.add_hotkey('f', lambda: Actived(mainWindow.ui.ButtonPlus.click))
    keyboard.add_hotkey('g', lambda: Actived(mainWindow.ui.ButtonSub.click))
    keyboard.add_hotkey('r', lambda: Actived(mainWindow.ui.ButtonMul.click))
    keyboard.add_hotkey('t', lambda: Actived(mainWindow.ui.ButtonDiv.click))
    keyboard.add_hotkey('v', lambda: Actived(mainWindow.ui.ButtonPoint.click))
    keyboard.add_hotkey('b', lambda: Actived(mainWindow.ui.ButtonBackspace.click))
    keyboard.add_hotkey('n', lambda: Actived(mainWindow.ui.ButtonClear.click))
    keyboard.add_hotkey('space', lambda: Actived(mainWindow.ui.ButtonEqual.click))

    keyboard.add_hotkey('0', lambda: Actived(mainWindow.ui.Button0.click))
    keyboard.add_hotkey('1', lambda: Actived(mainWindow.ui.Button1.click))
    keyboard.add_hotkey('2', lambda: Actived(mainWindow.ui.Button2.click))
    keyboard.add_hotkey('3', lambda: Actived(mainWindow.ui.Button3.click))
    keyboard.add_hotkey('4', lambda: Actived(mainWindow.ui.Button4.click))
    keyboard.add_hotkey('5', lambda: Actived(mainWindow.ui.Button5.click))
    keyboard.add_hotkey('6', lambda: Actived(mainWindow.ui.Button6.click))
    keyboard.add_hotkey('7', lambda: Actived(mainWindow.ui.Button7.click))
    keyboard.add_hotkey('8', lambda: Actived(mainWindow.ui.Button8.click))
    keyboard.add_hotkey('9', lambda: Actived(mainWindow.ui.Button9.click))
    keyboard.add_hotkey('shift+=', lambda: Actived(mainWindow.ui.ButtonPlus.click))
    keyboard.add_hotkey('-', lambda: Actived(mainWindow.ui.ButtonSub.click))
    keyboard.add_hotkey('shift+8', lambda: Actived(mainWindow.ui.ButtonMul.click))
    keyboard.add_hotkey('/', lambda: Actived(mainWindow.ui.ButtonDiv.click))
    keyboard.add_hotkey('.', lambda: Actived(mainWindow.ui.ButtonPoint.click))
    keyboard.add_hotkey('backspace', lambda: Actived(mainWindow.ui.ButtonBackspace.click))
    keyboard.add_hotkey('`', lambda: Actived(mainWindow.ui.ButtonClear.click))
    keyboard.add_hotkey('enter', lambda: Actived(mainWindow.ui.ButtonEqual.click))
    keyboard.add_hotkey('=', lambda: Actived(mainWindow.ui.ButtonEqual.click))

if __name__ == '__main__':
    app = QApplication([])
    mainWindow = MainWindow()
    KeyboardInput()
    mainWindow.show()
    app.exec()