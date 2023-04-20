# bili-json2srt

Convert bilibili json captions to a srt file

And split video / audio referring to time of captions

Requires:

1. ffmpeg
2. ffprobe

This may be helpful

```shell
ffmpeg -i video.mp4 -vn -acodec libmp3lame -q:a 4 video.mp3
```
