# Python Cybersecurity Tools

A collection of simple Python tools built while learning cybersecurity fundamentals through TryHackMe labs, CTFs, and hands-on scripting practice.

These scripts were created to better understand hashing, encoding, brute forcing, and automation workflows commonly encountered in cybersecurity exercises.

---

# Tools Included

## `hashgen.py`

Generates hashes using multiple hashing algorithms supported by Python's `hashlib` library.

### Features

* Supports multiple hashing algorithms
* Simple command-line usage
* Useful for understanding how hashes are generated
* Great for CTF practice and password storage concepts

### Example Usage

```bash
python3 hashgen.py
```

Example output:

```text
MD5: 5f4dcc3b5aa765d61d8327deb882cf99
SHA1: 5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8
SHA256: 5e884898da28047151d0e56f8dc6292773603d0d6aabbdd...
```

---

## `hashcracker.py`

Attempts to crack hashes using a wordlist-based attack.

### Features

* Supports common hash algorithms
* Reads hashes from user input
* Iterates through a wordlist and compares generated hashes
* Useful for understanding password cracking workflows

### Example Usage

```bash
python3 hashcracker.py
```

---

# Skills Practiced

* Python scripting
* Hashing algorithms
* Wordlist attacks
* Command-line workflows
* Cybersecurity automation concepts
* Debugging and problem solving

---

# Future Improvements

* Add command-line arguments with `argparse`
* Support hash detection automatically
* Add salting functionality
* Improve performance for larger wordlists
* Add logging and better output formatting

---

# Disclaimer

These tools were created strictly for educational purposes and authorized lab environments such as TryHackMe and CTF challenges.
