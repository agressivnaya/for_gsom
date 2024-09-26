print ('Hello, stranger!')
name = input ('What is your name? ')
print ('Hi,', name, '\nPlease, read this, meditate and understand:')
import this

accept = input ('Do you accept Zen of Python? (Y or N) ')
if accept == 'Y':
    bool_accept = True
else:
    bool_accept = False

if bool_accept == 1:
    print ('Congrats,', name, '! You may get to work')
else:
    print ('Sorry, go home')