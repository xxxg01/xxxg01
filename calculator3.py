
#!/usr/bin/env python3

import sys
import csv

class Args(object):
    
    def __init__(self):
        self.args = sys.argv[1:]
  
    def Return_Path(self,types_of):
        try:
            file_path = self.args[self.args.index(types_of)+1]
            value = file_path
        except ValueError:
            value = None
        return value

class Config(object):

    def __init__(self,File):
        self.jishu_low,self.jishu_high,self.total_rate = self._read_config(File)

    def _read_config(self,File):
        jishul = 0
        jishuh = 0
        totalr = 0
        with open(File) as f:
            for line in f:
                KEY,VALUE = line.split('=')
                KEY = KEY.strip()
                try:
                    VALUE = float(VALUE.strip())
                except ValueError:
                    continue
                if KEY == 'JiShuL':
                    jishul = VALUE
                elif KEY == 'JiShuH':
                    jishuh = VALUE
                else:
                    totalr += VALUE
        return jishul,jishuh,totalr
   
class UserData(object):

     def __init__(self,File):
         self.userdata = self._read_users_data(File)

     def _read_users_data(self,File):
         userdata = []
         with open(File) as f:
             for line in f:
                 name_id,gongzi = line.split(',')
                 userdata.append((int(name_id),int(gongzi)))
         return userdata


class IncomeTaxCalculator(object):
    
    tay_start = 3500

    
    Income_Tax_Payable = [
    (80000,0.45,13505),
    (55000,0.35,5505),
    (35000,0.30,2755),
    (9000,0.25,1005),
    (4500,0.20,555),
    (1500,0.10,105),
    (0,0.03,0),
    ]  

    def calc_for_all_userdata(self):
        Args_qd = Args()
        Config_qd = Config(Args_qd.Return_Path('-c'))
        UserData_qd = UserData(Args_qd.Return_Path('-d'))
        shebao = 0
        tax = 0
        tax_gongzi = 0
        last_gongzi = 0
        for user_gongzi in UserData_qd.userdata:
            if user_gongzi[1] < Config_qd.jishu_low:import sys
import csv

class Args(object):
    
    def __init__(self):
        self.args = sys.argv[1:]
  
    def Return_Path(self,types_of):
        try:
            file_path = self.args[self.args.index(types_of)+1]
            value = file_path
        except ValueError:
            value = None
        return value

class Config(object):

    def __init__(self,File):
        self.jishu_low,self.jishu_high,self.total_rate = self._read_config(File)

    def _read_config(self,File):
        jishul = 0
        jishuh = 0
        totalr = 0
        with open(File) as f:
            for line in f:
                KEY,VALUE = line.split('=')
                KEY = KEY.strip()
                try:
                    VALUE = float(VALUE.strip())
                except ValueError:
                    continue
                if KEY == 'JiShuL':
                    jishul = VALUE
                elif KEY == 'JiShuH':
                    jishuh = VALUE
                else:
                    totalr += VALUE
        return jishul,jishuh,totalr
   
class UserData(object):

     def __init__(self,File):
         self.userdata = self._read_users_data(File)

     def _read_users_data(self,File):
         userdata = []
         with open(File) as f:
             for line in f:
                 name_id,gongzi = line.split(',')
                 userdata.append((int(name_id),int(gongzi)))
         return userdata


class IncomeTaxCalculator(object):
    
    tay_start = 3500
    def __init__(self):
        self.Args_qd = Args()
    
    Income_Tax_Payable = [
    (80000,0.45,13505),
    (55000,0.35,5505),
    (35000,0.30,2755),
    (9000,0.25,1005),
    (4500,0.20,555),
    (1500,0.10,105),
    (0,0.03,0),
    ]  
    
    def calc_for_all_userdata(self):
        
        Config_qd = Config(self.Args_qd.Return_Path('-c'))
        UserData_qd = UserData(self.Args_qd.Return_Path('-d'))
        zh = []
        
        shebao = 0
        tax = 0
        tax_gongzi = 0
        last_gongzi = 0
        for user_gongzi in UserData_qd.userdata:
            if user_gongzi[1] < Config_qd.jishu_low:
                shebao = Config_qd.jishu_low * Config_qd.total_rate
                
            elif user_gongzi[1]  >Config_qd.jishu_high:
                shebao = Config_qd.jishu_high * Config_qd.total_rate
            else:
                shebao = user_gongzi[1] * Config_qd.total_rate
           
            tax =  user_gongzi[1] -shebao - self.tay_start
            for line in self.Income_Tax_Payable:
                if tax < 0:
                   tax_gongzi = 0
                   last_gongzi = user_gongzi[1] - shebao
                else:
                    if tax > line[0]:
                        tax_gongzi = tax * line[1] - line[2]
                        last_gongzi = user_gongzi[1] - tax_gongzi - shebao
                        break
            zh.append((user_gongzi[0],user_gongzi[1],format(shebao,".2f"),format(tax_gongzi,'.2f'),format(last_gongzi,'.2f')))
        return zh
    def export(self,default='csv'): 
        Storage = self.Args_qd.Return_Path('-o')
        result = self.calc_for_all_userdata()
        with open(Storage,'w') as f:
            writer = csv.writer(f)
            writer.writerows(result)     
if __name__ == '__main__':
    A = IncomeTaxCalculator()
    A.export()

                shebao = Config_qd.jishu_low * Config_qd.total_rate
                
            elif user_gongzi[1]  >Config_qd.jishu_high:
                shebao = Config_qd.jishu_high * Config_qd.total_rate
            else:
                shebao = user_gongzi[1] * Config_qd.total_rate
            print(shebao)
            tax = user_gongzi[1] -shebao - self.tay_start
            for line in self.Income_Tax_Payable:
                if tax < 0:
                   tax_gongzi = 0
                   last_gongzi = user_gongzi[1] - shebao
                else:
                    if tax > line[0]:
                        tax_gongzi = tax * line[1] - line[2]
                        last_gongzi = user_gongzi[1] - tax_gongzi - shebao
                        break
            print(user_gongzi[0],user_gongzi[1],shebao,tax_gongzi,last_gongzi)
           
                
if __name__ == '__main__':
    A = IncomeTaxCalculator()
    A.calc_for_all_userdata()
