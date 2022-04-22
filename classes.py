class Television:
    """
    A class representing details for an object, Television.
    """
    
    
    MIN_CHANNEL = 0  # Minimum TV channel
    MAX_CHANNEL = 3  # Maximum TV channel

    MIN_VOLUME = 0  # Minimum TV volume
    MAX_VOLUME = 2  # Maximum TV volume

    def __init__(self):
        """
        Constructer to create intial state of the Television object.
        """

        self.__channel = Television.MIN_CHANNEL
        self.__volume = Television.MIN_VOLUME
        self.__TV_power = 'False'

    def power(self):
        """
        Method for changing the power of the television to on or off.
        """
        
        if self.__TV_power == 'False':
            self.__TV_power = 'True'

        else:
            self.__TV_power = 'False'

    def channel_up(self):
        """
        Method for changing the channel on the television up 1.
        """
        
        if self.__TV_power == 'True':
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel = self.__channel + 1
        else:
            self.__channel = Television.MIN_CHANNEL

    def channel_down(self):
        """
        Method for changing the channel on the television down 1. 
        """

        if self.__TV_power == 'True':
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel = self.__channel - 1
        else:
            self.__channel = Television.MIN_CHANNEL

    def volume_up(self):
        """
        Method for turning the volume on the television up 1.
        """
        
        if self.__TV_power == 'True':
            if self.__volume == Television.MAX_VOLUME:
                self.__volume = Television.MAX_VOLUME
            else:
                self.__volume = self.__volume + 1
        else:
            self.__volume = Television.MIN_VOLUME

    def volume_down(self):
        """
        Method for turning the volume on the television down 1.
        """
        
        if self.__TV_power == 'True':
            if self.__volume == Television.MIN_VOLUME:
                self.__volume = Television.MIN_VOLUME
            else:
                self.__volume = self.__volume - 1
        else:
            self.__volume = Television.MIN_VOLUME

    def __str__(self):
        """
        Method for printing out the current status of the television.
        :return: Whether the TV is on or off, What channel the TV is on, and the volume of the TV.
        """
        return 'TV status: Is on = {}, Channel = {}, Volume = {}'.format(self.__TV_power, self.__channel, self.__volume)
    


