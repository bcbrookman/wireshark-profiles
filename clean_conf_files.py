"""
This helper script cleans up Wireshark profile config files by removing commented, blank, and unnecessary lines.
"""

import os


def is_filtered(line_text):
    filter_rules = [
        {
            "condition": line_text in ['\n', '\r\n'],
            "filtered": True
        },
        {
            "condition": line_text.startswith("#"),
            "filtered": True
        },
    ]

    for rule in filter_rules:
        if rule["condition"]:
            return rule["filtered"]


if __name__ == "__main__":

    profiles_dir = os.path.join(".", "profiles")
    build_dir = os.path.join(".", ".build")
    output_dir = os.path.join(".", ".output")

    for root, dirs, files in os.walk(profiles_dir):
        if root != profiles_dir:  # Filter out excluded directories
            for conf_file in files:
                # Read the current file, and exclude any lines matching is_filtered() filter rules
                with open(os.path.join(root, conf_file), "r", newline="") as current_file:
                    unfiltered_lines = []
                    for line in current_file:
                        if is_filtered(line):
                            continue
                        else:
                            unfiltered_lines.append(line)

                # Open the current file again, replacing its contents with only the remaining unfiltered lines
                with open(os.path.join(root, conf_file), "w", newline="") as current_file:
                    current_file.writelines(unfiltered_lines)
