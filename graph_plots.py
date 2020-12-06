import matplotlib.pyplot as plt 
  
fig = plt.gcf()
fig.set_size_inches(18.5, 10.5)
fig.savefig('specsjeng.png', dpi=300)
#specsjeng
# line 1 points 
cpi = [11.665655,7.056395,4.984822,3.715453] 
cacheline_size = [32,64,128,256] 
# plotting the line 1 points  
plt.plot(cacheline_size,cpi,'-o',linestyle='dashed', linewidth = 3, label = "cpi line") 

  
# naming the x axis 
plt.xlabel('x - axis ~ cache line size') 
# naming the y axis 
plt.ylabel('y - axis ~ CPI') 
# giving a title to my graph 
plt.title('Secsjeng benchmark with different cache line sizes') 
plt.xticks(cacheline_size)
plt.yticks(cpi)
# show a legend on the plot 
plt.legend() 

# function to show the plot 
plt.show() 

fig2 = plt.gcf()
fig2.set_size_inches(18.5, 10.5)
fig2.savefig('specbzip.png', dpi=300)
#specbzip
cpi = [1.707788,1.603595,1.596596,1.594472] 
cacheline_size = [32,64,128,256] 
# plotting the line 1 points  
plt.plot(cacheline_size,cpi,'-o',linestyle='dashed', linewidth = 3, label = "cpi line") 

  
# naming the x axis 
plt.xlabel('x - axis ~ cache line size') 
# naming the y axis 
plt.ylabel('y - axis ~ CPI') 
# giving a title to my graph 
plt.title('Specbzip benchmark with different cache line sizes') 
plt.xticks(cacheline_size)
plt.yticks(cpi)
# show a legend on the plot 
plt.legend() 

# function to show the plot 
plt.show() 

fig3 = plt.gcf()
fig3.set_size_inches(18.5, 10.5)
fig3.savefig('specmcf.png', dpi=300)

#specmcf

cpi = [1.214562, 1.232645, 1.236049, 1.240908] 
cacheline_size = [32,64,128,256] 
# plotting the line 1 points  
plt.plot(cacheline_size,cpi,'-o',linestyle='dashed', linewidth = 3, label = "cpi line") 

  
# naming the x axis 
plt.xlabel('x - axis ~ cache line size') 
# naming the y axis 
plt.ylabel('y - axis ~ CPI') 
# giving a title to my graph 
plt.title('Specmcf benchmark with different cache line sizes') 
plt.xticks(cacheline_size)
plt.yticks(cpi)
# show a legend on the plot 
plt.legend() 

# function to show the plot 
plt.show() 
fig4 = plt.gcf()
fig4.set_size_inches(18.5, 10.5)
fig4.savefig('spechmmer.png', dpi=300)

#spechmmer
cpi = [1.191936, 1.185174, 1.180157, 1.181056]  
cacheline_size = [32,64,128,256] 
# plotting the line 1 points  
plt.plot(cacheline_size,cpi,'-o',linestyle='dashed', linewidth = 3, label = "cpi line") 

  
# naming the x axis 
plt.xlabel('x - axis ~ cache line size') 
# naming the y axis 
plt.ylabel('y - axis ~ CPI') 
# giving a title to my graph 
plt.title('Spechmmer benchmark with different cache line sizes') 
plt.xticks(cacheline_size)
plt.yticks(cpi)
# show a legend on the plot 
plt.legend() 

# function to show the plot 
plt.show() 

fig5 = plt.gcf()
fig5.set_size_inches(18.5, 10.5)
fig5.savefig('speclibm.png', dpi=100)
#speclibm
cpi = [3.92066,2.622616,1.989979,1.654439]  
cacheline_size = ['A','B','C','D'] 
# plotting the line 1 points  
plt.plot(cacheline_size,cpi,'-o',linestyle='dashed', linewidth = 3, label = "cpi line") 

  
# naming the x axis 
plt.xlabel('x - axis ~ cache line size') 
# naming the y axis 
plt.ylabel('y - axis ~ CPI') 
# giving a title to my graph 
plt.title('Speclibm benchmark with different cache line sizes') 
plt.xticks(cacheline_size)
plt.yticks(cpi)
# show a legend on the plot 
plt.legend() 

# function to show the plot 
plt.show() 



