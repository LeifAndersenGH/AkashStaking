import math

# compound interest formula: A = P (1 + r/n)**(nt)
# r = annual interest rate   n = number of compounds per period (usually in months)    t = time

def Staking(principal, annualrate, numberoftimescompounded, years, monthlycontribution):
    
    print ("Initial Akash amount ", principal)
      
    annualrate = (int(annualrate))/100
    numberoftimescompounded = int(numberoftimescompounded)
    years = int(years)
    monthlycontribution = int(monthlycontribution)   
    
    preliminarynumber = (1 + (annualrate/numberoftimescompounded))
  
    raisedtopower = (numberoftimescompounded * years)

    
    compoundinterestplusprincipal = principal * (preliminarynumber**raisedtopower)
    
    print("The compound interest plus the principal is: ", compoundinterestplusprincipal)    
    
    oneplus = (1+(annualrate/numberoftimescompounded))
    raisedtopower2 = ((numberoftimescompounded*years))
    ratedividedbynumberoftimes = annualrate/numberoftimescompounded
    
    halfdone = (((oneplus**raisedtopower2)-1)/ratedividedbynumberoftimes)
    futurevaluewithdeposits = monthlycontribution*halfdone
    print ("Future value with deposits: ",futurevaluewithdeposits)
    
    totalamount = compoundinterestplusprincipal + futurevaluewithdeposits
    print ("Total Amount:", totalamount)    

Staking(420, 58, 365, 1, 0)






