import psutil

def get_cpu_info():
    cpu_info = {}
    cpu_info["CPU Count"] = psutil.cpu_count(logical=False)
    cpu_info["Logical CPU Count"] = psutil.cpu_count(logical=True)
    cpu_info["CPU Frequency"] = psutil.cpu_freq().current
    return cpu_info

def get_memory_info():
    memory_info = {}
    virtual_memory = psutil.virtual_memory()
    memory_info["Total Memory"] = virtual_memory.total
    memory_info["Available Memory"] = virtual_memory.available
    memory_info["Used Memory"] = virtual_memory.used
    return memory_info

def get_disk_info():
    disk_info = {}
    partitions = psutil.disk_partitions()
    for partition in partitions:
        usage = psutil.disk_usage(partition.mountpoint)
        disk_info[partition.device] = {
            "Total Space": usage.total,
            "Used Space": usage.used,
            "Free Space": usage.free
        }
    return disk_info

def main():
    print("===== Hardware Data Analysis =====")
    
    cpu_info = get_cpu_info()
    print("\nCPU Information:")
    for key, value in cpu_info.items():
        print(f"{key}: {value}")
    
    memory_info = get_memory_info()
    print("\nMemory Information:")
    for key, value in memory_info.items():
        print(f"{key}: {value} bytes")
    
    disk_info = get_disk_info()
    print("\nDisk Information:")
    for device, details in disk_info.items():
        print(f"Device: {device}")
        for key, value in details.items():
            print(f"  {key}: {value} bytes")

if __name__ == "__main__":
    main()
