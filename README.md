# -Computer_Architecture_Assignment2-7th_Semester-
## ΑΡΧΙΤΕΚΤΟΝΙΚΗ ΠΡΟΗΓΜΕΝΩΝ ΥΠΟΛΟΓΙΣΤΩΝ

#### Αναφορά 2ου Εργαστηρίου 

### Συγγραφείς : Σακελλαρίου Βασίλειος ΑΕΜ: 9400, Φίλης Χάρης ΑΕΜ:9449



### Βήμα 1ο. Εκτέλεση SPEC CPU2006 Benchmarks στον gem5 </br>
**1) Βασικές παράμετροι επεξεργαστή / Υποσύστημα μνημών cache**</br>
Ανοίγοντας το [config.ini](https://github.com/harryfilis/Computer_Architecture_Assignment2-7th_Semester/blob/master/spec_results/spechmmer/config.ini):
* L1--dcache:
  * Μέγεθος : 64KB
  * associativity : 2
  * cache_line_size : 64 Bytes
* L1--icache:
  * Μέγεθος : 32KB
  * associativity : 2
  * cache_line_size : 64 Bytes
---------------------------------
* L2--icache:
  * Μέγεθος : 2MB
  * associativity : 8
  * cache_line_size : 64 Bytes
  
**2) Αποτελέσματα απο κάθε benchmark**</br>

* -- Benchmark **specbzip**</br>
Από το αρχείο [stats.txt](https://github.com/harryfilis/Computer_Architecture_Assignment2-7th_Semester/blob/master/spec_results/specbzip/stats.txt):</br>
  --Χρόνος εκτέλεσης:</br>
  * sim_seconds                                  0.083654                       # Number of seconds simulated
  
  --Μέσο CPI:</br>
  
  * system.cpu.cpi                               1.673085                       # CPI: cycles per instruction
  
  --Miss rate</br>
  
   * L1 cache:
     - icache
      ```
      line332: system.cpu.icache.overall_miss_rate::total     0.000075                       # miss rate for overall accesses
      ```
     - dcache
     ```
     system.cpu.dcache.overall_miss_rate::total     0.014312                       # miss rate for overall accesses
     ```
  * L2 cache
  ```
  system.l2.overall_miss_rate::total           0.295247                       # miss rate for overall accesses
  ```
* -- Benchmark **spechmmer**</br>
Από το αρχείο [stats.txt](https://github.com/harryfilis/Computer_Architecture_Assignment2-7th_Semester/blob/master/spec_results/spechmmer/stats.txt):</br>
  --Χρόνος εκτέλεσης:</br>
  * sim_seconds                                  0.059390                       # Number of seconds simulated
  
  --Μέσο CPI:</br>
  
  * system.cpu.cpi                               1.187803                       # CPI: cycles per instruction
  
  --Miss rate</br>
  
   * L1 cache:
     - icache
      ```
      system.cpu.icache.overall_miss_rate::total     0.000212                       # miss rate for overall accesses
      ```
     - dcache
     ```
     system.cpu.dcache.overall_miss_rate::total     0.001628                       # miss rate for overall accesses
     ```
  * L2 cache
  ```
  system.l2.overall_miss_rate::total           0.078296                       # miss rate for overall accesses
  ```
* -- Benchmark **speclibm**</br>
Από το αρχείο [stats.txt](https://github.com/harryfilis/Computer_Architecture_Assignment2-7th_Semester/blob/master/spec_results/speclibm/stats.txt):</br>
  --Χρόνος εκτέλεσης:</br>
  * sim_seconds                                   0.174763                       # Number of seconds simulated
  
  --Μέσο CPI:</br>
  
  * system.cpu.cpi                               3.495270                       # CPI: cycles per instruction
  
  --Miss rate</br>
  
   * L1 cache:
     - icache
      ```
      system.cpu.icache.overall_miss_rate::total     0.000095                       # miss rate for overall accesses
      ```
     - dcache
     ```
     system.cpu.dcache.overall_miss_rate::total     0.060972                       # miss rate for overall accesses
     ```
  * L2 cache
  ```
  system.l2.overall_miss_rate::total           0.999940                       # miss rate for overall accesses
  ```
* -- Benchmark **specmcf**</br>
Από το αρχείο [stats.txt](https://github.com/harryfilis/Computer_Architecture_Assignment2-7th_Semester/blob/master/spec_results/specmcf/stats.txt):</br>
  --Χρόνος εκτέλεσης:</br>
  * sim_seconds                                   0.062553                      # Number of seconds simulated
  
  --Μέσο CPI:</br>
  
  * system.cpu.cpi                               1.251067                       # CPI: cycles per instruction
  
  --Miss rate</br>
  
   * L1 cache:
     - icache
      ```
      system.cpu.icache.overall_miss_rate::total     0.019032                       # miss rate for overall accesses
      ```
     - dcache
     ```
     system.cpu.dcache.overall_miss_rate::total     0.002062                       # miss rate for overall accesses
     ```
  * L2 cache
  ```
  system.l2.overall_miss_rate::total           0.067668                       # miss rate for overall accesses
  ```
* -- Benchmark **specsjeng**</br>
Από το αρχείο [stats.txt](https://github.com/harryfilis/Computer_Architecture_Assignment2-7th_Semester/blob/master/spec_results/specsjeng/stats.txt):</br>
  --Χρόνος εκτέλεσης:</br>
  * sim_seconds                                   0.513823                      # Number of seconds simulated
  
  --Μέσο CPI:</br>
  
  * system.cpu.cpi                                10.276466                       # CPI: cycles per instruction
  
  --Miss rate</br>
  
   * L1 cache:
     - icache
      ```
      system.cpu.icache.overall_miss_rate::total     0.000020                       # miss rate for overall accesses
      ```
     - dcache
     ```
     system.cpu.dcache.overall_miss_rate::total     0.121831                       # miss rate for overall accesses
     ```
  * L2 cache
  ```
  system.l2.overall_miss_rate::total           0.999978                       # miss rate for overall accesses
  ```
  **3)Benchmarks cpu_clock = 2Ghz, 1Ghz**
  
  Benchmarks για cpu clock 2Ghz</br>
  απο το [stats.txt](https://github.com/harryfilis/Computer_Architecture_Assignment2-7th_Semester/blob/master/spec_results/spechmmer/stats.txt)</br>
  ```
   system.clk_domain.clock                          1000                       # Clock period in ticks
   system.cpu_clk_domain.clock                       500                       # Clock period in ticks
  ```
  από το [config.json](https://github.com/harryfilis/Computer_Architecture_Assignment2-7th_Semester/blob/master/spec_results/spechmmer/config.json)</br>
  ```json
   "system":{
   ...
   "clk_domain": {
            "type": "SrcClockDomain",
            "cxx_class": "SrcClockDomain",
            "name": "clk_domain",
            "path": "system.clk_domain",
            "clock": [
                1000
            ]
     }
  ```
  ```json
    "cpu_clk_domain": {
            "type": "SrcClockDomain",
            "cxx_class": "SrcClockDomain",
            "name": "cpu_clk_domain",
            "path": "system.cpu_clk_domain",
            "clock": [
                500
            ]
  ```
  Benchmarks για cpu clock 1Ghz</br>
  απο το [stats.txt](https://github.com/harryfilis/Computer_Architecture_Assignment2-7th_Semester/blob/master/spec_results/spechmmer1/stats.txt)</br>
  ```
   system.clk_domain.clock                          1000                       # Clock period in ticks
   system.cpu_clk_domain.clock                      1000                       # Clock period in ticks
  ```
  από το [config.json](https://github.com/harryfilis/Computer_Architecture_Assignment2-7th_Semester/blob/master/spec_results/spechmmer1/config.json)</br>
  ```json
   "system":{
   ...
   "clk_domain": {
            "type": "SrcClockDomain",
            "cxx_class": "SrcClockDomain",
            "name": "clk_domain",
            "path": "system.clk_domain",
            "clock": [
                1000
            ]
     }
  ```
  ```json
    "cpu_clk_domain": {
            "type": "SrcClockDomain",
            "cxx_class": "SrcClockDomain",
            "name": "cpu_clk_domain",
            "path": "system.cpu_clk_domain",
            "clock": [
                1000
            ]
  ```
  
  
  
  
    
   Για τους χρόνους εκτέλεσης:

 * specbzip

   1GHz: sim_seconds 0.160359 # Number of seconds simulated

   2GHz: sim_seconds 0.083654 # Number of seconds simulated

   0.160359 ÷ 0.083654 = 1,9169
   
   Ο λόγος αυτός είναι πολύ κοντά στο τέλειο scaling, γιατί για το συγκεκριμένο benchmark το ρολόι του επεξεργαστή παίζει τον καθοριστικό παράγοντα και όχι τόσο οι ταχύτητες των μνημών.  
   
 * spechmmer 
   
   1GHz: sim_seconds 0.118517 # Number of seconds simulated

   2GHz: sim_seconds 0.059390 # Number of seconds simulated

   0.118517 ÷ 0.059390 = 1,995571645
   
   Πρόκειται για τελειο scaling, γιατί για το συγκεκριμένο benchmark το ρολόι του επεξεργαστή παίζει τον καθοριστικό παράγοντα και όχι τόσο οι ταχύτητες των μνημών.
* specmcf 
   
   1GHz: sim_seconds 0.123107# Number of seconds simulated

   2GHz: sim_seconds 0.062553 # Number of seconds simulated

   0.123107 ÷ 0.062553 = 1,968043099
   
   Ο λόγος αυτός είναι πολύ κοντά στο τέλειο scaling, γιατί για το συγκεκριμένο benchmark το ρολόι του επεξεργαστή παίζει τον καθοριστικό παράγοντα και όχι τόσο οι ταχύτητες των μνημών.
* specsjeng 
   
   1GHz: sim_seconds 0.705640 # Number of seconds simulated

   2GHz: sim_seconds 0.513823 # Number of seconds simulated

   0.705640 ÷ 0.513823 = 1,373313378</br>
   
  Ο λόγος απέχει αρκετά από το τέλειο scaling καθώς εδώ(συγκεκριμένο benchmark) είναι καθοριστικός και ο ρόλος των μνημών cache(προσβάσεις στην μνήμη).

 
* speclibm

   1GHz: sim_seconds 0.262262 # Number of seconds simulated

   2GHz: sim_seconds 0.174763 # Number of seconds simulated

   0.262262 ÷ 0.174763 = 1,500672339</br>
   
  Ο λόγος απέχει αρκετά από το τέλειο scaling καθώς εδώ(συγκεκριμένο benchmark) είναι καθοριστικός και ο ρόλος των μνημών cache(προσβάσεις στην μνήμη).
  ### Βήμα 2ο. Bελτιστοποίηση απόδοσης στα benchmarks  ~ CPIwise </br>
  Μετά από τέστ που τρέξαμε προβήκαμε στις εξής βελτιστοποιήσεις(σειρά)</br>
  **1) Η πρώτη βελτιστοποίηση που κάναμε αφορούσε το cache line size == block size κρατώντας τα υπόλοιπα στις default τιμές τους.**</br>
 | l1_dsize | l1_isize | l2_size | l1d_assoc | l1i_assoc | l2_assoc | cacheline_size | specbzip | specmcf | specsjeng | spechmmer | speclibm |
 |----------|----------|---------|-----------|-----------|----------|----------------|----------|---------|-----------|-----------|----------|
 | 64KB     | 32KB     | 2MB     | 2         | 2         | 8        | 64B            | 1.603595 | 1.23264 | 7.056     | 1.18517   | 2.623    |
 | 64KB     | 32KB     | 2MB     | 2         | 2         | 8        | 32B            | 1.7078   | 1.21456 | 11.666    | 1.19194   | 3.921    |
 | 64KB     | 32KB     | 2MB     | 2         | 2         | 8        | 128B           | 1.5966   | 1.23605 | 4.985     | 1.18016   | 1.990    |
 | 64KB     | 32KB     | 2MB     | 2         | 2         | 8        | 256B           | 1.5945   | 1.24091 | 3.715     | 1.18106   | 1.654    |

| l1_dsize | l1_isize | l2_size | l1d_assoc | l1i_assoc | l2_assoc | cacheline_size | specbzip | specmcf | specsjeng | spechmmer | speclibm |
|-|-|-|-|-|-|-|-|-|-|-|-|
| 64KB | 32KB | 2MB | 2 | 2 | 8 | 64 | 1.603595 | 1.23264 | 7.056 | 1.18517 | 2.623 |
| 64KB | 32KB | 2MB | 2 | 2 | 8 | 32 | 1.7078 | 1.21456 | 11.666 | 1.19194 | 3.921 |
| 64KB | 32KB | 2MB | 2 | 2 | 8 | 128 | 1.5966 | 1.23605 | 4.985 | 1.18016 | 1.990 |
| 64KB | 32KB | 2MB | 2 | 2 | 8 | 256 | 1.5945 | 1.24091 | 3.715 | 1.18106 | 1.654 |
