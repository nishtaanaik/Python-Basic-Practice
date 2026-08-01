# TO store price of book,notebook and pen and calculate total bill, gst and final amount
Book=int(input("Enter the amount of book "))
Pen=int(input("Enter the amount of pen  "))
Notebook=int(input("Enter the amount of notebook "))

Total= Book+Pen+Notebook
Gst = Total * 18/100
Final = Total + Gst
print(f"Total:{Total}")
print(f"Gst:{Gst}")
print(f"Final:{Final}")