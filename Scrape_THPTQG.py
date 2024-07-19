import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
import time

# Update the path to msedgedriver if necessary
edge_service = EdgeService(executable_path=r"D:\code\vsc\msedgedriver.exe")  # Replace with the correct path if necessary
driver = webdriver.Edge(service=edge_service)

# Open the website
driver.get('http://tracuudiem.langson.edu.vn/?fbclid=IwZXh0bgNhZW0CMTEAAR1C1zUz7PDPKVDxWWAHGhxi8iKizEhV3ctnA86ZA5JK_pw23flLp8VtuVE_aem_RUn1CLLwl_qBMRrSWejk_w')

# Prepare the CSV file
with open('TeST.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Number', 'Result'])

    # Loop through the specified range
    for number in range(10000001, 10000002):
        # Find the input field and enter the number
        input_field = driver.find_element(By.ID, 'search_text')
        input_field.clear()
        input_field.send_keys(str(number))
        
        # Execute the JavaScript function to submit the form
        driver.execute_script("eventSearch()")
        
        # Wait for the results to load (adjust the sleep duration as needed)
        time.sleep(2)
        
        # Extract the results
        result = driver.find_element(By.ID, 'search_result').text
        print(f'Result for {number}: {result}')
        
        # Write the result to the CSV file
        writer.writerow([number, result])

# Close the driver
driver.quit()
