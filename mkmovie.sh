#!/usr/bin/env sh
ffmpeg \
-framerate 14 \
-pattern_type glob \
-i '*.png' \
-c:v libx264 \
-pix_fmt yuv420p \
-y \
mandelbrot.mp4
