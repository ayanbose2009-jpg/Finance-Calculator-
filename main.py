l=[]
d={}
decision="y"
count=1
k=[]

import database

while decision=="y":
    decision=input("Do you wish to continue with today's expense? (y/n)")

    if decision=="y":
        date=input("Enter date of expenditures: ")
        priceComp=input("Enter Reason and amount(space seperated):- ")
        l=priceComp.split()

#sum of expenditure       
        for i in range(0,len(l)-1,2):
            d[l[i]]=int(l[i+1])
            
        print(d)
        where_s=list(d.keys())
        amt=list(d.values())
        
        TotalExpense=sum(d.values())
        print("TotalExpense: ",TotalExpense)



#maximum expenditure
        maxi=max(d.values())
        for i in range(len(l)):
            if l[i]==str(maxi):
                count+=1
                if count>1:
                    k.append(i)

                    for o in k:
                        j=int(o)-1
                        max_keyval={l[j]:maxi}

                else:
                    j=l.index(i)-1

                    max_keyval={l[j]:maxi}

                print("Maximum Expenditure: ",max_keyval)

                
#loan feature
        loan="y"
        while loan=="y":
            loan=input("Did you take any loan? (y/n)")
            if loan=="y":
                datel=input("Enter date of Loan taken")
                print("Please mention Transaction details:-")
                loanw=input("Enter loan (Lender:amount:reason):- ")
                loan_lst=loanw.split(":")
                print(loan_lst)
                lender=loan_lst[0]
                cost=loan_lst[1]
                why=loan_lst[2]

                database.var_push_loans(datel,lender,cost,why)

            else:
                print("No more loans taken :)")   
        d.clear()
    
        database.var_push_expense(date,where_s,amt)

    else:
        print("Thank you for your time")


    