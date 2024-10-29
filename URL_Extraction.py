# Function to extract URLs
def extract(data_path, file_save):
    
    # Open and read data in the input file
    with open(data_path,"r") as file:
        lines = file.readlines()

    urls = []           # List to store extracted URLs
    post = []           # List to temporarily store lines related to POST requests
    post_flag = False   # Flag to indicate if a POST request is being processed

    for line in lines:
        # GET request
        if line.startswith("GET"):
            url = line.split(" ")
            urls.append(url[1].strip(' \n'))
            
        # POST request
        if line.startswith("POST"):
            post_flag = True
            
        if post_flag: 
            post.append(line)       # Add a line until the word "End" appears
            
        if post_flag & line.startswith("End") :
            post_cut = post[0].split(" ")
            url = post_cut[1] + post[-3]        # Request + id
            urls.append(url.strip(' \n'))
            post.clear()
            post_flag = False

    # Remove duplicate URLs by converting the list to a set and back to a list
    new_urls = list(set(urls))
    
    # Open and write result to the output file
    with open(file_save,"w") as file:
        for url in new_urls:   
            file.write(url.lstrip('https://')+ "\n")

extract("Database\dataset_cisc_train_test\cisc_anomalousTraffic_test.txt", "Dataset\cisc_anomalousTraffic_dataset.txt")
extract("Database\dataset_cisc_train_test\cisc_normalTraffic_test.txt", "Dataset\cisc_normalTraffic_dataset.txt")