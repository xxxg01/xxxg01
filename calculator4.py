#!/usr/bin/env python3
import sys
import csv
import queue
from multiprocessing import Process,Queue

class Args(object):
    
    def __init__(self,args):
        self.args = args
    
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
                KEY, VALUE = line.split('=')
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
                    totalr = totalr + VALUE
        return jishul,jishuh,totalr

class UserData(Process):
    
    def __init__(self,_file,output_queue):
       self._file = _file
       self.output_q = output_queue


       super().__init__()



    def __parse(self):
       for line in open(self._file):
           employee_id,gongzi = line.split(',')
           yield(int(employee_id),int(gongzi))

    def run(self):
        for item in self.__parse():
            self.output_q.put(item)


class calculator(Process):
    tax_start = 3500

    tax_table = [
    (80000,0.45,13505),
    (55000,0.35,5505),
    (35000,0.30,2755),
    (9000,0.25,1005),
    (4500,0.20,555),
    (1500,0.10,105),
    (0,0.03,0),
    ] 

    def __init__(self,config,input_queue,out_queue):
        self.config = config
        self.input_q = input_queue
        self.output_q = out_queue
        super().__init__()


    def calculate(self,data_item):
        employee_id,gongzi = data_item
        tax = 0

        if gongzi < self.config.jishu_low:
            shebao = self.config.jinshu_low * self.config.total_rate
        elif gongzi > self.config.jishu_high:
            shebao = self.config.jishu_high * self.config.total_rate
        else:
            shebao = gongzi * self.config.total_rate

        left_gongzi = gongzi - shebao
      
        tax_gongzi = left_gongzi - self.tax_start

        if tax_gongzi < 0 :
            tax = 0
        else:
            for item in self.tax_table:
                if tax_gongzi > item[0]:
                    tax = tax_gongzi * item[1] - item[2]
                    break
        print(tax)
        last_gongzi = left_gongzi - tax
        return str(employee_id),str(gongzi),'{:.2f}'.format(shebao),'{:.2f}'.format(tax),'{:.2f}'.format(last_gongzi)

    def run(self):
        while True:
            try:
                item = self.input_q.get(timeout=1)
            except queue.Empty:
                return 
            result = self.calculate(item)
            self.output_q.put(result)


class Exporter(Process):
    def __init__(self,_file,input_queue):
        self._file = open(_file,'w')
        self.input_q = input_queue
        super().__init__()
    def export(self,item):
        line = ','.join(item) + '\n'
        self._file.write(line)



    def close(self):
        self._file.close()
    def run(self):
        while True:
            try:
                item = self.input_q.get(timeout=1)
            except queue.Empty:
                self.close()
                return
            self.export(item)


if __name__ == '__main__':
    args = Args(sys.argv[1:])

    config = Config(args.Return_Path('-c'))
    q1 = Queue()
    q2 = Queue()

    employee_data = UserData(args.Return_Path('-d'),q1)
    calculator = calculator(config,q1,q2)
    exporter = Exporter(args.Return_Path('-o'),q2)

    employee_data.start()
    calculator.start()
    exporter.start()

    employee_data.join()
    calculator.join()
    exporter.join()
