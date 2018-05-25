import sys

def calculation(WAGE):
    STARTING_POINT = 3500
    Social_Insurance ={
    'pension':0.08,
    'medical':0.02,
    'unemployment':0.005,
    'lnjury':0,
    'mateenity':0,
    'provident_fund':0.06
    }

    Income_Tax_Payable = [
    (80000,0.45,13505),
    (55000,0.35,5505),
    (35000,0.30,2755),
    (9000,0.25,1005),
    (4500,0.20,555),
    (1500,0.10,105),
    (0,0.03,0),
    ]
    SI = WAGE * sum(Social_Insurance.values())
    YJ = WAGE - SI - STARTING_POINT
    for CN in Income_Tax_Payable:
        if YJ > CN[0]:
            PAYABLE = YJ * CN[1] - CN[2]
            
            WAGE = WAGE - SI - PAYABLE
            return format(WAGE,".2f")
        elif YJ < 0:
            WAGE = WAGE - SI
            return format(WAGE,".2f")
  
def main():
    for G_WAGE in sys.argv[1:]:
        ID_NUMBER,H_WAGE = G_WAGE.split(':')
        try:
            WAGE = int(H_WAGE)
            AFTER_TAX = calculation(WAGE)
            print(ID_NUMBER + ":" + AFTER_TAX)
        except ValueError:
            print("Parameter Error")

if __name__ == '__main__':
    main()
