# glyph

converts images to ascii art in your terminal. works best with high-contrast images.

```
python glyph.py dog.jpg --width 100 --color
```

## usage

```
python glyph.py <image> [--width 120] [--method average|minmax|luminosity] [--invert] [--color]
```

- `--width` — output width in columns, default 120
- `--method` — brightness calculation: `average` (default), `minmax`, or `luminosity`
- `--invert` — flip brightness, good for dark images on white background
- `--color` — ansi color output using original pixel rgb

## example

```
$ python glyph.py portrait.jpg --width 80 --method luminosity
loaded 1024x768
`````````````````````````````````````````````````````````
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
...
```

## install

```
pip install -r requirements.txt
```

i built this because i wanted something simple that i could tweak. most ascii art tools online are either bloated or don't give you control over the brightness method.
