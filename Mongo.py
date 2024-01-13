from pymongo import MongoClient

# MongoDB connection string
mongo_connection_string = "mongodb+srv://DevilGood:DevilGood@cluster0.v8o3kr8.mongodb.net/?retryWrites=true&w=majority"

# Connect to MongoDB
client = MongoClient(mongo_connection_string)

# Select or create a database (replace 'your_database' with the desired database name)
db = client['your_database']

# Create or select a collection (replace 'your_collection' with the desired collection name)
collection = db['your_collection']

# Sample data to save
sample_data = [
    {"name": "John", "age": 25},
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 28}
]

# Insert data into the collection
collection.insert_many(sample_data)

# Retrieve and display all data from the collection
all_data = collection.find()

print("All Data:")
for data in all_data:
    print(data)

# Close the MongoDB connection
client.close()
