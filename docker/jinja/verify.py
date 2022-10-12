#!/usr/bin/env python3
from jinja2 import Environment, DictLoader

TEST_TEMPLATES = {
    "default": "This test template {%- if works %} works! {%- else %} doesn't work! {%- endif -%}"
}

j2_env = Environment(loader=DictLoader(TEST_TEMPLATES), trim_blocks=True, lstrip_blocks=True)  # nosec
template = j2_env.get_template("default")

assert template.render(works=True) == "This test template works!"
assert template.render(works=False) == "This test template doesn't work!"
