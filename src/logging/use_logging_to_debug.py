# Instrucitons -
# 1.What does the code do? Fix it so it will work
# 2.Use prints to show the execution of the program
# 3.Use prints for each edge case that you can think of. call the instructor when you are done.
# 4.Replace these prints with logs with a matching log level, to stdout using logging
# 5.Add a file logger to the code
# 6.Add an id parameter to the configuration, and create the log file name using that id parameter
# (what happens when loading the configuration fails?)
# 7. run three instances of you code using different configurations and ids
# 8. Create a bash script that prints only the critical errors out of the three log files

import os
import time
import json


def watch_directory():
    current_config = {}

    while True:
        # Load the configuration every loop iteration
        with open('config.json', 'r') as f:
            new_config = json.load(f)

        # If the configuration has changed, update it
        if new_config != current_config:
            source_directory = new_config["source_directory"]
            destination_directory = new_config["destination_directory"]

            if not os.path.exists(source_directory):
                continue

            # Update the current configuration
            current_config = new_config
            already_existing_files = set(os.listdir(source_directory))


        time.sleep(2)

        current_files = set(os.listdir(source_directory))
        new_files = current_files - already_existing_files

        if new_files:
            for new_file in new_files:
                new_file_path = os.path.join(source_directory, new_file)

                if not os.path.exists(destination_directory):
                    os.makedirs(destination_directory)

                os.rename(new_file_path, os.path.join(destination_directory, new_file))

        already_existing_files = current_files


if __name__ == "__main__":
    watch_directory()
