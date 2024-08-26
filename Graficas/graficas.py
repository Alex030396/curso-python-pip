import matplotlib.pyplot as plt

def grafica_pie():
    labels = ['A','B','C']
    values = [200,30,150]
    
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig('pie.png')
    plt.close()