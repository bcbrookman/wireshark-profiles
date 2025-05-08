"""
This helper script creates an importable profile bundle.
"""

import datetime
import os
import shutil


if __name__ == "__main__":

    author = "bcbrookman"
    date_str = datetime.date.today().strftime("%Y.%m.%d")

    profiles_dir = os.path.join(".", "profiles")
    build_dir = os.path.join(".", ".build")
    output_dir = os.path.join(".", ".output")
    
    for root, dirs, files in os.walk(profiles_dir):
        if root != profiles_dir:
            shutil.copytree(root, f"{build_dir}/{root} ({author}_{date_str})")

    shutil.make_archive(f"{output_dir}/wireshark-profiles_{author}_{date_str}", "zip", build_dir)
    shutil.rmtree(build_dir)
