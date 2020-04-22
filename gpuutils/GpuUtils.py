import os
import json
import pandas as pd
import subprocess

#---------------------------------

def analyzeSystem(pandas_format = True, mock_response = None):
	
	gpu_indexes = []
	memory_usage_percentages = []; available_memories = []; total_memories = []
	utilizations = []
	power_usages = []; power_capacities = []
	
	try:
		if mock_response == None:
			result = subprocess.check_output(['nvidia-smi']) #result is bytes
			dashboard = result.decode("utf-8").split("=|")
		else:
			mock_response = mock_response.replace("\t", " ")
			dashboard = mock_response.split("=|")
			
		dashboard = dashboard[1].split("\n")
		
		#print(dashboard)
		
		gpu_idx = 0
		for line in dashboard:
			if ("MiB" in line):
				power_info = line.split("|")[1]
				power_capacity = int(power_info.split("/")[-1].replace("W", ""))
				power_usage = int((power_info.split("/")[-2]).strip().split(" ")[-1].replace("W", ""))
				
				power_usages.append(power_usage)
				power_capacities.append(power_capacity)
				
				#----------------------------
				
				memory_info = line.split("|")[2].replace("MiB","").split("/")
				utilization_info = int(line.split("|")[3].split("%")[0])
				
				allocated = int(memory_info[0])
				total_memory = int(memory_info[1])
				available_memory = total_memory - allocated
				
				total_memories.append(total_memory)
				available_memories.append(available_memory)
				memory_usage_percentages.append(round(100*int(allocated)/int(total_memory), 4))
				utilizations.append(utilization_info)
				gpu_indexes.append(gpu_idx)
				
				gpu_idx = gpu_idx + 1
				
	except Exception as err:
		print("there are no GPUs on your system (", str(err), ")")
		
	#------------------------------
	
	if pandas_format:
		
		df = pd.DataFrame(gpu_indexes, columns = ["gpu_index"])
		df["total_memories_in_mb"] = total_memories
		df["available_memories_in_mb"] = available_memories
		df["memory_usage_percentage"] = memory_usage_percentages
		df["utilizations"] = utilizations
		df["power_usages_in_watts"] = power_usages
		df["power_capacities_in_watts"] = power_capacities
		
		df = df.sort_values(by = ["available_memories_in_mb"], ascending = False).reset_index(drop = True)
		
		return df
	
	else: #json format
		
		resp_obj = {}
		
		#resp_obj["gpu_count"] = len(memory_usage_percentages)
		resp_obj["gpu_index"] = gpu_indexes
		resp_obj["total_memories_mb"] = total_memories
		resp_obj["available_memories_in_mb"] = available_memories
		resp_obj["memory_usage_percentage"] = memory_usage_percentages
		resp_obj["utilizations"] = utilizations
		resp_obj["power_usages_in_watts"] = power_usages
		resp_obj["power_capacities_in_watts"] = power_capacities
		
		return resp_obj
		
#---------------------------------

def allocate(required_memory = 1024, gpu_count = 1, framework = None):
	
	if gpu_count < 1:
		raise ValueError("You must pass a positive value for gpu count but you passed ", gpu_count)
	
	df = analyzeSystem(pandas_format = True)
	
	if df.shape[0] == 0:
		print("No GPU found on your system!")
	else:
		df = df[(df.available_memories_in_mb > required_memory)]

		if df.shape[0] >= gpu_count:
			reserved_gpus = df.iloc[0:gpu_count].gpu_index.values

			devices = ""
			for i in range(0, len(reserved_gpus)):
				idx = reserved_gpus[i]

				if i > 0:
					devices += ","

				devices += str(idx)
				
			if gpu_count == 1:
				print("GPU ", end='')
			elif gpu_count > 1:
				print("GPUs ", end='')

			print(devices, " will be allocated")

			os.environ["CUDA_VISIBLE_DEVICES"] = devices
			
			#----------------------------------
			#avoid greedy approach based on framework
			
			if framework.lower() == "keras":
				
				import tensorflow as tf
				import keras
				config = tf.ConfigProto()
				config.gpu_options.allow_growth = True
				session = tf.Session(config=config)
				keras.backend.set_session(session)
				
				print("Allow growth option in Keras is set to True to avoid to allocate all memory")
			
			elif framework.lower() == "tensorflow":
				import tensorflow as tf
				config = tf.ConfigProto()
				config.gpu_options.allow_growth = True
				session = tf.Session(config=config)
				
				print("Allow growth option in TensorFlow is set to True to avoid to allocate all memory")
				
			#----------------------------------

		else:
			print("Unavavailable resources. You will continue to work on CPU.")
			os.environ["CUDA_VISIBLE_DEVICES"] = ""

#---------------------------------