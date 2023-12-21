## Information Gathering Methods:

```sh
  whois domain_name
  ```
- Gunakan whois untuk mendapatkan informasi domain dengan memasukkan nama domain
```sh
  whatweb -v domain_name
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

## Email Hunter Methods
- theHarvester
```sh
theHarvester -d domain_name -b all
  ```
- [Hunter.io](https://hunter.io/)


<br>
<br>

## Sherlock (Username Hunter)
```sh
cd /Users/naufalazhar/Documents/NAUFAL_AZHAR/HACKING/Hacking_tools/sherlock/sherlock
  ```
```sh
python3 sherlock.py username
  ```
<br>
<br>

## NMAP Scanning
### IP Range Scan & List Scan:
 ```sh
  sudo netdiscover -r ip_address
  ```
- Gunakan sudo netdiscover untuk melakukan pemindaian rentang dengan IP yang ditentukan
 ```sh
nmap -Pn ip_address
  ```
- Gunakan nmap dengan opsi -Pn untuk melakukan pemindaian daftar pada alamat IP target yang ditentukan
- Catatan: Gunakan ini jika Windows memblokir permintaan ping
 ```sh
nmap -iL file_name
  ```
  - Gunakan nmap dengan opsi -iL untuk melakukan pemindaian pada beberapa IP yang ditentukan dalam file yang diberikan
  - Contoh: nmap -iL targets.txt
```sh
nmap ip_address 0/24
  ```
<br>

### Syn Scan, TCP Connect Scan, UDP Scan:
- Syn scan
```sh
sudo nmap -sS ip_address_target
  ```
- TCP connect scan
```sh
sudo nmap -sT ip_address_target
  ```
<br>

### OS Detection Scanning (nmap):
```sh
sudo nmap -O ip_address_target
  ```
<br>

### Port Service Version Scanning (nmap):
```sh
sudo nmap -sV ip_address_target
  ```
- Lower intensity
```sh
sudo nmap -sV  —version-intensity 2 ip_address_target
  ```
```sh
sudo nmap -sV --version-all ip_address_target
  ```
- Lower intensity 
```sh
sudo nmap -sV --version-light ip_address_target
  ```
<br>
<br>

### Aggressive Scan (not recommended, too much noise):
```sh
sudo nmap -A ip_address_target
  ```
<br>

### Port Specification & Output Handling:
- select ports
```sh
sudo nmap -sS -p port1,port2,... ip_address_target
  ```
- all ports
```sh
sudo nmap -sS -p- ip_address_target
  ```
- top 100 ports
```sh
sudo nmap -sS -F ip_address_target
  ```
- save output logs
```sh
sudo nmap -sS -F ip_address_target >> nama_file.txt
  ```
- save log dan menampilkan output 
```sh
sudo nmap -sS -F -oN nama_file ip_address_target
  ```
- Lower intensity 
```sh
sudo nmap -sV  —version-intensity 2 ip_address_target
  ```

<br>
<br>

## Vulnerability SECTION
### Nmap Script (Group Script)
https://nmap.org/book/nse-usage.html
### Vulnerability Analysis with Nmap (Group Scripts):
 ```sh
  sudo nmap --script auth ip_address_target -sS
  ```
- Perintah sudo nmap --script auth ip_address_target -sS digunakan untuk melakukan pemindaian jaringan pada alamat IP tertentu dengan fokus pada deteksi otentikasi dan keamanan. Opsi -sS menunjukkan penggunaan pemindaian TCP SYN (half-open scan), sementara --script auth memaksa Nmap menggunakan skrip khusus untuk mengidentifikasi masalah otentikasi pada sistem target.

<img width="974" alt="Screenshot 2023-12-21 at 16 51 13" src="https://github.com/naufalazhar65/ETHICAL-HACKING-DOCS/assets/123730742/726c79c1-9e3c-4a6d-9888-2de0a56379b9">
Pada alamat IP 192.168.1.4, Nmap menemukan bahwa kredensial tomcat:tomcat adalah valid dan dapat digunakan untuk mengakses server web Apache Tomcat.
<br>
<br>
  
```sh
  sudo nmap --script malware ip_address_target -sS
  ```
- Perintah sudo nmap --script malware ip_address_target -sS digunakan untuk melakukan pemindaian jaringan pada alamat IP tertentu dengan fokus pada deteksi potensi malware.
<img width="947" alt="Screenshot 2023-12-21 at 16 55 31" src="https://github.com/naufalazhar65/ETHICAL-HACKING-DOCS/assets/123730742/3bd1b010-cdd3-4f0a-ac25-7261ffcff751">
<br>
<br>


```sh
  sudo nmap --script banner ip_address_target -sS
  ```
- Perintah sudo nmap --script banner ip_address_target -sS digunakan untuk melakukan pemindaian jaringan pada alamat IP tertentu dengan fokus pada deteksi dan pengekspos banner atau informasi servis pada port tertentu.
<img width="971" alt="Screenshot 2023-12-21 at 17 29 44" src="https://github.com/naufalazhar65/ETHICAL-HACKING-DOCS/assets/123730742/46786610-5ba4-41b8-9167-b85385e0a745">
<br>
<br>

### Vulnerability Analysis with Nmap (Single Scripts):
```sh
  cd /usr/share/nmap/scripts
  ```

  ```sh
  sudo nmap --script-help Vulnerability
  ```
- Access target through anonymous FTP if vulnerable:
  
  ```sh
  sudo nmap --script ftp-anon.nse ip_address -sS
  ```
<img width="537" alt="Screenshot 2023-12-21 at 17 45 17" src="https://github.com/naufalazhar65/ETHICAL-HACKING-DOCS/assets/123730742/ac186912-f06e-4389-8ab4-ad51ef13d24f">


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

1. Temukan port terbuka pada target menggunakan nmap `sudo nmap -sV ip_address_target`.
2. Untuk melihat exploit apa yang dapat digunakan untuk mengeksploitasi `vsFTPd`, gunakan perintah `searchsploit vsftpd 2.3.3`.
3. Selanjutnya, buka `MSFCONSOLE` di `cd /usr/share/metasploit-framework`.
4. Cari exploit yang dapat digunakan untuk mengeksploitasi `vsFTPd` menggunakan perintah `search vsftpd 2.3.3`.
5. Cara menggunakan exploit adalah dengan menggunakan perintah `USE 0` (bisa menggunakan nomor di depan).
6. Cara mengetahui informasi tentang exploit yang baru digunakan adalah dengan menggunakan perintah `SHOW INFO`.
7. Jika `RHOST` masih kosong, kita harus mengisinya.
8. Cara memasukkan `RHOST (IP TARGET)` adalah dengan menggunakan perintah `SET RHOSTS (IP TARGET)`.
9. Untuk memastikan apakah sudah terisi atau belum, gunakan perintah `SHOW OPTIONS`.
10. Cara mengeksploitasi mesin target adalah dengan menggunakan perintah `EXPLOIT` / `RUN`.
11. Untuk keluar, gunakan perintah `EXIT`.

