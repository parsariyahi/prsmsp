import abc


class ABCSmsPanel(abc.ABC):

    @abc.abstractmethod
    def send_sms(self):
        raise NotImplementedError
