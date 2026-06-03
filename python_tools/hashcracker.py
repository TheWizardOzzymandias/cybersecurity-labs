# import the hash library
import hashlib

# Introduction for the user
print("Welcome to HashCRACK!")

# Asks user for hash to be cracked
hash_input = input('Enter hash to be cracked: ').strip()

# Creates a list of algorithms based on the available ones from hashlib. sorts them
algorithms_list = sorted(list(hashlib.algorithms_available))

# Asks user for path to wordlist with potential passwords
wordlist_location = input('Enter wordlist file location: ').strip()

with open(wordlist_location, 'r', errors='ignore') as file:

	for line in file:
		candidate = line.strip()
		for current_hash in algorithms_list:
			hash_object = hashlib.new(current_hash)
			hash_object.update(candidate.strip().encode())

			if current_hash.startswith("shake"):
				result = hash_object.hexdigest(32)
			else:
				result = hash_object.hexdigest()
			if result == hash_input:
				print("Congradulations! Cleartext Password Found")
				print("Algorithm: ", current_hash)
				print("Password: ", candidate)
				exit(0)

print("No Password Found")
