# Wireshark Profiles

A collection of Wireshark profiles I've developed over time while frequently troubleshooting, and analzying network protocols.

## Features

These profiles aim to save time by applying some common configurations, and protocol specific customizations. In general, they include:

- The preferred split layout
- Protocol specific columns
- Quick filter buttons 
- Useful I/O graph presets
- Mostly default coloring rules
- Mostly default "decode as" rules
- A few other basic configs

## Installation

1. Download the latest `wireshark-profiles_bcbrookman_YYYY.MM.DD.zip` from [Releases](https://github.com/bcbrookman/wireshark-profiles/releases)
2. Launch Wireshark and navigate to "**Edit**" → "**[Configuration Profiles…](https://www.wireshark.org/docs/wsug_html_chunked/ChCustConfigProfilesSection.html#ChCustGUIConfigProfilesPage)**" in the menu bar
3. Click the "**Import**" button, and select "**From Zip File...**" in the dropdown menu
4. Navigate to and select the release zip file downloaded in step 1 to import the profiles
5. Finally, don't forget to click the "**OK**" button in the "**Configuration Profiles…**" window to confirm your changes

## Development

Development really just means making changes within Wireshark and exporting or copying profiles.

Whenever changes are saved, however, Wireshark also includes some unnecessary comments, line breaks, and user-specific settings which are undesirable in shared profiles (see [Wireshark Configuration Files](https://www.wireshark.org/docs/wsug_html_chunked/ChAppFilesConfigurationSection.html) for more). To exclude this unwanted content, a `.gitignore` and Python script, `.scripts/clean_conf_files.py`, are used.

A [Taskfile](https://taskfile.dev/) is also included to help automate this process and perform other common tasks.
To see a list of tasks available in the Taskfile, run `task --list`.
