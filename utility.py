def plotter(r,c,vals):
    a=0
    fig,ax=plt.subplots(figsize=(25,15),nrows=r,ncols=c)
    plt.tight_layout(h_pad=1)
    for i in range(r):
        for j in range(c):
            if a==len(vals):
                break
            else:
                sns.countplot(df[list(vals)[a]],ax=ax[i][j])
                a+=1
    