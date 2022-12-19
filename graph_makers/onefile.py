import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib

params = {"ytick.color": "w",
          "xtick.color": "w",
          "axes.labelcolor": "w",
          "axes.edgecolor": "w"}
plt.rcParams.update(params)

palette = ['#CBEDD5', '#97DECE', '#62B6B7']


def main():
    matplotlib.rcParams['savefig.transparent'] = True
    dataset = sns.load_dataset(
        'result', data_home="./data_home")
    ax = sns.barplot(data=dataset, x="weekday",
                     y="count", hue='Время', palette=palette)
    ax.set(xlabel='День недели', ylabel='Заказы в день на население')
    plt.xticks(rotation=20)
    plt.tight_layout()
    plt.savefig(f'images/onefile.png')


if __name__ == '__main__':
    main()
