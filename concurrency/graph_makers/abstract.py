import matplotlib.pyplot as plt
import seaborn as sns
from constants import max_value


def main(name: str):
    plt.ylim(0, max_value)

    dataset = sns.load_dataset(name, data_home="./data_home")
    ax = sns.barplot(data=dataset, x="movie",
                     y="count")
    ax.set(xlabel='Название фильма', ylabel='Количество проданных билетов')
    plt.xticks(rotation=20)
    plt.tight_layout()
    plt.savefig(f'images/{name}.png')
