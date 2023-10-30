import pyodbc
import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate

# Connect to the database
connection = pyodbc.connect(f'DRIVER={{SQL Server}};SERVER=DIDLERPC\SQLEXPRESS;DATABASE=TravelAgencyDB_zapros;Trusted_Connection=yes;')


sql_query = """
SELECT C.Id AS ClientId, C.FirstName, C.LastName, C.PhoneNumber, SUM(R.Price) AS TotalCost
FROM dbo.Client AS C
INNER JOIN dbo.Trip AS T ON C.Id = T.ClientId
INNER JOIN dbo.Route AS R ON T.RouteId = R.Id
GROUP BY C.Id, C.FirstName, C.LastName, C.PhoneNumber
"""

data = pd.read_sql(sql_query, connection)


fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))


ax1.bar(data['ClientId'], data['TotalCost'])
ax1.set_xlabel('Client ID')
ax1.set_ylabel('Total Cost')
ax1.set_title('Total Cost per Client')


table = tabulate(data, headers='keys', tablefmt='pretty', showindex=False)

# Display the table
ax2.text(0.01, 0.01, table, fontsize=10, transform=ax2.transAxes)

# Display the report with the chart and table
plt.tight_layout()
plt.show()  # Display the report in a GUI window
# plt.savefig('total_cost_per_client.png')  # Save the report as an image

# Optionally, you can also save the data to a CSV file for further analysis
data.to_csv('total_cost_per_client_data.csv', index=False)
