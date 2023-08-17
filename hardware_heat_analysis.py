import random
import time
import pandas as pd

# Simulate hardware data collection
def collect_hardware_data(node_id):
    data = {
        'Node ID': node_id,
        'CPU Temperature': random.uniform(40, 80),
        'Memory Usage (%)': random.uniform(20, 90),
        'Disk Usage (%)': random.uniform(10, 80),
        'Network Traffic (Mbps)': random.uniform(100, 1000)
    }
    return data

# Main monitoring loop
def main():
    num_nodes = 10
    monitoring_interval = 5  # seconds
    
    while True:
        hardware_data = []
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        
        for node_id in range(1, num_nodes + 1):
            node_data = collect_hardware_data(node_id)
            hardware_data.append(node_data)
        
        # Create a DataFrame from collected data
        df = pd.DataFrame(hardware_data)
        df['Timestamp'] = timestamp
        
        # Perform analysis on the data
        avg_temp = df['CPU Temperature'].mean()
        max_memory_usage = df['Memory Usage (%)'].max()
        
        print(f"===== Hardware Health Analysis ({timestamp}) =====")
        print(f"Average CPU Temperature: {avg_temp:.2f}°C")
        print(f"Max Memory Usage: {max_memory_usage:.2f}%")
        
        # Save data to a CSV file
        df.to_csv('hardware_health_data.csv', mode='a', header=False, index=False)
        
        time.sleep(monitoring_interval)

if __name__ == "__main__":
    main()
