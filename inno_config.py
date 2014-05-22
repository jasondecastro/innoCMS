config = {

    ##################
    # SQL Management #
    ##################

    "sql": {
        # SQL server's IP.
        # Is a string, not an integer.
        "host": 'localhost',

        # SQL username.
        "username": 'root',

        # SQL password.
        "password": 'password',

        # SQL database name.
        "database": 'database_name',
    },

    ####################
    # Hotel Management #
    ####################

    "hotel": {
        # Hotel's server IP.
        # Is a string, not an integer.
        "serverIP": '127.0.0.1',

        # URL to your hotel.
        # Does not end in '/'.
        "url": 'http://localhost',

        # Name of your hotel.
        "name": 'Inno Hotel',

        # Description of your hotel.
        "description": 'innoCMS v0.1',

        # Email where people can send mail to you .
        "email": 'fag@g.pl',

        # Is maintenance enabled?
        # Is a boolean, not a string.
        "maintenence": False,

        # Mainenance message.
        # Will only be shown if mainenance is enabled.
        "maint_message": 'Inno will be back soon!',

        # Current web build.
        "webBuild": '63_1dc60c6d6ea6e089c6893ab4e0541ee0/527',

        # Link to your external_texts file.
        "external_texts": '/gamedata/external_texts.txt',

        # Link to your product_data file.
        "product_data": '/gamedata/product_data.txt',

        # Link to your furni_data file.
        "furni_data": '/gamedata/furni_data.txt',

        # Link to your SWF folder.
        # Does not end in a '/'.
        "swf_folder": '/gamedata',

        # Max motto length, used for the CMS.
        # Is an integer, not a string.
        "max_motto_length": 10,

        # Template
        "template": 'template_name'
    },

    ###########################
    # Registration Management #
    ###########################

    "registration": {

        # Minimum and maximum character length for
        # usernames when registering.
        "maxmin_character_count": [3, 12],

        # Amount of credits that you'd like users to recieve upon registering.
        # Is an integer, not a string.
        "credits": 1000,

        # Amount of pixels (or duckets) that you'd like users to recieve
        # upon registering.
        # Is an integer, not a string.
        "pixels": 100,

        # Default figure for users.
        "figure": '-',

        # Default motto for users.
        "motto": 'Welcome to innoHotel!',
    }
}
