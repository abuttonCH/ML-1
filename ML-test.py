import nibabel as nib
import matplotlib.pyplot as plt
import os
import numpy as np
from sklearn.decomposition import PCA

target_list=[]

targets=open('targets.csv','r')
for lines in targets:
    target_list.append(int(lines.strip('\n')))

os.chdir('set_train')
L=os.listdir('./')

target_min=np.amin(target_list)
target_max=np.amax(target_list)

increment=10

bins=range(target_min,target_max,increment)
target_bin = np.digitize(target_list, bins)
target_bin = target_bin.tolist()

for j in list(set(target_bin)):
    indices=[]
    index=0
    for entry in target_bin:
        if entry == j:
           indices.append(index)
        index=index+1

    if j != np.amax(target_bin):
        print "The age group is :",bins[j-1], "-", bins[j], " The number of samples are :", len(indices)
    else:
        print "The age group is :", bins[j-1],"-", np.amax(bins)+increment, " The number of samples are :", len(indices)


    scans=[]

#indices = range(278)

    for i in indices:
        img=nib.load(L[i])
        data=img.get_data()
        data=data[:,:,80,0]
        scans.append(data)

    print

#mean_scan=np.average(np.array(scans),weights=target_list,axis=0)
    std_scans=np.std(np.array(scans),axis=0)
    mean_scans = np.mean(np.array(scans), axis=0)

    plt.imshow(mean_scans)
#plt.plot(target_list)
    plt.show()


########-PCA dimension reduction-#######

#img = nib.load(L[i])
#data = img.get_data()
#data = data[:, :, 91, 0]


#pca = PCA(n_components=10)
#pca.fit(data)

#print pca.explained_variance_ratio_
#print pca.components_

########################################



############-distrubtion of scans-#############

#plt.hist(target_list,20)
#plt.title("Number of scans from different age groups")
#plt.show()

###############################################
