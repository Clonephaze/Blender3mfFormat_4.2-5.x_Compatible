# Copilot Instructions for Blender 3MF Format

## Project Overview

Blender addon for importing/exporting 3MF files. Targets **3MF Core Spec v1.3.0** with Production Extension support for Orca Slicer/BambuStudio compatibility.

## Architecture

```
io_mesh_3mf/
├── __init__.py       # Addon registration, operators, preferences
├── import_3mf.py     # Import3MF operator - main import logic
├── export_3mf.py     # Export3MF operator - main export logic  
├── extensions.py     # ExtensionManager & extension registry
├── constants.py      # 3MF spec constants, namespaces, paths
├── metadata.py       # Metadata class for scene/object metadata
├── annotations.py    # ContentType and Relationship classes (OPC)
├── unit_conversions.py # Unit scale conversions (mm, inch, etc.)
```

**Key patterns:**
- Import/Export classes inherit from `bpy.types.Operator` + `ImportHelper`/`ExportHelper`
- 3MF files are ZIP archives with XML model files + OPC structure
- Use `xml.etree.ElementTree` for XML parsing (not lxml)
- Colors stored as hex strings (`#RRGGBB`), converted to/from Blender's 0-1 floats

## Orca Slicer / Production Extension

Two export modes exist:
1. **Standard export** (`execute_standard_export`) - spec-compliant single model file
2. **Orca export** (`execute_orca_export`) - Production Extension multi-file structure:
   - Individual objects in `3D/Objects/*.model` with `paint_color` attributes
   - Main model with `p:path` component references
   - `Metadata/project_settings.config` JSON with filament colors

**Paint color encoding** (Orca format):
```python
# export: filament index → paint code
ORCA_FILAMENT_CODES = ["", "4", "8", "0C", "1C", ...]  # index 0=none, 1="4", 2="8"

# import: paint code → filament index (1-based, subtract 1 for array lookup)
ORCA_PAINT_TO_INDEX = {"": 0, "4": 1, "8": 2, "0C": 3, ...}
```

## Testing

Tests require **Blender's Python** (not system Python):

```powershell
# All tests (185 total)
python tests/run_all_tests.py

# Unit tests only (fast, mocked bpy)
blender --background --python tests/run_unit_tests.py

# Integration tests (real Blender)
blender --background --python tests/run_tests.py

# Specific module
blender --background --python tests/run_tests.py -- test_export
```

Unit tests use mocked `bpy` in `tests/unit/mock_bpy.py`. Integration tests create real Blender objects.

## Common Patterns

### Adding namespace support
1. Add constant in `constants.py` (e.g., `NEW_NAMESPACE = "http://..."`)
2. Add to `SUPPORTED_EXTENSIONS` set if consumer should accept it
3. Register in `extensions.py` with `Extension` dataclass
4. Add to `MODEL_NAMESPACES` dict for XML parsing

### Unicode safety
Always cache strings before XML operations to prevent garbage collection:
```python
object_name = str(blender_object.name)  # Cache before use
```

### Material colors
```python
# Blender → hex
color = (0.8, 0.2, 0.1)  # RGB 0-1
hex_color = "#%02X%02X%02X" % (int(color[0]*255), int(color[1]*255), int(color[2]*255))

# hex → Blender  
r, g, b = int(hex[1:3], 16)/255, int(hex[3:5], 16)/255, int(hex[5:7], 16)/255
```

### Extension prefix resolution
`requiredextensions="p"` uses prefixes, not URIs. Use `resolve_extension_prefixes()` to map:
```python
known_prefix_mappings = {
    "p": PRODUCTION_NAMESPACE,
    "m": MATERIAL_NAMESPACE,
}
```

## Build & Install

```powershell
cd io_mesh_3mf
blender --command extension build  # Creates .zip in current dir
```

Drag resulting `.zip` into Blender to install.

## Key Files to Reference

- `constants.py` - All 3MF namespaces and file paths
- `extensions.py` - Extension registry and `ExtensionManager`
- `EXTENSIONS.md` - Detailed extension support documentation
- `orca_project_template.json` - Template for Orca metadata export
