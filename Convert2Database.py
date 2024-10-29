from urllib.parse import unquote
import random
import csv

def analysis(filepath, label):
    """
    Analyzes the URLs in the given file, processes them, and returns a list of URLs with their labels.

    Args:
        filepath (str): Path to the input file containing URLs.
        label (int): Label to assign to the URLs (1 for attack, 0 for normal).

    Returns:
        list: A list of processed URLs with their labels.
    """
    with open(filepath, "r") as file:
        lines = file.readlines()

    special_chars = r"+-*/.,:;'=()<>%&?@~\"#$_|"
    url_list = []

    for line in lines:
        line = unquote(line, encoding='latin-1').lower().strip()
        url = ""
        for char in line:
            if char not in special_chars:
                url += char
            else:
                url += f" {char} "
        url_list.append([url, label])

    return url_list

# Analyze and label URLs
url_attack = analysis("Dataset\cisc_anomalousTraffic_dataset.txt", 1)
url_normal = analysis("Dataset\cisc_normalTraffic_dataset.txt", 0)

# Combine and shuffle URLs
url_all = url_attack + url_normal
random.shuffle(url_all)

# Split data into training and testing sets (80% train, 20% test)
split_index = len(url_all) * 4 // 5
url_train = url_all[:split_index]
url_test = url_all[split_index:]

# Write training data to CSV
with open("Dataset\Dataset\Dataset_Train.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(url_train)

# Write testing data to CSV
with open("Dataset\Dataset\Dataset_Test.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(url_test)