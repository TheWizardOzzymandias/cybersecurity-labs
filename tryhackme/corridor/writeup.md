# Corridor CTF Walkthrough

## Overview

This room focused on identifying insecure use of hashed identifiers within a web application.

The application used MD5 hashes of sequential integers to represent room identifiers. By reversing the pattern and enumerating additional values, it was possible to access a hidden page containing the flag.

## Tools Used

* Nmap
* Browser Developer Tools
* hashid
* John the Ripper
* md5sum

---

## Initial Enumeration

I began with a basic service scan against the target machine:

```bash
nmap -sCV <target_ip>
```

The scan did not reveal anything particularly useful, so I moved to manual web enumeration.

When visiting the webpage, it initially appeared to simply display an image of a hallway. After interacting with the page, I discovered that the doors were clickable.

Clicking different doors changed the URL to paths containing hash-like values.

Example:

```text
http://<target>/<hash>
```

This suggested the application was using hashed identifiers for each room.

---

## Hash Analysis

The room hints suggested an IDOR-style vulnerability involving hashing.

While inspecting the page source using browser developer tools, I noticed that multiple room hashes were exposed within the HTML map section.

I copied the hashes into a text file:

```bash
nano hash.txt
```

I then identified the hash type using `hashid`, which indicated the hashes were MD5.

---

## Cracking the Hashes

To determine what values the hashes represented, I used John the Ripper:

```bash
john --format=raw-md5 --wordlist=/usr/share/wordlists/rockyou.txt hash.txt
```

After cracking completed, I displayed the results:

```bash
john --show --format=Raw-MD5 hash.txt
```

The hashes corresponded to sequential integers:

```text
1
2
3
...
13
```

This revealed that the application was simply hashing predictable numeric identifiers.

---

## Enumerating Additional Values

Since the visible rooms only covered values `1-13`, I tested adjacent numbers.

First, I generated an MD5 hash for `14`:

```bash
echo -n "14" | md5sum
```

The resulting page did not exist.

I then generated a hash for `0`:

```bash
echo -n "0" | md5sum
```

Navigating to the resulting hash revealed the flag.

---

## Key Takeaways

* MD5 should not be used as a security mechanism for hiding resources.
* Predictable identifiers can often be enumerated.
* Hidden application functionality may exist outside the visible UI.
* Browser developer tools can expose valuable information during web assessments.
* Sequential resource enumeration is an important web exploitation technique.
