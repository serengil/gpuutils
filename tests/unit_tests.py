from gpuutils import GpuUtils
import pandas as pd

#------------------------------

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

#------------------------------

print("GPU analysis of a machine have 8 GPUs")

mock_response = 'Tue Apr 21 09:58:12 2020	   \n+-----------------------------------------------------------------------------+\n| NVIDIA-SMI 418.67	   Driver Version: 418.67	   CUDA Version: 10.1	 |\n|-------------------------------+----------------------+----------------------+\n| GPU  Name		Persistence-M| Bus-Id		Disp.A | Volatile Uncorr. ECC |\n| Fan  Temp  Perf  Pwr:Usage/Cap|		 Memory-Usage | GPU-Util  Compute M. |\n|===============================+======================+======================|\n|   0  Tesla V100-SXM2...  Off  | 00000000:15:00.0 Off |				  N/A |\n| N/A   34C	P0	56W / 300W |   1280MiB / 32480MiB |	  0%	  Default |\n+-------------------------------+----------------------+----------------------+\n|   1  Tesla V100-SXM2...  Off  | 00000000:16:00.0 Off |					0 |\n| N/A   34C	P0	43W / 300W |	 11MiB / 32480MiB |	  0%	  Default |\n+-------------------------------+----------------------+----------------------+\n|   2  Tesla V100-SXM2...  Off  | 00000000:3A:00.0 Off |					0 |\n| N/A   33C	P0	41W / 300W |	 11MiB / 32480MiB |	  0%	  Default |\n+-------------------------------+----------------------+----------------------+\n|   3  Tesla V100-SXM2...  Off  | 00000000:3B:00.0 Off |					0 |\n| N/A   35C	P0	42W / 300W |	 11MiB / 32480MiB |	  0%	  Default |\n+-------------------------------+----------------------+----------------------+\n|   4  Tesla V100-SXM2...  Off  | 00000000:89:00.0 Off |					0 |\n| N/A   31C	P0	42W / 300W |	 11MiB / 32480MiB |	  0%	  Default |\n+-------------------------------+----------------------+----------------------+\n|   5  Tesla V100-SXM2...  Off  | 00000000:8A:00.0 Off |					0 |\n| N/A   33C	P0	41W / 300W |	 11MiB / 32480MiB |	  0%	  Default |\n+-------------------------------+----------------------+----------------------+\n|   6  Tesla V100-SXM2...  Off  | 00000000:B2:00.0 Off |					0 |\n| N/A   33C	P0	43W / 300W |	 11MiB / 32480MiB |	  0%	  Default |\n+-------------------------------+----------------------+----------------------+\n|   7  Tesla V100-SXM2...  Off  | 00000000:B3:00.0 Off |					0 |\n| N/A   33C	P0	43W / 300W |	 11MiB / 32480MiB |	  0%	  Default |\n+-------------------------------+----------------------+----------------------+\n																			   \n+-----------------------------------------------------------------------------+\n| Processes:													   GPU Memory |\n|  GPU	   PID   Type   Process name							 Usage	  |\n|=============================================================================|\n+-----------------------------------------------------------------------------+\n'

df = GpuUtils.analyzeSystem(mock_response = mock_response)

print(type(df))
print(df)

required_memory = 10000
gpu_count = 1

df = df[(df.available_memories_in_mb > required_memory)]


print("--------------------------------------------")

print("GPU analysis of this machine:")
GpuUtils.analyzeSystem()

print("--------------------------------------------")

print("Allocate GPU on this machine")

GpuUtils.allocate()
