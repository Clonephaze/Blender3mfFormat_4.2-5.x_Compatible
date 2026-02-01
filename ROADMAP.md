# 🗺️ Development Roadmap

> **3MF Import/Export for Blender** — Future Development Plan

Features and improvements organized by priority. Complexity ratings help with planning but don't determine feasibility — we can tackle hard problems with proper research.

---

## 📊 Legend

| Symbol | Meaning |
|--------|---------|
| ✅ | Completed |
| 📋 | Planned |
| 💭 | Needs Research |

**Complexity:** `🟢 Easy` `🟡 Medium` `🔴 Hard`

---

## 🎯 Current: v1.2.4

- ✅ 3MF Core Specification v1.4.0 compliance
- ✅ Production Extension (multi-file structure)
- ✅ Orca Slicer color zone export/import (`paint_color`)
- ✅ PrusaSlicer MMU export/import (`mmu_segmentation`)
- ✅ Color metadata for PrusaSlicer round-trips
- ✅ Automatic thumbnail generation
- ✅ OPC Core Properties (Dublin Core metadata)
- ✅ Progress messages during operations

---

## 📦 3MF Extensions

### Materials Extension
> `http://schemas.microsoft.com/3dmanufacturing/material/2015/02`

| Status | Feature | Complexity | Description |
|--------|---------|------------|-------------|
| ✅ | Base Materials | 🟢 | Basic material colors via `<basematerials>` |
| 📋 | Color Groups | 🟡 | `<colorgroup>` — similar structure to basematerials |
| 📋 | Texture 2D | 🔴 | UV-mapped textures with embedded images |

### Triangle Sets Extension
> `http://schemas.microsoft.com/3dmanufacturing/trianglesets/2021/07`

| Status | Feature | Complexity | Description |
|--------|---------|------------|-------------|
| ✅ | Namespace Support | 🟢 | Framework ready |
| 📋 | Import Triangle Sets | 🟡 | Map to Blender face maps |
| 📋 | Export Triangle Sets | 🟡 | Export face maps as triangle sets |

---

## 🖨️ Slicer Compatibility

### Orca Slicer / BambuStudio
| Status | Feature | Complexity | Description |
|--------|---------|------------|-------------|
| ✅ | Paint Color Export | 🟡 | Per-triangle `paint_color` attributes |
| ✅ | Paint Color Import | 🟡 | Read paint colors → Blender materials |
| ✅ | Project Settings | 🟡 | Filament colors from config |
| 📋 | Object Settings | 🟡 | Per-object print settings preservation |

### PrusaSlicer / SuperSlicer
| Status | Feature | Complexity | Description |
|--------|---------|------------|-------------|
| ✅ | MMU Segmentation Import | 🟡 | Reading `slic3rpe:mmu_segmentation` |
| ✅ | MMU Segmentation Export | 🟡 | Write segmentation for PrusaSlicer |
| ✅ | Color Metadata | 🟡 | Preserve RGB colors on round-trip |
| 📋 | Object Config | 🟡 | `slic3rpe:` per-object attributes |

### Cura
| Status | Feature | Complexity | Description |
|--------|---------|------------|-------------|
| 📋 | Cura Settings | 🟡 | `cura:` namespace support |

### General
| Status | Feature | Complexity | Description |
|--------|---------|------------|-------------|
| 📋 | Auto-Detect Format | 🟢 | Detect slicer by namespace presence |
| 📋 | Format Selection | 🟢 | Export format dropdown |

---

## 🎨 Blender Integration

### Materials
| Status | Feature | Complexity | Description |
|--------|---------|------------|-------------|
| ✅ | Basic Colors | 🟢 | Diffuse color from base materials |
| 📋 | Principled BSDF | 🟢 | Better material node setup on import |
| 📋 | Alpha/Transparency | 🟢 | RGBA support with blend modes |
| 📋 | Material Reuse | 🟡 | Match existing materials by name |

### Geometry
| Status | Feature | Complexity | Description |
|--------|---------|------------|-------------|
| ✅ | Mesh Import/Export | 🟢 | Triangulated mesh support |
| 📋 | Sharp Edges | 🟡 | Preserve via edge marks |
| 📋 | Non-Manifold Warning | 🟢 | Alert on export issues |

### Scene
| Status | Feature | Complexity | Description |
|--------|---------|------------|-------------|
| ✅ | Object Transforms | 🟢 | Position, rotation, scale |
| ✅ | Object Names | 🟢 | Name preservation |
| 📋 | Collections → Components | 🟡 | Map hierarchy to 3MF structure |
| 📋 | Instances | 🟡 | Linked duplicates as component refs |

### Thumbnails
| Status | Feature | Complexity | Description |
|--------|---------|------------|-------------|
| ✅ | Auto Thumbnail | 🟡 | Viewport snapshot |
| 📋 | Custom Thumbnail | 🟢 | Use custom image file |
| 📋 | Resolution Option | 🟢 | Configurable size |

---

## 💾 Metadata

| Status | Feature | Complexity | Description |
|--------|---------|------------|-------------|
| ✅ | Dublin Core | 🟡 | Core properties (title, creator, etc.) |
| 📋 | Custom Metadata | 🟡 | Preserve vendor metadata on re-export |
| 📋 | Metadata Panel | 🟡 | UI to view/edit 3MF metadata |
| 📋 | Blender Info | 🟢 | Export Blender version, author |

---

## 🖥️ User Experience

### Export
| Status | Feature | Complexity | Description |
|--------|---------|------------|-------------|
| ✅ | Multi-Material Toggle | 🟢 | Enable/disable color zones |
| ✅ | Format Selection | 🟢 | Export format dropdown (Standard/Orca/PrusaSlicer) |
| ✅ | Progress Messages | 🟢 | Status feedback during export |
| ✅ | Default Preference | 🟢 | Remember settings |
| 📋 | Selection Only | 🟢 | Export selected objects |
| 📋 | Batch Export | 🟡 | Export objects as separate files |
| 📋 | Export Presets | 🟡 | Save/load configurations |
| 📋 | Compression Level | 🟢 | Adjustable ZIP compression |

### Import
| Status | Feature | Complexity | Description |
|-✅ | Progress Messages | 🟢 | Status feedback during import |
| -------|---------|------------|-------------|
| ✅ | Auto-Scale | 🟢 | Scale based on unit metadata |
| 📋 | Import Location | 🟢 | Cursor/origin placement options |
| 📋 | Material Handling | 🟢 | Create new / Reuse existing / Skip |
| 📋 | Merge Objects | 🟢 | Join all meshes on import |

### UI
| Status | Feature | Complexity | Description |
|--------|---------|------------|-------------|
| ✅ | Preferences | 🟢 | Addon preferences panel |
| 📋 | Properties Panel | 🟡 | Sidebar panel for 3MF data |
| 📋 | Validation | 🟡 | Check export-readiness |

### Errors
| Status | Feature | Complexity | Description |
|--------|---------|------------|-------------|
| ✅ | Extension Warnings | 🟢 | Unsupported extension alerts |
| 📋 | Error Log | 🟡 | Detailed error reporting |
| 📋 | Recovery Mode | 🟡 | Partial import of corrupt files |

---

## ⚡ Performance

| Status | Feature | Complexity | Description |
|--------|---------|------------|-------------|
| 📋 | Progress Indicators | 🟢 | Progress bar for long operations |
| 📋 | Large Files | 🟡 | Streaming XML parsing |
| 📋 | Optimize Output | 🟡 | Minimize file size |

---

## 🧪 Testing & Docs

| Status | Feature | Complexity | Description |
|--------|---------|------------|-------------|
| ✅ | Unit Tests | 🟡 | Mock-based tests |
| ✅ | Integration Tests | 🟡 | Full cycle tests |
| 📋 | Slicer Round-Trip | 🟡 | Test with real slicer files |
| 📋 | User Guide | 🟡 | Usage documentation |

---

## 🚀 Priority Tiers

### High Priority
*Core functionality and features*

- [x] PrusaSlicer MMU export (write `mmu_segmentation` for round-trip editing)
- [x] Slicer format auto-detection (already implemented: `detect_vendor()` on import)
- [x] Export format selection (Standard/Orca/PrusaSlicer dropdown)
- [x] Slicer format auto-detection (already implemented: `detect_vendor()` on import)
- [ ] Custom thumbnail option
- [ ] Non-manifold warning

### Medium Priority
*Quality of life improvements*

- [ ] Export format dropdown
- [ ] Material reuse option
- [ ] Compression level option
- [ ] Import location options
- [ ] Properties panel

### Lower Priority
*Nice to have*

- [ ] Triangle Sets full support
- [ ] Texture 2D support
- [ ] Batch export
- [ ] Export presets
- [ ] Cura support
- [ ] Collections → Components

### Research Needed
*Requires investigation before committing*

- [ ] Seam/support painting formats (undocumented)
- [ ] Modifier mesh preservation
- [ ] Object settings round-trip

---

## 🤝 Contributing

Help wanted:
1. **Testing** — Try different slicers, report issues
2. **Research** — Document undocumented slicer formats
3. **Code** — Pick something from the roadmap and PR it

---

*Current version: 1.2.4*
