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
================================================================================================

## Vulnerability SECTION

### Vulnerability Analysis with Nmap (Group Scripts):
[Usage and Examples](https://nmap.org/book/nse-usage.html)

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

================================================================================================

## Via NESSUS
### INSTALLATIONS
1. [Nessus Download](https://www.tenable.com/downloads/nessus?loginAttempted=true)
2. Select your version
3. Download.
4. cd (file download directory)
5. `sudo dpkg -i Nessus-10.6.4-debian10_amd64.deb`
6. You can `start` Nessus Scanner by typing `sudo /bin/systemctl start nessusd.service`
7. You can `stop` Nessus Scanner by typing `sudo /bin/systemctl stop nessusd.service`
8. Access Nessus: https://kali:8834/

[Nessus Download](https://www.tenable.com/downloads/nessus?loginAttempted=true)
### EXAMPLE :
<img width="1400" alt="Screenshot 2023-12-22 at 14 14 49" src="https://github.com/naufalazhar65/ETHICAL-HACKING-DOCS/assets/123730742/8746ad5d-1e99-4be6-99af-2a36c6524153">


<br>
<br>

================================================================================================

## EXPLOITS SECTION `Metasploit Framework`
### To view Metasploit location in Linux:

```sh
  cd /usr/share/metasploit-framework
  ```
```sh
  cd /usr/share/metasploit-framework/modules
  ```
### Modules :
- `exploits`
    - Modul ini digunakan untuk mengeksploitasi kerentanan keamanan pada suatu sistem.
    - Contoh: `exploit/windows/smb/ms08_067_netapi`
      
- `nops`
    - Nops (No Operations) adalah instruksi atau serangkaian instruksi yang tidak melakukan operasi apapun. Modul ini digunakan untuk memasukkan nops sled di antara payload dan shellcode.
    - Contoh: `nops/linux/x86/mov`
      
- `payloads`
    - Payload adalah kode yang dieksekusi setelah eksploitasi berhasil. Modul payload menentukan apa yang akan dilakukan setelah keberhasilan eksploitasi.
    - Contoh: `windows/meterpreter/reverse_tcp`
      
- `post`
    - Modul ini digunakan setelah berhasil melakukan eksploitasi untuk mengekstrak informasi tambahan dari sistem target.
    - Contoh: `post/windows/gather/enum_logged_on_users`

- `encoders`
    - Modul ini digunakan untuk mengubah payload sehingga dapat menghindari deteksi oleh perangkat lunak keamanan.
    - Contoh: `encoder/x86/alpha_mixed`
- `evasion`
    - Modul ini membantu dalam menghindari deteksi oleh alat keamanan dan perangkat lunak antivirus.
    - Contoh: `evasion/windows/disable_defender`

- `auxiliary`
    - Modul ini memberikan fungsionalitas tambahan yang dapat membantu dalam pengumpulan informasi, pemindaian, atau eksploitasi non-invasif.
    - Contoh: `auxiliary/scanner/http/http_version`

<br>

================================================================================================

## STEP BY STEP EXPLOITATION `vsftpd 2.3.4` Metasploit-framework
Langkah-langkah ini secara umum mencakup pencarian kelemahan (vulnerabilities) pada sistem target dan eksploitasi kelemahan tersebut menggunakan alat seperti Metasploit Framework. Metode ini umumnya digunakan oleh peneliti keamanan atau profesional keamanan informasi untuk mengidentifikasi dan memperbaiki kelemahan yang mungkin dapat dieksploitasi oleh penyerang. Ini penting dalam memastikan bahwa sistem dan jaringan memiliki tingkat keamanan yang tinggi terhadap potensi ancaman.

1. Temukan port terbuka pada target menggunakan nmap `sudo nmap -sV ip_address_target`.
    - sebagai contoh disini saya akan mencoba mengekspolit port 21 yaitu `vsFTPd 2.3.4`
2. Untuk melihat exploit apa yang dapat digunakan untuk mengeksploitasi `vsFTPd`, gunakan perintah `searchsploit vsftpd 2.3.4`.
   - <img width="450" alt="Screenshot 2023-12-22 at 12 32 05" src="https://github.com/naufalazhar65/ETHICAL-HACKING-DOCS/assets/123730742/2872fcef-a89c-44f4-8a81-292c6ef67e0f">

3. Selanjutnya, buka `MSFCONSOLE` untuk membuka Metasploit.
    - <img width="350" alt="Screenshot 2023-12-22 at 17 50 47" src="https://github.com/naufalazhar65/ETHICAL-HACKING-DOCS/assets/123730742/54695667-4e87-4ec2-9974-1ef268c5e864">

4. Cari exploit yang dapat digunakan untuk mengeksploitasi `vsFTPd` menggunakan perintah `search vsftpd 2.3.4`.
    - <img width="450" alt="Screenshot 2023-12-22 at 17 59 37" src="https://github.com/naufalazhar65/ETHICAL-HACKING-DOCS/assets/123730742/b5ee22e7-a81d-444b-8dd2-865126699078">

5. Cara menggunakan exploit adalah dengan menggunakan perintah `use 0` (bisa menggunakan nomor di depan).
   - <img width="490" alt="Screenshot 2023-12-22 at 18 06 38" src="https://github.com/naufalazhar65/ETHICAL-HACKING-DOCS/assets/123730742/9b6ba305-5bb1-4afa-b70c-70d894ab760b">

6. Cara mengetahui informasi tentang exploit yang baru digunakan adalah dengan menggunakan perintah `show info`.
   - <img width="450" alt="Screenshot 2023-12-22 at 18 09 52" src="https://github.com/naufalazhar65/ETHICAL-HACKING-DOCS/assets/123730742/58916478-3864-439f-bb11-022735a7dd0e">

7. Jika `RHOST` masih kosong, kita harus mengisinya.
8. Cara memasukkan `RHOST (IP TARGET)` adalah dengan menggunakan perintah `set RHOSTS ip_addres_target`.
    - <img width="450" alt="Screenshot 2023-12-22 at 18 13 54" src="https://github.com/naufalazhar65/ETHICAL-HACKING-DOCS/assets/123730742/944e24ed-ad09-42fb-81a7-d5d6c4f673f6">

9. Untuk memastikan apakah sudah terisi atau belum, gunakan perintah `SHOW OPTIONS`.
10. Cara mengeksploitasi mesin target adalah dengan menggunakan perintah `EXPLOIT` / `RUN`.
    - <img width="450" alt="Screenshot 2023-12-22 at 18 18 23" src="https://github.com/naufalazhar65/ETHICAL-HACKING-DOCS/assets/123730742/4e88b2fd-4576-440f-987c-bc7a2ec1323a">

11. Untuk keluar, gunakan perintah `EXIT`.

<br>
================================================================================================

## STEP BY STEP EXPLOITATION `Telnet`

Eksploitasi pada port 23, yang merupakan port standar untuk layanan Telnet, dapat berbahaya karena Telnet mengirim informasi, termasuk kata sandi, dalam bentuk teks biasa tanpa enkripsi. Telnet adalah protokol lama dan tidak aman yang digunakan untuk mengakses dan mengelola perangkat jarak jauh. Seiring waktu, Telnet telah digantikan oleh protokol yang lebih aman seperti SSH.

1. Gunakan perintah `telnet ip_address`
  - <img width="450" alt="Screenshot 2023-12-22 at 19 51 09" src="https://github.com/naufalazhar65/ETHICAL-HACKING-DOCS/assets/123730742/6e78f2b2-7374-405e-a723-2dc49fb059c3">

2. Login menggunakan `msfadmin` dan password: `msfadmin`
3. kini kita sudah berhasil mengeksploit dan masuk ke target mesin
  - <img width="450" alt="Screenshot 2023-12-22 at 19 54 24" src="https://github.com/naufalazhar65/ETHICAL-HACKING-DOCS/assets/123730742/4fdae79f-5a3c-403b-9117-8f5377676763">
4. Untuk masuk sebagai `root` gunakan perintah `sudo su`, jika meminta password, passwordnya adalah `msfadmin`.

<br>
================================================================================================

## STEP BY STEP EXPLOITATION `Samba samb 3.X 4.X`

1. di bagian ini saya akan menggunakan `Scanner` untuk menegetahui versi dari service tersebut.
2. cd ke `/usr/share/metasploit-framework/modules/auxiliary/scanner/smb` untuk menggunakan `smb_version.rb`.
3. selanjutnya gunakan perintah `msfconsole` untuk membuka metasploit.
4. gunakan perintah `use auxiliary/scanner/smb/` tekan `enter`.
5. pilih `smb_version` dengan menggunakan perintah `use 12`.
6. untuk mengetahui informasi tentang exploit yang baru digunakan adalah dengan menggunakan perintah `show info`.
7. untuk memasukkan `RHOST (IP TARGET)` adalah dengan menggunakan perintah `set RHOSTS ip_addres_target`.
8. gunakan perintah `run` untuk menggunakan Scanner dan untuk melihat hasil dari scannernya.
9. dan versi dari samba tersebut ada lah `Samba 3.0.20`
  - <img width="450" alt="Screenshot 2023-12-22 at 20 40 49" src="https://github.com/naufalazhar65/ETHICAL-HACKING-DOCS/assets/123730742/f213a32a-1143-4e41-a83f-8018bcfbe97a">
10. untuk mencari exploitnya gunakan perintah `searchsploit samba 3.0.20`.
11. buka metasploit gunakan perintah `msfconsole`.
12. cari exploit `samba 3.0.2` gunakan perintah `search samba 3.0.20`.
13. dan pilih exploit tersebut gunakan perintah `use 0`.
14. untuk melihat semua `options` nya gunakan perintah `show options`
15. Cara memasukkan `RHOST (IP TARGET)` adalah dengan menggunakan perintah `set RHOSTS ip_addres_target`.
16. Cara mengeksploitasi mesin target adalah dengan menggunakan perintah `EXPLOIT` / `RUN`.



