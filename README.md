A [yt-dlp](https://github.com/yt-dlp/yt-dlp) extractor [plugin](https://github.com/yt-dlp/yt-dlp#plugins) to disable YouTube HTTPS-to-DASH format conversion

---

The construction of DASH-y formats is enabled by default.

Pass `--extractor-args "youtube:construct_dash=off"` to disable it.

The `NO_DASHY_DEFAULT` class variable can also be toggled to `True` to disable DASH conversion by default. Then you could pass `--extractor-args "youtube:construct_dash"` to enable it.

## Installation

Requires yt-dlp `2023.03.12` or above.

You can install this package with pip:
```
python3 -m pip install -U https://github.com/bashonly/yt-dlp-YTNoDashy/archive/master.zip
```

See [yt-dlp installing plugins](https://github.com/yt-dlp/yt-dlp#installing-plugins) for the many other ways this plugin package can be installed.
