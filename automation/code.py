from os import closerange
import re

# Send phone numbers to phone_numbers.txt file
# Send emails to emails.txt file

### ------ READ THE FILE ------ ###

with open("assets/potential-contacts.txt", 'r') as file:
    contents = file.read()

### ------ PHONE NUMBERS ------ ###

# // variables holding results of regex searches //
nums1 = re.findall(r"[1-9]\d{2}-\d{3}-\d{4}", contents) # xxx-yyy-zzzz
nums2 = re.findall(r"\(\d{3}\)\d{3}-\d{4}", contents) # (xxx)yyy-zzzz
nums3 = re.findall(r"\d{3}-\d{4}", contents) # yyy-zzzz <-- this one has duplicates from other results


# // append 10-digit phone numbers to 10-digit list, removing dups //
ten_digit_list = []
for i in nums1:
    if i not in ten_digit_list:
        ten_digit_list.append(i)

# // remove parenthesis and add a dash, append to 10-digit list, removing dups //    
for i in nums2:
    i = i.replace('(', '').replace(')', '-')
    if i not in ten_digit_list:
        ten_digit_list.append(i)

# // strip 10-digit list down to last 7 digits of all phone numbers for comparing //
last_seven = []
for i in ten_digit_list:
    last_seven.append(i[-8:])

# // check 7 digit search results against stripped 10-digit results and remove duplicates from results //
for i in last_seven:
    if i in nums3:
        nums3.remove(i)

# // add area codes to remaining 7-digit numbers //
added_area_codes = ["206-"+str(i) for i in nums3]

# // add the lists together into one master list //
master_list = []
for i in ten_digit_list:
    if i not in master_list:
        master_list.append(i)
for i in added_area_codes:
    if i not in master_list:
        master_list.append(i)

# // sort phone numbers in ascending order //
SORTED_PHONE_NUMS = sorted(master_list)

phone_list = ''
for i in SORTED_PHONE_NUMS:
    phone_list += i + '\n'

with open('assets/phone_numbers.txt', 'w+') as phone_file:
    phone_file.write(phone_list)

### ------ FIND EMAILS ------ ###
rule = r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+"
emails = re.findall(rule, contents)

# emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", contents)
ascending_emails = sorted(emails)
EMAIL_DUPS_REMOVED = set(ascending_emails) # emails with duplicates removed in ascending order
# print("Dups removed, ascending order, ", len(DUPS_REMOVED))

email_list = ''
for i in EMAIL_DUPS_REMOVED:
    email_list += i + '\n'

with open('assets/emails.txt', 'w+') as email_file:
    email_file.write(email_list)



