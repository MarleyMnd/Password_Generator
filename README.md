# Password generator
---

_This program was developed using **Python 3.11**_

---
You can generate a password of chosen *length* and choose its *composition* (only numbers, letter and special characters, etc.).

Explanations about choosing the 'secrets' librairy instead of the 'random' one:

---

> Random librairy: ❌
If you generate an element on a computer previously used to generate another element, you have a small chance to get both the same elements. It **doesn't ensure the safety of the password** because teh "random" generation is based on the seed of the computer.
---

What's the difference with 'secrets' then?

---
> Secrets librairy: ✅
We can avoid this using the 'secrets' librairy. It **doesn't take into account the seed** of the computer to generate an element and thus, it ensures the safety of the generated password.



---

### How to run it?
You just have to make sure Python is installed on your computer and to run the 'main.py' file.
