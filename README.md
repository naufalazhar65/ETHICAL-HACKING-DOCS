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
  whatweb domain_name -v --log-file=namafile
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
  sudo nmap --script auth ip_address_target -sS
  ```
- Gunakan sudo nmap dengan opsi --script auth untuk mencari informasi username & password pada alamat IP target
- Gunakan -sS untuk melakukan Syn scan (direkomendasikan)
```sh
  sudo nmap --script malware ip_address_target -sS
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
  cd /usr/share/metasploit-framework
  ```
### Modules :
- `exploits` - untuk mengeksploitasi target
- `nops` - untuk memberi instruksi kepada prosesor agar tidak melakukan operasi apa pun, penting selama buffer overflows
- `payloads` - untuk mengontrol target
- `post` - untuk ketahanan setelah eksploitasi, eskalasi hak privilage, dan memperoleh akses administrator
<br>

## STEP BY STEP EXPLOITATION `Metasploit Framework`
Langkah-langkah ini secara umum mencakup pencarian kelemahan (vulnerabilities) pada sistem target dan eksploitasi kelemahan tersebut menggunakan alat seperti Metasploit Framework. Metode ini umumnya digunakan oleh peneliti keamanan atau profesional keamanan informasi untuk mengidentifikasi dan memperbaiki kelemahan yang mungkin dapat dieksploitasi oleh penyerang. Ini penting dalam memastikan bahwa sistem dan jaringan memiliki tingkat keamanan yang tinggi terhadap potensi ancaman.

1. Temukan port terbuka pada target menggunakan `portscanner.py`.
2. Untuk melihat exploit apa yang dapat digunakan untuk mengeksploitasi `vsFTPd`, gunakan perintah `SEARCHSPLOIT`.
3. Selanjutnya, buka `MSFCONSOLE` di `cd /usr/share/metasploit-framework`.
4. Cari exploit yang dapat digunakan untuk mengeksploitasi `vsFTPd` menggunakan perintah `search vsftpd 2.3.3`.
5. Cara menggunakan exploit adalah dengan menggunakan perintah `USE 0` (bisa menggunakan nomor di depan).
6. Cara mengetahui informasi tentang exploit yang baru digunakan adalah dengan menggunakan perintah `SHOW INFO`.
7. Jika `RHOST` masih kosong, kita harus mengisinya.
8. Cara memasukkan `RHOST (IP TARGET)` adalah dengan menggunakan perintah `SET RHOSTS (IP TARGET)`.
9. Untuk memastikan apakah sudah terisi atau belum, gunakan perintah `SHOW OPTIONS`.
10. Cara mengeksploitasi mesin target adalah dengan menggunakan perintah `EXPLOIT` / `RUN`.
11. Untuk keluar, gunakan perintah `EXIT`.

