# [Bases](https://play.picoctf.org/practice/challenge/67)

---

# 🔎 How to Check and Identify Base64 Text

---

## 1. **What is Base64?**

* Base64 is an **encoding scheme** that represents binary data (bytes) using only **64 printable characters**:

  ```
  A–Z, a–z, 0–9, +, /
  ```
* Sometimes `=` is used as **padding** at the end.

✅ Example:
Text `hello` in Base64 → `aGVsbG8=`

---

## 2. **Characteristics of Base64 Text**

When you see some suspicious text, here are the clues that it might be Base64:

1. **Allowed characters only**

   * Contains only:

     ```
     A–Z a–z 0–9 + / =
     ```
   * In URL-safe Base64, `+` and `/` are replaced by `-` and `_`.

   Example: `bDNhcm5fdGgzX3IwcDM1` contains only `a–z`, `0–9`, `_` → looks like Base64 (URL-safe variant).

---

2. **Length is a multiple of 4**

   * Base64 strings are usually **padded** so their length is divisible by 4.
   * Example: `bDNhcm5fdGgzX3IwcDM1` has 20 characters → divisible by 4 ✅

---

3. **Ends with `=` or `==` padding (optional)**

   * Many Base64 strings end with `=` or `==`.
   * Not mandatory in all cases, especially if padding was stripped.
   * Example: `aGVsbG8=` (hello) ends with `=`.

---

4. **Not human-readable**

   * If the string looks random (mixed case letters and numbers, maybe ending with `=`), but when decoded gives readable text, it’s likely Base64.

---

## 3. **How to Verify**

### ✅ Method 1: Use Linux `base64 -d`

```bash
echo "bDNhcm5fdGgzX3IwcDM1" | base64 -d
```

Output:

```
l3arn_th3_r0p35
```

👉 Decoded successfully = It is Base64.

---

### ✅ Method 2: Check with `file` command

```bash
echo "bDNhcm5fdGgzX3IwcDM1" | base64 -d | file -
```

If it says `ASCII text`, then the decoded content is plain text.
If it says `data` or `image`, then it was encoding something binary.

---

### ✅ Method 3: Online checkers

There are online Base64 validators where you paste the text, and it tells you if it’s valid Base64.

---

## 4. **Signs That It’s Not Base64**

* Contains characters outside the Base64 set (`$`, `%`, `@`, spaces, etc.).
* Length not divisible by 4 (unless padding was trimmed).
* Fails to decode (`base64 -d` gives error).

---

## 5. **Conclusion**

The string:

```
bDNhcm5fdGgzX3IwcDM1
```

✔ Contains only valid Base64 characters.
✔ Length = 20 (multiple of 4).
✔ Successfully decodes into `l3arn_th3_r0p35`.

👉 Therefore, it **is Base64-encoded text**.
