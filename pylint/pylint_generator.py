import os
import re


class PylintGenerator:
    def __init__(self, report: dict):
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
        self._rating = int()
        self._colour = str()
        self.error = list()
        self.warning = list()
        self.refactor = list()
        self.convention = list()
        self.set_rating_and_colour(report)
        self.set_pylint_messages(report)

    def set_rating_and_colour(self, report: dict):
        statement = report['stats'].get('statement')
        error = report['stats'].get('error', 0)
        warning = report['stats'].get('warning', 0)
        refactor = report['stats'].get('refactor', 0)
        convention = report['stats'].get('convention', 0)

        if not statement or statement <= 0:
            return None

        malus = float(5 * error + warning + refactor + convention)
        malus_ratio = malus / statement

        rating = abs(10.0 - (malus_ratio * 10))
        colour = '9d9d9d'
        if rating > 0:
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
    def get_rating(self):
        return int(self._rating)

    @property
    def get_svg(self):
        return self.BADGE_TEMPLATE.format(self._rating, self._colour)

    def set_pylint_messages(self, report: dict):
        for message in report['messages']:
            if message['type'] == "convention":
                self.convention.append(message)
            elif message['type'] == "error":
                self.error.append(message)
            elif message['type'] == "warning":
                self.warning.append(message)
            elif message['type'] == "refactor":
                self.refactor.append(message)

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
