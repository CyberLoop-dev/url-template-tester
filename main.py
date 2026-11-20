#!/usr/bin/env python3
"""Expand a practical RFC 6570 URI-template subset."""
import argparse
import json
import re
import sys
from urllib.parse import quote

EXPRESSION = re.compile(r"\{([+?&]?)([^{}]+)\}")
UNRESERVED = "-._~"
RESERVED = ":/?#[]@!$&'()*+,;="

def expand(template, variables):
    def replace(match):
        operator, names_text = match.groups()
        names = [name.strip() for name in names_text.split(",") if name.strip()]
        if not names:
            raise ValueError("An expression must name at least one variable")
        pairs = []
        simple = []
        for name in names:
            if name not in variables or variables[name] is None:
                continue
            value = variables[name]
            if isinstance(value, (dict, list)):
                raise ValueError(f"Variable '{name}' must be a scalar value")
            text = str(value)
            if operator in ("?", "&"):
                pairs.append(quote(name, safe=UNRESERVED) + "=" + quote(text, safe=UNRESERVED))
            else:
                safe = RESERVED if operator == "+" else UNRESERVED
                simple.append(quote(text, safe=safe))
        if operator == "?":
            return "?" + "&".join(pairs) if pairs else ""
        if operator == "&":
            return "&" + "&".join(pairs) if pairs else ""
        return ",".join(simple)
    result = EXPRESSION.sub(replace, template)
    if "{" in result or "}" in result:
        raise ValueError("Unmatched or unsupported template expression")
    return result

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("template")
    parser.add_argument("--vars", default="{}", help="JSON object containing scalar variables")
    args = parser.parse_args()
    try:
        variables = json.loads(args.vars)
        if not isinstance(variables, dict):
            raise ValueError("--vars must be a JSON object")
        print(expand(args.template, variables))
    except (json.JSONDecodeError, ValueError) as exc:
        parser.error(str(exc))

if __name__ == "__main__":
    main()
