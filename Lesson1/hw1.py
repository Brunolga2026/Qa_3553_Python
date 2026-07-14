def print_string_reverse(s):
    if s is None or s.strip() == "":
        print("Wrong string")
        return
    reversed_s = s[::-1]
    print(reversed_s)

print_string_reverse("Shalom")
print_string_reverse(None)
print_string_reverse("")
print_string_reverse(" ")

#************************************

def is_isr_phone_number(phone):
    if phone is None or phone.strip() ==:
        return None
    if len(phone)!=10:
        return False
    if phone[0]!="0":
        return False
    if not phone.isdigit():
        return False
    return True

print(is_isr_phone_number("0521234567"))
print()
print(is_isr_phone_number("52358879"))
pr
