# swaylock-fancy
A small python script for fancy use of swaylock.

Screenshots of all individual monitors are taken using 
[grim](https://github.com/emersion/grim), 
gaussian blurred with adjustable radius, and set as backgrounds 
for [swaylock](https://github.com/swaywm/sway).

This script can easily be adjusted for use with i3lock. Just change the binaries of `swaylock` and `grim`.

The `lock.png` image is taken from [i3lock-fancy-multimonitor](https://github.com/guimeira/i3lock-fancy-multimonitor),
which also somewhat inspired this script.

## Requirements

  * [grim](https://github.com/emersion/grim)
  * [sway (swaylock)](https://github.com/swaywm/sway)
  * [Pillow](https://pillow.readthedocs.io/)

## Installation

Git clone the repository, change to it and run `make install` as root:

```bash
git clone --depth 1 https://github.com/janoliver/swaylock-fancy.git && cd swaylock-fancy
make install
```

## Usage

```
usage: lock.py [-h] [-r RADIUS] [-l LOCK_IMAGE]
               [--swaylock-args SWAYLOCK_ARGS]

Fancy screen locking for sway.

optional arguments:
  -h, --help            show this help message and exit
  -r RADIUS, --radius RADIUS
                        Blur radius.
  -l LOCK_IMAGE, --lock-image LOCK_IMAGE
                        Lock image.
  --swaylock-args SWAYLOCK_ARGS
                        Additional arguments for swaylock.
```

### Examples

```
$ python lock.py -l lock.png -r 15 \
     --swaylock-args="--ring-color #00000000 \
                      --line-color #00000000 \
                      --inside-color=#00000000"
```
