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
- Verified round-trip import/export
- Scriptable import/export operators
- Extensive automated testing

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

### Export Options
- **Selection Only**
- **Scale**
- **Apply Modifiers**
- **Coordinate Precision**

---

## Testing

This add-on includes comprehensive automated testing to ensure reliability.

See [`tests/README.md`](tests/README.md) for detailed testing information.

---

## 3MF Specification Support

This add-on targets the **3MF Core Specification v1.2.3**.

### Behavior Notes

> **NOTE**  
> The 3MF specification requires consumers to fail hard on malformed files. In practice, this add-on favors recoverability in a DCC environment.

- Core requirements (ZIP/OPC structure, model XML, units, build definitions) are enforced on export.
- On import, partially malformed files may load with warnings rather than failing entirely.
- When conflicts arise while importing multiple 3MF files into a single scene, conflicting metadata may be skipped to preserve scene integrity.

### Extensions

> **NOTE**  
> Support for 3MF extensions is intentionally incremental.

- No optional 3MF extensions are fully implemented yet.
- The codebase is structured to support future extension work (materials, properties, metadata, slicer-specific data).

---

## Project History

This project began as a modernization of the original Blender 3MF add-on by Ghostkeeper and has since continued as an independently maintained fork.

- Original Author: Ghostkeeper (2020–2023)
- Modernization & Ongoing Maintenance: Jack (2025–)

Original authorship, attribution, and the **GPL v2+ license** are fully preserved.

---

## License

GPL v2+
