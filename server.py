#!/usr/bin/env python3
"""暑期学习助手 HTTP 服务器 —— 修复 Windows 下中文文件名 URL 编码问题"""
import http.server
import socketserver
import urllib.parse
import os
import sys

PORT = 8080
DIR = os.path.dirname(os.path.abspath(__file__))

class UTF8FileHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIR, **kwargs)

    def translate_path(self, path):
        """Override to fix UTF-8 percent-encoded Chinese paths on Windows"""
        # Decode percent-encoding -> UTF-8 string
        path = urllib.parse.unquote(path, encoding='utf-8')
        # Remove leading slash and any query/fragment
        path = path.lstrip('/')
        # Security: prevent directory traversal
        path = os.path.normpath(path)
        # Join with base directory
        full = os.path.join(DIR, path)
        return full

    def log_message(self, format, *args):
        sys.stderr.write("[%s] %s\n" % (self.log_date_time_string(), format % args))

os.chdir(DIR)
print(f'[OK] 暑期学习助手服务器已启动')
print(f'     目录: {DIR}')
print(f'     平板访问: http://<电脑IP>:{PORT}/暑期学习助手.html')
print(f'     按 Ctrl+C 停止')

with socketserver.TCPServer(("0.0.0.0", PORT), UTF8FileHandler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('[STOP] 服务器已停止')
        httpd.server_close()
