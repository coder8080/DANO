import matplotlib.pyplot as plt
import seaborn as sns
from constants import max_value


def main():
    plt.ylim(0, max_value)

    dataset_after = sns.load_dataset("after", data_home="./data_home")
    sns.barplot(data=dataset_after, x="weekday",
                y="count")
    plt.savefig('images/after.png')


if __name__ == '__main__':
    main()
