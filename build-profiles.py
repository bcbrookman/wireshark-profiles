"""
This helper script creates an importable profile bundle.
"""

import datetime
import os
import shutil


if __name__ == "__main__":

    author = "bcbrookman"
    date_str = datetime.date.today().strftime("%Y.%m.%d")

    git_dir = os.path.join(".",".git")
    build_dir = os.path.join(".", ".build")
    output_dir = os.path.join(".", ".output")
    excluded_dirs = (git_dir, build_dir, output_dir)

    for root, dirs, files in os.walk("."):  # Finds all files under the current working directory
        if not root.startswith(excluded_dirs) and root != ".":  # Filter out excluded directories
            shutil.copytree(root, f"{build_dir}/{root} ({author}_{date_str})")

    shutil.make_archive(f"{output_dir}/wireshark-profiles_{author}_{date_str}", "zip", build_dir)
    shutil.rmtree(build_dir)
