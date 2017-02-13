class BaseMusic:
    @staticmethod
    def support_error():
        raise Exception('不支持的分享地址')

    def analysis(self, url):
        raise Exception('Don\'t call this function not Implementation')
