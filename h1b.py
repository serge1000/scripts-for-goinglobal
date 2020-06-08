import csv
import os
import sys


# Directory for H1B CSV files and h1b_import.conf
path = 'D:/GG/H1B/2020_March/script/'

"""
The configuration file (h1b_import.conf) maps fields from latest OFLC raw file  (i.e. BEGIN_DATE, END_DATE)
to list of fields required for import process(i.e. EMPLOYMENT_START_DATE, EMPLOYMENT_END_DATE).
On right side  we place fields from latest OFLC raw file.
"""

configfile = path+'h1b_import.conf'

# CSV file containing new H1B update
#inputfile = path+'FY2020_Q2_TEST.CSV'
inputfile = path+'FY2020_Q2_ORIG_CSV.CSV'

resultfile = open(path+'RES.CSV', 'w')

#read conf file

ConfDict={}

with open(configfile, 'r') as ll:
    for line in ll:
            lineforsplit = line.rstrip(os.linesep)
            res1 = lineforsplit.split('=')
            ConfDict[res1[0]]=res1[1]
    ll.close()

#count records in input file

recordcounter=0
with open(inputfile, 'r') as ll:
    for line in ll:
        recordcounter+=1
    ll.close()
print ('\n'+inputfile+' has '+str(recordcounter)+' records'+'\n')


#create result file with header

FirstField=True
for key in ConfDict:
    if not FirstField:
        resultfile.write(",")
    else:
        FirstField=False
    resultfile.write(key)        

#read input file and process each line,  field by field:
recordcounter = 0
counter50 = 1
print('\n')

with open(inputfile) as fh_input:

    rd_input = csv.DictReader(fh_input, delimiter=',')
    
    for row_input in rd_input:

        recordcounter+=1
        if recordcounter==counter50*50000:
            print(str(recordcounter)+' records processed\n')
            counter50 += 1
            
        resultfile.write('\n')
        FirstField=True
        
        #loop to write data to result file
        for key in ConfDict:
            if not FirstField:
                resultfile.write(",")
            else:
                FirstField=False
                
            #"EMPLOYER_ADDRESS=EMPLOYER_ADDRESS1" is special case.
            #The script compiles EMPLOYER_ADDRESS of two fields EMPLOYER_ADDRESS1 and EMPLOYER_ADDRESS2
            temp = row_input[ConfDict[key]]
            if key=='EMPLOYER_ADDRESS1':
                # if EMPLOYER_ADDRESS2 contains N/A, use  EMPLOYER_ADDRESS1 only
                if row_input['EMPLOYER_ADDRESS2']=='N/A':
                    temp = row_input['EMPLOYER_ADDRESS1']
                else:
                    temp = row_input['EMPLOYER_ADDRESS1']+' '+row_input['EMPLOYER_ADDRESS2']
                    
            #if  field contains comma , add quotes.
            if temp.find(",")!=-1:
                temp = '"'+temp+'"'
            resultfile.write(temp)                   
        
resultfile.close()

print('All processed\n')





