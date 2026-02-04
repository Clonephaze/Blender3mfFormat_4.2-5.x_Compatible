# 3MF Consortium Sample Files

This directory contains official sample files from the [3MF Consortium](https://github.com/3MFConsortium/3mf-samples).

## Files

- `dodeca_chain_loop_color.3mf` - Demonstrates colorgroup element
- `pyramid_vertexcolor.3mf` - Demonstrates vertex colors using colorgroup
- `multipletextures.3mf` - Demonstrates texture2d and texture2dgroup elements
- `sphere_logo.3mf` - Demonstrates combined colorgroup and texture usage
- `multiprop-opaque.3mf` - Demonstrates multiproperties with opaque materials
- `multiprop-metallic.3mf` - Demonstrates multiproperties with pbmetallicdisplayproperties
- `multiprop-translucent.3mf` - Demonstrates multiproperties with translucentdisplayproperties

## Modifications

**Note:** The files `multiprop-metallic.3mf` and `multiprop-translucent.3mf` originally contained a namespace prefix typo (`ms:` instead of `m:`). We've corrected this typo locally to enable testing. The original files can be found in the [3MF samples repository](https://github.com/3MFConsortium/3mf-samples).

## License

These files are licensed under the BSD 2-Clause License.

Copyright (c) 2018, 3MF Consortium. See [LICENSE](./LICENSE) file for full terms.

## Source

Downloaded from: https://github.com/3MFConsortium/3mf-samples

## Purpose

These files are used in the integration test suite to verify compatibility with official 3MF specification samples, ensuring the implementation correctly handles real-world 3MF files.
