from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5 import uic
from PyQt5.QtWidgets import *

#import main

                

class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(2000, 1000)
        MainWindow.setMinimumSize(QSize(1000, 500))
        MainWindow.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Top_Bar = QFrame(self.centralwidget)
        self.Top_Bar.setObjectName(u"Top_Bar")
        self.Top_Bar.setMaximumSize(QSize(16777215, 40))
        self.Top_Bar.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.Top_Bar.setFrameShape(QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.Top_Bar)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(200, 40))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.frame_toggle.setFrameShape(QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Btn_Toggle = QPushButton(self.frame_toggle)
        self.Btn_Toggle.setObjectName(u"Btn_Toggle")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_Toggle.sizePolicy().hasHeightForWidth())
        self.Btn_Toggle.setSizePolicy(sizePolicy)
        self.Btn_Toggle.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 0px solid;")

        self.verticalLayout_2.addWidget(self.Btn_Toggle)


        self.horizontalLayout.addWidget(self.frame_toggle)

        self.frame_top = QFrame(self.Top_Bar)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_top)


        self.verticalLayout.addWidget(self.Top_Bar)

        self.Content = QFrame(self.centralwidget)
        self.Content.setObjectName(u"Content")
        self.Content.setFrameShape(QFrame.NoFrame)
        self.Content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.Content)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setMinimumSize(QSize(200, 0))
        self.frame_left_menu.setMaximumSize(QSize(200, 16777215))
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.frame_left_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_top_menus = QFrame(self.frame_left_menu)
        self.frame_top_menus.setObjectName(u"frame_top_menus")
        self.frame_top_menus.setFrameShape(QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QFrame.Raised)


        self.verticalLayout_4 = QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)

# КНОПКИ
#######################################################################################################################        
        self.btn_page_1 = QPushButton(self.frame_top_menus)
        self.btn_page_1.setObjectName(u"btn_page_1")
        self.btn_page_1.setMinimumSize(QSize(0, 40))
        self.btn_page_1.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_page_1)

        self.btn_page_2 = QPushButton(self.frame_top_menus)
        self.btn_page_2.setObjectName(u"btn_page_2")
        self.btn_page_2.setMinimumSize(QSize(0, 40))
        self.btn_page_2.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_page_2)

        self.btn_page_3 = QPushButton(self.frame_top_menus)
        self.btn_page_3.setObjectName(u"btn_page_3")
        self.btn_page_3.setMinimumSize(QSize(0, 40))
        self.btn_page_3.setStyleSheet(u"QPushButton {\n""color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_page_3)

        self.btn_page_7 = QPushButton(self.frame_top_menus)
        self.btn_page_7.setObjectName(u"btn_page_7")
        self.btn_page_7.setMinimumSize(QSize(0, 40))
        self.btn_page_7.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_page_7)

        self.btn_page_4 = QPushButton(self.frame_top_menus)
        self.btn_page_4.setObjectName(u"btn_page_3")
        self.btn_page_4.setMinimumSize(QSize(0, 40))
        self.btn_page_4.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_page_4)

        self.btn_page_5 = QPushButton(self.frame_top_menus)
        self.btn_page_5.setObjectName(u"btn_page_4")
        self.btn_page_5.setMinimumSize(QSize(0, 40))
        self.btn_page_5.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_page_5)

        self.btn_page_6 = QPushButton(self.frame_top_menus)
        self.btn_page_6.setObjectName(u"btn_page_5")
        self.btn_page_6.setMinimumSize(QSize(0, 40))
        self.btn_page_6.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_page_6)

        self.calc_btn = QPushButton(self.frame_top_menus)
        self.calc_btn.setObjectName(u"calc_btn")
        self.calc_btn.setMinimumSize(QSize(0, 40))
        self.calc_btn.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_4.addWidget(self.calc_btn)
###############################################################################################################
    


        self.verticalLayout_3.addWidget(self.frame_top_menus, 0, Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_pages = QFrame(self.Content)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.stackedWidget = QStackedWidget(self.frame_pages)
        self.stackedWidget.setObjectName(u"stackedWidget")

        # СТРАНИЦЫ
        ################################################################################################################
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.verticalLayout_7 = QVBoxLayout(self.page_1)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")

        


        #self.label_1 = QLabel(self.page_1)
        #self.label_1.setObjectName(u"label_1")
        #font = QFont()
        #font.setPointSize(40)
        #self.label_1.setFont(font)
        #self.label_1.setStyleSheet(u"color: #FFF;")
        #self.label_1.setAlignment(Qt.AlignCenter)        
        self.pandasTv = QTableView()
        self.pandasTv.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.pandasTv.setStyleSheet("color: rgb(0, 0, 0);"
                        "background-color: rgb(255,255, 255);" #rgb(85, 170, 255) - цвет кнопки
                        "selection-color: yellow;"
                        "selection-background-color: blue;"
                        "QHeaderView::section { background-color:red };")
        
        self.verticalLayout_7.addWidget(self.pandasTv)
        self.pandasTv.setSortingEnabled(True)
        font = QFont()
        font.setPointSize(40)  
        
        '''      
        model = PandasModel(main.df)
        self.pandasTv.setModel(model)
        '''
        #self.verticalLayout_7.addWidget(self.label_1)

        self.stackedWidget.addWidget(self.page_1)

        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_6 = QVBoxLayout(self.page_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")

        self.normedTv = QTableView()
        self.normedTv.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.normedTv.setStyleSheet("color: rgb(0, 0, 0);"
                        "background-color: rgb(255,255, 255);" #rgb(85, 170, 255) - цвет кнопки
                        "selection-color: yellow;"
                        "selection-background-color: blue;"
                        "QHeaderView::section { background-color:red };")
        
        self.verticalLayout_6.addWidget(self.normedTv)
        self.normedTv.setSortingEnabled(True)
        font = QFont()
        font.setPointSize(40) 
        #self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        #self.label_2 = QLabel(self.page_2)
        #self.label_2.setObjectName(u"label_2")
        #self.label_2.setFont(font)
        #self.label_2.setStyleSheet(u"color: #FFF;")
        #self.label_2.setAlignment(Qt.AlignCenter)

        #self.verticalLayout_6.addWidget(self.label_2)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_8 = QVBoxLayout(self.page_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        #self.label = QLabel(self.page_3)
        #self.label.setObjectName(u"label")
        #self.label.setFont(font)
        #self.label.setStyleSheet(u"color: #FFF;")
        #self.label.setAlignment(Qt.AlignCenter)
        self.describeTv = QTableView()
        self.describeTv.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.describeTv.setStyleSheet("color: rgb(0, 0, 0);"
                        "background-color: rgb(255,255, 255);" #rgb(85, 170, 255) - цвет кнопки
                        "selection-color: yellow;"
                        "selection-background-color: blue;"
                        "QHeaderView::section { background-color:red };")
        
        self.verticalLayout_8.addWidget(self.describeTv)
        self.describeTv.setSortingEnabled(True)
        font = QFont()
        font.setPointSize(40) 

        #self.verticalLayout_8.addWidget(self.label)

        

        self.stackedWidget.addWidget(self.page_3)

        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.verticalLayout_12 = QVBoxLayout(self.page_7)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        #self.label_4 = QLabel(self.page_4)
        #self.label_4.setObjectName(u"label")
        #self.label_4.setFont(font)
        #self.label_4.setStyleSheet(u"color: #FFF;")
        #self.label_4.setAlignment(Qt.AlignCenter)
        self.pearsonTv = QTableView()
        self.pearsonTv.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.pearsonTv.setStyleSheet("color: rgb(0, 0, 0);"
                        "background-color: rgb(255,255, 255);" #rgb(85, 170, 255) - цвет кнопки
                        "selection-color: yellow;"
                        "selection-background-color: blue;"
                        "QHeaderView::section { background-color:red };")
        
        self.verticalLayout_12.addWidget(self.pearsonTv)
        self.pearsonTv.setSortingEnabled(True)
        font = QFont()
        font.setPointSize(40) 
        #self.verticalLayout_9.addWidget(self.label_4)

        self.stackedWidget.addWidget(self.page_7)

        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_3")
        self.verticalLayout_9 = QVBoxLayout(self.page_4)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        #self.label_4 = QLabel(self.page_4)
        #self.label_4.setObjectName(u"label")
        #self.label_4.setFont(font)
        #self.label_4.setStyleSheet(u"color: #FFF;")
        #self.label_4.setAlignment(Qt.AlignCenter)
        self.paircorrTv = QTableView()
        self.paircorrTv.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        #self.paircorrTv.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.paircorrTv.setStyleSheet("color: rgb(0, 0, 0);"
                        "background-color: rgb(255,255, 255);" #rgb(85, 170, 255) - цвет кнопки
                        "selection-color: yellow;"
                        "selection-background-color: blue;")
        
        self.verticalLayout_9.addWidget(self.paircorrTv)
        self.paircorrTv.setSortingEnabled(True)        
        font = QFont()
        font.setPointSize(40) 
        self.paircorrsignTv = QTableView()
        self.paircorrsignTv.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        #self.paircorrTv.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.paircorrsignTv.setStyleSheet("color: rgb(0, 0, 0);"
                        "background-color: rgb(255,255, 255);" #rgb(85, 170, 255) - цвет кнопки
                        "selection-color: yellow;"
                        "selection-background-color: blue;")
        
        self.verticalLayout_9.addWidget(self.paircorrsignTv)
        self.paircorrsignTv.setSortingEnabled(True)        
        font = QFont()
        font.setPointSize(40) 
        #self.verticalLayout_9.addWidget(self.label_4)

        self.stackedWidget.addWidget(self.page_4)

        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_4")
        self.verticalLayout_10 = QVBoxLayout(self.page_5)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        #self.label_4 = QLabel(self.page_4)
        #self.label_4.setObjectName(u"label")
        #self.label_4.setFont(font)
        #self.label_4.setStyleSheet(u"color: #FFF;")
        #self.label_4.setAlignment(Qt.AlignCenter)
        self.partialcorrTv = QTableView()
        self.partialcorrTv.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.partialcorrTv.setStyleSheet("color: rgb(0, 0, 0);"
                        "background-color: rgb(255,255, 255);" #rgb(85, 170, 255) - цвет кнопки
                        "selection-color: yellow;"
                        "selection-background-color: blue;"
                        "QHeaderView::section { background-color:red };")
        
        self.verticalLayout_10.addWidget(self.partialcorrTv)
        self.partialcorrTv.setSortingEnabled(True)
        font = QFont()
        font.setPointSize(40) 
        #self.verticalLayout_9.addWidget(self.label_4)

        self.partialcorrsignTv = QTableView()
        self.partialcorrsignTv.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.partialcorrsignTv.setStyleSheet("color: rgb(0, 0, 0);"
                        "background-color: rgb(255,255, 255);" #rgb(85, 170, 255) - цвет кнопки
                        "selection-color: yellow;"
                        "selection-background-color: blue;"
                        "QHeaderView::section { background-color:red };")
        
        self.verticalLayout_10.addWidget(self.partialcorrsignTv)
        self.partialcorrsignTv.setSortingEnabled(True)
        font = QFont()
        font.setPointSize(40) 
       

        self.stackedWidget.addWidget(self.page_5)

        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_5")
        self.verticalLayout_11 = QVBoxLayout(self.page_6)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")         

        self.regr_coefTv = QTableView()
        self.regr_coefTv.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.regr_coefTv.setStyleSheet("color: rgb(0, 0, 0);"
                        "background-color: rgb(255,255, 255);" #rgb(85, 170, 255) - цвет кнопки
                        "selection-color: yellow;"
                        "selection-background-color: blue;"
                        "QHeaderView::section { background-color:red };")        
        
        self.regr_coefTv.setSortingEnabled(True)
        font = QFont()
        font.setPointSize(40) 
        self.verticalLayout_11.addWidget(self.regr_coefTv)

        self.regr_coefTv2 = QTableView()
        self.regr_coefTv2.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.regr_coefTv2.setStyleSheet("color: rgb(0, 0, 0);"
                        "background-color: rgb(255,255, 255);" #rgb(85, 170, 255) - цвет кнопки
                        "selection-color: yellow;"
                        "selection-background-color: blue;"
                        "QHeaderView::section { background-color:red };")        
        
        self.regr_coefTv2.setSortingEnabled(True)
        font = QFont()
        font.setPointSize(40) 
        self.verticalLayout_11.addWidget(self.regr_coefTv2)

        self.regr_coefTv3 = QTableView()
        self.regr_coefTv3.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.regr_coefTv3.setStyleSheet("color: rgb(0, 0, 0);"
                        "background-color: rgb(255,255, 255);" #rgb(85, 170, 255) - цвет кнопки
                        "selection-color: yellow;"
                        "selection-background-color: blue;"
                        "QHeaderView::section { background-color:red };")        
        
        self.regr_coefTv3.setSortingEnabled(True)
        font = QFont()
        font.setPointSize(40) 
        self.verticalLayout_11.addWidget(self.regr_coefTv3)
        '''
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.m_w11 = QWidget()
        self.m_w12 = QWidget()
        self.m_w21 = QWidget()
        self.m_w22 = QWidget()

        lay = QGridLayout(central_widget)

        for w, (r, c) in zip(
            (self.m_w11, self.m_w12, self.m_w21, self.m_w22),
            ((0, 0), (0, 1), (1, 0), (1, 1)),
        ):
            lay.addWidget(w, r, c)
        for c in range(2):
            lay.setColumnStretch(c, 1)
        for r in range(2):
            lay.setRowStretch(r, 1)

        lay = QVBoxLayout(self.m_w11)
        lay.addWidget(QTextEdit())

        lay = QVBoxLayout(self.m_w12)
        self.regr_coefTv = QTableView()
        self.regr_coefTv.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.regr_coefTv.setStyleSheet("color: rgb(0, 0, 0);"
                        "background-color: rgb(255,255, 255);" #rgb(85, 170, 255) - цвет кнопки
                        "selection-color: yellow;"
                        "selection-background-color: blue;"
                        "QHeaderView::section { background-color:red };")        
        
        self.regr_coefTv.setSortingEnabled(True)
        font = QFont()
        font.setPointSize(40) 
        lay.addWidget(self.regr_coefTv)

        lay = QVBoxLayout(self.m_w21)  

        lay.addWidget(QLineEdit())
        # ИДЕЯ: добавить три QHBoxLayout и по кд заполнять их Label и QLineEdit и в последнем ящике сделать кнопку расчёта
        # как вариант - снести 4 клетки и выстроить 3 вертикальных QVBoxLayout (а ещё лучше 1 и туда всё пихать)

        lay = QVBoxLayout(self.m_w22)
        lay.addWidget(QLabel("Text", alignment=Qt.AlignCenter))
        
        self.verticalLayout_11.addWidget(central_widget)
        '''
        self.stackedWidget.addWidget(self.page_6)

        
########################################################################################################################
        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.frame_pages)


        self.verticalLayout.addWidget(self.Content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Btn_Toggle.setText(QCoreApplication.translate("MainWindow", u"Загрузить файл", None))
        self.btn_page_1.setText(QCoreApplication.translate("MainWindow", u"Исходные данные", None))
        self.btn_page_2.setText(QCoreApplication.translate("MainWindow", u"Нормированные данные", None))
        self.btn_page_3.setText(QCoreApplication.translate("MainWindow", u"Описательная статистика", None))
        self.btn_page_4.setText(QCoreApplication.translate("MainWindow", u"Парная корреляция", None))
        self.btn_page_5.setText(QCoreApplication.translate("MainWindow", u"Частная корреляция", None))
        self.btn_page_6.setText(QCoreApplication.translate("MainWindow", u"Регрессионный анализ", None))
        self.btn_page_7.setText(QCoreApplication.translate("MainWindow", u"Проверка нормальности", None))
        self.calc_btn.setText(QCoreApplication.translate("MainWindow", u"Калькулятор предсказания", None))
        #self.label_1.setText(QCoreApplication.translate("MainWindow", u"PAGE 1", None))
        #self.label_2.setText(QCoreApplication.translate("MainWindow", u"PAGE 2", None))
        #self.label.setText(QCoreApplication.translate("MainWindow", u"PAGE 3", None))
        #self.label_4.setText(QCoreApplication.translate("MainWindow", u"PAGE 4", None))
    # retranslateUi



