import csv

dates = []
monthly_change = 0
total_months = 0
total_profit = 0
previous_profit = 0
new_value = 0
average_change = 0  
profit_change = 0
great_inc = ["", 0]
great_dec = ["",99999999999999999]


#open file_path
file = r'PyBank\budget_data.csv'
#open file in read mode
with open (file, 'r') as csv_file:
    csvreader = csv.reader(csv_file, delimiter=',')
    header = next(csvreader)
    
    for row in csvreader:
        dates.append(row[0])    
        value = int(row[1])
        total_profit += value
        if previous_profit != 0:
            profit_change = value - previous_profit
            monthly_change += profit_change
            new_value +=1
            if profit_change > great_inc[1]:
                great_inc = [row[0], profit_change]
            if profit_change < great_dec[1]:
                great_dec = [row[0], profit_change]
        previous_profit = value
       
total_months = len(dates)
if new_value > 0:
    average_change = monthly_change / new_value
else:
    average_change = 0
        

        
#print statement
print('Financial Analysis')
print('-------------------------')
print(f'Total Months: {total_months}')
print(f'Total Profit: {total_profit}')
print(f'Average Change: {average_change}')
print(f'Greatest Increase: {great_inc}')
print(f'Greatest Decrease: {great_dec}')

file_path = r'PyBank\Analysis_Folder\PyBankAnalysist.txt'
with open(file_path, 'w') as output:
    output.write('Financial Analysis\n')
    output.write('-------------------------\n')
    output.write(f'Total Months: {total_months}\n')         
    output.write(f'Total Profit: {total_profit}\n')
    output.write(f'Average Change: {average_change}\n')
    output.write(f'Greatest Increase: {great_inc}\n')
    output.write(f'Greatest Decrease: {great_dec}\n')