# SPDX-License-Identifier: GPL-3.0-or-later
import logging
from gettext import gettext as _

from graphs import file_io, utilities

from matplotlib import RcParams, cbook
from matplotlib.font_manager import font_scalings, weight_dict
from matplotlib.style.core import STYLE_BLACKLIST


STYLE_IGNORELIST = [
    "savefig.dpi", "savefig.facecolor", "savefig.edgecolor", "savefig.format",
    "savefix.bbox", "savefig.pad_inches", "savefig.transparent",
    "savefig.orientation",
]
FONT_SIZE_KEYS = [
    "font.size", "axes.labelsize", "xtick.labelsize", "ytick.labelsize",
    "legend.fontsize", "figure.labelsize", "figure.titlesize",
    "axes.titlesize",
]


def parse_style(file):
    """
    Parse a style to RcParams.

    This is an improved version of matplotlibs '_rc_params_in_file()' function.
    It is also modified to work with GFile instead of the python builtin
    functions.
    """
    style = RcParams()
    filename = utilities.get_filename(file)
    try:
        lines = file_io.read_file(file).splitlines()
        for line_number, line in enumerate(lines, 1):
            line = line.strip()
            if line_number == 2:
                style.name = line[2:]
            line = cbook._strip_comment(line)
            if not line:
                continue
            try:
                key, value = line.split(":", 1)
            except ValueError:
                logging.warning(
                    _("Missing colon in file {}, line {}").format(
                        filename, line_number))
                continue
            key = key.strip()
            value = value.strip()
            if value.startswith('"') and value.endswith('"'):
                value = value[1:-1]  # strip double quotes
            if key in STYLE_BLACKLIST:
                message = _("Non-style related parameter {} in file {}")
                logging.warning(message.format(key, filename))
            elif key in STYLE_IGNORELIST:
                message = _("Ignoring parameter {} in file {}")
                logging.warning(message.format(key, filename))
            elif key in style:
                message = _("Duplicate key in file {}, on line {}")
                logging.warning(message.format(filename, line_number))
            else:
                if key in FONT_SIZE_KEYS \
                        and not value.replace(".", "", 1).isdigit():
                    try:
                        value = font_scalings[value]
                    except KeyError:
                        continue
                elif key == "font.weight" and not value.isdigit():
                    try:
                        value = weight_dict[value]
                    except KeyError:
                        continue
                try:
                    style[key] = value
                except (KeyError, ValueError):
                    message = _("Bad value in file {} on line {}")
                    logging.exception(
                        message.format(filename, line_number))
    except UnicodeDecodeError:
        logging.exception(_("Could not parse {}").format(filename))
    return style


WRITE_IGNORELIST = STYLE_IGNORELIST + [
    "lines.dashdot_pattern", "lines.dashed_pattern",
    "lines.dotted_pattern", "lines.dash_capstyle", "lines.dash_joinstyle",
    "lines.solid_capstyle", "lines.solid_joinstyle",
]


def write_style(file, style):
    stream = file_io.get_write_stream(file)
    file_io.write_string(stream, "# Generated via Graphs\n")
    file_io.write_string(stream, f"# {style.name}\n")
    for key, value in style.items():
        if key not in STYLE_BLACKLIST and key not in WRITE_IGNORELIST:
            value = str(value).replace("#", "")
            if key != "axes.prop_cycle":
                value = value.replace("[", "").replace("]", "")
                value = value.replace("'", "").replace("'", "")
                value = value.replace('"', "").replace('"', "")
            line = f"{key}: {value}\n"
            file_io.write_string(stream, line)
    stream.close()
