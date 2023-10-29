from __future__ import annotations

import unittest

from mypy.test.helpers import assert_string_arrays_equal
from mypyc.codegen.emit import Emitter, EmitterContext, ReturnHandler
from mypyc.codegen.emitwrapper import generate_arg_check
from mypyc.ir.rtypes import int_rprimitive, list_rprimitive
from mypyc.namegen import NameGenerator


class TestArgCheck(unittest.TestCase):
    def setUp(self) -> None:
        self.context = EmitterContext(NameGenerator([["mod"]]))

    def test_check_list(self) -> None:
        emitter = Emitter(self.context)
        generate_arg_check("x", list_rprimitive, emitter, ReturnHandler("NULL"))
        lines = emitter.fragments
        self.assert_lines(
            [
                "PyObject *arg_x;",
                "if (likely(PyList_Check(obj_x)))",
                "    arg_x = obj_x;",
                "else {",
                '    CPy_TypeError("list", obj_x);',
                "    return NULL;",
                "}",
            ],
            lines,
        )

    def test_check_int(self) -> None:
        emitter = Emitter(self.context)
        generate_arg_check("x", int_rprimitive, emitter, ReturnHandler("NULL"))
        generate_arg_check(
            "y", int_rprimitive, emitter, ReturnHandler("NULL"), optional=True
        )
        lines = emitter.fragments
        self.assert_lines(
            [
                "CPyTagged arg_x;",
                "if (likely(PyLong_Check(obj_x)))",
                "    arg_x = CPyTagged_BorrowFromObject(obj_x);",
                "else {",
                '    CPy_TypeError("int", obj_x); return NULL;',
                "}",
                "CPyTagged arg_y;",
                "if (obj_y == NULL) {",
                "    arg_y = CPY_INT_TAG;",
                "} else if (likely(PyLong_Check(obj_y)))",
                "    arg_y = CPyTagged_BorrowFromObject(obj_y);",
                "else {",
                '    CPy_TypeError("int", obj_y); return NULL;',
                "}",
            ],
            lines,
        )

    def assert_lines(self, expected: list[str], actual: list[str]) -> None:
        actual = [line.rstrip("\n") for line in actual]
        assert_string_arrays_equal(expected, actual, "Invalid output")
