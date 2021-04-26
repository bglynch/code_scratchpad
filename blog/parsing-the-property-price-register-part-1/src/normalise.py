import re


def normalise_county_name(address: str):
    counties = ['carlow', 'cavan', 'clare', 'cork', 'donegal', 'down', 'dublin', 'fermanagh', 'galway', 'kerry',
                'kildare', 'kilkenny', 'laois', 'leitrim', 'limerick', 'longford', 'louth', 'mayo', 'meath', 'monaghan',
                'offaly', 'roscommon', 'sligo', 'tipperary', 'waterford', 'westmeath', 'wexford', 'wicklow']
    address = address.lower().strip(' ,.')
    address = re.sub(r' po$', '', address)
    address = re.sub(r', co$', '', address)
    # correct misspelling at end of address
    address = re.sub(r" c[la][lqare]{2,3}e$",              " clare", address)
    address = re.sub(r" [co][corkl]{1,3}[rkl]$",           " cork", address)
    address = re.sub(r" do[nega]+[lk]$",                   " donegal", address)
    address = re.sub(r" du[bl][biln]{1,3}ni?$",            " dublin", address)
    address = re.sub(r" g[al]{1,2}w[ayt]{1,3}$",           " galway", address)
    address = re.sub(r" k[ilfd]{1,3}[dar]{1,3}[ed]$",      " kildare", address)
    address = re.sub(r" ki[lk]{1,2}[ken]{2,4}[yt]$",       " kilkenny", address)
    address = re.sub(r" loais$",                           " laois", address)
    address = re.sub(r" le[it]rim$",                       " leitrim", address)
    address = re.sub(r" l[im]{1,2}[eri]{1,3}c[fk]{1,2}$",  " limerick", address)
    address = re.sub(r" lon[gfo]{1,3}[rds]{1,2}$",         " longford", address)
    address = re.sub(r" l[ou][uthrg]+$",                   " louth", address)
    address = re.sub(r" m[maor]{1,2}[yo]{1,2}$",           " mayo", address)
    address = re.sub(r" m[ae][aeth]+$",                    " meath", address)
    address = re.sub(r" m[oa][nagho]+$",                   " monaghan", address)
    address = re.sub(r" of[faly]+$",                       " offaly", address)
    address = re.sub(r" r[osd]{1,2}[cos]{1,3}mm[mon]{1,3}$",   " roscommon", address)
    address = re.sub(r" s[li]{1,3}go$",                    " sligo", address)
    address = re.sub(r" tip{1,3}[eart]{1,5}y$",            " tipperary", address)
    address = re.sub(r" wa[tr]er[forite]{1,4}d$",          " waterford", address)
    address = re.sub(r" we[staer]{1,3}m[ea]{1,2}th$",      "westmeath", address)
    address = re.sub(r" w[ex]{1,2}[fv][fords]{1,3}$",      "wexford", address)
    address = re.sub(r" w[ic]{1,3}[kl]{1,2}[ow]{1,2}$",    "wicklow", address)



    counties_regex = r"(" + '|'.join(counties) + r")"
    address = re.sub(r"[ ,]+(c[coiunty]{1,2}[un][tn][ty]|[co][doip0lc]{0,2}[\.\;\:]?) *\.?" + counties_regex, r", co_\2", address)
    address = re.sub(r"[ ,]" + counties_regex + r" ?(county|co\.|co)\b", r", co_\1", address)
    address = re.sub(r"  +" + counties_regex + r"$", r", co_\1", address)
    address = re.sub(r", ?" + counties_regex + r"$", r", co_\1", address)
    address = re.sub(r"[, ]+(west) meath", r", co_westmeath", address)
    address = re.sub(r"[, ]+(west|near|nr) cork", r", co_cork", address)
    address = re.sub(r"[, ]+(north|south) tipperary", r", co_tipperary", address)
    address = re.sub(r"[, ]+(north) dublin", r", co_dublin", address)
    address = re.sub(r"[, ]+city of dublin", r", co_dublin", address)
    address = re.sub(r"co_[a-z]+]", '**', address)

    return address
