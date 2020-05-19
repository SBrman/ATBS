#! python3

''' readCensusExcel.py - Tabulates population and number of census tracts for
each county.'''

import openpyxl, pprint

print('Opening workbook...')
wb = openpyxl.load_workbook(r'H:\python\files\Chapter 13\censuspopdata.xlsx')
sheet = wb.active

countyData = {}

for row in range(2, sheet.max_row+1):
    state = sheet['B'+str(row)].value
    county = sheet['C'+str(row)].value
    pop = sheet['D'+str(row)].value

    '''countyData = {'State_1': {'county_1': {'tracts': x, 'pop': 'y'},
                                 'county_2': {'tracts': x, 'pop': 'y'}},
                                 
                     'State_2': {'county_1': {'tracts': x, 'pop': 'y'},
                                 'county_2': {'tracts': x, 'pop': 'y'}},

                      ...}'''

    # Make sure the key for this state exists 
    countyData.setdefault(state,{})
    # Make sure the key and value for county in this state exists
    countyData[state].setdefault(county, {'Tracts': 0, 'Pop': 0})

    #countyData[state] = {county: {'Tracts': ,'Pop': pop}}

    countyData[state][county]['Tracts'] += 1
    countyData[state][county]['Pop'] += int(pop)


file = open(r'H:\python\files\Chapter 13\census2010.py','w')
file.write('countyData = ' + pprint.pformat(countyData))
file.close()
