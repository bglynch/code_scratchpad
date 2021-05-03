import re


def normalise_dublin_postcode(address: str):
    address = address.lower().strip(',. ')
    address = re.sub(r"(apt|block) +(d\d+)", r"\1==\2", address)
    address = re.sub(r"[, ]*\b[db]+y?[iunb]{1,2}[okgbil]{1,3}[nhei]{1,2} *(\d)", r", dublin \1", address)
    address = re.sub(r'\bd(ublin)? *6 *(west|w)\b', 'dublin_6w', address)
    address = re.sub(r'\bdublin\.? *0?(\d+)', r'dublin_\1', address)
    address = re.sub(r'([a-z]{3,})dublin\.? *0?(\d+)', r'\1, dublin_\2', address)
    address = re.sub(r" d[ /\.]*([012]?[0-9]w?)\b", r" dublin_\1", address)
    address = re.sub(r"\b(dublin_([12]?[0-9]w?)),? \1$", r", dublin_\2", address)
    address = re.sub(r" ?,[, ]+", r", ", address)
    address = re.sub("==", r" ", address)
    return address


def normalise_county(address: str):
    counties = ['carlow', 'cavan', 'clare', 'cork', 'donegal', 'down', 'dublin', 'fermanagh', 'galway', 'kerry',
                'kildare', 'kilkenny', 'laois', 'leitrim', 'limerick', 'longford', 'louth', 'mayo', 'meath', 'monaghan',
                'offaly', 'roscommon', 'sligo', 'tipperary', 'waterford', 'westmeath', 'wexford', 'wicklow']
    counties_regex = r"(" + '|'.join(counties) + r")"
    address = address.lower().strip(' ,.')
    # mistakes
    address = re.sub(r" port laoise?$", " portlaoise", address)
    address = re.sub(r' po$', '', address)
    address = re.sub(r', co$', '', address)
    address = normalise_county_spelling(address)
    address = normalise_county_prefix_spelling(address)

    address = re.sub(r"county " + counties_regex + r"$", r"co_\1", address)
    address = re.sub(r"  +" + counties_regex + r"$", r", co_\1", address)
    address = re.sub(r", ?" + counties_regex + r"$", r", co_\1", address)
    address = re.sub(r"[, ]+(west|near|nr) cork( city)?", r", co_cork", address)
    address = re.sub(r"[, ]+(north|south) tipperary", r", co_tipperary", address)
    address = re.sub(r"[, ]+(north) dublin", r", co_dublin", address)
    address = re.sub(r"[, ]+(city of dublin|dublin city)", r", co_dublin", address)
    address = re.sub(r"(?<!(the|via)) " + counties_regex + r"$", r", co_\2", address)
    return address


def normalise_county_prefix_spelling(address: str):
    counties = ['carlow', 'cavan', 'clare', 'cork', 'donegal', 'down', 'dublin', 'fermanagh', 'galway', 'kerry',
                'kildare', 'kilkenny', 'laois', 'leitrim', 'limerick', 'longford', 'louth', 'mayo', 'meath', 'monaghan',
                'offaly', 'roscommon', 'sligo', 'tipperary', 'waterford', 'westmeath', 'wexford', 'wicklow']
    counties_regex = r"(" + '|'.join(counties) + r")"
    # mistakes
    address = re.sub(r" i f s c ", " ifsc, ", address)

    address = re.sub(r"[ ,]+c[oc]{0,1}[iun]{1,2}[tnuy]{1,3} *" + counties_regex, r", county \1", address)
    address = re.sub(r"[ ,]+c[doip0lc]{0,2} ?[\.\;\:]? *\.?" + counties_regex, r", county \1", address)
    address = re.sub(r"[ ,]+o " + counties_regex, r", county \1", address)
    address = re.sub(r"[ ,]" + counties_regex + r" ?(county|co\.|co)\b", r", county \1", address)
    address = re.sub(r"([a-z])(co\.?|county) " + counties_regex, r"\1, county \3", address)
    return address


def normalise_county_spelling(address: str):
    address = re.sub(r" c[la][lqare]{2,3}e$", " clare", address)
    address = re.sub(r" [co][corkl]{1,3}[rkl]$", " cork", address)
    address = re.sub(r" do[nega]+[lk]$", " donegal", address)
    address = re.sub(r" du[bl][biln]{1,3}ni?$", " dublin", address)
    address = re.sub(r" g[al]{1,2}w[ayt]{1,3}$", " galway", address)
    address = re.sub(r" k[ilfd]{1,3}[dar]{1,3}[ed]$", " kildare", address)
    address = re.sub(r" ki[lk]{1,2}[ken]{2,4}[yt]$", " kilkenny", address)
    address = re.sub(r" loais$", " laois", address)
    address = re.sub(r" le[it]rim$", " leitrim", address)
    address = re.sub(r" l[im]{1,2}[eri]{1,3}c[fk]{1,2}$", " limerick", address)
    address = re.sub(r" lon[gfo]{1,3}[rds]{1,2}$", " longford", address)
    address = re.sub(r"(?<!the) l[ou][uthrg]+$", " louth", address)
    address = re.sub(r" m[maor]{1,2}[yo]{1,2}$", " mayo", address)
    address = re.sub(r" m[ae][aeth]+$", " meath", address)
    address = re.sub(r" m[oa][nagho]+$", " monaghan", address)
    address = re.sub(r" of[faly]+$", " offaly", address)
    address = re.sub(r" r[osd]{1,2}[cos]{1,3}mm[mon]{1,3}$", " roscommon", address)
    address = re.sub(r" s[li]{1,3}go$", " sligo", address)
    address = re.sub(r" tip{1,3}[eart]{1,5}y$", " tipperary", address)
    address = re.sub(r" wa[tr]er[forite]{1,4}d$", " waterford", address)
    address = re.sub(r" we[staer]{1,3}m[ea]{1,2}th$", " westmeath", address)
    address = re.sub(r"[, ]+(west) meath", r", westmeath", address)
    address = re.sub(r" w[ex]{1,2}[fv][fords]{1,3}$", " wexford", address)
    address = re.sub(r" w[ic]{1,3}[kl]{1,2}[ow]{1,2}$", " wicklow", address)
    return address
