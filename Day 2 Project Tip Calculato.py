#Day 2 Project: Tip Calculato

print ("######################## Welcome to the tip calculator! ########################")

bill = float(input ("What was the total bills? R$"))
tip = int(input ("How much tip would you like to give ? 10, 12 or 15 ?"))
people = int(input("How many people to split the biil?"))

bill_with_tip = tip / 100 * bill + bill
bill_per_person = bill_with_tip / people
final_amount = round(bill_per_person,2)

print(f"Each person should be pay?: R$  {final_amount}")