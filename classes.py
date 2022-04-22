class Television:
    MIN_CHANNEL = 0  # Minimum TV channel
    MAX_CHANNEL = 3  # Maximum TV channel

    MIN_VOLUME = 0  # Minimum TV volume
    MAX_VOLUME = 2  # Maximum TV volume

    def __init__(self):

        self.__channel = Television.MIN_CHANNEL
        self.__volume = Television.MIN_VOLUME
        self.__TV_power = 'False'

    def power(self):
        if self.__TV_power == 'False':
            self.__TV_power = 'True'

        else:
            self.__TV_power = 'False'

    def channel_up(self):
        if self.__TV_power == 'True':
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel = self.__channel + 1
        else:
            self.__channel = Television.MIN_CHANNEL

    def channel_down(self):

        if self.__TV_power == 'True':
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel = self.__channel - 1
        else:
            self.__channel = Television.MIN_CHANNEL

    def volume_up(self):
        if self.__TV_power == 'True':
            if self.__volume == Television.MAX_VOLUME:
                self.__volume = Television.MAX_VOLUME
            else:
                self.__volume = self.__volume + 1
        else:
            self.__volume = Television.MIN_VOLUME

    def volume_down(self):

        if self.__TV_power == 'True':
            if self.__volume == Television.MIN_VOLUME:
                self.__volume = Television.MIN_VOLUME
            else:
                self.__volume = self.__volume - 1
        else:
            self.__volume = Television.MIN_VOLUME

    def __str__(self):
        return 'TV status: Is on = {}, Channel = {}, Volume = {}'.format(self.__TV_power, self.__channel, self.__volume)
    


