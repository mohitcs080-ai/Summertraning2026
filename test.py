pan_numbers = ["ABCDE1234F", "PQRSX5678K", "ABCDE1234F", "LMNOP9876Q","LMNOP9876Q"]

if len(pan_numbers) != len(set(pan_numbers)):
    print("⚠️ Duplicate PAN numbers found in upload sheet!") 
    duplicates = [pan for pan in set(pan_numbers) if pan_numbers.count(pan) > 1]
    print(duplicates)
    
    installed_apps = {"PhonePe", "GPay", "Paytm", "BHIM"}
recommended_apps = {"GPay", "Paytm", "AmazonPay", "CRED"}

only_one_has = installed_apps ^ recommended_apps
print(only_one_has)   # {'PhonePe', 'BHIM', 'AmazonPay', 'CRED'}


express_stops = {"Mathura", "Agra", "Gwalior", "Bhopal", "Nagpur"}
passenger_stops = {"Mathura", "Agra", "Gwalior"}

print(passenger_stops.issubset(express_stops))   # True — express covers all passenger stops

# frozenset
ALLOWED_CENTRES = frozenset({"Centre-10", "Centre-15", "Centre-22"})
# frozenset prevents accidental modification — good for constants in exam software

def validate_centre(code):
    return code in ALLOWED_CENTRES

print(validate_centre("Centre-10")) # True
print(validate_centre("Centre-1"))