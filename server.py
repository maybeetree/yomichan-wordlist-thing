#!/usr/bin/env python

import json
from http.server import BaseHTTPRequestHandler, HTTPServer
import re
import html

def add_note(req):
    kanji = req["params"]["note"]["fields"]["kanji"]
    furi = req["params"]["note"]["fields"]["furi"]
    eng = req["params"]["note"]["fields"]["eng"]

    kanji = html.unescape(
        kanji
        .replace('\n','')
        .replace('\r','')
        .replace('\t','')
        )
    furi = html.unescape(
        furi
        .replace('\n','')
        .replace('\r','')
        .replace('\t','')
        )
    eng = html.unescape(
        eng
        .replace('\n','')
        .replace('\r','')
        .replace('\t','')
        )

    # Making it a set removes duplicates
    definitions = {
        stripped
        for part in eng.split('<li>')
        if (stripped := re.sub('<[^>]*>', '', part).strip())
        }

    eng = '; '.join(definitions)

    with open('yomichan_notes.tsv', 'a') as file:
        file.write(f"{kanji}\t{furi}\t{eng}\n")

def handle_req(req):
    action = req["action"]
    print(action)

    if action == "version":
        return 2

    if action == "canAddNotes":
        return [True] * len(req["params"]["notes"])

    elif action == "deckNames":
        return ["Fake Anki Server"]

    elif action == "modelNames":
        return ["Fake Anki Card Model"]

    elif action == "modelFieldNames":
        return ["kanji", "furi", "eng"]

    elif action == "addNote":
        add_note(req)
        return []


class Server(BaseHTTPRequestHandler):

    def do_POST(self):
        content_length = int(self.headers.get("Content-Length", 0))
        post_data = self.rfile.read(content_length)
        req = json.loads(post_data.decode("utf-8"))

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()

        resp = handle_req(req)

        self.wfile.write(
            json.dumps(
                resp
                ).encode("utf-8")
            )

if __name__ == "__main__":
    server = HTTPServer(("127.0.0.1", 8765), Server)
    server.serve_forever()


