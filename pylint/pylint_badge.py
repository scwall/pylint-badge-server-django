import os
import re


class PylintSvg:
    def __init__(self, report: str):
        self.BADGE_TEMPLATE = """<svg xmlns="http://www.w3.org/2000/svg" width="85" height="20">
          <linearGradient id="a" x2="0" y2="100%">
            <stop offset="0" stop-color="#bbb" stop-opacity=".1"/>
            <stop offset="1" stop-opacity=".1"/>
          </linearGradient>
          <!-- whole rectangle -->
          <rect rx="3" width="85" height="20" fill="#555"/>
        
          <!-- rating part -->
          <rect rx="3" x="50" width="35" height="20" fill="#{1}"/>
          <path fill="#{1}" d="M50 0h4v20h-4z"/>
        
          <!-- whole rectangle -->
          <rect rx="3" width="85" height="20" fill="url(#a)"/>
        
          <g fill="#fff" text-anchor="middle"
                         font-family="DejaVu Sans,Verdana,Geneva,sans-serif"
                         font-size="11">
            <text x="25" y="15" fill="#010101" fill-opacity=".3">pylint</text>
            <text x="25" y="14">pylint</text>
            <text x="67" y="15" fill="#010101" fill-opacity=".3">{0:.2f}</text>
            <text x="67" y="14">{0:.2f}</text>
          </g>
        </svg>
        """
        self._rating = str()
        self._colour = str()
        self.get_rating_and_colour(report)
        self.error = dict()
        self.warning = dict()
        self.refactor = dict()
        self.convention = dict()

    def get_rating_and_colour(self, report: str):
        colour = '9d9d9d'
        rating = 0
        match = re.search("Your code has been rated at (.+?)/10", report)
        if match:
            rating = float(match.group(1))
            if rating >= 9 and rating <= 10:
                colour = '44cc11'
            elif rating < 9 and rating >= 7:
                colour = 'f89406'
            elif rating >= 0 and rating < 7:
                colour = 'b94947'
            else:
                colour = '9d9d9d'
        self._rating = rating
        self._colour = colour

    @property
    def get_svg(self):
        return self.BADGE_TEMPLATE.format(self._rating, self._colour)

    def set_pylint_messages(self, message_json: dict):
        for message in message_json:
            if message['type'] == "convention":
                self.convention['column'] = message['column']
                self.convention['message'] = message['message']
                self.convention['line'] = message['line']
            elif message['type'] == "error":
                self.error['message'] = message['convention']
                self.error['column'] = message['column']
                self.error['message'] = message['message']
                self.error['line'] = message['line']
            elif message['type'] == "warning":
                self.warning['message'] = message['convention']
                self.warning['column'] = message['column']
                self.warning['message'] = message['message']
                self.warning['line'] = message['line']
            elif message['type'] == "refactor":
                self.refactor['message'] = message['convention']
                self.refactor['column'] = message['column']
                self.refactor['message'] = message['message']
                self.refactor['line'] = message['line']

    @property
    def get_convention(self):
        return self.convention

    @property
    def get_refactor(self):
        return self.refactor

    @property
    def get_warning(self):
        return self.warning

    @property
    def get_error(self):
        return self.error
