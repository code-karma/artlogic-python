  
  # Run file as python stock_number_challenge.py (if in the directory)

example_artwork_data = [
	{
		'stock_number': '', 
		'title': 'Untitled (Florence) 1', 
		'id': 456, 
		'artist': 'Flora Brooke'
	},
	{'stock_number': '', 'title': 'Untitled (Florence) 10', 'id': 465, 'artist': 'Flora Violet Brooke'},
	{'stock_number': '', 'title': 'Untitled (Florence) 11', 'id': 466, 'artist': 'Flora Violet Brooke'},
	{'stock_number': '', 'title': 'Untitled (Florence) 12', 'id': 467, 'artist': 'Flora Violet Brooke'},
	{'stock_number': '003', 'title': 'Untitled (Florence) 2', 'id': 457, 'artist': 'Flora Violet Brooke'},
	{'stock_number': '', 'title': 'Untitled (Florence) 3', 'id': 458, 'artist': 'Flora Violet Brooke'},
	{'stock_number': '', 'title': 'Untitled (Florence) 4', 'id': 459, 'artist': 'Flora Violet Brooke'},
	{'stock_number': '', 'title': 'Untitled (Florence) 5', 'id': 460, 'artist': 'Flora Violet Brooke'},
	{'stock_number': '', 'title': 'Untitled (Florence) 6', 'id': 461, 'artist': 'Flora Violet Brooke'},
	{'stock_number': '', 'title': 'Untitled (Florence) 7', 'id': 462, 'artist': 'Flora Violet Brooke'},
	{'stock_number': '', 'title': 'Untitled (Florence) 8', 'id': 463, 'artist': ''},
	{'stock_number': '', 'title': 'Untitled (Florence) 9', 'id': 464, 'artist': ''},
	{'stock_number': 'KAD 0002', 'title': 'Dubai Construction Workers 1', 'id': 448, 'artist': 'Kadeem Darzi'},
	{'stock_number': 'KAD 001', 'title': 'Dubai Construction Workers 2', 'id': 447, 'artist': 'Kadeem Darzi'},
	{'stock_number': '', 'title': 'Dubai Construction Workers 3', 'id': 449, 'artist': 'Kadeem Darzi'},
	{'stock_number': '', 'title': 'Dubai Construction Workers 4', 'id': 450, 'artist': 'Kadeem Darzi'},
	{'stock_number': '', 'title': 'Dubai Construction Workers 5', 'id': 451, 'artist': 'Kadeem Darzi'},
	{'stock_number': 'KDA', 'title': 'Dubai Construction Workers 6', 'id': 452, 'artist': 'Kadeem Darzi'},
	{'stock_number': '', 'title': 'Dubai Construction Workers 7', 'id': 453, 'artist': 'Kadeem Darzi'},
	{'stock_number': '', 'title': 'Dubai Construction Workers 8', 'id': 454, 'artist': 'Kadeem Darzi'},
	{'stock_number': 'DOO 003', 'title': 'Untitled', 'id': 621, 'artist': 'Katherine Dooley'},
	{'stock_number': 'DOO 004', 'title': 'Untitled', 'id': 622, 'artist': 'Katherine Dooley'},
	{'stock_number': '', 'title': 'Dubai Construction Workers 9', 'id': 455, 'artist':''},
	{'stock_number': '', 'title': 'Pastoral Scene', 'id': 468, 'artist': 'Thomas Dedrick'},
	{'stock_number': '', 'title': 'Pastoral Scene', 'id': 470, 'artist': 'Thomas Dedrick'},
	{'stock_number': '', 'title': 'Pastoral Scene', 'id': 471, 'artist': 'Thomas Dedrick'},
	{'stock_number': '', 'title': 'Stormy Seas', 'id': 469, 'artist': 'Thomas Dedrick'},
	{'stock_number': '', 'title': 'Lady Cynthia Stephenson', 'id': 472, 'artist': 'Charles Eggins'},
	{'stock_number': '', 'title': 'Pongo and Westie', 'id': 473, 'artist': 'Charles Eggins'},
	{'stock_number': '', 'title': 'Rover', 'id': 474, 'artist': 'Charles Eggins'},
	{'stock_number': 'BL 001', 'title': 'Energy and serenity 1', 'id': 440, 'artist': 'Blake Ellery'},
	{'stock_number': 'BLA 004', 'title': 'Energy and serenity 2', 'id': 441, 'artist': 'Blake Ellery'},
	{'stock_number': '', 'title': 'Energy and serenity 3', 'id': 442, 'artist': 'Blake Ellery'},
	{'stock_number': '', 'title': 'Energy and serenity 4', 'id': 443, 'artist': 'Blake Ellery'},
	{'stock_number': 'BLA 004', 'title': 'Energy and serenity 5', 'id': 444, 'artist': 'Blake Ellery'},
	{'stock_number': 'BLA 004', 'title': 'Energy and serenity 5', 'id': 444, 'artist': 'Blake Ellery'},
	{'stock_number': '', 'title': 'Energy and serenity 6', 'id': 445, 'artist': 'Blake Ellery'},
	{'stock_number': '', 'title': 'Energy and serenity 7', 'id': 446, 'artist': 'Blake Ellery'},
	{'stock_number': '', 'title': 'Relief 39', 'id': 281, 'artist': 'Yuming Han'},
	{'stock_number': 'Y', 'title': 'Rust 1', 'id': 283, 'artist': 'Yuming Han'},
	{'stock_number': '', 'title': 'Rust 2', 'id': 284, 'artist': 'Yuming Han'},
	{'stock_number': 'ABC 022', 'title': 'Pineapple ', 'id': 285, 'artist': 'Banksy'},
]
# Check if stock_number is not empty and has a number (Task-1)
def not_empty_has_numbers(inputStr):
    if inputStr != '':
        return any(char.isdigit() for char in inputStr)
    else:
        return False

# split stock_number by delimiter (Task1)
def pull_stock_number_by_space(inputStr):
    split = stock_number.split(" ")
    count = 0
    for part in split:
          if  part.isdigit():
              print('Digits found' + ': ' + part)
              return part
              count += 1
    # Edge case:          
    if count == 0:
        return False
        
# Get initials (prefix) and add number or fallback (Task-1 and Task-2)
def get_prefix_and_number_or_fallback(inputStr, inputInt):
    # Edge Case
    if not inputStr or not inputInt:
        return False
    # Get first characters from string (artist)
    initials = [ s[0] for s in inputStr.split() ]
    print('Initials processed:')
    print(initials)
    if len(initials) == 2:
        print('Initials OK')
        return initials[0] + initials[1] + ' ' + inputInt
    elif len(initials) == 1:
        print('Initials Fallback - Repeat letter for prefix')
        return initials[0] + initials[0] + ' ' + inputInt 
    elif len(initials) > 2:
        print('Initials Fallback - Use 1st and last')
        return initials[0] + initials[2] + ' ' + inputInt
    else:
        print('No Name')
        return False

# Checks for duplicate and adds /1+ if found (Task-1)
def check_uniqness_of_new_stock_number_and_return(stock_str,stock_list):
    i = 1
    matching = [s for s in stock_list if stock_str + "/" in s]
    print('MATCHING Duplicates: ')
    print(matching)
    # if the list is empty (first item), return stock_number
    if not stock_list:
        return stock_str
    # increment number if already a duplicate (x+1)
    elif matching:
        splitStr = matching[-1].split("/",1)
        i = int(splitStr[1]) + 1
        return splitStr[0] + '/' + str(i)
    # New duplicate, add (1)
    elif stock_str in stock_list:
        # new duplicate
        return stock_str + '/' + str(i)
    # stock number is unique
    else:
        return stock_str

# Increment initials if duplicated (Task-2)        
def increment_initials_with_number(result, last_prefix, n):
    if n == 1:
        return result + str(1)
    else:
        return last_prefix
 
 # Generating artwork number incrementing for each artwork per artist using count (Task-2)      
def generate_unique_number_per_artist_per_stock(item, names_list, unique_prefixes_list, last_prefix):
    n = 1
    artist = item.get('artist')
    if artist: print(artist)
    artist_in_name_list = artist in names_list
    if names_list and artist_in_name_list:
        n = names_list.count(artist)
    number = "{:03d}".format(n)
    print('Number processed: ' + str(number))
    result = get_prefix_and_number_or_fallback(artist, number)
    if unique_prefixes_list and result and result.split(" ",1)[0] in unique_prefixes_list:
        new_result = increment_initials_with_number(result.split(" ",1)[0], last_prefix, n)
        return new_result + ' ' + result.split(" ",1)[1]
    else:
        return result
    

# Print the results
stock_numbers_list = []
print('========TASK 1================')
for item in example_artwork_data:
    stock_number = item.get('stock_number')
    artist = item.get('artist')
    # Take only entries with Stock Number
    if not_empty_has_numbers(stock_number):
      print('\n')
      print(stock_number + ' ' + artist)
      print('-------')
      number = pull_stock_number_by_space(stock_number)  
      new_stock_number = get_prefix_and_number_or_fallback(artist, number)
      unique_stock_number = check_uniqness_of_new_stock_number_and_return(new_stock_number, stock_numbers_list)
      stock_numbers_list.append(unique_stock_number)
      print(stock_numbers_list)
      print('New Stock Number Created: ' + new_stock_number)
      print('New Stock Number Created (unique): ' + unique_stock_number)
      print('\n')
print('============END Task 1================')
print('\n')


print('========TASK 2================')
print('\n')
names_list = []
unique_prefixes_list = []
last_prefix = ''
for item in example_artwork_data:
    artist = item.get('artist')
    names_list.append(artist)
    result = generate_unique_number_per_artist_per_stock(item, names_list, unique_prefixes_list, last_prefix)
    if result: last_prefix = result.split(" ",1)[0]
    if last_prefix not in unique_prefixes_list:
        unique_prefixes_list.append(last_prefix)
    if not result:
        print('Artist field is empty!')
    # print(unique_prefixes_list)
    if result: print('Stock Number: ' + result)
    print('\n')
    
print('===========END')
    
    
      



      
      
      
      
      
      