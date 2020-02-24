# errors are 3 types : Compile Error, Logical Error, RunTime Error
# code Statements are 2 types : Simple, Critical

a=int(input('ENter number here: '))
b=int(input('ENter number here: '))


try:
    print("Feature Open-->")
    print(a/b) #it is a critical statement

except ZeroDivisionError as error_msg: # when we know the error type , when 'ZeroDivisionError' error happens this block executed
    print( 'Done an error: ',error_msg)

except Exception as error_msg: # When we don't know the error type
    print('Unknown error type: ',error_msg)

finally: #-------------When we want to do an task without regarding an error
    print("Feature Close -->")

print('!!!!!!!!!!!!!!!      Good Bye Chuck      !!!!!!!!!!!!!!!!')