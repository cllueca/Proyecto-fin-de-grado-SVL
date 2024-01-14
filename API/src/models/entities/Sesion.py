class Sesion():

    def __init__(self, sec_ch_ua, user_agent, http_origin) -> None:
        self.sec_ch_ua = sec_ch_ua,
        self.user_agent = user_agent,
        self.http_origin = http_origin

    def to_dict(self):
        return {
            'HTTP_SEC_CH_UA': self.sec_ch_ua,
            'HTTP_USER_AGENT': self.user_agent,
            'HTTP_ORIGIN': self.http_origin
        }