
from PyQt5 import QtWidgets
from regr_calc import Ui_Form  # импорт нашего сгенерированного файла

import sys
import ui_functions
 
class mywindow(QtWidgets.QMainWindow):
    def __init__(self, regr_coefs):
        super(mywindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.x = [0 for i in range(7)]
        self.regr_coefs = regr_coefs
        self.ui.pushButton.clicked.connect(self.push_btn)
    
    def is_float(self,value):
        try:
            float(value)
            return True
        except:
            return False

    def push_btn(self):
        buttons = [self.ui.nn_field, self.ui.tn_field, self.ui.tr_field, self.ui.pu_field, self.ui.cwt_filed, self.ui.iwt_filed,self.ui.cu_field]
        flag = True
        for i in range(len(buttons)):
            if self.is_float(buttons[i].text()):
                self.x[i] = float(buttons[i].text())
            else:
                buttons[i].clear()
                flag = False
        if flag:
            pred = self.calculate_pred()
            self.ui.nrt_field.setText(str(round(pred,3)))

                
    
    def calculate_pred(self):
        pred = 0
        for i in range(len(self.regr_coefs)-1):
            pred += self.x[i]*self.regr_coefs[i]
        pred += self.regr_coefs[-1]
        print(pred)
        return pred 

app = QtWidgets.QApplication([])
application = mywindow([9.20176680e+00, 7.09278178e+01, 7.11171054e+02, 8.08432390e+02,
       2.95971460e+00, 4.28404035e-01, 1.46444039e+02,-1034.0071343350833])
application.show()
 
sys.exit(app.exec())