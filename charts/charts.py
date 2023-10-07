import matplotlib.pyplot as plt

def generate_pie_charts():
    labels = ["a", "b", "c"]
    values = [200, 124, 40]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig("pie.png")
    plt.close()

generate_pie_charts()

