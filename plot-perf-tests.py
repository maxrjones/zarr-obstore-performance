import pandas as pd
import matplotlib.pyplot as plt

# Read the data
data = pd.read_csv("timings.csv")

# Set up the plot
plt.figure(figsize=(7, 5))

# Colors and markers for the libraries
colors = {"fsspec": "darkorchid", "obstore": "darkorange"}
markers = {"fsspec": "o", "obstore": "d"}

# Plot each library
for lib in ["fsspec", "obstore"]:
    lib_data = data[data["library"] == lib]

    # Plot each individual data point
    for concurrency in sorted(lib_data["concurrency"].unique()):
        concurrency_data = lib_data[lib_data["concurrency"] == concurrency]

        x_values = [concurrency] * len(concurrency_data)

        plt.scatter(
            x_values,
            concurrency_data["execution_time"],
            color=colors[lib],
            marker=markers[lib],
            s=60,
            alpha=0.7,
            label=f"{lib} (concurrency={concurrency})"
            if lib_data["concurrency"].eq(concurrency).any()
            else None,
        )

# Set the scale for x-axis to log scale since concurrency values span orders of magnitude
plt.grid(True, which="both", ls="-", alpha=0.2)

# Labels and title
plt.xlabel("Concurrency", fontsize=12)
plt.ylabel("Time (s)", fontsize=12)

# Create a more concise legend
handles, labels = plt.gca().get_legend_handles_labels()
by_label = dict(zip(labels, handles))
filtered_labels = [
    label
    for label in labels
    if label.startswith("fsspec (concurrency=10)")
    or label.startswith("obstore (concurrency=10)")
]
filtered_handles = [by_label[label] for label in filtered_labels]
plt.legend(
    [by_label["fsspec (concurrency=10)"], by_label["obstore (concurrency=10)"]],
    ["FSSpec-backed store", "Obstore-backed store"],
    fontsize=10,
    loc="upper right",
)
plt.title("Loading a 10 GB array using Zarr Python 3.0", fontsize=14)

# Show the concurrency values on x-axis
plt.xticks(data["concurrency"].unique())

# Ensure y-axis starts at 0 for better visual comparison
plt.ylim(bottom=0)

# # Add a text annotation with summary statistics
# for lib in ['fsspec', 'obstore']:
#     stats_text = ""
#     lib_data = data[data['library'] == lib]
#     for concurrency in sorted(lib_data['concurrency'].unique()):
#         concurrency_data = lib_data[lib_data['concurrency'] == concurrency]
#         median = concurrency_data['execution_time'].median()
#         stats_text += f"Concurrency {concurrency}: {median:.1f}s median\n"

#     text_x = 0.02 if lib == 'fsspec' else 0.75
#     plt.figtext(text_x, 0.02, f"{lib} summary:\n{stats_text}", fontsize=8,
#                 bbox=dict(facecolor=colors[lib], alpha=0.1))

# # Tight layout to optimize spacing
# plt.tight_layout()

# Save figure
plt.savefig("zarr_performance_comparison.png", dpi=300)
