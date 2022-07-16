class singleton(type):
    """
    | A metaclass of Singleton pattern.

    | Singleton pattern is a software design pattern
      that restricts the instantiation of a class to one “single” instance.

    .. note::
        | A singleton pattern is “acceptable” when it doesn’t affect the execution of the code.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        | Apply a single instance.

        :param args:
            | Arguments will be passed to the original class constructor.
        :type args: `any`
        :param kwargs:
            | Keyword arguments will be passed to the original class constructor.
        :type kwargs: `any`
        :return: An instance of a selected class as a singleton object.
        :rtype: `any`
        """
        if cls not in cls._instances:
            cls._instances[cls] = super(singleton, cls).__call__(*args, **kwargs)
        return cls._instances.get(cls)
