import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib

params = {"ytick.color": "w",
          "xtick.color": "w",
          "axes.labelcolor": "w",
          "axes.edgecolor": "w"}
plt.rcParams.update(params)


def main(name):
    lim = None
    if name == 'before':
        lim = 250
    elif name == 'during':
        lim = 25
    elif name == 'after':
        lim = 50
    plt.ylim(0, lim)
    matplotlib.rcParams['savefig.transparent'] = True

    dataset = sns.load_dataset(name, data_home="./data_home")
    ax = sns.barplot(data=dataset, x="weekday",
                     y="count")
    ax.set(xlabel='День недели', ylabel='Заказы в день на население')
    plt.xticks(rotation=20)
    plt.tight_layout()
    plt.savefig(f'images/{name}.png')
