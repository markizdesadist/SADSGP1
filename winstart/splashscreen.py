# from PyQt5.QtCore import QTimer, Qt
# from PyQt5.QtGui import QMovie
# from PyQt5.QtWidgets import QApplication, QSplashScreen, QWidget, \
#     QMainWindow, QLabel, QGridLayout, QHBoxLayout, QVBoxLayout, QFrame
# from setting import logger
# import os
#
#
# class GifSplashScreen(QSplashScreen):
#     def __init__(self, *args, **kwargs):
#         super(GifSplashScreen, self).__init__(*args, **kwargs)
#         self.movie = QMovie(os.path.join(os.getcwd(), '..', 'templatefiles', 'CZk.gif'))
#         self.movie.frameChanged.connect(self.onFrameChanged)
#         self.movie.start()
#
#     @logger.logger.catch
#     def onFrameChanged(self, _):
#         self.setPixmap(self.movie.currentPixmap())
#
#     @logger.logger.catch
#     def finish(self, widget):
#         self.movie.stop()
#         super(GifSplashScreen, self).finish(widget)
#
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('Main Form')
#         self.resize(640, 480)
#
#         self.centralwidget = QWidget()
#         self.setCentralWidget(self.centralwidget)
#
#         # self.label = QLabel('<h1>Hello World.</h1>')
#         # self.layout = QGridLayout(self.centralwidget)
#         # self.layout.addWidget(self.label, 0, 0, alignment=Qt.AlignCenter)
#         self.frame = QFrame()
#         self.hbox = QHBoxLayout()
#         self.vbox = QVBoxLayout()
#         self.hbox.addWidget(self.vbox)
#
#
#
#
# if __name__ == '__main__':
#     import sys
#
#     app = QApplication(sys.argv)
#     splash = GifSplashScreen()
#     splash.show()
#
#
#     def createWindow():
#         app.w = MainWindow()
#         # Имитация начального отображения через 3 секунды
#         splash.showMessage(
#             'Ожидание отображения интерфейса',
#             Qt.AlignHCenter | Qt.AlignBottom, Qt.white
#         )
#         QTimer.singleShot(3000, lambda: (
#             splash.showMessage(
#                 'Загрузка завершена',
#                 Qt.AlignHCenter | Qt.AlignBottom, Qt.white
#             ),
#             app.w.show(),
#             splash.finish(app.w))
#                           )
#
#
#     # Симуляция занимает 6 секунд. Вы не можете использовать sleep.
#     # Можете использовать дочерние потоки для загрузки трудоемких данных.
#     # Интерфейс настройки цикла в основном потоке может взаимодействовать с
#     # QApplication.instance().processEvents()
#     splash.showMessage(
#         'Ожидание создания интерфейса',
#         Qt.AlignHCenter | Qt.AlignBottom, Qt.white
#     )
#     QTimer.singleShot(3000, createWindow)
#
#     sys.exit(app.exec_())


# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
#
# __author__ = 'ipetrash'
#
#
# from PyQt5 import Qt
#
#
# class URLView(Qt.QWidget):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#
#         layout = Qt.QVBoxLayout(self)
#
#         self.urlEdit = Qt.QLineEdit()
#         self.urlEdit.setText('https://www.python.org/static/img/python-logo.png')
#         layout.addWidget(self.urlEdit)
#
#         self.imageLabel = Qt.QLabel("No image")
#         self.imageLabel.setScaledContents(True)
#         layout.addWidget(self.imageLabel)
#
#         self.loadButton = Qt.QPushButton("Load")
#         layout.addWidget(self.loadButton)
#
#         self.loadButton.clicked.connect(self.on_load)
#
#         self.nam = Qt.QNetworkAccessManager()
#         self.nam.finished.connect(self.finish_request)
#
#     def on_load(self):
#         print("Load image")
#
#         url = self.urlEdit.text()
#         self.nam.get(Qt.QNetworkRequest(Qt.QUrl(url)))
#
#     def finish_request(self, reply):
#         img = Qt.QPixmap()
#         img.loadFromData(reply.readAll())
#
#         self.imageLabel.setPixmap(img)
#
#
# if __name__ == '__main__':
#     app = Qt.QApplication([])
#     w = URLView()
#     w.show()
#     app.exec()