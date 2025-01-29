def read_number_from_file(file_path):
	with open(file_path, 'r') as file:
		number = file.read().strip()
		return int(number)

def assign_output(params):
	outputNumber = read_number_from_file('source_output.txt')
	return outputNumber
	
	
if __name__ == "__main__":
	print(assign_output(None))