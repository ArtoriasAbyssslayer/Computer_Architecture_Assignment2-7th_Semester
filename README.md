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
|-|-|-|-|-|-|-|-|-|-|-|-|
| 64KB | 32KB | 2MB | 2 | 2 | 8 | 64B | 1.603595 | 1.23264 | 7.056 | 1.18517 | 2.623 |
| 64KB | 32KB | 2MB | 2 | 2 | 8 | 32B | 1.7078 | 1.21456 | 11.666 | 1.19194 | 3.921 |
| 64KB | 32KB | 2MB | 2 | 2 | 8 | 128B | 1.5966 | 1.23605 | 4.985 | 1.18016 | 1.990 |
| 64KB | 32KB | 2MB | 2 | 2 | 8 | 256B | 1.5945 | 1.24091 | 3.715 | 1.18106 | 1.654 |

![SpecbzipCPI-Cachelinesizes](https://github.com/harryfilis/Computer_Architecture_Assignment2-7th_Semester/blob/master/plots/cache_line_chage_plots/specbzip.png)

![SpecmcfCPI-Cachelinesizes](https://github.com/harryfilis/Computer_Architecture_Assignment2-7th_Semester/blob/master/plots/cache_line_chage_plots/specmcf.png)

![SpecsjengCPI-Cachelinesizes](https://github.com/harryfilis/Computer_Architecture_Assignment2-7th_Semester/blob/master/plots/cache_line_chage_plots/specsjeng.png)

![SpechmmerCPI-Cachelinesizes](https://github.com/harryfilis/Computer_Architecture_Assignment2-7th_Semester/blob/master/plots/cache_line_chage_plots/spechmmer.png)

![SpeclibmCPI-Cachelinesizes](https://github.com/harryfilis/Computer_Architecture_Assignment2-7th_Semester/blob/master/plots/cache_line_chage_plots/speclibm.png)

**2) Με βάση το best case cachelinesize-cpi εκτελούμε τα παρακάτω πειράματα**
| TEST_TYPE | l1_dsize | l1_isize | l2_size | l1d_assoc | l1i_assoc | l2_assoc | cacheline_size | speclibm |
|-|-|-|-|-|-|-|-|-|
| A | 64KB | 64KB | 512KB | 2 | 2 | 8 | 256 | 1.654968 |
| B | 128KB | 128KB | 1MB | 2 | 2 | 8 | 256 | 1.654777 |
| C | 128KB | 128KB | 2MB | 2 | 2 | 8 | 256 | 1.654405 |
| D | 128KB | 128KB | 4MB | 2 | 2 | 8 | 256 | 1.653662 |

![speclibmCPI-FORTYPESABCD](https://github.com/harryfilis/Computer_Architecture_Assignment2-7th_Semester/blob/master/plots/other_modifications/speclibm.png)

| TEST_TYPE | l1_dsize | l1_isize | l2_size | l1d_assoc | l1i_assoc | l2_assoc | cacheline_size | spechmmer |
|-|-|-|-|-|-|-|-|-|
| A | 64KB | 64KB | 512KB | 2 | 2 | 8 | 128 | 1.179634 |
| B | 128KB | 128KB | 1MB | 2 | 2 | 8 | 128 | 1.178092 |
| C | 128KB | 128KB | 2MB | 2 | 2 | 8 | 128 | 1.178092 |
| D | 128KB | 128KB | 4MB | 2 | 2 | 8 | 128 | 1.178092 |

![spechmmerCPI-FORTYPESABCD](https://github.com/harryfilis/Computer_Architecture_Assignment2-7th_Semester/blob/master/plots/other_modifications/spechmmer.png)

| TEST_TYPE | l1_dsize | l1_isize | l2_size | l1d_assoc | l1i_assoc | l2_assoc | cacheline_size | specsjeng |
|-|-|-|-|-|-|-|-|-|
| A | 64KB | 64KB | 512KB | 2 | 2 | 8 | 256 | 3.715711  |
| B | 128KB | 128KB | 1MB | 2 | 2 | 8 | 256 | 3.715872  |
| C | 128KB | 128KB | 2MB | 2 | 2 | 8 | 256 | 3.715443  |
| D | 128KB | 128KB | 4MB | 2 | 2 | 8 | 256 | 3.714662  |

![specsjengCPI-FORTYPESABCD](https://github.com/harryfilis/Computer_Architecture_Assignment2-7th_Semester/blob/master/plots/other_modifications/specsjeng.png)

| TEST_TYPE | l1_dsize | l1_isize | l2_size | l1d_assoc | l1i_assoc | l2_assoc | cacheline_size | specbzip |
|-|-|-|-|-|-|-|-|-|
| A | 64KB | 64KB | 512KB | 2 | 2 | 8 | 256 | 1.647000 |
| B | 128KB | 128KB | 1MB | 2 | 2 | 8 | 256 | 1.571640 |
| C | 128KB | 128KB | 2MB | 2 | 2 | 8 | 256 | 1.557965 |
| D | 128KB | 128KB | 4MB | 2 | 2 | 8 | 256 | 1.550634 |

![SpecbzipCPI-FORTYPESABCD](https://github.com/harryfilis/Computer_Architecture_Assignment2-7th_Semester/blob/master/plots/other_modifications/specbzip.png)

| TEST_TYPE | l1_dsize | l1_isize | l2_size | l1d_assoc | l1i_assoc | l2_assoc | cacheline_size | specmcf |
|-|-|-|-|-|-|-|-|-|
| A | 64KB | 64KB | 512KB | 2 | 2 | 8 | 32 | 1.146603 |
| B | 128KB | 128KB | 1MB | 2 | 2 | 8 | 32 | 1.145850 |
| C | 128KB | 128KB | 2MB | 2 | 2 | 8 | 32 | 1.144656 |
| D | 128KB | 128KB | 4MB | 2 | 2 | 8 | 32 | 1.144551 |

![SpecmcfCPI-FORTYPESABCD](https://github.com/harryfilis/Computer_Architecture_Assignment2-7th_Semester/blob/master/plots/other_modifications/specmcf.png)

Συνεχίζουμε με το μικρότερο δυνατό cpi, που μας δίνουν οι περιπτώσεις A,B,C,D (που αφορούν μεγέθη μνημών) και προσπαθούμε για περαιτέρω βελτίωση του cpi αλλάζοντας το associativity των μνημών cache. Οπότε εκτελούμε τα παρακάτω πειράματα Α1,Β1,C1,D1 για τη καθεμία βέλτιστη περίπτωση αντίστοιχα.</br>

Για το benchmark **specbzip**, για το πείραμα type D (l1_dsize = l1_isize = 128KB, l2_size = 4MB) : </br>

| TEST_TYPE | l1_dsize | l1_isize | l2_size | l1d_assoc | l1i_assoc | l2_assoc | cacheline_size | specbzip |
|-|-|-|-|-|-|-|-|-|
| A1 | 128KB | 128KB | 4MB | 1 | 1 | 8 | 256 | 1.569167 |
| B1 | 128KB | 128KB | 4MB | 4 | 4 | 8 | 256 | 1.545340 |
| C1 | 128KB | 128KB | 4MB | 8 | 8 | 8 | 256 | 1.539940 |
| D1 | 128KB | 128KB | 4MB | 8 | 8 | 16| 256 | 1.539524 |


Για το benchmark **spechmmer**, για το πείραμα type B (l1_dsize = l1_isize = 128KB, l2_size = 1MB) : </br>


| TEST_TYPE | l1_dsize | l1_isize | l2_size | l1d_assoc | l1i_assoc | l2_assoc | cacheline_size | spechmmer |
|-|-|-|-|-|-|-|-|-|
| A1 | 128KB | 128KB | 1MB | 1 | 1 | 8 | 128 | 1.184147 |
| B1 | 128KB | 128KB | 1MB | 4 | 4 | 8 | 128 | 1.177829 |
| C1 | 128KB | 128KB | 1MB | 8 | 8 | 8 | 128 | 1.177692 |
| D1 | 128KB | 128KB | 1MB | 8 | 8 | 16 | 128 | 1.177692 |


Για το benchmark **specmcf**, για το πείραμα type D (l1_dsize = l1_isize = 128KB, l2_size = 4MB) : </br>


| TEST_TYPE | l1_dsize | l1_isize | l2_size | l1d_assoc | l1i_assoc | l2_assoc | cacheline_size | specmcf |
|-|-|-|-|-|-|-|-|-|
| A1 | 128KB | 128KB | 4MB | 1 | 1 | 8 | 32 | 1.145174  |
| B1 | 128KB | 128KB | 4MB | 4 | 4 | 8 | 32 | 1.144551  |
| C1 | 128KB | 128KB | 4MB | 8 | 8 | 8 | 32 | 1.144551  |
| D1 | 128KB | 128KB | 4MB | 8 | 8 | 16 | 32 | 1.144551 |


Για το benchmark **specsjeng**, για το πείραμα type D (l1_dsize = l1_isize = 128KB, l2_size = 4MB) : </br>


| TEST_TYPE | l1_dsize | l1_isize | l2_size | l1d_assoc | l1i_assoc | l2_assoc | cacheline_size | specsjeng |
|-|-|-|-|-|-|-|-|-|
| A1 | 128KB | 128KB | 4MB | 1 | 1 | 8 | 256 | 3.714885 |
| B1 | 128KB | 128KB | 4MB | 4 | 4 | 8 | 256 | 3.714674 |
| C1 | 128KB | 128KB | 4MB | 8 | 8 | 8 | 256 | 3.714681 |
| D1 | 128KB | 128KB | 4MB | 8 | 8 | 16| 256 | 3.714669 |


Για το benchmark **speclibm**, για το πείραμα type D (l1_dsize = l1_isize = 128KB, l2_size = 4MB) : </br>


| TEST_TYPE | l1_dsize | l1_isize | l2_size | l1d_assoc | l1i_assoc | l2_assoc | cacheline_size | speclibm |
|-|-|-|-|-|-|-|-|-|
| A1 | 128KB | 128KB | 4MB | 1 | 1 | 8 | 256 | 1.672409  |
| B1 | 128KB | 128KB | 4MB | 4 | 4 | 8 | 256 | 1.653656  |
| C1 | 128KB | 128KB | 4MB | 8 | 8 | 8 | 256 | 1.653656  |
| D1 | 128KB | 128KB | 4MB | 8 | 8 | 16| 256 | 1.653656  |
