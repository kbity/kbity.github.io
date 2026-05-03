# Aperture Picture Format 2
---

<small>From Maripedia, the Maristocratic encyclopedia</small>

| Field  | Aperture Picture Format 2  |
|-----------|------|
| Filename extension      | `.af2`, `.apf2` |
| MIME Type | `image/x-aperture-picture-1993`, `image/x-aperture-picture-1994` |
| Uniform Type Identifier (UTI) | `public.image.apf2` (1993), `public.video.apf2` (1994) |
| Developed by | Aperture Laboratories |
| Initial release | 1993; 33 years ago |
| Latest release | 1994; 32 years ago |
| Type of format | computer animation, plain text |

**Aperture Picture Format 2** (**APF2**, often shortened to **AF2** and officially pronounced as "Ayph-2") is a lossless bitmap image format.
It was designed by Aperture Laboratories in 1993 as an optimized ASCII image format using RLE and is backwards compatible with the 1985 APF.
APF2 Supports a palette of 95 colors (corresponding to the 95 printable ASCII characters), transparency (which takes up a palette space), animation, and more optimized 2-color 1985 APF-styled data.
An APF can be trivially upgraded to APF2 with a simple header-swap as is.
The Format supports interleaved data, scanning the image bottom-to-top, skipping X amounts of rows in order to form a more visible image earlier into transmission.

The 1994 version of APF2 introduces 3 new features: The Dual-Indexed Mode (DIM), Alpha in Palette, and Frame Delay.
Frame Delay is backwards compatible and will work just fine in APF2-1993 tooling, but DIM and alpha require newer software to use.

## APF2 Format Information
The Aperture Picture Format is an ASCII file that can be identified by its plaintext header: 
```
APERTURE IMAGE FORMAT (c) 1993
```
The convention for the end of a line is given by hex code 0x0A, or `<LF>`, unlike the original 1985 APF's convention of 0x0D0D0A (`<CR CR LF>`), however, either is supported.

The APF2 file format has the following basic structure: 
```
Header<LF>
<resolution>,<flags>,<line skip>,<description><LF>
palette<LF>
frame data, separated by newlines
EOF
```
Resolution is formatted as: `WxH`, with W being a width, and H being a height<br>
Flags specify information about the image, with 't' indicating transparency, 'm' indicating multiple frames, and 'l' specifying that the image has 2 colors.

## Encoding
APF2 encoding uses Run-length Encoding (RLE). Worst case for the format is 2 bytes per pixel (Palette index and run-length of 1).<br>
A run is specified using `PR` (or `PPR` under DIM) with P/PP being the palette index and R being the length (encoded in ASCII base95, with space being 0 and ~ being 94)<br>
Palette entries are encoded as `P######`, `PP######`, `P########`, or `PP########` with P/PP being the ASCII palette index and the hashtags being the 24-bit RGB hex code for the color or 32-bit RGBA hex code for the color.<br>
With transparency, the space pallete entry is ignored and transparency is written instead.
It is considered good practice to specify it with a color like FF00FF or 000000 to support encoders without transparency support.

The following is an example of an APF2 image
```
APERTURE IMAGE FORMAT (c) 1993
9x9,m,1,This is a sample APF2 image
b000000RFF0000G00FF00B0000FFC00FFFFMFF00FFYFFFF00WFFFFFFg999999
R#G#B#R#G#B#R#G#B#C#M#Y#C#M#Y#C#M#Y#b#g#W#b#g#W#b#g#W#
```
This image as a PNG is the following:
![Image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAkAAAAJCAMAAAGgSMa0AAAAAXNSR0IB2cksfwAAAARnQU1BAACxjwv8YQUAAAAgY0hSTQAAeiYAAICEAAD6AAAAgOgAAHUwAADqYAAAOpgAABdwnLpRPAAAABtQTFRFAAAAAAD//wAA/wD/mZmZAP8AAP////8A////AsaPigAAAAlwSFlzAAAuIwAALiMBeKU/dgAAAAd0SU1FB+oEGwEtMuCshUIAAAA9SURBVAjXTYs3DgAwDAJxA///xSHKkgVRDmCRgcaAJThRtwB6veSEffc+YZnJmXhyKdcGSU8l6XPpt6mIAzoPAUVll3//AAAAAElFTkSuQmCC)

The following is an example of an 1994 revision APF2 image
```
APERTURE IMAGE FORMAT (c) 1994
9x9,ma,1,This is a sample APF2 image using 1994's Alpha feature and animation speed feature,1000
b000000AARFF0000BBG00FF00CCB0000FFDDC00FFFFEEMFF00FFFFYFFFF0099WFFFFFF88g99999977
R#G#B#R#G#B#R#G#B#C#M#Y#C#M#Y#C#M#Y#b#g#W#b#g#W#b#g#W#
B#G#R#B#G#R#B#G#R#Y#M#C#Y#M#C#Y#M#C#W#g#b#W#g#b#W#g#b#
```

## Trivia
* For 1993, this format is rather dated, with its limited 95 color palette and simplistic compression, when GIF existed for 6 years at the time.
* Despite the simple compression, APF2 can sometimes compress an image better than an RGB PNG, and occasionally even Indexed PNG.
* Due to using pure ASCII, APF2s can technically be packaged using 7 bits for a character rather than 8, reducing file sizes by ~12.5%
* APF2 is sometimes used to embed images directly into code and documents, similarly to XBM and XPM.
* The format only got 1 major update past inception, the 1994 revision. The 9025 color palette is notable as most paletted images only go up to 256 colors, 1 byte per color.

<small>*This Aperture Science-related article is a stub. You can help Maripedia by adding missing information.*</small>