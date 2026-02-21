"""
Unit tests for ``io_mesh_3mf.export_3mf.context``.

Tests ExportOptions and ExportContext dataclass defaults and field types.
"""

import unittest
from io_mesh_3mf.export_3mf.context import ExportOptions, ExportContext


class TestExportOptionsDefaults(unittest.TestCase):
    """ExportOptions defaults are correct."""

    def test_thumbnail_mode_default(self):
        opts = ExportOptions()
        self.assertEqual(opts.thumbnail_mode, "AUTO")

    def test_thumbnail_resolution_default(self):
        opts = ExportOptions()
        self.assertEqual(opts.thumbnail_resolution, 256)

    def test_thumbnail_image_default(self):
        opts = ExportOptions()
        self.assertEqual(opts.thumbnail_image, "")

    def test_all_thumbnail_modes_accepted(self):
        for mode in ("AUTO", "CUSTOM", "NONE"):
            opts = ExportOptions(thumbnail_mode=mode)
            self.assertEqual(opts.thumbnail_mode, mode)

    def test_custom_resolution(self):
        opts = ExportOptions(thumbnail_resolution=512)
        self.assertEqual(opts.thumbnail_resolution, 512)

    def test_custom_image_path(self):
        opts = ExportOptions(thumbnail_image="/some/path.png")
        self.assertEqual(opts.thumbnail_image, "/some/path.png")


class TestExportContextDefaults(unittest.TestCase):
    """ExportContext creates with sane defaults."""

    def test_default_options(self):
        ctx = ExportContext()
        self.assertIsInstance(ctx.options, ExportOptions)
        self.assertEqual(ctx.options.thumbnail_mode, "AUTO")

    def test_options_pass_through(self):
        opts = ExportOptions(thumbnail_mode="NONE", thumbnail_resolution=128)
        ctx = ExportContext(options=opts)
        self.assertEqual(ctx.options.thumbnail_mode, "NONE")
        self.assertEqual(ctx.options.thumbnail_resolution, 128)


if __name__ == "__main__":
    unittest.main()
