import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib

params = {"ytick.color": "w",
          "xtick.color": "w",
          "axes.labelcolor": "w",
          "axes.edgecolor": "w"}
plt.rcParams.update(params)


def main(name):
    matplotlib.rcParams['savefig.transparent'] = True

    dataset = sns.load_dataset(name, data_home="./data_home")
    ax = sns.barplot(data=dataset, x="week",
                     y="percent")
    # ax.set(xlabel='День недели', ylabel='Заказы в день на население')
    # plt.xticks(rotation=20)
    # plt.tight_layout()
    plt.savefig(f'images/{name}.png')
