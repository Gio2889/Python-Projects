ig=plt.figure(figsize=(18,18))
fig.suptitle('Pt(26)/Co(26) 111 checkered ' + r'$\hat{x}$'+ ' ' + r'$a_{lat} =%.4f$' % (alatnew,),fontsize=20,y=0.93)
frplot = fig.add_subplot(2,2,1)
frplot.set_xticks(xc-0.5)
frplot.set_ylabel("Atomic Shifts [$a_{lat}^{-1}$]")
frplot.set_xticklabels(labelmix)
frplot.bar(xc,shiftdiff2[::4,dir],color=['forestgreen']*6+['red']*1+['navy']*6)
frplot.set_facecolor('lightgray')
frplot.set_title('Position #1',fontdict ={'fontsize': 18})
frplot.grid(which='both',axis='both',color='gray', linestyle='-', linewidth=1)
boxstr = '\n'.join((
    r'$d_{0_pt-mix}=%.6f$' % (origitldx1, ),
    r'$d_{0_mix-co}=%.6f$' % (origitldx2, ),
    r'$d_{pt-mix}=%.6f$' % (itld(pc,0,dir,1), ),
    r'$d_{mix-co}=%.6f$' % (itld(pc,0,dir,2), ),
    r'$F_{conv.}<5.0x10^{-3}$'
    ))
props = dict(boxstyle='round', facecolor='wheat', alpha=1.0)
frplot.text(0.55, 0.88, boxstr, transform=frplot.transAxes, fontsize=16,
        verticalalignment='top', bbox=props)
frplot = fig.add_subplot(2,2,2)
frplot.set_xticks(xc-0.5)
frplot.set_xticklabels(labelmix)
frplot.bar(xc,shiftdiff2[1::4,dir],color=['forestgreen']*6+['red']*1+['navy']*6)
frplot.set_facecolor('lightgray')
frplot.set_title('Position #4',fontdict ={'fontsize': 18})
frplot.grid(which='both',axis='both',color='gray', linestyle='-', linewidth=1)
boxstr = '\n'.join((
    r'$d_{0_pt-mix}=%.6f$' % (origitldx1, ),
    r'$d_{0_mix-co}=%.6f$' % (origitldx2, ),
    r'$d_{pt-mix}=%.6f$' % (itld(pc,1,dir,1), ),
    r'$d_{mix-co}=%.6f$' % (itld(pc,1,dir,2), ),
    r'$F_{conv.}<5.0x10^{-3}$'
    ))
props = dict(boxstyle='round', facecolor='wheat', alpha=1.0)
frplot.text(0.6, 0.98, boxstr, transform=frplot.transAxes, fontsize=16,
        verticalalignment='top', bbox=props)
frplot = fig.add_subplot(2,2,3)
frplot.set_xticks(xc-0.5)
frplot.set_ylabel("Atomic Shifts [$a_{lat}^{-1}$]")
frplot.set_xticklabels(labels)
frplot.bar(xc,shiftdiff2[2::4,dir],color=['forestgreen']*6+['cyan']*1+['navy']*6)
frplot.set_facecolor('lightgray')
frplot.set_title('Position #3',fontdict ={'fontsize': 18})
frplot.grid(which='both',axis='both',color='gray', linestyle='-', linewidth=1)
boxstr = '\n'.join((
    r'$d_{0_pt-mix}=%.6f$' % (origitldx1, ),
    r'$d_{0_mix-co}=%.6f$' % (origitldx2, ),
    r'$d_{pt-mix}=%.6f$' % (itld(pc,2,dir,1), ),
    r'$d_{mix-co}=%.6f$' % (itld(pc,2,dir,2), ),
    r'$F_{conv.}<5.0x10^{-3}$'
    ))
props = dict(boxstyle='round', facecolor='wheat', alpha=1.0)
frplot.text(0.6, 0.98, boxstr, transform=frplot.transAxes, fontsize=16,
        verticalalignment='top', bbox=props)
frplot = fig.add_subplot(2,2,4)
frplot.set_xticks(xc-0.5)
frplot.set_xticklabels(labels)
frplot.bar(xc,shiftdiff2[3::4,dir],color=['forestgreen']*6+['cyan']*1+['navy']*6)
frplot.set_facecolor('lightgray')
frplot.set_title('Position #2',fontdict ={'fontsize': 18})
frplot.grid(which='both',axis='both',color='gray', linestyle='-', linewidth=1)
boxstr = '\n'.join((
    r'$d_{0_pt-mix}=%.6f$' % (origitldx1, ),
    r'$d_{0_mix-co}=%.6f$' % (origitldx2, ),
    r'$d_{pt-mix}=%.6f$' % (itld(pc,1,dir,1), ),
    r'$d_{mix-co}=%.6f$' % (itld(pc,1,dir,2), ),
    r'$F_{conv.}<5.0x10^{-3}$'
    ))
props = dict(boxstyle='round', facecolor='wheat', alpha=1.0)
frplot.text(0.6, 0.98, boxstr, transform=frplot.transAxes, fontsize=16,
        verticalalignment='top', bbox=props)
#######################################################################
#######################################################################
fig=plt.figure(figsize=(10,10))
fig.suptitle('Pt(27)/Co(25) 111 ',fontsize=20,y=0.93)
frplot = fig.add_subplot(2,2,1)
frplot.set_xticks(xc)
frplot.set_ylabel("Atomic Shifts [$a_{lat}^{-1}$]")
frplot.set_xticklabels(labelmix)
frplot.bar(xc,diff[::4,0],color=['forestgreen']*13,alpha=0.5)
frplot.bar(xc,diff[::4,1],color=['cyan']*13,alpha=0.5)
frplot.bar(xc,diff[::4,2],color=['orange']*13,alpha=0)
frplot.set_facecolor('lightgray')
frplot.set_title('Position #1',fontdict ={'fontsize': 18})
frplot.grid(which='both',axis='both',color='gray', linestyle='-', linewidth=1)

frplot = fig.add_subplot(2,2,2)
frplot.set_xticks(xc)
frplot.set_xticklabels(labelmix)
frplot.bar(xc,diff[1::4,0],color=['forestgreen']*13,alpha=0.5)
frplot.bar(xc,diff[1::4,1],color=['cyan']*13,alpha=0.5)
frplot.bar(xc,diff[1::4,2],color=['orange']*13,alpha=0)
frplot.set_facecolor('lightgray')
frplot.set_title('Position #4',fontdict ={'fontsize': 18})
frplot.grid(which='both',axis='both',color='gray', linestyle='-', linewidth=1)

frplot = fig.add_subplot(2,2,3)
frplot.set_xticks(xc)
frplot.set_ylabel("Atomic Shifts [$a_{lat}^{-1}$]")
frplot.set_xticklabels(labels)
frplot.bar(xc,diff[2::4,0],color=['forestgreen']*13,alpha=0.5)
frplot.bar(xc,diff[2::4,1],color=['cyan']*13,alpha=0.5)
frplot.bar(xc,diff[2::4,2],color=['orange']*13,alpha=0)
frplot.set_facecolor('lightgray')
frplot.set_title('Position #3',fontdict ={'fontsize': 18})
frplot.grid(which='both',axis='both',color='gray', linestyle='-', linewidth=1)

frplot = fig.add_subplot(2,2,4)
frplot.set_xticks(xc)
frplot.set_xticklabels(labels)
frplot.bar(xc,diff[3::4,0],color=['forestgreen']*13,alpha=0.5)
frplot.bar(xc,diff[3::4,1],color=['cyan']*13,alpha=0.5)
frplot.bar(xc,diff[3::4,2],color=['orange']*13,alpha=0)
frplot.set_facecolor('lightgray')
frplot.set_title('Position #2',fontdict ={'fontsize': 18})
frplot.grid(which='both',axis='both',color='gray', linestyle='-', linewidth=1)
plt.show()

##############################################################################
##############################################################################
fig=plt.figure(figsize=(10,10))
frplot = fig.add_subplot(1,1,1)
frplot.set_xticks(xc)
frplot.set_ylabel("Avg. layer Shifts [$a_{lat}^{-1}$]")
frplot.set_xticklabels(labelmix)
frplot.bar(xc,avgshiftz,width=0.6,color=['forestgreen']*6+['red']*1+['navy']*6)
frplot.bar(np.linspace(0.5,12.5,12),zdistances,width=0.3,color=['mediumspringgreen']*5+['gold']+['darkviolet']+['cyan']*6,alpha=0.9)
frplot.plot(np.linspace(0.0,6,100),np.full((100),ptavg,'float64'),'red')
frplot.plot(np.linspace(08.0,13,100),np.full((100),coavg,'float64'),'red')
frplot.set_facecolor('lightgray')
frplot.set_title('Average layer shift and distance Pt(26)/Pt(26)_lines_110',fontdict ={'fontsize': 18})
frplot.grid(which='both',axis='both',color='gray', linestyle='-', linewidth=1)
boxstr = '\n'.join((
    'Average Pt layer change='r'$%.6f$' % (ptavg, ),
    ))
props = dict(boxstyle='round', facecolor='white', alpha=1.0)
frplot.text(0.175, 0.25, boxstr, transform=frplot.transAxes, fontsize=16,
        verticalalignment='top', bbox=props)
boxstr = '\n'.join((
    'Average Co layer change='r'$ %.3f$' % (coavg, ),
    ))
props = dict(boxstyle='round', facecolor='lightgray', alpha=1.0)
frplot.text(0.5, 0.70, boxstr, transform=frplot.transAxes, fontsize=16,
        verticalalignment='top', bbox=props)
########################################################################
##for polar plots#######################################################
theta=np.full((52),0,'float64')
for i in range(52):
    x = diff[i,0]
    y = diff[i,1]
    if x > 0:
        res = np.arctan(y/x)
    elif x < 0 and y >= 0:
        res = np.arctan(y/x) + np.pi
    elif x < 0 and y < 0:
        res = np.arctan(y/x) - np.pi
    elif x == 0.0 and y < 0:
        res = -(np.pi)/2
    elif x == 0.0 and y > 0:
        res = (np.pi)/2
    else:
        res = 0.0
    theta[i] = res


rad=np.sqrt(diff[:,1]**2 + diff[:,0]**2)
fig1=plt.figure(figsize=(10,10))
fig1.suptitle('Pt(26)/Co(26) 111 xy shifts ',fontsize=20,y=0.93)
for j in range(4):
    pos =  j
    plot = j +1
    frplot = fig1.add_subplot(2,2,plot,projection='polar')
    frplot.scatter(theta[pos::4],rad[pos::4], c=xc,s=200,cmap='bwr',alpha=0.7)
    for i in range(pos,52,4):
        frplot.annotate(labelmix[int(i/4)],
        xy=(theta[i], rad[i]))
    frplot.set_title('Position#'+str(plot))
    frplot.set_rmax(0.06)
    frplot.set_rticks([0,0.02,0.04,0.06])
    frplot.set_facecolor('lightgray')
    frplot.grid(which='both',axis='both',color='gray', linestyle='-', linewidth=1)

plt.savefig('P27C25_111_xy.png')
