# -*- coding: utf-8
"""Regular expressions to parse error messages."""

UNBOUNDERROR_RE = r"^local variable '(\w+)' referenced before assignment$"
NAMENOTDEFINED_RE = r"^(?:global )?name '(\w+)' is not defined$"
ATTRIBUTEERROR_RE = r"^(?:module )?'?([\w\.]+)'? (?:object |instance )?" \
    r"has no attribute '(\w+)'$"
UNSUBSCRIBTABLE_RE = r"^'(\w+)' object " \
    r"(?:is (?:not |un)subscriptable|has no attribute '__getitem__')$"
UNEXPECTED_KEYWORDARG_RE = r"^(\w+)\(\) " \
    r"got an unexpected keyword argument '(\w+)'$"
NOMODULE_RE = r"^No module named '?(\w+)'?$"
CANNOTIMPORT_RE = r"^cannot import name '?(\w+)'?$"
INDEXOUTOFRANGE_RE = r"^list index out of range$"
ZERO_LEN_FIELD_RE = r"^zero length field name in format$"
MATH_DOMAIN_ERROR_RE = r"^math domain error$"
TOO_MANY_VALUES_UNPACK_RE = r"^too many values " \
    r"to unpack(?: \(expected \d+\))?$"
OUTSIDE_FUNCTION_RE = r"^'(\w+)' outside function$"
NEED_MORE_VALUES_RE = r"^need more than \d+ values to unpack$"
UNHASHABLE_RE = r"^unhashable type: '(\w+)'$"
MISSING_PARENT_RE = r"^Missing parentheses in call to '(\w+)'$"
INVALID_LITERAL_RE = r"^invalid literal for (\w+)\(\) with base \d+: '(\w+)'$"
NB_ARG_RE = r"^(\w+)\(\) takes (?:exactly )?\d+ " \
    r"(?:positional )?argument \(?(?:but )?\d+ (?:were )?given\)?$"
INVALID_SYNTAX_RE = r"^invalid syntax$"