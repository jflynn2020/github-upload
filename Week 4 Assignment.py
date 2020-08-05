# Week 4 Assignment
"""
Created on Mon Apr  6 09:59:14 2020

@author: mcblu
"""

def fidelity_sector_report(file1):
    with open('Sector Performance.htm') as f:
        file1 = f.readlines()
    from bs4 import BeautifulSoup
    SectorPerformanceResponse = BeautifulSoup("".join(file1), "lxml")
    table_tag = SectorPerformanceResponse.find('table',class_="sector-list")
    sectors_list = []
    for sector in table_tag.find_all('strong'):
        sectors_list.append(sector.get_text())
    useful_fundamentals_list = []
    useful_numbers_list = []
    inner_dict_list = []
    for i in sectors_list[0:11]:
        with open(i+'.htm') as f:
            file1 = f.readlines()
        from bs4 import BeautifulSoup
        CommunicationServicesResponse = BeautifulSoup("".join(file1), "lxml")
        sector_fundamentals = CommunicationServicesResponse.find('div',class_="sec-fundamentals")
        fundamentals_list = []
        for fundamental in sector_fundamentals.find_all('a'):
            fundamentals_list.append(fundamental.get_text())
        useful_fundamentals = [fundamentals_list[2], fundamentals_list[6], fundamentals_list[9]]
        useful_fundamentals_list.append(useful_fundamentals)
        numbers_list = []
        for number in sector_fundamentals.find_all('td'):
            numbers_list.append(number.get_text().strip())
        better_number = []
        for j in numbers_list:
            import re
            non_decimal = re.compile(r'[^\d.-]+')
            better_number.append(non_decimal.sub('', j))
        inner_dict = {'enterprise_value' : float(better_number[2]), 'return_on_equity' : float(better_number[6]), 'dividend_yield' : float(better_number[9])}
        inner_dict_list.append(inner_dict)
        useful_numbers = [float(better_number[2]), float(better_number[6]), float(better_number[9])]
        useful_numbers_list.append(useful_numbers)
    ref_json = {}
    for i in range (0, (len(sectors_list))):
        ref_json[sectors_list[i]] = inner_dict_list[i]
    return ref_json
    
    
# Getting keys for outer dictionary

table_tag = SectorPerformanceResponse.find('table',class_="sector-list")
sectors_list = []
for sector in table_tag.find_all('strong'):
    sectors_list.append(sector.get_text())
print(sectors_list)

# Getting keys for inner dictionary

sector_fundamentals = CommunicationServicesResponse.find('div',class_="sec-fundamentals")
fundamentals_list = []
for fundamental in sector_fundamentals.find_all('a'):
    fundamentals_list.append(fundamental.get_text())
useful_fundamentals = [fundamentals_list[2], fundamentals_list[6], fundamentals_list[9]]

# Getting values for inner dictionary

for i in sectors_list[0:11]:
    with open(i+'.htm') as f:
        file1 = f.readlines()
    from bs4 import BeautifulSoup
    CommunicationServicesResponse = BeautifulSoup("".join(file1), "lxml")
    sector_fundamentals = CommunicationServicesResponse.find('div',class_="sec-fundamentals")
    numbers_list = []
    for number in sector_fundamentals.find_all('td'):
        numbers_list.append(number.get_text().strip())
    better_number = []
    for j in numbers_list:
        import re
        non_decimal = re.compile(r'[^\d.-]+')
        better_number.append(non_decimal.sub('', j))
    inner_dict = {'enterprise_value' : better_number[2], 'return_on_equity' : better_number[6], 'dividend_yield' : better_number[9]}
        inner_dict_list.append(inner_dict)
        useful_numbers = [better_number[2], better_number[6], better_number[9]]
        useful_numbers_list.append(useful_numbers)
    print(inner_dict)

# How to compile dictionaries

a = ['Enterprise Value', 'Return on Equity (TTM)', 'Dividend Yield']
x2 = ['286.81', '15.82', '3.91']
dict1 = {}
for i in range (0, (len(a))):
    dict1[a[i]] = x2[i]
print(dict1)

b = ['Communication Services', 'Consumer Discretionary', 'Consumer Staples', 'Energy', 'Financials', 'Health Care', 'Industrials', 'Information Technology', 'Materials', 'Real Estate', 'Utilities']
dict2 = {}
for i in range (0, (len(b))):
    dict2[b[i]] = dict1
print(dict2)

c = ['$279.53B', '-293.98%', '2.32%']
d = []
for i in c:
    import re
    non_decimal = re.compile(r'[^\d.-]+')
    d.append(non_decimal.sub('', i))
print(d)


# For loop to run through all of the .htm pages and create the inner dictionary

for i in sectors_list[0:11]:
    with open(i+'.htm') as f:
        file1 = f.readlines()
    from bs4 import BeautifulSoup
    CommunicationServicesResponse = BeautifulSoup("".join(file1), "lxml")
    sector_fundamentals = CommunicationServicesResponse.find('div',class_="sec-fundamentals")
    fundamentals_list = []
    for fundamental in sector_fundamentals.find_all('a'):
        fundamentals_list.append(fundamental.get_text())
    useful_fundamentals = [fundamentals_list[2], fundamentals_list[6], fundamentals_list[9]]
    numbers_list = []
    for number in sector_fundamentals.find_all('td'):
        numbers_list.append(number.get_text().strip())
    better_number = []
    for j in numbers_list:
        import re
        non_decimal = re.compile(r'[^\d.-]+')
        better_number.append(non_decimal.sub('', j))
    useful_numbers = [better_number[2], better_number[6], better_number[9]]
    inner_dict = {}
    for k in range (len(useful_fundamentals)):
        inner_dict[useful_fundamentals[k]] = useful_numbers[k]
    print(inner_dict)

# Creation of outer dictionary

outer_dict = {}
for i in range (0, (len(sectors_list))):
    outer_dict[sectors_list[i]] = inner_dict
print(outer_dict)

### Practice

inner_dict_list = []
for k in range (0, (len(block))):
    for l in range (0, 3):
        value = [block[k][l], numbers_block[k][l]]
        inner_dict_list.append(value)
print(inner_dict_list)

inner_dict = {}
for i in range (0, (len(inner_dict_list))):
    inner_dict[inner_dict_list[i][0]] = inner_dict_list[i][1]
    inner_dict.update(inner_dict)
print(inner_dict)

dict4 = {}
dict4['results'] = dict2
print(dict4)

float_list = []
float_block = ['24.01', '27.97', '286.81', '9.99', '135.32', '17.33', '15.82', '10.22', '96.34', '3.91']
for i in range (0, (len(numbers_block))):
    for j in range (0, 3):
        value = float(numbers_block[i][j])
        float_list.append(value)
print(float_list)
    


block = [['Enterprise Value', 'Return on Equity (TTM)', 'Dividend Yield'], ['Enterprise Value', 'Return on Equity (TTM)', 'Dividend Yield'], ['Enterprise Value', 'Return on Equity (TTM)', 'Dividend Yield'], ['Enterprise Value', 'Return on Equity (TTM)', 'Dividend Yield'], ['Enterprise Value', 'Return on Equity (TTM)', 'Dividend Yield'], ['Enterprise Value', 'Return on Equity (TTM)', 'Dividend Yield'], ['Enterprise Value', 'Return on Equity (TTM)', 'Dividend Yield'], ['Enterprise Value', 'Return on Equity (TTM)', 'Dividend Yield'], ['Enterprise Value', 'Return on Equity (TTM)', 'Dividend Yield'], ['Enterprise Value', 'Return on Equity (TTM)', 'Dividend Yield'], ['Enterprise Value', 'Return on Equity (TTM)', 'Dividend Yield']]
numbers_block = [['286.81', '15.82', '3.91'], ['279.53', '-293.98', '2.32'], ['164.55', '-5.36', '2.75'], ['138.75', '14.43', '4.60'], ['155.26', '20.20', '3.43'], ['131.15', '-985.28', '2.36'], ['63.98', '-65.18', '2.11'], ['331.67', '28.22', '1.67'], ['53.49', '15.47', '3.00'], ['48.37', '25.46', '3.80'], ['57.48', '9.69', '3.81']]

dict = {block[0][0] : numbers_block[0][0]}




for i in range (0, (len(useful_numbers_list))):
    for j in range (0, 3):
        value = float(useful_numbers_list[i][j])
        float_list.append(value)
print(float_list)






