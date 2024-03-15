import matplotlib.pyplot as plt
import pymysql  # Assuming you're using SQL Server, adjust accordingly for other databases
import pandas as pd

# Connect to the SQL database
conn = pymysql.connect(host='localhost', user='root', password='P@ssw0rd', database='pulseanalytics')

# Query to retrieve the data (assuming the table name is 'your_table')
query = "SELECT MCV, DateColumn FROM cbc"

# Execute the query and fetch the results
data = pd.read_sql(query, conn)

# Close the connection
conn.close()

# Convert the DateColumn to datetime if it's not already
data['DateColumn'] = pd.to_datetime(data['DateColumn'])

# Plotting the graph
plt.figure(figsize=(5, 3))
plt.plot(data['DateColumn'], data['MCV'], marker='o', linestyle='-')
plt.title('MCV vs Time')
plt.xlabel('Time')
plt.ylabel('MCV')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.grid(True)
plt.tight_layout()
plt.show()