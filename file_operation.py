# #file operations
# def file_operations(key, value):
#     with open("hi.txt", "r") as file:
#         lines = file.readline()

#     with open("hi.txt", "w") as file:
#         for line in lines:
#             if key in line:
#                 file.write(key + "=" + value + "\n")
#             else:
#                 file.write(line)

# file_operations("123", "dushyant")

def update_server_config(file_path, key, value):
    """
    Update a specific key-value pair in a configuration file.

    Parameters:
    - file_path (str): Path to the configuration file.
    - key (str): The key to be updated.
    - value (str): The new value to set for the key.

    Returns:
    - None

    This function reads the content of the specified configuration file, searches for
    the provided key, and updates its corresponding value. The updated content is then
    written back to the file.

    Example:
    update_server_config("server.conf", "MAX_CONNECTIONS", "1200")
    """
    # Read the content of the file
    with open(file_path, "r") as file:
        lines = file.readlines()

    # Write back the updated content to the file
    with open(file_path, "w") as file:
        for line in lines:
            if key in line:
                # Update the line with the new key-value pair
                file.write(key + "=" + value + "\n")
            else:
                # Keep the original line unchanged
                file.write(line)

# Example usage
update_server_config("hi.txt", "MAX_CONNECTIONS", "2000")