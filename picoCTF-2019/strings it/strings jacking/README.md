```bash
┌──(sumit㉿kali)-[~/Desktop/CTF]
└─$ strings -a -n 8 strings_jacking | egrep -i 'flag|FLAG|CTF|fwectf|flag\{|FLAG\{|ctf\{|fwectf\{|{.*}' || true 
fwectf{5tr1n65_30F_p4ss937_0011}
This is flag!
fwectf_strings_jacking.c
```
