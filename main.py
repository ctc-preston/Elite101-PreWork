def age_introduction():
  if age < 18:
    print('Ah, I remember what it\'s like to be at that age.')
  elif age >= 18 and age < 55:
    print('I see, I always enjoyed being that old.')
  elif age >= 55 and age < 5000:
    print('Wow, it feels not so long ago I was that age.')
  elif age == 5000:
    print('Amazing! You and I are the same age!')
  else:
    print('You are older than me? I never knew that people could live for so long!')

def display_menu():
  print('Please select one of the following options:')
  print('1. Placeholder')
  print('2. Placeholder')
  print('3. Placeholder')
  print('4. Exit Conversation')

print('Hello! My name is Steve the chatbot!')
name = input('What is your name? ')
print()

print(f'Nice to meet you {name}!')
age = int(input('What is your age? '))
print()

age_introduction()
print()

print(f'Moving on, how can I help you today {name}?')

display_menu()
response = int(input())

if response == 1:
  print('Placeholder1')
elif response == 2:
  print('Placeholder2')
elif response == 3:
  print('Placeholder3')
elif response == 4:
  print('Very well, have a nice day!')
else:
  print('I am sorry but there is no option for your response.')
