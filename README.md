# System Information Tool

This Python tool displays key system information including the operating system, CPU details, and memory usage.

## Features

- OS details (type and version)
- CPU information (physical and logical cores, usage)
- Memory statistics (total, available, usage percentage)

## Requirements

- Python 3.x
- [`psutil`](https://pypi.org/project/psutil/)

## Installation

Install the required package using pip:

```bash
pip install psutil
```

## Usage

Run the script:

```bash
python system_info.py
```

You will see output similar to:

```
=== System Information ===
Operating System: Windows 10
Platform: Windows-10-10.0.19041-SP0

=== CPU Information ===
CPU Cores (Physical): 4
CPU Cores (Logical): 8
CPU Usage (%): 12.5

=== Memory Information ===
Total Memory (GB): 15.89
Available Memory (GB): 7.23
Used Memory (%): 54.5
```

## License

MIT License
