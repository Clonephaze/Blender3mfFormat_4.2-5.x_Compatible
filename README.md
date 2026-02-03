# Blender 3MF Format

> [!NOTE]  
> This repository is an actively maintained fork of the original Blender 3MF add-on, updated for modern Blender versions (4.2+) and ongoing development.

This is a Blender add-on for importing and exporting **3MF (3D Manufacturing Format)** files.

3MF is a modern interchange format for additive manufacturing. Unlike STL, it is designed to carry not only geometry, but also units, materials, colors, metadata, and other information relevant to real 3D printing workflows. In this context, Blender serves as a modeling and preparation tool upstream of slicers and manufacturing software.

The goal of this add-on is to make **Blender a practical and reliable tool in 3MF-based workflows**, with spec-aligned behavior and useful interoperability with modern slicers.

---

## Status

- ✅ Compatible with **Blender 4.2+**
- ✅ Actively maintained
- ✅ Production-ready

For Blender versions **2.80–3.6**, use the [original repository releases](https://github.com/Ghostkeeper/Blender3mfFormat/releases/latest).

---

## Features

- Import and export 3MF files
- Correct handling of units and build structure
- Material and color support compatible with modern Blender material APIs
- **Thumbnail generation** - viewport snapshot embedded in exported 3MF files
- Verified round-trip import/export
- Scriptable import/export operators
- Extensive automated testing

### Slicer Compatibility

| Slicer | Round-Trip Support | Notes |
|--------|-------------------|-------|
| **Orca Slicer / BambuStudio** | ✅ Full | Multi-color zones (per-triangle), materials, and metadata preserved |
| **PrusaSlicer** | ⚠️ Partial | Per-triangle MMU segmentation supported. Paint bucket tool (volumetric) not yet supported |
| **Standard 3MF** | ✅ Full | Geometry, materials, and metadata |

---

## Installation

### Blender 4.2+

**Option 1: Drag & Drop (Recommended)**
1. Download this repository as a ZIP
2. Open Blender
3. Drag the `io_mesh_3mf` folder into the Blender window
4. Confirm installation and enable the add-on

**Option 2: Preferences**
1. Extract the ZIP
2. Open *Edit → Preferences → Add-ons*
3. Click *Install…* and select the `io_mesh_3mf` folder
4. Enable **Import-Export: 3MF format**

**Option 3: Development Setup**
Symlink or copy `io_mesh_3mf` into Blender’s add-ons directory:
- Windows: `%APPDATA%\\Blender Foundation\\Blender\\4.5\\scripts\\addons\\`
- macOS: `~/Library/Application Support/Blender/4.5/scripts/addons/`
- Linux: `~/.config/blender/4.5/scripts/addons/`

Reload scripts and enable the add-on.

---

## Usage

After installation, the following menu entries are available:

- **File → Import → 3D Manufacturing Format (.3mf)**
- **File → Export → 3D Manufacturing Format (.3mf)**

![Screenshot](screenshot.png)

### Import Options
- **Scale**: Uniform scale applied from the scene origin
- **Import Materials**: Import material colors from the file (disable for geometry-only import)
- **Import Vendor Extensions**: Import vendor-specific data like Orca Slicer color zones (disable for standard-only import)

### Export Options
- **Selection Only**
- **Scale**
- **Apply Modifiers**
- **Coordinate Precision**
- **Export Hidden Objects**
- **Multi-Material Format**: Choose between Standard 3MF, Orca Slicer, or PrusaSlicer MMU export formats
  - **Orca Slicer**: Production Extension with paint_color attributes
  - **PrusaSlicer**: slic3rpe:mmu_segmentation attributes with color metadata for perfect round-trips

---

## Development & Contributing

For detailed feature status, upcoming improvements, and contribution opportunities, see the **[Development Roadmap](ROADMAP.md)**.

Key areas:
- **Completed**: PrusaSlicer MMU export, Orca Slicer compatibility, automatic thumbnails
- **In Progress**: Triangle Sets Extension, texture support
- **Help Wanted**: Testing with different slicers, documenting vendor formats

---

## Testing

This add-on includes comprehensive automated testing to ensure reliability.

See [`tests/README.md`](tests/README.md) for detailed testing information.

---

## 3MF Specification Support

This add-on targets the **3MF Core Specification v1.3.0**.

### Behavior Notes

> **NOTE**  
> The 3MF specification requires consumers to fail hard on malformed files. In practice, this add-on favors recoverability in a DCC environment.

- Core requirements (ZIP/OPC structure, model XML, units, build definitions) are enforced on export.
- On import, partially malformed files may load with warnings rather than failing entirely.
- When conflicts arise while importing multiple 3MF files into a single scene, conflicting metadata may be skipped to preserve scene integrity.

### Extensions

This add-on supports several 3MF extensions for enhanced interoperability with slicers and manufacturing software.

#### Supported Extensions

| Extension | Namespace | Support Level |
|-----------|-----------|---------------|
| **Core Materials** (`basematerials`) | Core Spec v1.3.0 | ✅ Full |
| **Production Extension** | `http://schemas.microsoft.com/3dmanufacturing/production/2015/06` | ✅ Full |
| **Materials Extension** | `http://schemas.microsoft.com/3dmanufacturing/material/2015/02` | 🔶 Partial |

#### Orca Slicer / BambuStudio Compatibility

This add-on includes special support for **Orca Slicer** and **BambuStudio** multi-color workflows:

**Import:**
- Reads multi-file Production Extension structure (`3D/Objects/*.model`)
- Imports `paint_color` attributes as Blender materials
- Reads actual filament colors from `Metadata/project_settings.config`
- Supports files exported from Orca Slicer, BambuStudio, and PrusaSlicer

**Export (Orca Slicer Color Zones option):**
- Exports using Production Extension multi-file structure
- Writes per-triangle `paint_color` attributes for filament assignment
- Generates `project_settings.config` with filament colors
- Creates proper OPC relationships for slicer compatibility
- Embeds viewport thumbnail for file preview

**Automatically loads filament colors from metadata for accurate material recreation
- Compatible with files exported from both Blender and PrusaSlicer

**Export (PrusaSlicer MMU Format):**
- Exports face colors with `slic3rpe:mmu_segmentation` attributes
- Stores actual RGB colors in `Metadata/blender_filament_colors.txt`
- Perfect round-trip: Blender → PrusaSlicer → Blender maintains exact colors
- Compatible with PrusaSlicer's multi-material painting tools

> **NOTE**  
> Previous versions could not preserve colors on round-trip. Version 1.2.4+ now includes color metadata export, enabling full-fidelity workflows between Blender and PrusaSlicer MMU painting
#### PrusaSlicer Compatibility

**Import:**
- Reads `slic3rpe:mmu_segmentation` attributes for per-triangle multi-material zones
- Color zones are preserved and converted to Blender materials
- Uses the same filament index encoding as Orca Slicer
- ⚠️ **Paint bucket tool (volumetric paint) not yet supported** - files using this feature will import as single-color

**Export:**
- Per-triangle face materials exported with `slic3rpe:mmu_segmentation` attributes
- Color zones exported via Orca format are compatible with PrusaSlicer's multi-material modifier workflow
- Compatible with models where different materials are assigned to mesh parts

> **NOTE**  
> **Per-triangle vs Paint Bucket:** We support PrusaSlicer's per-triangle MMU segmentation (where each face has one material), but not the volumetric paint bucket tool which uses a proprietary per-vertex encoding. This is a research task for future versions.
> 
> PrusaSlicer does not embed actual RGB colors in 3MF files - it uses filament indices that reference your local filament profiles. When round-tripping through Blender, colors are generated based on zone indices and may not match your original filament colors exactly.

See [EXTENSIONS.md](EXTENSIONS.md) for detailed documentation on extension support, vendor-specific features, and adding new extensions.

---

## Project History

This project began as a modernization of the original Blender 3MF add-on by Ghostkeeper and has since continued as an independently maintained fork.

- Original Author: Ghostkeeper (2020–2023)
- Modernization & Ongoing Maintenance: Jack (2025–)

Original authorship, attribution, and the **GPL v2+ license** are fully preserved.

---

## License

GPL v2+
