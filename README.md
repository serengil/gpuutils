# GpuUtils

Working on a shared environment with multiple GPUs might be problematic. Advanced frameworks apply greedy approach and they tend to allocate all GPUs and all memory of your system. GpuUtils helps you to find the best GPU on your system to allocate. It also provides a gpu related information in a structure format.

## What GpuUtils Offer

Regular frameworks tend to allocate GPU memory.

<p align="center"><img src="https://raw.githubusercontent.com/serengil/gpuutils/master/demo/gpuutils-off.png" width="95%" height="95%"></p>

Enabling GpuUtils provides you not to use GPU resources greedy

<p align="center"><img src="https://raw.githubusercontent.com/serengil/gpuutils/master/demo/gpuutils-on.png" width="95%" height="95%"></p>

## Installation

The easiest way to install GpuUtils is to install it via [PyPI](https://pypi.org/project/gpuutils).

```
pip install gpuutils
```

## Analyzing system

Running **nvidia-smi** command in the command prompt allows users to monitor GPU related information such as memory and utilization. Herein, system analysis function loads GPU related information into a pandas data frame or json array.

```python
from gpuutils import GpuUtils
df = GpuUtils.analyzeSystem() #this will return a pandas data frame
#dict = GpuUtils.analyzeSystem(pandas_format = False) #this will return a json array
```

Default configuration of system analysis returns a Pandas data frame.

| gpu_index | total_memories_in_mb | available_memories_in_mb | memory_usage_percentage | utilizations | power_usages_in_watts | power_capacities_in_watts |
| ---       | ---                  | ---                      | ---                     | ---          | ---                   | ---                       |
| 1         | 32480                | 32469                    | 0.0339                  | 0            | 43                    | 300                       |
| 2         | 32480                | 32469                    | 0.0339                  | 0            | 43                    | 300                       |
| 3         | 32480                | 32469                    | 0.0339                  | 0            | 44                    | 300                       |
| 4         | 32480                | 32469                    | 0.0339                  | 0            | 43                    | 300                       |
| 5         | 32480                | 32469                    | 0.0339                  | 0            | 43                    | 300                       |
| 6         | 32480                | 32469                    | 0.0339                  | 0            | 43                    | 300                       |
| 7         | 32480                | 32469                    | 0.0339                  | 0            | 43                    | 300                       |
| 0         | 32480                | 31031                    | 4.4612                  | 7            | 56                    | 300                       |

## Allocation

GpuUtils can allocate GPUs as well. Calling allocation function directly finds the available GPUs and allocate based on your demand.

```python
from gpuutils import GpuUtils
GpuUtils.allocate() #this tries to allocate a GPU having 1GB memory
#GpuUtils.allocate(required_memory = 10000)
#GpuUtils.allocate(required_memory = 10000, gpu_count=1)
```

# To avoid greedy approach

Advanced frameworks such as TensorFlow tend to allocate all memory. You can avoid this approach if you pass the framework argument in allocate function. In this way, the framework will use the gpu memory as much as needed. Currently, keras and tensorflow frameworks are supported in allocate function.

```python
GpuUtils.allocate(framework = 'keras')
```

# Support

There are many ways to support a project - starring⭐️ the GitHub repos is just one.

# Licence

GpuUtils is licensed under the MIT License - see [`LICENSE`](https://github.com/serengil/gpuutils/blob/master/LICENSE) for more details.
