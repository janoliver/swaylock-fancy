#!/bin/env python

import subprocess
import os
import sys
import re
import json
import argparse

from PIL import ImageFilter, Image

def get_outputs():
    outp = subprocess.check_output(["swaymsg", "-t", "get_outputs"])
    for screen in json.loads(outp):
        o = screen["name"]
        w,h = screen["rect"]["width"], screen["rect"]["height"]
        x,y = screen["rect"]["x"], screen["rect"]["y"]
        yield o, (w,h), (x,y)

def make_screenshot(output_file, position, size):
    x,y = position
    w,h = size
    subprocess.call(["grim", "-g", "%d,%d %dx%d" % (x,y,w,h), output_file])
    im = Image.open(output_file)
    os.remove(output_file)
    return im

def lock(blur_radius=15, lock_img="", swaylock_args=""):
    swaylock = ["swaylock"]
    for i,(o, (w,h), (x,y)) in enumerate(get_outputs()):
        screenshot_path = "/tmp/swaylock-python%d.png" % i
        
        im = make_screenshot(screenshot_path, (x,y), (w,h))
        im = im.filter(ImageFilter.GaussianBlur(blur_radius))

        if lock_img:
            lock_im = Image.open(lock_img)
            lw, lh = lock_im.size
            im.paste(lock_im, box=((w-lw)//2, (h-lh)//2), mask=lock_im)
        
        im.save(screenshot_path)

        swaylock.extend(["-i", "%s:%s" % (o, screenshot_path)])

    if swaylock_args:
        swaylock.extend(swaylock_args.split())
    subprocess.call(swaylock)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Fancy screen locking for sway.')
    parser.add_argument('-r', '--radius', type=int, default=15, 
        help='Blur radius of the Gaussian filter in px.')
    parser.add_argument('-l', '--lock-image', type=str, 
        help='Image to be displayed in the center of each output.')
    parser.add_argument('--swaylock-args', type=str, 
        help='Additional arguments that are passed to swaylock.')
    args = parser.parse_args()

    lock(lock_img=args.lock_image, 
         blur_radius=args.radius, 
         swaylock_args=args.swaylock_args)