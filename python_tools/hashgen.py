# import the hashlib library
import hashlib

# Introduction for the user
print("Welcome to HashGEN!")

# Input String to be hashed
print("Please Provide Your String To Be Hashed")
plaintext = input()

# Generates a SET of hashing algorithms available from Hashlib. Set is the standard output
algorithms_set = hashlib.algorithms_available

# Sorts Algorithms from the above set and places them in a sorted list so we can index for a loop
algorithms_list = sorted(list(algorithms_set))

print("Congradulations! Here Are Your Hashes Sorted By Algorithm:")

# Use a for loop to iterate through the lists of hashes

for index, current_hash in enumerate(algorithms_list):

# Hash the user input string for the current interated hash

	hash_object = hashlib.new(current_hash)
	hash_object.update(plaintext.encode())

# Transform into hexadecmial output using hexdigest function. Conditional statement required for "shake" algorithms as they require a specified length, currently set at 32

	if current_hash.startswith("shake"):
		result = hash_object.hexdigest(32)
	else:
		result = hash_object.hexdigest()

	print(current_hash,result)
