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

1. Clone the repo locally with `git clone https://github.com/bcbrookman/wireshark-profiles.git`
2. Launch Wireshark and navigate to "**Edit**" → "**[Configuration Profiles…](https://www.wireshark.org/docs/wsug_html_chunked/ChCustConfigProfilesSection.html#ChCustGUIConfigProfilesPage)**"
3. In the open "**Configuration Profiles…**" window, click the "**Import**" button, and select "**from directory**" in the dropdown menu
4. When the browse window opens, navigate to the location where you locally cloned the git repo
5. Highlight the cloned git repo, and click the "**Select Folder**" button to import all profiles in the directory
6. Lastly, click the "**OK**" button in the "**Configuration Profiles…**" window to confirm your changes
