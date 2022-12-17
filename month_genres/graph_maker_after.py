import matplotlib.pyplot as plt
import seaborn as sns


def main():
    plt.ylim(0, 70)

    dataset_after = sns.load_dataset("after", data_home="./data_home")
    sns.barplot(data=dataset_after, x="genre",
                y="count", palette=['#845b53', '#3a923a', '#3274a1', '#e1812c', '#c03d3e'])
    plt.savefig('images/after.png')


if __name__ == '__main__':
    main()
