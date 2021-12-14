#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def ndprint(a, format_string ='{0:.2f}'):
    print([format_string.format(v,i) for i,v in enumerate(a)])

