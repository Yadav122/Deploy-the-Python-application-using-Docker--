# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
# print('Program to sum two numbers')
# num1=int(input('Enter the first no= '))
# num2=int(input('Enter the second no= '))
# result = num1+num2
#
# print(f'The sum of= {result}')

# user_name = input("Enter your name to store in file or enter to proceed: ")
# if user_name:
#     with open('user_info.txt', 'a') as file:
#         file.write(user_name+ "\n")
# show_info = input("Do you want to see all user names? y/n: ")
# if show_info == 'y':
#     try:
#         # with open('user_info','r') as file:
#         with open('user_info.txt', 'r') as file:
#             content = file.readlines()
#     except Exception as e:
#         print(e, type(e) )
#     else:
#         for line in content:
#          print(f'{line.rstrip()}')
try:
   with open('servers.txt', 'r') as file:
    content=file.readlines()
except Exception as e:
     print(e, type(e))

else:
   for line in content:
      print(f'{line.rstrip()}')