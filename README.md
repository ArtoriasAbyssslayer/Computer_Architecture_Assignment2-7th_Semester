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
      
    - dcache
    
