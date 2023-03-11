import abc


class ABCSmsPanel(abc.ABC):

    @abc.abstractmethod
    def _response_parser(self):
        raise NotImplementedError

    @abc.abstractmethod
    def send_sms(self):
        raise NotImplementedError
