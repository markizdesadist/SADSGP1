from PyQt5.QtWidgets import QHBoxLayout, QFrame, QPushButton
from PyQt5.QtCore import Qt
from abc import ABC, abstractmethod


class ButtonGroupFrame:
    def __init__(self):
        self.frame = QFrame()
        self.vmain_btn = QHBoxLayout(self.frame)
        self.btn_exit = BtnExit().set_button()
        self.btn_save = BtnSave().set_button()
        self.settings_elements()

    def settings_elements(self):
        self.set_background()
        self.add_action()

    def set_background(self):
        self.frame.setMaximumWidth(598)
        self.frame.setStyleSheet("background-color: rgb(185, 185, 185);")

    def set_frame(self):
        self.vmain_btn.addWidget(self.btn_save, alignment=Qt.AlignRight)
        self.vmain_btn.addWidget(self.btn_exit, alignment=Qt.AlignRight)
        return self.frame

    def add_action(self):
        pass


# ======================================


class BaseBtn(ABC):
    def __init__(self):
        super(BaseBtn, self).__init__()
        self.btn = QPushButton()
        self.action()
        self.setting_btn()

    def set_button(self):
        return self.btn

    @abstractmethod
    def setting_btn(self):
        pass

    @abstractmethod
    def action(self):
        pass


# ======================================

class BtnSave(BaseBtn):
    def __init__(self):
        super(BtnSave, self).__init__()
        pass

    def setting_btn(self):
        self.btn.setText('SAVE')
        self.btn.setMinimumSize(50, 40)

    def action(self):
        self.btn.clicked.connect(lambda: print('Save'))


# ======================================

class BtnExit(BaseBtn):
    def __init__(self):
        super(BtnExit, self).__init__()
        pass

    def setting_btn(self):
        self.btn.setText('EXIT')
        self.btn.setMinimumSize(50, 40)

    def action(self):
        self.btn.clicked.connect(lambda: print('Exit'))


if __name__ == '__main__':
    pass

# # from frame.CSS_template import CSS
# from setting.logger import logger
#
# btn_color = 'green'
# # if int(config['HELP']['btn_news']):
# #     btn_color = 'red'
#
#
# class BtnFrame:
#     def __int__(self):
#         self.frame = QtWidgets.QFrame()
#
#     def set_frame(self):
#         self.frame = QtWidgets.QFrame()
#         self.frame.setMinimumSize(QtCore.QSize(0, 40))
#         self.frame.setMaximumSize(QtCore.QSize(16777215, 40))
#         self.frame.setLayoutDirection(QtCore.Qt.LeftToRight)
#         self.frame.setAutoFillBackground(True)
#         self.frame.setStyleSheet("background-color: rgb(85, 170, 0);")
#         self.frame.setFrameShape(QtWidgets.QFrame.WinPanel)
#         self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.frame.setObjectName("frame")
#
#         self.set_body()
#         return self.frame
#
#     def set_body(self):
#         self.btn_pushButton_exit = QtWidgets.QPushButton(self.frame)
#         self.btn_pushButton_exit.setGeometry(QtCore.QRect(1110, 5, 117, 30))
#         # self.btn_pushButton_exit.setFont(CSS.set_font())
#         self.btn_pushButton_exit.setAutoFillBackground(False)
#         self.btn_pushButton_exit.setStyleSheet("background-color: rgb(0, 170, 0);\n"
#                                                "border-bottom-color: rgb(255, 255, 127);")
#         self.btn_pushButton_exit.setObjectName("btn_pushButton_exit")
#
#         self.btn_pushButton_help = QtWidgets.QPushButton(self.frame)
#         self.btn_pushButton_help.setGeometry(QtCore.QRect(900, 5, 117, 30))
#         # self.btn_pushButton_help.setFont(CSS.set_font())
#         self.btn_pushButton_help.setLayoutDirection(QtCore.Qt.LeftToRight)
#         self.btn_pushButton_help.setAutoFillBackground(False)
#         self.btn_pushButton_help.setStyleSheet("background-color: {};\n"
#                                                "border-bottom-color: rgb(255, 255, 127);".format(btn_color))
#         self.btn_pushButton_help.setObjectName("btn_pushButton_help")
#
#         self.pushButton_6 = QtWidgets.QPushButton(self.frame)
#         self.pushButton_6.setGeometry(QtCore.QRect(50, 5, 117, 30))
#         # self.pushButton_6.setFont(CSS.set_font())
#         self.pushButton_6.setAutoFillBackground(False)
#         self.pushButton_6.setStyleSheet("background-color: rgb(0, 170, 0);\n"
#                                         "border-bottom-color: rgb(255, 255, 127);")
#         self.pushButton_6.setObjectName("pushButton_6")
#         self.pushButton_7 = QtWidgets.QPushButton(self.frame)
#         self.pushButton_7.setGeometry(QtCore.QRect(170, 5, 117, 30))
#         # self.pushButton_7.setFont(CSS.set_font())
#         self.pushButton_7.setAutoFillBackground(False)
#         self.pushButton_7.setStyleSheet("background-color: rgb(0, 170, 0);\n"
#                                         "border-bottom-color: rgb(255, 255, 127);")
#         self.pushButton_7.setObjectName("pushButton_7")
#
#         self.pushButton_8 = QtWidgets.QPushButton(self.frame)
#         self.pushButton_8.setGeometry(QtCore.QRect(290, 5, 117, 30))
#         # self.pushButton_8.setFont(CSS.set_font())
#         self.pushButton_8.setAutoFillBackground(False)
#         self.pushButton_8.setStyleSheet("background-color: rgb(0, 170, 0);\n"
#                                         "border-bottom-color: rgb(255, 255, 127);")
#         self.pushButton_8.setObjectName("pushButton_8")
#
#         self.pushButton_9 = QtWidgets.QPushButton(self.frame)
#         self.pushButton_9.setGeometry(QtCore.QRect(410, 5, 117, 30))
#         # self.pushButton_9.setFont(CSS.set_font())
#         self.pushButton_9.setAutoFillBackground(False)
#         self.pushButton_9.setStyleSheet("background-color: rgb(0, 170, 0);\n"
#                                         "border-bottom-color: rgb(255, 255, 127);")
#         self.pushButton_9.setObjectName("pushButton_9")
#
#         # self.btn_pushButton_exit.clicked.connect(QtWidgets.QApplication.exit())  # type: ignore
#
#         # self.add_action_btn()
#
#         self.retranslateUi()
#
#     def add_action_btn(self):
#         self.btn_pushButton_exit.clicked.connect(lambda: self.frame.parent().parent().close())
#         # self.btn_pushButton_help.clicked.connect(lambda: self.frame.parent().tabWidget.setCurrentIndex(4))
#
#     def retranslateUi(self):
#         _translate = QtCore.QCoreApplication.translate
#
#         self.btn_pushButton_exit.setText(_translate("MainWindow", "Exit"))
#         self.btn_pushButton_help.setText(_translate("MainWindow", "Справка"))
#         self.pushButton_6.setText(_translate("MainWindow", "....."))
#         self.pushButton_7.setText(_translate("MainWindow", "....."))
#         self.pushButton_8.setText(_translate("MainWindow", "....."))
#         self.pushButton_9.setText(_translate("MainWindow", "....."))
