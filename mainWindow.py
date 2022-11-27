import datetime
import sys
import io
import folium
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 750)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 160, 231, 241))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 80, 61, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 120, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 150, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 50, 47, 13))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(20, 20, 51, 16))
        self.label_5.setObjectName("label_5")
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(90, 150, 131, 20))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(86, 120, 131, 20))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setGeometry(QtCore.QRect(86, 80, 121, 20))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.groupBox)
        self.label_14.setGeometry(QtCore.QRect(86, 50, 131, 20))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.groupBox)
        self.label_15.setGeometry(QtCore.QRect(90, 20, 131, 20))
        self.label_15.setObjectName("label_15")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(20, 30, 231, 25))
        self.comboBox.setObjectName("comboBox")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 110, 101, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.start)

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 60, 231, 20))
        self.lineEdit.setObjectName("lineEdit")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 110, 101, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.stop)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.timer = QTimer()
        self.telemetry_timer = QTimer()


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Telemetry Data"))
        self.label.setText(_translate("MainWindow", "Longtitude"))
        self.label_2.setText(_translate("MainWindow", "Altitude"))
        self.label_3.setText(_translate("MainWindow", "Los Distance"))
        self.label_4.setText(_translate("MainWindow", "Latitude"))
        self.label_5.setText(_translate("MainWindow", "TIME"))
        self.label_11.setText(_translate("MainWindow", "Los Distance"))
        self.label_12.setText(_translate("MainWindow", "Los Distance"))
        self.label_13.setText(_translate("MainWindow", "Los Distance"))
        self.label_14.setText(_translate("MainWindow", "Los Distance"))
        self.label_15.setText(_translate("MainWindow", "Los Distance"))
        self.pushButton.setText(_translate("MainWindow", "Start "))
        self.pushButton_2.setText(_translate("MainWindow", "Stop"))


    def display_time(self):
        current_time = datetime.datetime.now().strftime('%Y.%m.%d - %H:%M:%S')
        self.label_15.setText(current_time)

    def display_telemetry_data(self):
        current_time = datetime.datetime.now().strftime('%Y.%m.%d - %H:%M:%S')
        self.label_14.setText(current_time)
        self.label_13.setText(current_time)
        self.label_12.setText(current_time)
        self.label_11.setText(current_time)

    def stop(self):
        try:
            self.telemetry_timer.stop()
        except:
            print("x")

    def start(self):
        print("telemetry started")
        self.telemetry_timer.timeout.connect(self.display_telemetry_data)
        self.telemetry_timer.setInterval(1000)  # 1000ms = 1s
        self.telemetry_timer.start()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    ui.timer.timeout.connect(ui.display_time)
    ui.timer.setInterval(1000)  # 1000ms = 1s
    ui.timer.start()

    sys.exit(app.exec_())
