import matplotlib.pyplot as plt
import seaborn as sns
sns.set_context("paper",font_scale=1.0,rc={"lines.linewidth": 0.5})

def plot_colors(yval=-4.5, alpha=0.15, xmin=-0.5, xmax=3.5,fontsize=16):
    colors = [
        {"min": -1, "max": -0.26, "alpha": alpha, "color": '#5b7cff', "label": 'O'},
        {"min": -0.25, "max": -0.038, "alpha": alpha, "color": '#6988ff', "label": 'B'},
        {"min": -0.037, "max": 0.327, "alpha": alpha, "color": '#93aaff', "label": 'A'},
        {"min": 0.326, "max": 0.767, "alpha": alpha, "color": '#dddeff', "label": 'F'},
        {"min": 0.768, "max": 0.984, "alpha": alpha, "color": '#ffebdf', "label": 'G'},
        {"min": 0.983, "max": 1.85, "alpha": alpha, "color": '#ffb177', "label": 'K'},
        {"min": 1.85, "max": 4.86, "alpha": alpha, "color": '#ffa448', "label": 'M'}
    ]

    for c in colors:
        if c["min"] < xmax and c["max"] > xmin: # Check if the color is within xmin and xmax
            bprp1 = max(c["min"], xmin)
            bprp2 = min(c["max"], xmax)

            plt.axvspan(bprp1, bprp2, alpha=c["alpha"], color=c["color"], zorder=1)
            val = bprp1 + (bprp2 - bprp1) / 2
            plt.annotate(c["label"], xy=(val, yval), xytext=(val, yval), fontsize=fontsize,zorder=8)
    return

def plot_colors_old(yval,alpha,xmin,xmax):
    #https://www.pas.rochester.edu/~emamajek/EEM_dwarf_UBVIJHK_colors_Teff.txt
    #colors from Mamajek+2022 file
    #bprp1=-1 #should be -1 but we are cropping to the plot bounds
    if xmin>=-0.26:
        print('skipping')
    else:
        bprp1=xmin
        bprp2=-0.26
        plt.axvspan(bprp1,bprp2, alpha=alpha, color='#5b7cff',zorder=1)#0
        val=bprp1+(bprp2-bprp1)/2
        plt.annotate('O', xy =(0,0),xytext =(val, yval),fontsize=16)

    if xmin>-0.25:
        bprp1=xmin
    else:
        bprp1=-0.25
    bprp2=-0.038
    plt.axvspan(bprp1,bprp2, alpha=0.35, color='#6988ff',zorder=1)#B
    val=bprp1+(bprp2-bprp1)/2
    plt.annotate('B', xy =(0,0),xytext =(val, yval),fontsize=16)

    bprp1=-0.037
    bprp2=0.327
    plt.axvspan(bprp1,bprp2, alpha=alpha, color='#93aaff',zorder=1)#A
    val=bprp1+(bprp2-bprp1)/3
    plt.annotate('A', xy =(0,0),xytext =(val, yval),fontsize=16)

    bprp1=0.326
    bprp2=0.767
    plt.axvspan(bprp1,bprp2, alpha=alpha, color='#dddeff',zorder=1)#F
    val=bprp1+(bprp2-bprp1)/2
    plt.annotate('F', xy =(0,0),xytext =(val, yval),fontsize=16)

    bprp1=0.768
    bprp2=0.984
    plt.axvspan(bprp1,bprp2, alpha=alpha, color='#ffebdf',zorder=1)#G
    val=bprp1+(bprp2-bprp1)/2
    plt.annotate('G', xy =(0,0),xytext =(val, yval),fontsize=16)

    bprp1=0.983
    bprp2=1.85
    if xmax<bprp2:
        bprp2=xmax
    plt.axvspan(bprp1,bprp2, alpha=alpha, color='#ffb177',zorder=1)#K
    val=bprp1+(bprp2-bprp1)/2
    plt.annotate('K', xy =(0,0),xytext =(val, yval),fontsize=16)

    bprp1=1.85
    bprp2=xmax #should be 4.86 but we are cropping to the plot bounds
    plt.axvspan(bprp1,bprp2, alpha=alpha, color='#ffa448',zorder=1)#M
    val=bprp1+(bprp2-bprp1)/2.5
    if xmax>1.8:
        plt.annotate('M', xy =(0,0),xytext =(val, yval),fontsize=16)
