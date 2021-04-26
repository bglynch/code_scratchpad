import re


def normalise_county_name(address: str):
    counties = ['carlow', 'cavan', 'clare', 'cork', 'donegal', 'down', 'dublin', 'fermanagh', 'galway', 'kerry',
                'kildare', 'kilkenny', 'laois', 'leitrim', 'limerick', 'longford', 'louth', 'mayo', 'meath', 'monaghan',
                'offaly', 'roscommon', 'sligo', 'tipperary', 'waterford', 'westmeath', 'wexford', 'wicklow']
    address = address.lower().strip(' ,.')
    counties_regex = r"(" + '|'.join(counties) + r")"
    address = re.sub(r"[ ,]+(county|co\.?) *\.?" + counties_regex, r", co_\2", address)
    address = re.sub(r"[ ,]" + counties_regex + r" ?(county|co\.|co)\b", r", co_\1", address)
    address = re.sub(r"  +" + counties_regex + r"$", r", co_\1", address)
    address = re.sub(r", ?" + counties_regex + r"$", r", co_\1", address)

    return address
