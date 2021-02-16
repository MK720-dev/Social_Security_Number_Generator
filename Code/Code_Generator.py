from random import randint
from random import seed
from random import choice
from datetime import datetime
import pandas


# initiating the random numbers generator with the actual time
seed(datetime.now())

def Birth_Year(B_Year):
    # year in string form
    if (B_Year in range(0, 10)):
        B_YearS = f'0{B_Year}'
        return B_YearS
    elif (B_Year in range(50, 99)) or (B_Year in range(10, 22)):
        B_YearS = f'{B_Year}'
        return B_YearS

def Generate_Code(file):
    Commune_Codes = []
    List = [] #list where we store generated codes
    df = pandas.read_csv(file, delimiter='  ', index_col='Department_Code')
    for index , row in df.iterrows():
        if (row['Commune_Code'][:2] not in ['2A', '2B']):
            Commune_Codes.append(row['Commune_Code'])
    #Generating Code of 100 persons
    for x in range(100):
        #Gender
        Gender = str(randint(1 , 2))
        # year and month of birth:
        B_Year = randint(0, 100)
        B_YearS = Birth_Year(B_Year)
        #Generating years from 1950 to 2021 only
        while (B_YearS == None) :
            B_Year = randint(0, 100)
            B_YearS = Birth_Year(B_Year)
        #Birth Month
        B_Month =randint(1 , 12)
        #B_Month string form
        if (B_Month in range(1, 10)):
            B_MonthS = f'0{B_Month}'
        else:
            B_MonthS=f'{B_Month}'
        #Tha code of the Commune of birth
        B_Place = choice(Commune_Codes)
        #Last three digits of the NIR to differenciate people born in the same region and day
        Diff_digits = randint(0 , 1000)
        #String form
        if (Diff_digits in range(10)):
            Diff_digitsS=f'00{Diff_digits}'
        elif (Diff_digits in range(10 ,100)):
            Diff_digitsS=f'0{Diff_digits}'
        else :
            Diff_digitsS = f'{Diff_digits}'
        #First 13 digits : Numero d'inscription (NIR)
        NIR=''.join([Gender, B_MonthS ,B_YearS, B_Place, Diff_digitsS])
        #Social Sceurity Key
        Key=int(NIR)%97
        if (Key in range(0,10)):
            KeyS=f'0{Key}'
        else:
            KeyS=f'{Key}'
        # Social scurity's code string
        Sec_Code = NIR + KeyS
        List.append(Sec_Code)
    return List



"""if __name__=='__main__':
    List = Generate_Code('DataBase.txt')"""



