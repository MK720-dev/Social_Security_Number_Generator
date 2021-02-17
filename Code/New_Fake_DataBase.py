import Code_Generator
from random import choice
import pandas
import csv


#Searching for well_known and the most used surnames and names in France
def Name_Surname(file1 , file2):
    df1 = pandas.read_csv(file1 , delimiter = ',' ,index_col='patronyme', encoding='iso-8859-1')
    df2= pandas.read_csv(file2, delimiter=',',index_col='prenom', encoding='iso-8859-1')
    Name =[]
    Surname = []
    for index , row in df1.iterrows():
        if (int(row['count']) > 1000):
            Surname.append((index))
    for index , row  in df2.iterrows():
        if (int(row['sum']) > 1000):
            Name.append(index)

    return Surname, Name

#Function to generate the fake database from the list of fake social sec codes
def Generate_DataBase(List ,file ,Surname, Name ):
    df = pandas.read_csv(file , delimiter='  ', index_col='Department_Code', encoding='iso-8859-1')
    #Creating a list for the different data
    Month = ['January', 'February', 'Mars', 'April', 'May', 'June', 'July', 'August', 'September', 'October' , 'November', 'December' ]
    Gender= []
    MB= []
    YB= []
    BD= []
    BC= []
    Name_List = []    #final name list to be used in the fake database not to be confused with Name list
    Surname_List = [] #final surname list to be used in the fake database not to be confused with Surname List
    Email = []
    for x in range(len(List)):
        if int(List[x][0]) == 1 :
            Gender.append('man')
        else:
            Gender.append('women')
        MB.append(Month[int(List[x][1:3])-1])
        if int(List[x][3:5]) in range(0 , 10):
            YB.append(f'200{int(List[x][3:5])}')
        elif int(List[x][3:5]) in range(10 , 22):
            YB.append(f'20{int(List[x][3:5])}')
        elif int(List[x][3:5]) in range(50 , 100):
            YB.append(f'19{int(List[x][3:5])}')
        for index , row in df.iterrows():
            if (List[x][5:10] == row['Commune_Code']):
                BD.append(row['Department_Name'])
                BC.append(row['Commune_Name'])
        BName = choice(Name)  #Name of the person
        BSurname = choice(Surname) #Surname of the person
        Name_List.append(BName)
        Surname_List.append(BSurname)
        Email.append(BSurname+'.'+BName+'@gmail.com')
        print(BName+' ' + BSurname+ ' '+ Gender[x] +' ' + MB[x]+' ' +YB[x] +' ' + BD[x] +' ' + BC[x] +'\n' )
    #Zipping different lists into a single data list for all citizens with social security code
    Data= zip(Name_List,Surname_List, Gender, MB, YB, BD, BC,Email)
    Data_List = list(Data)
    return Data_List

#Creating a csv file containing the fake database
def Create_csv (List):
    Headers = ['Name', 'Surname','Gender', 'Month of Birth', 'Year of Birth', 'Birth Department', 'Birth Commune','Email']
    with open('Social_Sec_DataBase.csv' , 'a') as SDB :
        file_writer = csv.writer(SDB, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        file_writer.writerow(Headers)
        for x in range(len(List)):
            file_writer.writerow(List[x])
    with open('Social_Sec_DataBase.csv', 'r') as SDB:
        file_reader = csv.reader(SDB, delimiter=',', quotechar='|')
        for row in file_reader:
            print(row)
            print('\n')





if __name__=='__main__':
    # Calling the Generate_Code function from another file in the projec
    Code_List = Code_Generator.Generate_Code('DataBase.txt') #Generating fake codes
    print(Code_List)
    Surname, Name = Name_Surname('patronymes.csv','prenom.csv')  #Generating lists of most used names and surnames
    Data_List= Generate_DataBase(Code_List, 'DataBase.txt', Surname , Name) #Generating the final Database
    Create_csv(Data_List) #Creating a csv file for the DataBase
