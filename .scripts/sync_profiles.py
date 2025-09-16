#!/usr/bin/env python3
import os
import sys
import shutil
import platform
from pathlib import Path

AUTHOR = "bcbrookman"
DEV_PROFLE_SUFFIX = f" ({AUTHOR}_dev)"
PROFILES_DIR = os.path.join(".", "profiles")

def get_wireshark_profiles_dir():
    system = platform.system()
    if system == "Windows":
        return Path(os.getenv("APPDATA")) / "Wireshark" / "profiles"
    elif system == "Darwin":  # macOS
        return Path.home() / ".config" / "wireshark" / "profiles"
    elif system == "Linux":
        return Path.home() / ".config" / "wireshark" / "profiles"
    else:
        print(f"Unsupported OS: {system}")
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

def main():
    if len(sys.argv) != 2 or sys.argv[1] not in ["push", "pull"]:
        print("Usage: sync_profiles.py [push|pull]")
        sys.exit(1)

    action = sys.argv[1]
    ws_profiles_dir = get_wireshark_profiles_dir()

    if action == "push":
        push_profiles(Path(PROFILES_DIR).resolve(), ws_profiles_dir)
    elif action == "pull":
        pull_profiles(ws_profiles_dir, Path(PROFILES_DIR).resolve())

if __name__ == "__main__":
    main()
