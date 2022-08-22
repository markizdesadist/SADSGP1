from PyQt5.QtWidgets import QWidget, QTabWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt
from winstart.order_frame import Order
from winstart.button_frame import ButtonGroupFrame


class LeftCentralWidget:
    def __init__(self):
        self.vmain = QVBoxLayout()
        self.tab = TabWidget().set_body()
        self.btn_frame = ButtonGroupFrame().set_frame()
        self.lower_lbl = QLabel()
        self.settings_elements()

    def settings_elements(self):
        self.set_label()

    def set_label(self):
        self.lower_lbl.setText('123123123')
        self.lower_lbl.setMinimumHeight(23)
        self.lower_lbl.setStyleSheet("background-color: rgb(0, 170, 0);")

    def set_frame(self):
        self.vmain.addWidget(self.tab, alignment=Qt.AlignTop | Qt.AlignLeft)
        self.vmain.addWidget(self.btn_frame)
        self.vmain.addWidget(self.lower_lbl, alignment=Qt.AlignBottom)

        return self.vmain


class TabWidget(QTabWidget):
    def __init__(self):
        super(TabWidget, self).__init__()
        self.tabWidget = QTabWidget()
        self.setMaximumSize(600, 700)
        self.setMinimumSize(600, 700)
        self.tab_order = QWidget()
        self.tab_client = QWidget()
        self.tab_new_car = QWidget()
        self.tab_old_order = QWidget()
        self.tab_help = QWidget()

    def set_body(self):
        self.setAutoFillBackground(True)
        self.setStyleSheet("background-color: rgb(185, 185, 185);")
        self.setTabPosition(QTabWidget.North)
        self.setTabShape(QTabWidget.Rounded)
        self.setElideMode(Qt.ElideNone)
        self.setObjectName("tabWidget")

        self.tab_order = QWidget()
        self.tab_order.setObjectName('tab_order')
        Order().set_frame(self.tab_order)
        self.addTab(self.tab_order, '')

        self.tab_client = QWidget()
        self.tab_client.setObjectName('tab_client')
        self.addTab(self.tab_client, '')

        self.tab_new_car = QWidget()
        self.tab_new_car.setObjectName('tab_new_car')
        self.addTab(self.tab_new_car, '')

        self.tab_old_order = QWidget()
        self.tab_old_order.setObjectName('tab_old_order')
        self.addTab(self.tab_old_order, '')

        self.tab_help = QWidget()
        self.tab_help.setObjectName('tab_help')
        self.addTab(self.tab_help, '')

        self.setTabText(0, 'Печать Актов')
        self.setTabText(1, 'Новый клиент')
        self.setTabText(2, 'Новая машина')
        self.setTabText(3, 'Закрытые акты')
        self.setTabText(4, 'Справка')

        self.setCurrentIndex(0)

        return self
