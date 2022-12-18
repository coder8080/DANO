import matplotlib.pyplot as plt
import seaborn as sns
from constants import max_value


def main(name):
    # plt.ylim(0, max_value)

    dataset = sns.load_dataset(name, data_home="./data_home")
    ax = sns.barplot(data=dataset, x="weekday",
                     y="count")
    ax.set(xlabel='День недели', ylabel='Заказы в день на население')
    plt.xticks(rotation=20)
    plt.tight_layout()
    plt.savefig(f'images/{name}.png')
