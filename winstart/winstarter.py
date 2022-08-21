# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QFrame, QSplashScreen
from winstart import order_frame
from winstart import texttranslate
from winstart import button_frame
from setting import logger
import sys
import os
from datetime import datetime
from functools import wraps
import time


class MainWindow(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

    @logger.logger.catch
    def setting_window(self):
        """
        Настройки основного окна.
        :return: None
        """
        self.setObjectName("MainWindow")
        self.setWindowTitle("Пробная кукушка")
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowFlags(QtCore.Qt.Window)
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(os.path.join(os.getcwd(), '..', 'templatefiles', 'lpgo.jpg')),
            QtGui.QIcon.Normal,
            QtGui.QIcon.On
        )
        self.setWindowIcon(icon)
        self.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.setMinimumSize(650, 900)
        self.resize(1500, 800)
        self.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.setAutoFillBackground(True)

        self.ui_window()
        """
        Размещение окна по центру:
        desktop = QtWidgets.QApplication.desktop()
        x = (desktop.width() - self.width()) // 2
        y = (desktop.height() - self.height()) // 2
        self.move(x, y)"""

    @logger.logger.catch
    def ui_window(self):
        self.root_frame = QtWidgets.QHBoxLayout(self)
        self.upper_frame = QtWidgets.QVBoxLayout()
        self.center_frame = QtWidgets.QVBoxLayout()
        self.lower_frame = QtWidgets.QVBoxLayout()
        frame = UpperFrame().set_frame()
        frame2 = order_frame.Order().set_frame()
        self.root_frame.addWidget(frame)
        self.root_frame.addLayout(self.center_frame)
        self.root_frame.addWidget(frame2)
        tab = TabWidget().frame_left()
        self.center_frame.addWidget(tab)


""" @@@@@@@@@@@@@@@@@@@@@@@@   windows        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  """

class UpperFrame:
    def __init__(self):
        self.frame = Frame()

    def set_frame(self):
        self.frame = Frame()
        self.frame.resize(300, 500)
        self.frame.setMaximumHeight(100)
        self.frame.setMinimumHeight(100)
        self.frame.setStyleSheet("background-color: rgb(215, 215, 215);")
        self.v_box = QtWidgets.QVBoxLayout(self.frame)
        self.btn = Button()
        self.btn.setText("Button")
        self.lbl = Label()
        self.lbl.setText("Label")

        self.v_box.addWidget(self.btn)
        self.v_box.addWidget(self.lbl)

        return self.frame

""" @@@@@@@@@@@@@@@@@@@@@@@@   ELEMENTS        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  """





class Frame(QtWidgets.QFrame):
    def __init__(self):
        super(Frame, self).__init__()


class TabWidget(QtWidgets.QTabWidget):
    def __init__(self):
        super(TabWidget, self).__init__()
        self.tabWidget = QtWidgets.QTabWidget()
        self.tabWidget.setMaximumWidth(600)
        self.tabWidget.setMaximumSize(600, 700)
        self.tab_order = QtWidgets.QWidget()
        self.tab_client = QtWidgets.QWidget()
        self.tab_new_car = QtWidgets.QWidget()
        self.tab_old_order = QtWidgets.QWidget()
        self.tab_help = QtWidgets.QWidget()

    def frame_left(self):
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setStyleSheet("background-color: rgb(185, 185, 185);")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setObjectName("tabWidget")

        self.tab_order = QtWidgets.QWidget()
        self.tab_order.setObjectName('tab_order')
        order_frame.Order().set_frame(self.tab_order)
        self.tabWidget.addTab(self.tab_order, '')

        self.tab_client = QtWidgets.QWidget()
        self.tab_client.setObjectName('tab_client')
        self.tabWidget.addTab(self.tab_client, '')

        self.tab_new_car = QtWidgets.QWidget()
        self.tab_new_car.setObjectName('tab_new_car')
        self.tabWidget.addTab(self.tab_new_car, '')

        self.tab_old_order = QtWidgets.QWidget()
        self.tab_old_order.setObjectName('tab_old_order')
        self.tabWidget.addTab(self.tab_old_order, '')

        self.tab_help = QtWidgets.QWidget()
        self.tab_help.setObjectName('tab_help')
        self.tabWidget.addTab(self.tab_help, '')

        self.tabWidget.setCurrentIndex(0)

        # super().retranslate()

        return self.tabWidget


class Button(QtWidgets.QPushButton):
    def __init__(self):
        super(Button, self).__init__()


class Label(QtWidgets.QLabel):
    def __init__(self):
        super(Label, self).__init__()
        self.setStyleSheet("background-color: rgb(255, 255, 255);")


class Timer:
    def __init__(self):
        self.timeEdit = QtWidgets.QTimeEdit()
        self.current_time = QtCore.QTime.currentTime()
        self.timer = QtCore.QTimer()

    def set_timer(self):
        # self.timeEdit.setGeometry(QtCore.QRect(50, 0, 150, 70))
        size = QtCore.QSize(300, 100)
        size.scale(300, 100, QtCore.Qt.KeepAspectRatio)
        self.timeEdit.setMaximumSize(size)
        self.timeEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.timeEdit.setStyleSheet("background-color: rgb(207, 207, 207);")
        self.timeEdit.setWrapping(False)
        self.timeEdit.setFrame(True)
        self.timeEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.timeEdit.setReadOnly(True)
        self.timeEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.timeEdit.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToPreviousValue)
        self.timeEdit.setKeyboardTracking(False)
        self.timeEdit.setObjectName("timeEdit")
        self.timeEdit.setTime(datetime.now().time())

        self.timer.timeout.connect(self.time_edit_update)
        self.timer.start(1000)

        return self.timeEdit

    def time_edit_update(self):
        self.timeEdit.setTime(self.current_time)


""" @@@@@@@@@@@@@@@@@@@@@@@@   SplashScreen        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  """


def splasher(func):
    # @wraps
    def wrapper(*args, **kwargs):
        def load_data(sp):
            for i in range(1, 3):
                time.sleep(1)
                sp.showMessage(
                    "Загрузка данных ... 0%",
                    QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom,
                    QtCore.Qt.red
                )
                QtWidgets.qApp.processEvents()

        splash = QtWidgets.QSplashScreen(QtGui.QPixmap(""))
        splash.showMessage(
            "Загрузка данных ... 0%",
            QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom,
            QtCore.Qt.white
        )
        splash.show()
        QtWidgets.qApp.processEvents()
        load_data(splash)
        splash.finish(*args)
        func(*args, **kwargs)

    return wrapper


@logger.logger.catch
@splasher
def start(win):
    logger.logger.info(': Начал работу с программой.')
    win.show()


if __name__ == '__main__':
    start_app = QApplication(sys.argv)
    windows = MainWindow()
    start(windows)
    sys.exit(start_app.exec_())
