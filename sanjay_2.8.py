import csv 
#----------------------------------------------------------------------
def get_desired_data(file_obj):
    """ Read a csv file and returns the desired format of the data,  
        List for each Company year and month in which the share price was highest    
    """  
      
    reader = csv.DictReader(file_obj, delimiter=',')
    results = []
    for row in reader:                             #each row is a dictionary 
        list = []
        list.append(row.pop('Year'))               #exclude year and month value for comparing the share price values
        list.append(row.pop('Month'))              #appending these values in list for desired output
        higest_share_price = max(map(int, row.values()))        
        [list.append(key) for key in row if int(row[key]) == higest_share_price]    #appending company name which have highest share price    
        results.append(list)
        print list       
    #for result in results: print '%s has highest share price in %s %s ' % (result[2], result[1], result[0])   # for old python versions 
    for result in results: print '{2} has highest share price in {1} {0} '.format(*result)                     # as per new format
#----------------------------------------------------------------------
if __name__ == "__main__":
    csv_path = "TB_data_dictionary_2014-07-09.csv"
    f_obj = open(csv_path, "rb")
    get_desired_data(f_obj)
