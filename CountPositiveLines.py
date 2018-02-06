import os
from CountWorker import *
from commands import getoutput


class CountPositiveLines:

    def __init__(self):
        pass

    @staticmethod
    def get_positive_files(base_dir, file_pattern):

        file_name_list = []

        # base + folder name + file name
        folder_name_list = getoutput("ls -d " + base_dir + file_pattern).split('\n')

        # Queries all the folders that match the input naming rules
        for i in range(len(folder_name_list)):

            file_name_list_array = getoutput("ls " + folder_name_list[i]).split('\n')

            # Get all the file names
            for file_name in file_name_list_array:
                file_path_temp_array = [os.path.join(folder_name_list[i], file_name)]

                file_name_list += file_path_temp_array

        return file_name_list

    # Entrance
    @staticmethod
    def count_folder_positive_line(base_dir, file_pattern, num_threads=1):

        # Generate the full path to all files within the matched folder under the base path
        file_name_list = CountPositiveLines.get_positive_files(base_dir, file_pattern)

        # Counter Calculates the number of positive lines it counts in the data processed by each thread
        counter = [0] * num_threads

        num_files = len(file_name_list)
        # limited thread numbers
        partition_size = num_files // num_threads
        worker_list = [None] * num_files

        for i in range(num_threads):

            # i is present counter index
            worker_list[i] = CountWorker(file_name_list[i * partition_size:(i + 1) * partition_size], counter, i)
            worker_list[i].start()

        # Wait for thread processing finish
        for i in range(num_threads):

            worker_list[i].join()

        total_count = 0

        # Calculate the total number of positives
        for i in range(len(counter)):
            total_count += counter[i]

        return total_count
