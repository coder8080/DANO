import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib


def main():
    dataset = sns.load_dataset("result", data_home="./data_home")
    ax = sns.lineplot(data=dataset, x="timepoint",
                      y="price")
    ax.set(xlabel='Время (2020 год)', ylabel='Цена билета')
    # plt.xticks(rotation=20)
    ax.axvspan(69, 174, color='green', alpha=0.2)
    matplotlib.rcParams['savefig.transparent'] = True
    plt.tight_layout()
    plt.savefig(f'images/result.png')


if __name__ == '__main__':
    main()
