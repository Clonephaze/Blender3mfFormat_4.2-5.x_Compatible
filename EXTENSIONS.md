# 3MF Extension Support

This document describes how the Blender 3MF addon handles 3MF extensions, both official extensions from the 3MF Consortium and vendor-specific extensions.

## Extension Architecture

The addon uses a centralized extension management system (`io_mesh_3mf/extensions.py`) that provides:

- **Extension Registry**: Central catalog of known extensions with metadata
- **Extension Manager**: Runtime management of active extensions during import/export
- **Type Classification**: Official (3MF Consortium) vs Vendor-specific extensions
- **Namespace Management**: Automatic XML namespace registration

## Supported Extensions

### Core Specification

The addon implements **3MF Core Specification v1.3.0**, which includes:

- ✅ `<basematerials>` - Material colors and properties (fully supported)
- ✅ `requiredextensions` attribute - Extension requirements (validated on import)
- ✅ `recommendedextensions` attribute - Optional extension hints (v1.3.0 feature)
- ✅ OPC Core Properties - Dublin Core metadata (creator, timestamps)

### Materials Extension (Partial)

**Namespace:** `http://schemas.microsoft.com/3dmanufacturing/material/2015/02`

**Status:** Vendor-specific implementation for Orca Slicer/BambuStudio

#### Export

- **Standard Mode:** Uses core spec `<basematerials>` (fully spec-compliant)
- **Orca Mode:** Uses `<m:colorgroup>` with `<m:color>` elements
  - Each color becomes a separate colorgroup resource
  - Compatible with Orca Slicer and BambuStudio
  - **Note:** This is a vendor-specific interpretation, not defined in core spec

#### Import

- ✅ Reads core spec `<basematerials>` elements
- ✅ Reads `<m:colorgroup>` elements (when vendor extensions enabled)
- ✅ Auto-detects Orca/BambuStudio files
- ⚙️ Optional: Can disable vendor extensions via import options

### Vendor-Specific Extensions

#### Orca Slicer / BambuStudio

**Namespace:** `http://schemas.bambulab.com/package/2021`

**Detection Markers:**
- `BambuStudio:3mfVersion` metadata
- Application metadata containing "Orca" or "Bambu"
- BambuStudio-prefixed attributes

**Features:**
- Color zones via `<m:colorgroup>` (Materials extension)
- BambuStudio metadata attributes
- Orca project settings (in separate JSON file)
- `paint_color` attribute for filament mapping

**Export Options:**
- **"Orca Slicer Color Zones"** checkbox enables Orca-specific export
- Automatically registers Materials + BambuStudio namespaces
- Generates vendor metadata
- Creates `Metadata/project_settings.config` JSON file

**Import Options:**
- **"Import Vendor Extensions"** controls Orca/BambuStudio data import
- Auto-detects vendor format
- Imports colorgroups as materials
- Can be disabled for standard-only import

## Extension Registry

Located in `io_mesh_3mf/extensions.py`:

### Official Extensions (Registered but Not Implemented)

```python
PRODUCTION_EXTENSION   # Manufacturing metadata
SLICE_EXTENSION        # Pre-sliced geometry
BEAM_LATTICE_EXTENSION # Lattice structures
VOLUMETRIC_EXTENSION   # Voxel-based models
```

These are registered in the system but not yet implemented. Adding support requires:

1. Register namespace in `extensions.py`
2. Add parsing/generation logic in import/export modules
3. Update `SUPPORTED_EXTENSIONS` in `constants.py`
4. Add tests
5. Document behavior

## Usage

### For Users

**Export:**
1. **Standard 3MF:** Default mode, fully spec-compliant
   - Uses core spec `<basematerials>`
   - Compatible with all 3MF consumers
   
2. **Orca Slicer Mode:** Enable "Orca Slicer Color Zones"
   - Assigns materials to faces in Edit mode
   - Each material color becomes a separate filament zone
   - Exports vendor-specific `<m:colorgroup>` elements

**Import:**
1. **Default:** Imports everything including vendor extensions
   - Auto-detects Orca/BambuStudio files
   - Imports colorgroups as materials
   
2. **Standard Only:** Disable "Import Vendor Extensions"
   - Ignores vendor-specific data
   - Imports only core spec elements
   
3. **Geometry Only:** Disable "Import Materials"
   - No material/color import
   - Geometry and structure only

### For Developers

**Adding a New Official Extension:**

```python
# 1. Define in extensions.py
MY_EXTENSION = Extension(
    namespace="http://schemas.microsoft.com/3dmanufacturing/myext/2025/01",
    prefix="mx",
    name="My Extension",
    extension_type=ExtensionType.OFFICIAL,
    description="Description of what this provides",
    required=False,  # or True if must be in requiredextensions
)

# 2. Register in EXTENSION_REGISTRY
EXTENSION_REGISTRY[MY_EXTENSION.namespace] = MY_EXTENSION

# 3. Update constants.py
SUPPORTED_EXTENSIONS.add(MY_EXTENSION.namespace)

# 4. Implement in export_3mf.py
if self.extension_manager.is_active(MY_EXTENSION.namespace):
    # Write extension data
    pass

# 5. Implement in import_3mf.py
if self.extension_manager.is_active(MY_EXTENSION.namespace):
    # Read extension data
    pass
```

**Adding a New Vendor Extension:**

```python
# Same process, but use ExtensionType.VENDOR
VENDOR_EXTENSION = Extension(
    namespace="http://vendor.com/3mf/extension",
    prefix="vendor",
    name="Vendor Software",
    extension_type=ExtensionType.VENDOR,
    description="Vendor-specific features",
    required=False,
    vendor_attribute="Vendor:Version",  # Optional root attribute
)
```

**Extension Manager API:**

```python
# In export/import operators
self.extension_manager = ExtensionManager()

# Activate extensions
self.extension_manager.activate(MATERIALS_EXTENSION.namespace)

# Check if active
if self.extension_manager.is_active(namespace):
    # Handle extension

# Register with ElementTree
self.extension_manager.register_namespaces(xml.etree.ElementTree)

# Get requiredextensions string
req_string = self.extension_manager.get_required_extensions_string()

# Get vendor attributes
attrs = self.extension_manager.get_vendor_attributes()
```

## Specification Compliance

### What's Spec-Compliant

✅ **Core 3MF v1.3.0:**
- ZIP/OPC package structure
- Content types and relationships
- `<basematerials>` with `<base>` elements
- Build structure and transformations
- Metadata system
- `requiredextensions` and `recommendedextensions` attributes
- OPC Core Properties (Dublin Core)

✅ **Extension Mechanism:**
- Uses official namespace URIs
- Proper `@anyAttribute` and `<any>` extension points
- Respects required vs optional distinction

### What's Vendor-Specific

⚠️ **Orca Colorgroup Implementation:**
- Uses official Materials extension namespace
- BUT: `<m:colorgroup>` structure is not defined in core spec
- Appears to be Orca/BambuStudio's proprietary interpretation
- Works with their slicers but may not be recognized elsewhere
- Architectural difference: N property groups vs 1 group with N items

⚠️ **Orca Metadata:**
- `BambuStudio:3mfVersion` attribute
- `paint_color` attributes on triangles
- Orca-specific JSON configuration files

### Recommendations

- **For maximum compatibility:** Use standard mode (default)
- **For Orca Slicer:** Enable Orca mode when exporting specifically for Orca/BambuStudio
- **When importing:** Vendor extensions are auto-detected and handled appropriately
- **For other slicers:** Standard mode works with PrusaSlicer, Cura, Simplify3D, etc.

## Future Work

### Planned Extensions

1. **Production Extension** - Manufacturing metadata (UUID, paths, production instructions)
2. **Slice Extension** - Pre-sliced geometry for specific printers
3. **Beam Lattice** - Efficient lattice structure representation
4. **Volumetric** - Voxel-based model support

### Vendor Support

Potential future vendor integrations:
- PrusaSlicer-specific features
- Cura project metadata
- Simplify3D configurations

Adding new vendor support follows the same pattern as Orca implementation.

## Technical References

- **3MF Core Spec v1.3.0:** `3MF_Core_Specification_v1.3.0.md` (in repository)
- **Extension Registry:** `io_mesh_3mf/extensions.py`
- **Export Implementation:** `io_mesh_3mf/export_3mf.py`
- **Import Implementation:** `io_mesh_3mf/import_3mf.py`
- **Constants:** `io_mesh_3mf/constants.py`

## Testing

Extension support is tested via:
- **Unit tests:** `tests/unit/test_import_unit.py`, `tests/unit/test_export_unit.py`
- **Integration tests:** `tests/integration/test_export.py`, `tests/integration/test_import.py`
- **Roundtrip tests:** `tests/integration/test_import.py` (RoundtripTests)

Run all tests: `python tests/run_all_tests.py`

## Questions & Support

- **Spec compliance questions:** Refer to `3MF_Core_Specification_v1.3.0.md`
- **Vendor extension questions:** Check vendor (Orca/BambuStudio) documentation
- **Implementation questions:** Review `extensions.py` and module docstrings
- **Bug reports:** GitHub issues with "extension" label
