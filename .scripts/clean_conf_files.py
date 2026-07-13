#!/usr/bin/env python3
"""
This helper script cleans up Wireshark profile config files by removing commented, blank, and unnecessary lines.
"""

import os
import sys

if sys.version_info.major < 3:
    raise EnvironmentError("Python 3 required!")


def is_filtered(line_text):
    filter_rules = [
        {"condition": line_text in ["\n", "\r\n"], "filtered": True},
        {"condition": line_text.startswith("#"), "filtered": True},
    ]

    for rule in filter_rules:
        if rule["condition"]:
            return rule["filtered"]


if __name__ == "__main__":

    profiles_dir = os.path.join(".", "profiles")

    for root, dirs, files in os.walk(profiles_dir):
        if root != profiles_dir:  # Filter out excluded directories
            for conf_file in files:
                conf_file_path = os.path.join(root, conf_file)

                # Read the current file, and exclude any lines matching is_filtered() filter rules
                with open(conf_file_path, "r", newline="") as current_file:
                    unfiltered_lines = []
                    for line in current_file:
                        if is_filtered(line):
                            continue
                        else:
                            unfiltered_lines.append(line)

                # Open the current file again, replacing its contents with only the remaining unfiltered lines
                with open(conf_file_path, "w", newline="") as current_file:
                    current_file.writelines(unfiltered_lines)

                # Delete the current file, if now empty
                if (
                    os.path.isfile(conf_file_path)
                    and os.path.getsize(conf_file_path) == 0
                ):
                    os.remove(conf_file_path)
