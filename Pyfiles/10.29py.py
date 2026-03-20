date=input("Enter a date (DD/MM/YYYY):")
day,month,year=date.split('/')
month_names=["January","February","March","April","May","June","July","August","September","Ocrober","November","December"]
month_name=month_names[int(month)-1]
print(f"Formatted date:{month_name} {day}, {year}")













