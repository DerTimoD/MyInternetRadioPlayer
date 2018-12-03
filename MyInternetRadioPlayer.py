import sys

from qtpy import QtGui, QtWidgets

from UserInterface.RadioMainWindow import Ui_MainWindow

app = QtWidgets.QApplication(sys.argv)

class MainWindow (QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Test")
    
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButtonPlay.clicked.connect(self.OnPlay)
        self.ui.pushButtonPause.clicked.connect(self.OnPause)
        self.ui.pushButtonNext.clicked.connect(self.OnNext)
        self.ui.pushButtonPrev.clicked.connect(self.OnPrev)

        self._stationNumber = 1
        self._stationNumberMax = 12

    def OnPlay(self):
        print("Play")
        self.ui.TextBoxStatus.setText("Test hhsakdfhjhajsldhflkjhlakjsdhfjhjklasdhkfjhakljsdhkfhaksjdhfkj\n")
        
    def OnPause(self):
        print("Pause")

    def OnNext(self):
        if(self._stationNumber == self._stationNumberMax):
            self._stationNumber = 1
        else:
            self._stationNumber = self._stationNumber + 1

        print("Next")
        print("Stationnumber: " + str(self._stationNumber))
        self.ui.TextBoxStatus.setText(("Stationnumber: " + str(self._stationNumber)))

    def OnPrev(self):
        if(self._stationNumber == 1):
            self._stationNumber = self._stationNumberMax
        else:
            self._stationNumber = self._stationNumber - 1

        print("Prev")
        print("Stationnumber: " + str(self._stationNumber))

window = MainWindow()


window.show()  
sys.exit(app.exec())
