import json
import os


def track_access(selected_record):
    with open(os.environ['PATH_TO_HOSTS'], 'r') as f:
        data = json.load(f)

        # Check if the key exists in "accesses" section
        if selected_record['name'] in data["history"]:
            record_accesses = data["history"][selected_record['name']]
        else:
            # Create the key with default value 0
            record_accesses = 0

        record_accesses += 1

        data["history"][selected_record['name']] = record_accesses

    with open(os.environ['PATH_TO_HOSTS'], 'w') as f:
        json.dump(data, f, indent=4)
