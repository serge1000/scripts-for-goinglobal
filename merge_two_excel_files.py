import csv

file2019 = 'D:/GG/Misc/MergeTwoExcelFiles/2019.CSV'
file2020 = 'D:/GG/Misc/MergeTwoExcelFiles/2020new.CSV'
resultfile = open('D:/GG/Misc/MergeTwoExcelFiles/Results2020new.CSV', 'w')

resultfile.write('Organization'+','+'Salesforce ID'+','+'Expire Date'+','+'GA Pageviews Adjusted'+','+'GA Total Visits Adjusted'+','+'GA Pages Session Adjusted'+','+'GA Avg Session Duration Adjusted'+','+'GA Avg Time on Page Adjusted'+','+''+','+'Organization'+','+'Salesforce ID'+','+'Expire Date'+','+'GA Pageviews Adjusted'+','+'GA Total Visits Adjusted'+','+'GA Pages Session Adjusted'+','+'GA Avg Session Duration Adjusted'+','+'GA Avg Time on Page Adjusted'+'\n')

with open(file2020) as fh_2020:
    rd_2020 = csv.DictReader(fh_2020, delimiter=',')
    for row_2020 in rd_2020:
        #*****************MAIN LOOP (2020)**********************
        flag=0
        #print(row_2020['Organization']+row_2020['Salesforce ID']+'-----\n')

        #********************** 2019 ***************************
        with open(file2019) as fh_2019:
            rd_2019 = csv.DictReader(fh_2019, delimiter=',')
            for row_2019 in rd_2019:
                #print(row_2019['Organization']+row_2019['Salesforce ID']+'-----\n')
                if row_2020['Organization']==row_2019['Organization']:
                    
                    orgname = row_2020['Organization']
                    if orgname.find(",")!=-1:
                        orgname = '"'+orgname+'"'
                        
                    resultfile.write(orgname+','+row_2020['Salesforce ID']+','+row_2020['Expire Date']+','+row_2020['GA Pageviews Adjusted']+','+row_2020['GA Total Visits Adjusted']+','+row_2020['GA Pages Session Adjusted']+','+row_2020['GA Avg Session Duration Adjusted']+','+row_2020['GA Avg Time on Page Adjusted']+','+''+','+orgname+','+row_2019['Salesforce ID']+','+row_2019['Expire Date']+','+row_2019['GA Pageviews Adjusted']+','+row_2019['GA Total Visits Adjusted']+','+row_2019['GA Pages Session Adjusted']+','+row_2019['GA Avg Session Duration Adjusted']+','+row_2019['GA Avg Time on Page Adjusted']+'\n')
                    flag=1
        fh_2019.close()
        #***************** END OF 2019 *************************
        if flag==0 :
            print(row_2020['Organization']+ row_2019['Organization']  +' - DOES NOT EXIST IN 2020'+'\n')
        #*****************END MAIN LOOP (2020)******************


fh_2020.close()

resultfile.close()





