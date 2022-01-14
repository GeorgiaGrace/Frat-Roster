"""Creator: Daniel Lopez
   Created: January 12 2022
   Function: Will read an Excel and take an inputted major and output brothers in inputted major"""


import pandas as pd

path = 'Alpha Sig Brothers Majors.xlsx'

# Initial reading of the excel file and creating into dictionary
def createlists():
    data = pd.read_excel(path)
    dataDict = data.to_dict('info')
    return dataDict

# searches through dictionary for desired major. if desired major brother info is saved and appended into list.
def majorfinder(major):

    data = createlists()
    info = []
    brothers = len(data)
    for i in range(0, brothers):

        element = data[i]
        if element.get('Major') == major:
            info.append(element)

    return info


def output(info, major):
    print(major, 'Majors', '\n')
    for i in range(len(info)):
        print('Brother: ', info[i].get('Name'), ',', info[i].get('Year'))

# gathering info
# pathname = 'Alpha Sig Brothers Majors.xlsx'
# major = input('Enter Major: ')


# # calling functions
# data = createlists(pathname)
# info = majorfinder(major)
# output(info)
