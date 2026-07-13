#!/usr/bin/env python3
"""
This helper script syncs Wireshark profiles between this repo and the local Wireshark config directory.
"""

import os
import sys
import shutil
import platform
from pathlib import Path

if sys.version_info.major < 3:
    raise EnvironmentError("Python 3 required!")


AUTHOR = "bcbrookman"
DEV_PROFLE_SUFFIX = f" ({AUTHOR}_dev)"
LOCAL_PROFILES_DIR = os.path.join(".", "profiles")


def get_wireshark_profiles_dir(custom_ws_profile_dir=None):
    system = platform.system()
    if custom_ws_profile_dir:
        return Path(custom_ws_profile_dir)
    elif system == "Windows":
        return Path(os.getenv("APPDATA")) / "Wireshark" / "profiles"
    elif system == "Darwin":  # macOS
        return Path.home() / ".config" / "wireshark" / "profiles"
    elif system == "Linux":
        return Path.home() / ".config" / "wireshark" / "profiles"
    else:
        print(f"Unknown OS: {system}. Set custom_ws_profile_dir instead!")
        sys.exit(1)


def push_profiles(src_dir, dst_dir):
    for item in Path(src_dir).iterdir():
        if item.is_dir():
            target_name = item.name + DEV_PROFLE_SUFFIX
            target_path = dst_dir / target_name
            if target_path.exists():
                shutil.rmtree(target_path)
            shutil.copytree(item, target_path)
            print(f"Pushed '{item}' to '{target_path}'")


def pull_profiles(src_dir, dst_dir):
    for item in Path(src_dir).iterdir():
        if item.is_dir() and item.name.endswith(DEV_PROFLE_SUFFIX):
            target_name = item.name.removesuffix(DEV_PROFLE_SUFFIX)
            target_path = dst_dir / target_name
            if target_path.exists():
                shutil.rmtree(target_path)
            shutil.copytree(item, target_path)
            print(f"Pulled '{target_path}' from '{item}'")


if __name__ == "__main__":

    try:
        custom_ws_profile_dir = sys.argv[2]
        ws_profiles_dir = get_wireshark_profiles_dir(custom_ws_profile_dir)
    except IndexError:
        ws_profiles_dir = get_wireshark_profiles_dir()

    try:
        action = sys.argv[1]
        if action == "push":
            push_profiles(Path(LOCAL_PROFILES_DIR).resolve(), ws_profiles_dir)
        elif action == "pull":
            pull_profiles(ws_profiles_dir, Path(LOCAL_PROFILES_DIR).resolve())
        else:
            raise ValueError("Must specify either 'push' or 'pull'")
    except (IndexError, ValueError) as err:
        print(f"ERROR: {err}")
        print("Usage: sync_profiles.py {push|pull} [/optional/custom/profiles/dir]")
        sys.exit(1)
