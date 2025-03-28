import matplotlib.pyplot as plt

for i in range(4):
    filename = f"output/{i}__output.txt"
    with open(filename, "r") as f:
        values = [float(line.strip()) for line in f]

    plt.figure()
    plt.plot(range(len(values)), values)
    plt.xlabel("Iteration")
    plt.ylabel("Value")
    plt.title(f"Loss vs iteration plot for {i}th node.")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"{i}_node_loss.png")  # Saves the figure
    plt.close()


plt.show()
