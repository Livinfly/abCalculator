from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtCore import Qt
from PySide6.QtGui import QKeyEvent
from Resource.UI.abCalcUI import Ui_mainWindow as abCalcUI

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = abCalcUI()
        self.ui.setupUi(self)

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
                if len(self.course) == 2 and self.course[0] == '-':
                    self.course = '0'
                else :
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
    def keyPressEvent(self, e: QKeyEvent):
        # modifiers = e.modifiers()
        key = e.key()
        match key:
            case Qt.Key_Escape:
                app.exit()
            case Qt.Key_Alt:
                mainWindow.ui.Button0.click()
            case Qt.Key_Z:
                mainWindow.ui.Button1.click()
            case Qt.Key_X:
                mainWindow.ui.Button2.click()
            case Qt.Key_C:
                mainWindow.ui.Button3.click()
            case Qt.Key_A:
                mainWindow.ui.Button4.click()
            case Qt.Key_S:
                mainWindow.ui.Button5.click()
            case Qt.Key_D:
                mainWindow.ui.Button6.click()
            case Qt.Key_Q:
                mainWindow.ui.Button7.click()
            case Qt.Key_W:
                mainWindow.ui.Button8.click()
            case Qt.Key_E:
                mainWindow.ui.Button9.click()
            case Qt.Key_F:
                mainWindow.ui.ButtonPlus.click()
            case Qt.Key_G:
                mainWindow.ui.ButtonSub.click()
            case Qt.Key_R:
                mainWindow.ui.ButtonMul.click()
            case Qt.Key_T:
                mainWindow.ui.ButtonDiv.click()
            case Qt.Key_V:
                mainWindow.ui.ButtonPoint.click()
            case Qt.Key_B:
                mainWindow.ui.ButtonBackspace.click()
            case Qt.Key_N:
                mainWindow.ui.ButtonClear.click()
            case Qt.Key_Space:
                mainWindow.ui.ButtonEqual.click()
            case Qt.Key_0:
                mainWindow.ui.Button0.click()
            case Qt.Key_1:
                mainWindow.ui.Button1.click()
            case Qt.Key_2:
                mainWindow.ui.Button2.click()
            case Qt.Key_3:
                mainWindow.ui.Button3.click()
            case Qt.Key_4:
                mainWindow.ui.Button4.click()
            case Qt.Key_5:
                mainWindow.ui.Button5.click()
            case Qt.Key_6:
                mainWindow.ui.Button6.click()
            case Qt.Key_7:
                mainWindow.ui.Button7.click()
            case Qt.Key_8:
                mainWindow.ui.Button8.click()
            case Qt.Key_9:
                mainWindow.ui.Button9.click()
            case Qt.Key_Plus:
                mainWindow.ui.ButtonPlus.click()
            case Qt.Key_Minus:
                mainWindow.ui.ButtonSub.click()
            case Qt.Key_Asterisk:
                mainWindow.ui.ButtonMul.click()
            case Qt.Key_Slash:
                mainWindow.ui.ButtonDiv.click()
            case Qt.Key_Period:
                mainWindow.ui.ButtonPoint.click()
            case Qt.Key_Backspace:
                mainWindow.ui.ButtonBackspace.click()
            case Qt.Key_QuoteLeft:
                mainWindow.ui.ButtonClear.click()
            case Qt.Key_Return:
                mainWindow.ui.ButtonEqual.click()
            case Qt.Key_Equal:
                mainWindow.ui.ButtonEqual.click()
            case Qt.Key_Enter:
                mainWindow.ui.ButtonEqual.click()

if __name__ == '__main__':
    app = QApplication([])
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()