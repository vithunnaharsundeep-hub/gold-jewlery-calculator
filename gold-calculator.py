customer = input("Enter Customer Name: ")
num = input("Enter Gold Rate per gram: ")
weight = input("Enter weight of gold in grams: ")
bgst = float(num) * float(weight)
gst = bgst * 0.03
total = bgst + gst
print("Jewelry") 
print("Customer Name: ", customer)
print("Gold Rate per gram: ", num)
print("Weight of gold in grams: ", weight)
print("Basic Gold Price: ", bgst)
print("GST: ", gst)
print("Total Amount: ", total)



