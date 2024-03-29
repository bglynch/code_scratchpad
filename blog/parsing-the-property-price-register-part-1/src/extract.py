import re


def extract_eircode_from_end_of_address(address: str):
    address = address.lower().strip(' ,.')
    eircode_routing_keys = [
        'a41', 'a42', 'a45', 'a63', 'a67', 'a75', 'a81', 'a82', 'a83', 'a84', 'a85', 'a86', 'a91', 'a92', 'a94', 'a96',
        'a98', 'c15', 'd01', 'd02', 'd03', 'd04', 'd05', 'd06', 'd6w', 'd07', 'd08', 'd09', 'd10', 'd11', 'd12', 'd13',
        'd14', 'd15', 'd16', 'd17', 'd18', 'd20', 'd22', 'd24', 'e21', 'e25', 'e32', 'e34', 'e41', 'e45', 'e53', 'e91',
        'f12', 'f23', 'f26', 'f28', 'f31', 'f35', 'f42', 'f45', 'f52', 'f56', 'f91', 'f92', 'f93', 'f94', 'h12', 'h14',
        'h16', 'h18', 'h23', 'h53', 'h54', 'h62', 'h65', 'h71', 'h91', 'k32', 'k34', 'k36', 'k45', 'k56', 'k67', 'k78',
        'n37', 'n39', 'n41', 'n91', 'p12', 'p14', 'p17', 'p24', 'p25', 'p31', 'p32', 'p36', 'p43', 'p47', 'p51', 'p56',
        'p61', 'p67', 'p72', 'p75', 'p81', 'p85', 'r14', 'r21', 'r32', 'r35', 'r42', 'r45', 'r51', 'r56', 'r93', 'r95',
        't12', 't23', 't34', 't45', 't56', 'v14', 'v15', 'v23', 'v31', 'v35', 'v42', 'v92', 'v93', 'v94', 'v95', 'w12',
        'w23', 'w34', 'w91', 'x35', 'x42', 'x91', 'y14', 'y21', 'y25', 'y34', 'y35'
    ]
    regex = r"\b(" + '|'.join(eircode_routing_keys) + r") ?([a-z0-9]{4})$"
    regex_result = re.search(regex, address)
    eircode = None
    if regex_result is not None:
        eircode = f"{regex_result.group(1)} {regex_result.group(2)}".upper()
    return eircode


def extract_dublin_postcode_from_address(address: str):
    address = address.lower().strip(' ,.')
    regex = r'dublin_(\d+w?)'
    regex_result = re.search(regex, address)
    postcode = None
    if regex_result is not None:
        postcode = f"Dublin {regex_result.group(1).upper()}"
    return postcode


def extract_county_from_address(address: str):
    address = address.lower().strip(' ,.')
    regex = r'co_([a-z]+)'
    regex_result = re.search(regex, address)
    county = None
    if regex_result is not None:
        county = regex_result.group(1).title()
    return county
