from PySide6 import QtCore, QtGui
from PySide6.QtCore import QPropertyAnimation
from main import *
class Hint:
    hint_level_normal = """
    <html><head/><body><p><span style=" color:#ffffff;">提示: %s</span></p></body></html>
    """
    hint_level_waring = """
    <html><head/><body><p><span style=" color:#ff3c3c;">警告: %s</span></p></body></html>
    """
class Myselfunctions(MyselfGUI):
    def toggleMenu(self, maxWidth=200, enable=True, standard:int = 70):
        if enable:
            width = self.main.frame_left_menu.width()
            widthExtend = maxWidth if width == standard else standard
            if width == standard:
                widthExtend = maxWidth
                self.main.button_page_search.setText("主頁")
                self.main.button_page_schedule.setText("下載")
                self.main.button_page_setting.setText("設定")
            else:
                widthExtend = standard
                self.main.button_toggle.setText("")
                self.main.button_page_search.setText("")
                self.main.button_page_schedule.setText("")
                self.main.button_page_setting.setText("")


            self.animation = QPropertyAnimation(self.main.frame_left_menu, b'minimumWidth')
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtend)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()
    
    def hint(self, hint:str, level=Hint.hint_level_normal) -> None:
        self.main.hintbox.setText(level%hint)