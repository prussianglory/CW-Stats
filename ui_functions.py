
## ==> GUI FILE
import main
import pandas as pd
import copy
import statistics
import math
import numpy as np
from sklearn.metrics import r2_score
from scipy.stats import describe, variation, normaltest
from pingouin import pcorr
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
import statsmodels.formula.api as smf
class UIFunctions:
    def __init__(self,data):
        self.df = data
        for column in self.df.columns:
            self.df[column] = self.df[column].agg(UIFunctions.to_float)
            #self.df[column] = self.df[column].agg(UIFunctions.round_df)
    def to_float( num):
        s = float(str(num).replace(',','.'))
        return s
    def to_string(num):
        s  = str(num)
        return s

    def get_t_values(self):        
        new_df = self.df.rename(columns = {'Node Number':'X1', 'Thread Number':'X2', 'T/R':'X3', 'Processor Utilization ':'X4',
       'Channel Waiting Time':'X5', 'Input Waiting Time':'X6', 'Network Response Time':'Y',
       'Channel Utilization':'X7'})
        result = smf.ols(formula='Y ~ X1 + X2 + X3 +X4 + X5 + X6 + X7 ', data=new_df).fit()
        inters = []
        for i in result.conf_int().values:
            inters.append(str(i))
        return result.tvalues.values, inters


    def is_colin(num):
        if abs(float(num)) > 0.75:
            num += ' (к)'        
        return num

    def round_df(num):
        #print(type(num))
        if type(num) == np.float64 or type(num) == float :
            num = round(num,3)
        return num

    def get_normalized_data(self):
        self.norm_df = copy.deepcopy(self.df)
        for i in self.norm_df.columns:
            self.norm_df[i] = self.norm_df[i].apply(lambda x: x / (self.norm_df[i].max() - self.norm_df[i].min()))
            #self.norm_df[i] = self.norm_df[i].agg(UIFunctions.round_df)
        return self.norm_df
    def get_pairwise_corr_matrix(self):
        self.df_corr =  self.norm_df.corr()              
        for column in self.df_corr:
            self.df_corr[column] = self.df_corr[column].agg(UIFunctions.round_df)
            self.df_corr[column] = self.df_corr[column].agg(UIFunctions.to_string)
            self.df_corr[column] = self.df_corr[column].agg(UIFunctions.is_colin)


        return self.df_corr
    
    def get_partial_corr_matrix(self):
        self.df_pcorr = self.df.pcorr()
        for column in self.df_corr:
            self.df_pcorr[column] = self.df_pcorr[column].agg(UIFunctions.round_df)
            self.df_pcorr[column] = self.df_pcorr[column].agg(UIFunctions.to_string)
            self.df_pcorr[column] = self.df_pcorr[column].agg(UIFunctions.is_colin)
        return self.df_pcorr
    def get_describe_matrix(self):
        index_list = ['Арифметическое среднее', 'Мода', 'Медиана', 'Дисперсия', 'Стандартное отклонение', 'Эксцесс', 'Ассиметрия',
              'Коэффициент вариации', 'Предельная ошибка', 'Перцентиль 40%', 'Перцентиль 80%']
        desc_stats = {}
        for column in self.df.columns:
            desc_stats[column] = []
            desc_stats[column].append(round(np.mean(self.norm_df[column]),3))
            desc_stats[column].append(round(statistics.mode(self.norm_df[column]),3))
            desc_stats[column].append(round(statistics.median(self.norm_df[column]),3))
            desc_stats[column].append(round(statistics.variance(self.norm_df[column]),3))
            desc_stats[column].append(round(statistics.stdev(self.norm_df[column]),3))
            describtion = describe(self.norm_df[column])
            desc_stats[column].append(round(describtion.kurtosis,3))
            desc_stats[column].append(round(describtion.skewness,3))
            desc_stats[column].append(round(variation(self.norm_df[column]),3))
            desc_stats[column].append(round(0.5 * math.sqrt(statistics.variance(self.norm_df[column]) / len(self.norm_df)),3))
            desc_stats[column].append(round(self.norm_df[column].quantile(0.4),3))
            desc_stats[column].append(round(self.norm_df[column].quantile(0.8),3))
        
        return pd.DataFrame(desc_stats, index=index_list)

    def get_regr_coefs(self):
        y = self.df['Network Response Time']
        X_train = self.df.drop('Network Response Time', axis = 1)
        clf = LinearRegression(n_jobs=-1)
        clf.fit(X_train, y)
        regr_coefs = np.append(clf.intercept_, clf.coef_)
        return regr_coefs, X_train
    
    def get_regr_analyze(self):       
        
        self.regr_coefs, X_train = self.get_regr_coefs()
        cols = ['Свободный член']
        for col in X_train.columns.to_list():
            cols.append(col)      
        regr_data = pd.DataFrame([self.regr_coefs], columns=cols)
        regr_data.loc[1], regr_data.loc[2] = self.get_t_values()
        regr_data.index = ['Коэффициенты уравнения регрессии', 't-критерий', 'Доверительные интервалы']
        return regr_data
    
    def get_approximation_error(self):        
        X_train = self.df.drop('Network Response Time', axis = 1)

        y_pred = []
        new_y = []
        for record in X_train.to_numpy():
            y_i = 0
            for i in range(len(record)):
                #print(record)
                y_i += record[i]*self.regr_coefs[i+1]
            y_i += self.regr_coefs[0]
            y_pred.append(y_i)
            new_y.append(float(self.regr_coefs[1])*record[0]+float(self.regr_coefs[5])*record[4])
            #print(new_y[-1])
        y = self.df['Network Response Time'].to_numpy()
        A1 = 0
        A2 = 0
        for i in range(len(y)):
            A1+= abs((y[i] - y_pred[i])/y[i])
            A2+= abs((y[i]- new_y[i])/y[i])
        A1 = A1*100/len(y) 
        A2 = A2*100/len(y) 
        return A1, A2

    def get_pred_and_error(self):
        new_df = self.df.rename(columns = {'Node Number':'X1', 'Thread Number':'X2', 'T/R':'X3', 'Processor Utilization ':'X4',
       'Channel Waiting Time':'X5', 'Input Waiting Time':'X6', 'Network Response Time':'Y',
       'Channel Utilization':'X7'})
        result = smf.ols(formula='Y ~ X1 + X2 + X3 +X4 + X5 + X6 + X7 ', data=new_df).fit()
        prediction = result.get_prediction(new_df).summary_frame(0.05)
        y_pred = []
        y_error = []
        y_inter = []
        new_y = []
        new_y_error = []
        for i in range(len(self.df)):
            s = self.df.iloc[i].to_numpy()
            new_y.append(float(self.regr_coefs[1])*s[0]+float(self.regr_coefs[5])*s[4])

        for i in range(len(self.df)):
            cur_y = 0
            cur_values = self.df.drop('Network Response Time', axis = 1).iloc[i].to_numpy()
            for j in range(len(cur_values)):
                cur_y += cur_values[j]*self.regr_coefs[j+1]
            cur_y +=self.regr_coefs[0]
            y_pred.append(cur_y)
            y_error.append(abs(self.df.iloc[i]['Network Response Time']-y_pred[i]))
            new_y_error.append(abs(self.df.iloc[i]['Network Response Time']-new_y[i]))
            y_inter.append(str([round(prediction.iloc[i]['mean_ci_lower'],3),round(prediction.iloc[i]['mean_ci_upper'],3)]))
        return y_pred, y_error, y_inter, new_y, new_y_error
            

    def get_regr_error(self):
        self.y_pred, y_error, y_inter, new_y, new_y_error = self.get_pred_and_error()
        data = {'Истинные значения целевого признака':self.df['Network Response Time'].to_numpy(),
         'Расчитанные значения Y (полн) ':self.y_pred, 'Расчитанные значения Y (сокр)': new_y, 'Абсолютная ошибка (полн)':y_error, 'Абсолютная ошибка (сокр)':new_y_error, 'Интервальная оценка Y':y_inter}
        return pd.DataFrame(data)
        

    
    def get_t_coefs(self):
        t_coefs = []
        for x in self.regr_coefs:
            t_coefs.append(x/np.std(self.regr_coefs))
        return np.array(t_coefs)

    def get_normal_analyze(self):
        data = {'Признак':[], 'Статистика':[], 'Значение p':[], 'Принадлежит нормальному распределению':[]}
        f_crit = 100.7486
        alpha = 0.05
        for column in self.df.columns:
            data['Признак'].append(column)
            stat, p = normaltest(self.df[column])
            data['Статистика'].append(stat)
            data['Значение p'].append(p)
            #print('Statistics = %.5f, p-value= %.5f' % (stat, p))
            if stat < f_crit:            
                if p < alpha:
                   data['Принадлежит нормальному распределению'].append('Принадлежит')
                else:
                    data['Принадлежит нормальному распределению'].append('Не принадлежит')
            else:
                    data['Принадлежит нормальному распределению'].append('Не принадлежит')
        return pd.DataFrame(data)

    def significance(self, df_corr):
        #print(df_corr.to_numpy())
        r = copy.deepcopy(df_corr.to_numpy())
        n = len(self.df)
        matrix = list(map(list,np.zeros((len(r),len(r[0])))))
        for i in range(len(r)):
            for j in range(len(r[i])):
                if i == j:
                    matrix[i][j] = '-'
                else:
                    matrix[i][j] = r[i][j] * np.sqrt((n-2)/(1 - r[i][j] ** 2))
        sign_df = pd.DataFrame(matrix, index=self.df.columns, columns=self.df.columns)        
        for column in sign_df.columns:
            sign_df[column] = sign_df[column].agg(UIFunctions.round_df)
        return sign_df

    def calculateR2(self):
        y_true = self.df['Network Response Time']
        X_train = self.df.drop('Network Response Time', axis = 1)

        y_pred = []
        for record in X_train.to_numpy():
            y_i = 0
            for i in range(len(record)):
                #print(record)
                y_i += record[i]*self.regr_coefs[i+1]
            y_i += self.regr_coefs[0]
            y_pred.append(y_i)
        record = np.array(record)        
        return r2_score(y_true, y_pred)

    def calculateR(self,R2):
        return math.sqrt(R2)
    
    def calculateF(self):
        R2 = self.calculateR2()
        n = len(self.df)
        m = len(self.df.columns)
        #print(n, m, R2)
        return R2/(1-R2)*(n-m-1)/m

    def get_regr_stats(self):
        return pd.DataFrame(np.array([self.calculateR(self.calculateR2()), self.calculateR2(), 1.666599658, self.calculateF(), 2.065, self.get_approximation_error()[0],self.get_approximation_error()[1]]), index=['Множественный R','R^2', 't крит', 'Критерий Фишера', 'F крит', 'Средняя ошибка аппроксимации (полн), %', 'Средняя ошибка аппроксимации (сокр), %'])