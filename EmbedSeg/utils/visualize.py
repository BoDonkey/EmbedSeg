import matplotlib.pyplot as plt
from EmbedSeg.utils.glasbey import Glasbey
import numpy as np
from matplotlib.colors import ListedColormap

def create_color_map(n_colors= 10):
    gb = Glasbey(base_palette=[(255, 0, 0), (0, 255, 0), (0, 0, 255)], 
             lightness_range=(10,100), 
             hue_range=(10,100), 
             chroma_range=(10,100), 
             no_black=True)
    p = gb.generate_palette(size=n_colors)
    p[0, :] =[0, 0, 0] # make label 0 always black!
    p_ = np.hstack((p, np.ones((p.shape[0], 1))))
    p_ = np.where(p_>0, p_, 0)
    p_ = np.where(p_<=1, p_, 1)
    np.save('../../../cmaps/cmap_'+str(n_colors), p_)
    newcmp = ListedColormap(p_)
    return newcmp

def visualize(image, prediction, ground_truth, embedding, new_cmp):
    font = {'family': 'serif',
        'color':  'white',
        'weight': 'bold',
        'size': 16,
        }
    plt.figure(figsize=(15,15))
    img_show = image if image.ndim==2 else image[...,0]
    plt.subplot(221); 
    plt.imshow(img_show, cmap='magma'); 
    plt.text(20, 20, "IM", fontdict=font)
    plt.xlabel('Image')
    plt.axis('off')
    plt.subplot(222); 
    plt.axis('off')
    plt.imshow(ground_truth, cmap=new_cmp, interpolation = 'None')
    plt.text(20, 20, "GT", fontdict=font)
    plt.xlabel('Ground Truth')
    plt.subplot(223);
    plt.axis('off')
    plt.imshow(embedding,  interpolation = 'None')
    plt.subplot(224);  
    plt.axis('off')
    plt.imshow(prediction, cmap=new_cmp, interpolation = 'None')
    plt.text(20, 20, "PRED", fontdict=font)
    plt.xlabel('Prediction')
    plt.tight_layout()
    plt.show()
    
