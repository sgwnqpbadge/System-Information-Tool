import platform
import psutil

def get_os_info():
    print("Operating System:", platform.system(), platform.release())
    print("Platform:", platform.platform())

def get_cpu_info():
    print("CPU Cores (Physical):", psutil.cpu_count(logical=False))
    print("CPU Cores (Logical):", psutil.cpu_count(logical=True))
    print("CPU Usage (%):", psutil.cpu_percent(interval=1))

def get_memory_info():
    mem = psutil.virtual_memory()
    print("Total Memory (GB):", round(mem.total / (1024 ** 3), 2))
    print("Available Memory (GB):", round(mem.available / (1024 ** 3), 2))
    print("Used Memory (%):", mem.percent)

def display_system_info():
    print("=== System Information ===")
    get_os_info()
    print("\n=== CPU Information ===")
    get_cpu_info()
    print("\n=== Memory Information ===")
    get_memory_info()

if __name__ == "__main__":
    display_system_info()
