# -Computer_Architecture_Assignment2-7th_Semester-
## ΑΡΧΙΤΕΚΤΟΝΙΚΗ ΠΡΟΗΓΜΕΝΩΝ ΥΠΟΛΟΓΙΣΤΩΝ

### Αναφορά 2ου Εργαστηρίου 

#### Συγγραφείς : Σακελλαρίου Βασίλειος ΑΕΜ: 9400, Φίλης Χάρης ΑΕΜ:9449



#####**Βήμα 1ο. Εκτέλεση SPEC CPU2006 Benchmarks στον gem5 **</br>
**1) Βασικές παράμετροι επεξεργαστή / Υποσύστημα μνημών cache**</br>
Ανοίγοντας το [config.ini](https://github.com/harryfilis/Computer_Architecture_Assignment2-7th_Semester/blob/master/spec_results/spechmmer/config.ini):
* L1--dcache:
  * Μέγεθος : 64KB
  * associativity : 2
  * cache_line_size : 64Bytes
* L1--icache:
  * Μέγεθος : 32KB
  * associativity : 2
  * cache_line_size : 64Bytes
---------------------------------
* L2--icache:
  * Μέγεθος : 2MB
  * associativity : 8
  * cache_line_size : 64Bytes
  
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
   system:{
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
   system:{
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
  
  
  
     
    
