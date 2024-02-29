# Function 1: Parsing a .gal file
def read_gal_file(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()[1:]  
        gal_dict = {}
        for line in lines:
            parts = line.strip().split()
            id = int(parts[0])
            # There may be some rows that do not have neighbour information, so this needs to be dealt with
            neighbors = list(map(int, parts[1:])) if len(parts) > 1 else []
            gal_dict[id] = neighbors
    return gal_dict

# Function 2: Creating a histogram of the number of neighbours
def create_histogram(gal_dict):
    histogram = {}
    for id, neighbors in gal_dict.items():
        count = len(neighbors)
        if count not in histogram:
            histogram[count] = []
        histogram[count].append(id)
    return histogram

# Function 3: Detecting asymmetric neighbours
def test_asymmetries(gal_dict):
    asymmetries = []
    for id, neighbors in gal_dict.items():
        for neighbor in neighbors:
            if id not in gal_dict.get(neighbor, []):
                asymmetries.append((id, neighbor))
    return asymmetries
