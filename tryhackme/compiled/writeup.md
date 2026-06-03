# Compiled CTF

This room focused on basic binary analysis and reverse engineering of a compiled executable.

## Initial Enumeration

I first located the task files on the virtual machine and used the `file` command to identify the binary type:

```bash
file Compiled/Compiled
```

This revealed that the file was an ELF executable.

Next, I used the `strings` command to inspect readable text within the binary:

```bash
strings Compiled/Compiled
```

While this exposed some interesting strings, it was not enough to fully determine the password logic.

---

# Static Analysis with Ghidra

After some research, I learned that tools such as Ghidra can decompile binaries and help perform static analysis.

I opened the executable in Ghidra and found the following relevant section of decompiled code:

```c
undefined8 main(void)
{
    int iVar1;
    char local_28[32];

    fwrite("Password: ", 1, 10, stdout);
    __isoc99_scanf("DoYouEven%sCTF", local_28);

    iVar1 = strcmp(local_28, "__dso_handle");
    if ((-1 < iVar1) && (iVar1 = strcmp(local_28, "__dso_handle"), iVar1 < 1)) {
        printf("Try again!");
        return 0;
    }

    iVar1 = strcmp(local_28, "_init");
    if (iVar1 == 0) {
        printf("Correct!");
    } else {
        printf("Try again!");
    }

    return 0;
}
```

---

# Interpreting the Code

The program first prompts the user for input with:

```c
fwrite("Password: ", 1, 10, stdout);
```

It then reads user input using:

```c
__isoc99_scanf("DoYouEven%sCTF", local_28);
```

## Understanding `scanf`

`scanf` is a standard C library function used to read formatted input from the keyboard.

In this case:

```c
"DoYouEven%sCTF"
```

means the program expects input in the format:

```text
DoYouEven<user_input>CTF
```

The `%s` stores the middle portion of the input into the variable:

```c
local_28
```

---

# Password Validation Logic

The program then compares `local_28` against two strings using `strcmp`.

## First Comparison

```c
iVar1 = strcmp(local_28, "__dso_handle");
```

If the input exactly matches:

```text
__dso_handle
```

the program immediately prints:

```text
Try again!
```

and exits.

---

## Second Comparison

Next, the program checks:

```c
iVar1 = strcmp(local_28, "_init");

if (iVar1 == 0) {
    printf("Correct!");
}
```

`strcmp` returns `0` when both strings are identical.

Therefore, the correct value for:

```text
local_28
```

must be:

```text
_init
```

---

# Constructing the Password

Since the program expects input in the format:

```text
DoYouEven%sCTF
```

and `%s` must equal:

```text
_init
```

the final password becomes:

```text
DoYouEven_initCTF
```

Entering this results in the program printing:

```text
Correct!
```

---

# Takeaways

* Basic reverse engineering can often be performed through static analysis without running the program.
* Tools like Ghidra are extremely useful for viewing decompiled source code and understanding program logic.
* Understanding fundamental coding concepts such as:

  * `scanf`
  * `strcmp`
  * variables
  * conditional statements

  can make binary analysis much easier.
* Researching unfamiliar functions while working through a challenge is a powerful way to build programming knowledge alongside cybersecurity skills.
