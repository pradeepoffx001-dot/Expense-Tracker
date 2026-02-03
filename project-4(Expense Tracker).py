expenses=[]
def create_category():
    amount=int(input('Amount 💰: '))
    category=input('Category (Food, Travel, Books, etc.): ')
    expense={'amount':amount,'category':category}
    expenses.append(expense)
    print('✔ Category created successfully')
def add_expence():
    category=input('Enter Category to add expense: ')
    cash=int(input('Enter you cash to add: '))
    for e in expenses:
        if e['category']==category:
            e['amount']+=cash
            print('✔ Amount added')
            print('your current expense in ',category,': ',e['amount'])
            return
    print('❌ Category not found')
def sub_expence():
    category=input('Enter Category to sub expense: ')
    cash=int(input('Enter you cash to sub: '))
    for e in expenses:
        if e['category']==category:
            if e['amount']>=cash:
                e['amount']-=cash
                print('✔ Amount subracted')
                print('your current expense in ',category,': ',e['amount'])
                return
    print('❌ Category not found')
def view_expenses():
    if not expenses:
        print('❌ no expense registored')
    else:
        print('\n--- Total Expense ---')
        for e in expenses:
            print('amount',e['amount'],'-','category',e['category'])
def search_category():
    category=input('Enter category to search ⌕: ')
    for e in expenses:
        if e['category']==category:
            print('Amount you spent in ',category,': ')
            print('amount',e['amount'])
            return
    print('❌ Category not found')
def delete_category():
    category=input('Enter Category to delete: ')
    for e in expenses:
        if e['category']==category:
            expenses.remove(e)
            print('✔ Category removed successfully')
            return
    print('❌ Category not found')
while True:
    print('\n--- Expense Tracker ---')
    print('1.Create Category')
    print('2.Add Expence')
    print('3.Sub Expence')
    print('4.View Expence')
    print('5.Search Category')
    print('6.Delete Category')
    print('7.Exit')
    choise=input('Enter Your Choise: ')
    if choise=='1':
        create_category()
    elif choise=='2':
        add_expence()
    elif choise=='3':
        sub_expence()
    elif choise=='4':
        view_expenses()
    elif choise=='5':
        search_category()
    elif choise=='6':
        delete_category()
    elif choise=='7':
        print('👋 Program closed')
        break
    else:
        print('❌ Invalid choice')
        
        

               
               
               
    
                   
    
