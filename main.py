import sys
#import platform
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *
from PandasModel import PandasModel
import subprocess

# ФАЙЛ ИНТЕРФЕЙСА
#from ui_main import Ui_MainWindow
import ui_main
# ИМПОРТ ФУНКЦИЙ
from ui_functions import *
import pandas as pd
df = pd.DataFrame()

class MainWindow(QMainWindow):
        
    def read_csv(self, path):
        df = pd.read_csv(path, index_col=0)
        return df
    def press_load_file(self):
        self.pathFile, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Открыть файл','./', 
                                                'Files (*.csv)')
        if self.pathFile != '':
            self.is_file_opened = True
            stats = UIFunctions(self.read_csv(self.pathFile) )        
            model = PandasModel(stats.df)
            normed_model = PandasModel(stats.get_normalized_data())
            describe_model = PandasModel(stats.get_describe_matrix())
            paircorr_model = PandasModel(stats.get_pairwise_corr_matrix())
            partialcorr_model = PandasModel(stats.get_partial_corr_matrix())
            regr_coef_model = PandasModel(stats.get_regr_analyze())
            regr_stats_model = PandasModel(stats.get_regr_stats())
            regr_error_model = PandasModel(stats.get_regr_error()) 
            normal_distr_analyze = PandasModel(stats.get_normal_analyze())
            paircorrsign = PandasModel(stats.significance(stats.df.corr()))
            partialcorrsign = PandasModel(stats.significance(stats.df.pcorr()))
            self.ui.pandasTv.setModel(model)
            self.ui.normedTv.setModel(normed_model)
            self.ui.describeTv.setModel(describe_model)
            self.ui.paircorrTv.setModel(paircorr_model)
            self.ui.paircorrsignTv.setModel(paircorrsign)
            self.ui.partialcorrTv.setModel(partialcorr_model)
            self.ui.partialcorrsignTv.setModel(partialcorrsign)
            self.ui.regr_coefTv.setModel(regr_coef_model)
            self.ui.regr_coefTv2.setModel(regr_stats_model)
            self.ui.regr_coefTv3.setModel(regr_error_model)
            self.ui.pearsonTv.setModel(normal_distr_analyze)
    
    def run_calc(self):
        if self.is_file_opened:
            subprocess.Popen(['python', 'start_regr_calc.py'])

    def __init__(self):
        QMainWindow.__init__(self)
        self.is_file_opened = False
        df = pd.DataFrame()
        self.ui = ui_main.Ui_MainWindow()
        self.ui.setupUi(self)

        ## КНОПКА ЗАГРУЗКИ ФАЙЛА
        ########################################################################
        self.ui.Btn_Toggle.clicked.connect(self.press_load_file) # в случае чего, заменить на ui_functions.loadFile

        ## СТРАНИЦЫ
        ########################################################################

        # СТРАНИЦА 1
        self.ui.btn_page_1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_1))

        # СТРАНИЦА 2
        self.ui.btn_page_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))

        # СТРАНИЦА 3
        self.ui.btn_page_3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))

        # СТРАНИЦА 4
        self.ui.btn_page_4.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_4))

        # СТРАНИЦА 5
        self.ui.btn_page_5.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_5))

        # СТРАНИЦА 6
        self.ui.btn_page_6.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_6))

        # СТРАНИЦА 7
        self.ui.btn_page_7.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_7))

         # КНОПКА КАЛЬКУЛЯТОРА РЕГРЕССИИ
        self.ui.calc_btn.clicked.connect(self.run_calc)

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
