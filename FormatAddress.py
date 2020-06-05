def format_address(company_name, address):
    result = ''
    # divide address by comma delimiter and traverse through segments
    for segment in address.split(', '):
        # add each segment to result variable creating a comma and new line at end of each
        result += segment + ',' + '\n'
    # format the result by adding company name and replacing newline and comma with period
    return f'{company_name},\n{result[:-2]}.'


# open file to write
file = open('address.txt', 'w')
# insert result from format_address
file.write(format_address(input('Company Name: '), input('Address: ')))
file.close()

# keeps dialog box open
input('the file has been completed')
