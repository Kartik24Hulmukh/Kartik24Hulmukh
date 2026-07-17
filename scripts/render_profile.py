#!/usr/bin/env python3
"""Compatibility entrypoint for the existing validate workflow."""
from pathlib import Path
import runpy
runpy.run_path(str(Path(__file__).with_name("render_assets.py")), run_name="__main__")
