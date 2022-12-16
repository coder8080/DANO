import matplotlib.pyplot as plt
import seaborn as sns
from constants import max_value


def main():
    plt.ylim(0, max_value)
    dataset_during = sns.load_dataset("during", data_home="./data_home")
    sns.barplot(data=dataset_during, x="weekday",
                y="count")
    plt.savefig('images/during.png')


if __name__ == '__main__':
    main()
