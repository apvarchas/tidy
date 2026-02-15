# tidy

A simple command line tool that organizes files in a folder by type.

## Features
- Groups files into folders (Images, Documents, Videos, Audio, Others)
- Works on any directory
- Safe: never deletes files

## Installation
pip install .

## Usage
tidy /path/to/folder

## Example
Before:
folder/
    a.jpg
    b.pdf
    c.mp4

After:
folder/
    Images/a.jpg
    Documents/b.pdf
    Videos/c.mp4

## Status
Stable and usable
## Example

Input files:
a.jpg
b.pdf
c.mp4
notes.txt
song.mp3

After running tidy:
Images/a.jpg
Documents/b.pdf
Videos/c.mp4
Documents/notes.txt
Audio/song.mp3
