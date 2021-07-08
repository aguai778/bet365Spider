# -*- coding: utf-8 -*-

import re
import sys
import random
import time
import requests
import json
import mitmproxy.http
from mitmproxy import websocket,http,ctx
# from parse import Parse

class Counter:
    def __init__(self):
        self.num = 0

    def websocket_message(self, flow: mitmproxy.websocket.WebSocketFlow):

        if(flow.handshake_flow.server_conn.address[0] == "premws-pt3.365lpodds.com"):
            f = open("websocket_data.txt", "a", encoding="utf-8")
            f.write(flow.messages[len(flow.messages)-1].content + '\n')
            f.flush()
            message = flow.messages[len(flow.messages) - 1].content

            # ws_parse = Parse()
            # ws_parse.parse(message)

addons = [
    Counter()
]


