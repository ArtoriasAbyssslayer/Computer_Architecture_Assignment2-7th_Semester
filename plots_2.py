#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 19:08:34 2020

@author: harry
"""

import matplotlib.pyplot as plt 
  
fig = plt.gcf()
fig.set_size_inches(18.5, 10.5)
fig.savefig('specsjeng.png', dpi=300)
#specsjeng
# line 1 points 
cpi = [3.714885,3.714674,3.714681,3.714669] 
test_type = ['A1','B1','C1','D1'] 
# plotting the line 1 points  
plt.plot(test_type,cpi,'-or',linestyle='dashed', linewidth = 3, label = "cpi line") 

  
# naming the x axis 
plt.xlabel('x-axis~cache_assoc_mod_Tests') 
# naming the y axis 
plt.ylabel('y - axis ~ CPI') 
# giving a title to my graph 
plt.title('Secsjeng benchmark test with different cache associativity') 
plt.xticks(test_type)
plt.yticks(cpi)
# show a legend on the plot 
plt.legend() 

# function to show the plot 
plt.show() 

fig2 = plt.gcf()
fig2.set_size_inches(18.5, 10.5)
fig2.savefig('specbzip.png', dpi=300)
#specbzip
cpi = [1.569167,1.545340,1.539940,1.539524] 
test_type = ['A1','B1','C1','D1'] 
# plotting the line 1 points  
plt.plot(test_type,cpi,'-or',linestyle='dashed', linewidth = 3, label = "cpi line") 

  
# naming the x axis 
plt.xlabel('x-axis~cache_assoc_mod_Tests') 
# naming the y axis 
plt.ylabel('y - axis ~ CPI') 
# giving a title to my graph 
plt.title('Specbzip benchmark test with different cache associativity') 
plt.xticks(test_type)
plt.yticks(cpi)
# show a legend on the plot 
plt.legend() 

# function to show the plot 
plt.show() 

fig3 = plt.gcf()
fig3.set_size_inches(18.5, 10.5)
fig3.savefig('specmcf.png', dpi=300)

#specmcf

cpi = [1.145174, 1.144551, 1.144551, 1.144551] 
test_type = ['A1','B1','C1','D1'] 
# plotting the line 1 points  
plt.plot(test_type,cpi,'-or',linestyle='dashed', linewidth = 3, label = "cpi line") 

  
# naming the x axis 
plt.xlabel('x-axis~cache_assoc_mod_Tests') 
# naming the y axis 
plt.ylabel('y - axis ~ CPI') 
# giving a title to my graph 
plt.title('Specmcf benchmark test with different cache associativity') 
plt.xticks(test_type)
plt.yticks(cpi)
# show a legend on the plot 
plt.legend() 

# function to show the plot 
plt.show() 
fig4 = plt.gcf()
fig4.set_size_inches(18.5, 10.5)
fig4.savefig('spechmmer.png', dpi=300)

#spechmmer
cpi = [1.184147, 1.177829, 1.177692, 1.177692]  
test_type = ['A1','B1','C1','D1'] 
# plotting the line 1 points  
plt.plot(test_type,cpi,'-or',linestyle='dashed', linewidth = 3, label = "cpi line") 

  
# naming the x axis 
plt.xlabel('x-axis~cache_assoc_mod_Tests') 
# naming the y axis 
plt.ylabel('y - axis ~ CPI') 
# giving a title to my graph 
plt.title('Spechmmer benchmark test with different cache associativity') 
plt.xticks(test_type)
plt.yticks(cpi)
# show a legend on the plot 
plt.legend() 

# function to show the plot 
plt.show() 

fig5 = plt.gcf()
fig5.set_size_inches(18.5, 10.5)
fig5.savefig('speclibm.png', dpi=100)
#speclibm
cpi = [1.672409,1.653656, 1.653656,1.653656]  
test_type = ['A1','B1','C1','D1'] 
# plotting the line 1 points  
plt.plot(test_type,cpi,'-or',linestyle='dashed', linewidth = 3, label = "cpi line") 

  
# naming the x axis 
plt.xlabel('x-axis~cache_assoc_mod_Tests') 
# naming the y axis 
plt.ylabel('y - axis ~ CPI') 
# giving a title to my graph 
plt.title('Speclibm benchmark test with different cache associativity') 
plt.xticks(test_type)
plt.yticks(cpi)
# show a legend on the plot 
plt.legend() 

# function to show the plot 
plt.show() 