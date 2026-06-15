name, total = "Михаил", 3499.9

separator = "-" * 30


letter_var_1 = f"Здравствуйте, {name}!\n"  \
    f"Ваш счёт к оплате: {total} {chr(8381)}\n" \
    f"{separator}\n" \
    "Прошу оплатить сегодня" \

letter_var_2 = (
    f"Здравствуйте, {name}!\n"  
    f"Ваш счёт к оплате: {total:.2f} {chr(8381)}\n" 
    f"{separator}\n" 
    "Прошу оплатить сегодня" 
)
    

print(letter_var_2)