
#%%
from qtpy import uic


#uic.compileUiDir("UserInterface")
#uic.compileUi("RadioMainWindow.ui","RadioMainWindow.py")

with open('RadioMainWindow.py', 'w') as fout:
    uic.compileUi('RadioMainWindow.ui', fout)