A [yt-dlp](https://github.com/yt-dlp/yt-dlp) extractor [plugin](https://github.com/yt-dlp/yt-dlp#plugins) to disable YouTube HTTPS-to-DASH format conversion

---

## NOTICE

This plugin has been made obsolete by [yt-dlp version 2023.04.11.161417](https://github.com/yt-dlp/yt-dlp-nightly-builds/releases/tag/2023.04.11.161417), [commit c6786ff](https://github.com/yt-dlp/yt-dlp/commit/c6786ff3baaf72a5baa4d56d34058e54cbcf8ceb)

**yt-dlp's default behavior has been reverted, and now it only constructs DASH-y formats if toggled by extractor-arg. As such, this plugin will no longer be updated, and it has been disabled for yt-dlp versions where it is obsolete**

Run `yt-dlp --update-to nightly` or install the master branch.

---

The construction of DASH-y formats is enabled by default.

Pass `--extractor-args "youtube:construct_dash=off"` to disable it.

The `NO_DASHY_DEFAULT` class variable can also be toggled to `True` to disable DASH conversion by default. Then you could pass `--extractor-args "youtube:construct_dash"` to enable it.

If you wish to use this plugin as a workaround for mpv's issue with DASH-y youtube formats, you can add this line to your `mpv.conf`:
```
ytdl-raw-options="extractor-args=[youtube:construct_dash=off]"
```

## Installation

Requires yt-dlp version [2023.03.12.091732](https://github.com/yt-dlp/yt-dlp-nightly-builds/releases/tag/2023.03.12.091732) to [2023.04.11.160543](https://github.com/yt-dlp/yt-dlp-nightly-builds/releases/tag/2023.04.11.160543).

You can install this package with pip:
```
python3 -m pip install -U https://github.com/bashonly/yt-dlp-YTNoDashy/archive/master.zip
```

See [yt-dlp installing plugins](https://github.com/yt-dlp/yt-dlp#installing-plugins) for the many other ways this plugin package can be installed.
