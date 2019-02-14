#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#phone book directory

dct_phonebook = {}
print('Hello')
def phoneBookDir():
    print('PhoneBookDirectory')
    print('1.Add')
    print('2.Update')
    print('3.Delete')
    print('4.Search')
    print('5.View')
    print('6.Exit')
    int_choice = input('Enter your choice: ')
    if int(int_choice) == 1: #ADD
        str_name = input('Enter name:')
        if str_name in dct_phonebook.keys():
            print('Duplicate entry!!!')
            phoneBookDir()
        else:
            int_number = input('Enter phone number:')
            if int_number in dct_phonebook.values():
                print('Duplicate entry!!!')
                phoneBookDir()
            else:
                dct_phonebook[str_name] = int_number
                dct_phonebook.update(dct_phonebook)
                print('Added Successfully')
    if int(int_choice) == 3: #DELETE
        print('1.Delete by name')
        print('2.del by num')
        int_choice_delete = input('Enter 1 or 2')
        if int(int_choice_delete) == 1:
            str_name_delete = input('Enter name to delete:')
            if str_name_delete in dct_phonebook.keys():
                dct_phonebook.pop(str_name_delete)
                print('Deleted successfully')
            else:
                print('Data not found')
                phoneBookDir()
        elif int(int_choice_delete) == 2:
            int_number_delete = input('Enter number to delete')
            for name, number in dct_phonebook.items():
                if int_number_delete == number:
                    dct_phonebook.pop(name)
                    print('Deleted successfully')
                    break
            else:
                print('Data not found1')
        else:
            print('Invalid option')
            
    if int(int_choice) == 5: #VIEW
        for name, number in dct_phonebook.items():
            print(name, '\t', number)
    if int(int_choice) == 6: #EXIT
        exit()
    phoneBookDir()
phoneBookDir()


# In[ ]:





# In[ ]:




