from yt_dlp.utils import (
    LazyList,
    remove_end,
    traverse_obj,
    variadic,
)
from yt_dlp.extractor.youtube import YoutubeIE


class Youtube_NoDashyIE(YoutubeIE, plugin_name='NoDashy'):
    NO_DASHY_DEFAULT = False  # `False` means dashy formats are constructed by default

    def _real_extract(self, url):
        ret = super()._real_extract(url)

        if self._configuration_arg('construct_dash', ['off'])[0] in ('', 'on', 'yes', 'true', '1'):
            pass
        elif self.NO_DASHY_DEFAULT or self._configuration_arg('construct_dash', [''])[0] in ('off', 'no', 'false', '0'):
            for info_dict in variadic(traverse_obj(ret, ('entries', ...), None, expected_type=dict)):
                if info_dict.get('live_status') == 'post_live':
                    continue
                for fmt in traverse_obj(info_dict, ('formats', ..., {dict})):
                    if fmt.get('protocol') == 'http_dash_segments' and isinstance(fmt.get('fragments'), LazyList):
                        fmt['protocol'] = 'https'
                        fmt['container'] = remove_end(fmt.get('container'), '_dash')
                        fmt['fragments'] = None
                        fmt['downloader_options'] = {'http_chunk_size': 10 << 20}

        return ret


__all__ = []
