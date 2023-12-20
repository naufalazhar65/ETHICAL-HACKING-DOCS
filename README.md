# ETHICAL-HACKING-DOCS


## Information Gathering Methods:

```sh
  whois
  ```
- Gunakan whois untuk mendapatkan informasi domain dengan memasukkan nama domain
```sh
  whatweb -v
  ```
- Gunakan whatweb dengan opsi -v untuk mendapatkan informasi web secara rinci

<br>
<br>

## IP Scanning
```sh
  nslookup google.com
  ```
- Gunakan nslookup untuk mendapatkan informasi IP terkait dengan nama domain google.com
```sh
  ping  google.com -4
  ```
- Gunakan ping dengan opsi -4 untuk melakukan pengujian konektivitas ke alamat IP IPv4 dari google.com

<br>
<br>

## Saving Log Data Web:
```sh
  whatweb -v --log-file=namafile
  ```
<br>
<br>

## Email Hunter Methods (SOCIAL ENGINEERING):
- theHarvester
- Hunter.io

<br>
<br>

## Username Hunter:
```sh
  sherlock (python sherlock.py username)
  ```
<br>
<br>

## NMAP Scanning
### IP Range Scan & List Scan:
 ```sh
  sudo netdiscover -r (ip)
  ```
- Gunakan sudo netdiscover untuk melakukan pemindaian rentang dengan IP yang ditentukan
 ```sh
  nmap -Pn (ip address target)
  ```
- Gunakan nmap dengan opsi -Pn untuk melakukan pemindaian daftar pada alamat IP target yang ditentukan
- Catatan: Gunakan ini jika Windows memblokir permintaan ping
 ```sh
  nmap -iL (nama file)
  ```
  - Gunakan nmap dengan opsi -iL untuk melakukan pemindaian pada beberapa IP yang ditentukan dalam file yang diberikan
  - Contoh: nmap -iL targets.txt

<br>
<br>

## Vulnerability SECTION
### Vulnerability Analysis with Nmap (Group Scripts):
 ```sh
  sudo nmap --script auth ip_address_target -sS (find username & password info)
  ```
- Gunakan sudo nmap dengan opsi --script auth untuk mencari informasi username & password pada alamat IP target
- Gunakan -sS untuk melakukan Syn scan (direkomendasikan)
```sh
  sudo nmap --script malware ip_address_target -sS (check for malware or backdoor)
  ```
- Gunakan sudo nmap dengan opsi --script malware untuk memeriksa keberadaan malware atau backdoor pada alamat IP target
```sh
  sudo nmap --script banner ip_address_target -sS
  ```
- Gunakan sudo nmap dengan opsi --script banner untuk mendapatkan informasi banner pada alamat IP target

### Vulnerability Analysis with Nmap (Single Scripts):
```sh
  cd /usr/share/nmap/scripts
  ```
- Access target through anonymous FTP if vulnerable: 
  ```bash
  sudo nmap --script-help Vulnerability

<br>
<br>

## Via NESSUS
### Start Nessus
```sh
  sudo /bin/systemctl start nessusd.service
  ```
- Access Nessus: https://kali:8834/

<br>
<br>

## EXPLOITS SECTION
### To view Metasploit location in Linux:
```sh
  - cd /usr/share/metasploit-framework
  ```
### Modules :
- `exploits` - to exploit targets
- `nops` - to instruct the processor not to perform any operations, crucial during buffer overflows
- `payloads` - to control targets
- `post` - for persistence after exploitation, privilege escalation, and obtaining administrator access
<br>

## STEP BY STEP EXPLOITATION

1. Find open ports on the target using `portscanner.py`.
2. To see which exploits can be used to exploit `vsFTPd`, use the command `SEARCHSPLOIT`.
3. Next, open the `MSFCONSOLE` in `cd /usr/share/metasploit-framework`.
4. Search for an exploit that can be used to exploit `vsFTPd` using the command `search vsftpd 2.3.3`.
5. How to use the exploit is to use the command `USE 0` (can use the number in front).
6. How to find out information about the newly used exploit is to use the command `SHOW INFO`.
7. If `RHOST` is still empty, we must fill it in.
8. How to enter `RHOST (IP TARGET)` is to use the command `SET RHOSTS (IP TARGET)`.
9. To make sure it has been filled or not, use the command `SHOW OPTIONS`.
10. How to exploit the target machine is to use the command `EXPLOIT` / `RUN`.
11. To exit, use the command `EXIT`.

