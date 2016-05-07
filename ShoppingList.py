shopping_list_items = ['eggs', 'milk', 'cheese', 'apricots']

print shopping_list_items

def shopping_list():
	item = raw_input("What would you like to add to the list?").lower()
	if item in shopping_list_items:
		print "You already have that listed."
	else:
		shopping_list_items.append(item)
	
def alphabetize_list():
	return shopping_list_items.sort()
	print shopping_list_items
	
def remove_from_list():
	itemtoremove = raw_input("What would you like to remove?").lower()
	if itemtoremove not in shopping_list_items:
		print "This item isn't in your list"
	else:
		shopping_list_items.remove(itemtoremove)

shopping_list()
alphabetize_list()
remove_from_list()

for x in shopping_list_items:
	print x

if __name__ == '__shopping_list__':
	shopping_list()