import re
import json


def convert_nested_json_string_to_dict(text: str) -> dict:
    text = re.sub(r"\s*\\+n\s*", " ", text)
    text = re.sub(r"\\+\"", '"', text)
    text = re.sub(r"[\"\']{", "{", text)
    text = re.sub(r"}[\"\']", "}", text)

    return json.loads(text)