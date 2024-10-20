# ДЗ 8.2. Паліандром SATOR AREPO TENET OPERA ROTAS
# Ваше завдання – написати функцію is_palindrome, яка перевірятиме, чи є рядок паліндромом.
# Паліндромом - це такий рядок, який читається однаково зліва направо і зправа наліво без урахування знаків пунктуації та розмірності букв.
# Функція приймає на вхід рядок, та повертає булеве значення True або False
# Приклад:
# def is_palindrome(text):
#     pass
# assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
# assert is_palindrome('0P') == False, 'Test2'
# assert is_palindrome('a.') == True, 'Test3'
# assert is_palindrome('aurora') == False, 'Test4'
# assert is_palindrome('SATOR AREPO TENET OPERA ROTAS') == True, 'Test5'
# print("ОК")
def is_palindrome(text):
   import string
   list_p=string.punctuation+" " #
   i=0
   my_string1=''
   for i in range(len(text)): #прибираємо знаки пунктуації та пробіли
       if text[i] in list_p: #якщо пробіл або знак пропускаємо
           i=i+1
       else:
           my_string1=my_string1+text[i] #складаємо букви в рядок
           i=i+1
   my_string1=my_string1.lower() #приводимо всі букви до нижнього регістру
   k=len(my_string1)//2 #знаходимо середину
   palindrom1=my_string1[:k] # зріз від 0 до середини
   palindrom2=my_string1[:k:-1] # зріз з кінця до середини
   if palindrom1 in palindrom2: # порівнюємо
       return True #якщо тотожні
   else:
       return False #якщо не тотожні

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
assert is_palindrome('SATOR AREPO TENET OPERA ROTAS') == True, 'Test5'
print("ОК")