#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path


def render_html(html_file, **kwargs):
    return Path(html_file).read_text(encoding='utf-8')

