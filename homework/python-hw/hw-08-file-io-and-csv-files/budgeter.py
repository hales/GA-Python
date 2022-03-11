import csv
from csv import DictWriter

DATA_FILE = 'data.csv'
FIELDNAMES = ['date', 'transaction', 'amount', 'note']

def load_entries():
  pass

def view_previous_entries(entries):
  my_file = open(DATA_FILE)
  my_reader = csv.DictReader(my_file)
  for row in my_reader:
    print(row['date'], row['transaction'],"$" +row['amount'], row['note'])
  my_file.close()

def display_profit_loss(entries):
  total_income = 0
  total_expense = 0
  my_file = open(DATA_FILE)
  my_reader = csv.DictReader(my_file)
  for row in my_reader:
    if (row['transaction'] == 'Income'):
      total_income += int(row['amount'])
    elif (row['transaction'] == 'Expense'):
      total_expense += int(row['amount'])
  profit = total_income - total_expense
  print(f'The total income is ${total_income} \nThe total expenses are ${total_expense} \nThe current profit is ${profit}')
  my_file.close()

def add_new_entry(entries):
  # Date of transaction. Must be YYYY-MM-DD: 2021-01-03
  date_syntax_correct = False
  while date_syntax_correct == False:
    transaction_date = input("Date of transation (YYYY-MM-DD): ")
    if len(transaction_date) == 10 and transaction_date.count('-') == 2:
      date_syntax_correct = True
    else:
      print("Error! Please provide date as YYYY-MM-DD")
  # Transaction Details: Income or Expense
  transaction_answer = 'Nothing'
  while (transaction_answer != 'Y') and (transaction_answer != 'N'):
    transaction_answer = input("Was this Income (Y/N): ")
    if (transaction_answer == 'Y'):
      transaction_type = 'Income'
    elif (transaction_answer == 'N'):
      transaction_type = 'Expense'
    else:
      print("Error! Answer was not Y or N")
  #Amount: 25. Must be integer
  amount_syntax_correct = False
  while (amount_syntax_correct == False):
    transaction_amount = input("Amount: ")
    try:
      int(transaction_amount)
      amount_syntax_correct = True
    except ValueError:
      print("Error! Not an Integer")
      amount_syntax_correct = False

  #Describe the transaction: Sales
  transaction_description = input("Describe the transaction: ")

  # open in write mode
  my_file = open(DATA_FILE, 'a')
  my_writer = csv.DictWriter(my_file, fieldnames=FIELDNAMES)

  dict1 = {'date': transaction_date, 'transaction': transaction_type, 'amount': transaction_amount, 'note': transaction_description}
  my_writer.writerow(dict1)
  my_file.close()

  

# =====================================================
# ======    Do Not Modify Anything Below Here    ======
# =====================================================

def show_menu():
  print('\nWhat would you like to do?\n')
  print('1) View previous entries')
  print('2) Display the current profit/loss')
  print('3) Add a new entry')
  print('4) Quit\n')

def get_menu_choice():
  choice = None
  
  while choice == None:
    try:
      choice = int(input('> '))
    except ValueError:
      print('That was not a valid number, please try again!')
      continue

    if choice < 1 or choice > 4:
      print('That was not a valid choice, please try again!')
      choice = None

  return choice

def main():
  print('====================')
  print('Welcome to Budgeter!')
  print('====================')

  entries = load_entries()

  while True:
    show_menu()
    menu_choice = get_menu_choice()

    if menu_choice == 1:
      view_previous_entries(entries)
    elif menu_choice == 2:
      display_profit_loss(entries)
    elif menu_choice == 3:
      add_new_entry(entries)
    elif menu_choice == 4:
      print('\nGoodbye!\n\n')
      break

main()