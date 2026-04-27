# Aperture Picture Format 2
---

<small>From Maripedia, the Maristocratic encyclopedia</small>

| Field  | Aperture Picture Format 2  |
|-----------|------|
| Filename extension      | `.af2`, `.apf2` |
| MIME Type | `image/x-aperture-picture-1993` |
| Uniform Type Identifier (UTI) | `public.plain-text` |
| Developed by | Aperture Laboratories |
| Initial release | 1993; 33 years ago |
| Type of format | computer animation, plain text |

**Aperture Picture Format 2** (**APF2**, often shortened to **AF2** and officially pronounced as "Ayph-2") is a lossless bitmap image format.
It was designed by Aperture Laboratories in 1993 as an optimized ASCII image format using RLE and is backwards compatible with the 1985 APF.
APF2 Supports a palette of 95 colors (corresponding to the 95 printable ASCII characters), transparency (which takes up a palette space), animation, and more optimized 2-color 1985 APF-styled data.
An APF can be trivially upgraded to APF2 with a simple header-swap as is.
The Format supports interleaved data, scanning the image bottom-to-top, skipping X amounts of rows in order to form a more visible image earlier into transmission.

## APF2 Format Information
The Aperture Picture Format is an ASCII file that can be identified by its plaintext header: 
```
APERTURE IMAGE FORMAT (c) 1993
```
The convention for the end of a line is given by hex code 0x0A, or `<LF>`, unlike the original 1985 APF's convention of 0x0D0D0A (`<CR CR LF>`).

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
A run is specified using `PR` with P being the palette index and R being the length (encoded in ASCII base95, with space being 0 and ~ being 94)<br>
Palette entries are encoded as `P######` with P being the ASCII palette index and the hashtags being the 24-bit hex code for the color.<br>
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

## Trivia
* For 1993, this format is rather dated, with its limited 95 color palette and simplistic compression.
* Despite the simple compression, APF2 can sometimes compress an image better than an RGB PNG, and occasionally even Indexed PNG.
* Due to using ASCII, APF2s can technically be packaged using 7 bits for a character rather than 8, reducing file sizes by ~12.5%
* APF2 is sometimes used to embed images directly into code and documents, similarly to XBM and XPM.

<small>*This Aperture Science-related article is a stub. You can help Maripedia by adding missing information.*</small>