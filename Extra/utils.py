def plot_corr_quality(x, y, df):
    """ 
    Returns a barplot using the x and y from the dataframe provided
    """
    fig = plt.figure(figsize = (10,6))
    sns.barplot(x = x, y = y, data = df).set_title(col)
    plt.show()