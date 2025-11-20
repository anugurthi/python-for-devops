def update_server_config(file_path, key, value):
    """
    Reads a config file, updates a specific key with a new value, and saves it.
    """
    # Step 1: Read the existing content
    # 'r' means read mode
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Step 2: Write the changes back
    # 'w' means write mode (this overwrites the file!)
    with open(file_path, 'w') as file:
        for line in lines:
            # Check if this line contains the key we want to change
            if key in line:
                # Write the new value instead of the old line
                file.write(key + "=" + value + "\n")
            else:
                # If it's not the key we're looking for, write the line exactly as it was
                file.write(line)

# Path to the server configuration file
server_config_file = 'server.conf'

# Key and new value for updating the server configuration
key_to_update = 'MAX_CONNECTIONS'
new_value = '600'  # New maximum connections allowed

# Update the server configuration file
update_server_config(server_config_file, key_to_update, new_value)
print(f"Updated {key_to_update} to {new_value} in {server_config_file}")

